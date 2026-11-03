"""Tests for source and generator provenance in SFT dataset rows."""

import subprocess
from pathlib import Path
from types import SimpleNamespace

from satyrn.dataset import sft
from satyrn.dataset.utils.generation import Idea


def test_sft_row_includes_document_model_and_generator_commits(monkeypatch) -> None:
    idea = Idea(
        Path("PEP815.rst"),
        "demonstrate the feature",
        "3.15",
        doc_provenance={"source_commit": "a" * 40},
    )
    model = SimpleNamespace(model_name="deepseek-v4-flash")
    monkeypatch.setattr(
        sft,
        "generate_code_block",
        lambda *args: {"code": "print(1)", "trace": "", "expected_output": "1"},
    )
    monkeypatch.setattr(
        sft,
        "generate_conversation",
        lambda *args: {"prompt": "show it", "response": "1"},
    )
    monkeypatch.setattr(sft, "judge_conversation", lambda *args: None)

    row = sft.build_dataset_line(model, idea, object(), object(), "deepseek-v4-flash", "c" * 40)

    assert row["doc_commit"] == "a" * 40
    assert row["model_name"] == "deepseek-v4-flash"
    assert row["generator_commit"] == "c" * 40


def test_get_generator_commit_reads_satyrn_repository_head(tmp_path: Path, monkeypatch) -> None:
    repository = tmp_path / "project"
    module_path = repository / "corpus_builder/src/satyrn/dataset/sft.py"
    module_path.parent.mkdir(parents=True)
    (repository / "tracked.txt").write_text("source")
    subprocess.run(["git", "init", "--quiet", str(repository)], check=True)
    subprocess.run(["git", "-C", str(repository), "config", "user.name", "Test"], check=True)
    subprocess.run(["git", "-C", str(repository), "config", "user.email", "test@example.com"], check=True)
    subprocess.run(["git", "-C", str(repository), "add", "tracked.txt"], check=True)
    subprocess.run(["git", "-C", str(repository), "commit", "--quiet", "-m", "test source"], check=True)
    expected = subprocess.run(
        ["git", "-C", str(repository), "rev-parse", "HEAD"],
        capture_output=True,
        check=True,
        text=True,
    ).stdout.strip()
    monkeypatch.setattr(sft, "__file__", str(module_path))

    assert sft.get_generator_commit() == expected
