"""Tests for CPython documentation-change collection metadata."""

import json
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from types import SimpleNamespace

import click
import pytest

from satyrn.dataset.inputs import collect_doc_changes


def make_cpython_checkout(tmp_path: Path) -> tuple[Path, str]:
    """Create a local CPython-shaped Git checkout with a known commit."""
    repository = tmp_path / "cpython"
    doc_directory = repository / "Doc"
    doc_directory.mkdir(parents=True)
    (doc_directory / "conf.py").write_text("project = 'cpython test docs'\n")

    subprocess.run(["git", "init", "--quiet", str(repository)], check=True)
    subprocess.run(["git", "-C", str(repository), "config", "user.name", "Test"], check=True)
    subprocess.run(["git", "-C", str(repository), "config", "user.email", "test@example.com"], check=True)
    subprocess.run(["git", "-C", str(repository), "add", "Doc/conf.py"], check=True)
    subprocess.run(["git", "-C", str(repository), "commit", "--quiet", "-m", "test docs"], check=True)
    revision = subprocess.run(
        ["git", "-C", str(repository), "rev-parse", "HEAD"],
        capture_output=True,
        check=True,
        text=True,
    ).stdout.strip()
    return doc_directory, revision


def test_collect_writes_source_revision_and_utc_timestamp_to_manifest(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    doc_directory, revision = make_cpython_checkout(tmp_path)
    output_root = tmp_path / "project"
    fake_module_path = output_root / "corpus_builder/src/satyrn/dataset/inputs/collect_doc_changes.py"
    monkeypatch.setattr(collect_doc_changes, "__file__", str(fake_module_path))
    monkeypatch.setattr(
        collect_doc_changes,
        "parse_docs",
        lambda _: SimpleNamespace(env=SimpleNamespace(all_docs=set())),
    )
    monkeypatch.setattr(collect_doc_changes, "find_version_changes", lambda *_: iter(()))

    collect_doc_changes.main.callback("3.15", doc_directory)

    manifest_path = output_root / "datasets/python3.15/input/docs/changes/manifest.json"
    manifest = json.loads(manifest_path.read_text())
    assert manifest["source_commit"] == revision
    assert manifest["target_python_version"] == "3.15"
    extracted_at = datetime.fromisoformat(manifest["extracted_at"])
    assert extracted_at.utcoffset() == timedelta(0)


def test_source_revision_requires_a_git_checkout(tmp_path: Path) -> None:
    with pytest.raises(click.ClickException, match="Git checkout"):
        collect_doc_changes.get_source_commit(tmp_path)
