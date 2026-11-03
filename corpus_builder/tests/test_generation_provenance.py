"""Tests for carrying source-document provenance through idea generation."""

import json
from pathlib import Path

from satyrn.dataset.utils.generation import generate_ideas


class StubModel:
    def generate(self, *args, **kwargs) -> dict:
        return {"ideas": ["demonstrate the feature"]}


def test_generate_ideas_carries_matching_download_manifest_entry(tmp_path: Path) -> None:
    doc_path = tmp_path / "docs/sub/PEP815.rst"
    doc_path.parent.mkdir(parents=True)
    doc_path.write_text("source document")
    provenance = {
        "source_url": "https://example.test/PEP815.rst",
        "source_commit": "a" * 40,
        "fetched_at": "2026-02-20T12:00:00+00:00",
    }
    (tmp_path / "docs/manifest.json").write_text(json.dumps({"documents": {"sub/PEP815.rst": provenance}}))

    ideas = generate_ideas(StubModel(), doc_path, "3.15")

    assert len(ideas) == 1
    assert ideas[0].doc_provenance == provenance


def test_generate_ideas_carries_collection_manifest_provenance(tmp_path: Path) -> None:
    doc_path = tmp_path / "changes/library/example.rst"
    doc_path.parent.mkdir(parents=True)
    doc_path.write_text("collected source section")
    provenance = {
        "source_commit": "b" * 40,
        "target_python_version": "3.15",
        "extracted_at": "2026-02-20T12:00:00+00:00",
    }
    (doc_path.parent / "manifest.json").write_text(json.dumps(provenance))

    ideas = generate_ideas(StubModel(), doc_path, "3.15")

    assert ideas[0].doc_provenance == provenance


def test_generate_ideas_without_manifest_has_no_document_provenance(tmp_path: Path) -> None:
    doc_path = tmp_path / "PEP815.rst"
    doc_path.write_text("source document")

    ideas = generate_ideas(StubModel(), doc_path, "3.15")

    assert ideas[0].doc_provenance is None
