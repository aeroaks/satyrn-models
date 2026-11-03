"""Tests for provenance recorded while downloading source documents."""

import io
import json
from datetime import datetime, timedelta
from pathlib import Path
from urllib.parse import urlparse

from satyrn.dataset.inputs import download_inputs


def test_download_inputs_pins_content_and_writes_per_document_manifest(tmp_path: Path, monkeypatch) -> None:
    output_root = tmp_path / "project"
    fake_module_path = output_root / "corpus_builder/src/satyrn/dataset/inputs/download_inputs.py"
    monkeypatch.setattr(download_inputs, "__file__", str(fake_module_path))
    sources = {
        "PEP1": "https://raw.githubusercontent.com/python/peps/main/peps/pep-0001.rst",
        "PEP2": "https://raw.githubusercontent.com/python/peps/main/peps/pep-0002.rst",
        "whatsnew": "https://raw.githubusercontent.com/python/cpython/main/Doc/whatsnew/3.15.rst",
    }
    monkeypatch.setattr(download_inputs, "SOURCES", {"3.15": {"docs": sources}})
    commits = {"python/peps": "a" * 40, "python/cpython": "b" * 40}
    api_requests: list[str] = []
    downloaded: dict[str, str] = {}

    def fake_urlopen(url: str, timeout: int = 30) -> io.BytesIO:
        api_requests.append(url)
        parts = urlparse(url).path.strip("/").split("/")
        repository = "/".join(parts[1:3])
        return io.BytesIO(json.dumps({"sha": commits[repository]}).encode())

    def fake_urlretrieve(url: str, destination: Path) -> None:
        downloaded[str(destination)] = url
        Path(destination).write_text(url)

    monkeypatch.setattr(download_inputs.urllib.request, "urlopen", fake_urlopen)
    monkeypatch.setattr(download_inputs.urllib.request, "urlretrieve", fake_urlretrieve)

    download_inputs.main.callback("3.15")

    docs_dir = output_root / "datasets/python3.15/input/docs"
    manifest = json.loads((docs_dir / "manifest.json").read_text())
    assert manifest["target_python_version"] == "3.15"
    assert len(api_requests) == 2
    assert set(manifest["documents"]) == {"PEP1.rst", "PEP2.rst", "whatsnew.rst"}
    for name in ("PEP1", "PEP2", "whatsnew"):
        entry = manifest["documents"][f"{name}.rst"]
        assert entry["source_url"] == sources[name]
        expected_commit = commits["python/cpython" if name == "whatsnew" else "python/peps"]
        assert entry["source_commit"] == expected_commit
        timestamp = datetime.fromisoformat(entry["fetched_at"])
        assert timestamp.utcoffset() == timedelta(0)
        destination = docs_dir / f"{name}.rst"
        expected_url = sources[name].replace("/main/", f"/{expected_commit}/", 1)
        assert downloaded[str(destination)] == expected_url
        assert destination.read_text() == expected_url
