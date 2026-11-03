"""Download the PEP and whatsnew source documents used by dataset generation."""

import json
import logging
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import click

logger = logging.getLogger(__name__)

SOURCES = {
    "3.14": {
        "docs": {
            "PEP649": "https://raw.githubusercontent.com/python/peps/main/peps/pep-0649.rst",
            "PEP749": "https://raw.githubusercontent.com/python/peps/main/peps/pep-0749.rst",
            "PEP734": "https://raw.githubusercontent.com/python/peps/main/peps/pep-0734.rst",
            "PEP750": "https://raw.githubusercontent.com/python/peps/main/peps/pep-0750.rst",
            "PEP758": "https://raw.githubusercontent.com/python/peps/main/peps/pep-0758.rst",
            "PEP765": "https://raw.githubusercontent.com/python/peps/main/peps/pep-0765.rst",
            "PEP768": "https://raw.githubusercontent.com/python/peps/main/peps/pep-0768.rst",
            "whatsnew": "https://raw.githubusercontent.com/python/cpython/main/Doc/whatsnew/3.14.rst",
        }
    },
    "3.15": {
        "docs": {
            "PEP810": "https://raw.githubusercontent.com/python/peps/main/peps/pep-0810.rst",
            "PEP814": "https://raw.githubusercontent.com/python/peps/main/peps/pep-0814.rst",
            "PEP661": "https://raw.githubusercontent.com/python/peps/main/peps/pep-0661.rst",
            "PEP799": "https://raw.githubusercontent.com/python/peps/main/peps/pep-0799.rst",
            "PEP831": "https://raw.githubusercontent.com/python/peps/main/peps/pep-0831.rst",
            "PEP798": "https://raw.githubusercontent.com/python/peps/main/peps/pep-0798.rst",
            "PEP686": "https://raw.githubusercontent.com/python/peps/main/peps/pep-0686.rst",
            "PEP829": "https://raw.githubusercontent.com/python/peps/main/peps/pep-0829.rst",
            "PEP728": "https://raw.githubusercontent.com/python/peps/main/peps/pep-0728.rst",
            "PEP747": "https://raw.githubusercontent.com/python/peps/main/peps/pep-0747.rst",
            "PEP800": "https://raw.githubusercontent.com/python/peps/main/peps/pep-0800.rst",
            "PEP782": "https://raw.githubusercontent.com/python/peps/main/peps/pep-0782.rst",
            "PEP803": "https://raw.githubusercontent.com/python/peps/main/peps/pep-0803.rst",
            "PEP820": "https://raw.githubusercontent.com/python/peps/main/peps/pep-0820.rst",
            "PEP793": "https://raw.githubusercontent.com/python/peps/main/peps/pep-0793.rst",
            "PEP788": "https://raw.githubusercontent.com/python/peps/main/peps/pep-0788.rst",
            "whatsnew": "https://raw.githubusercontent.com/python/cpython/main/Doc/whatsnew/3.15.rst",
        }
    },
}


def get_repository_commit(source_url: str) -> str:
    """Return the commit SHA currently referenced by the source URL's main branch."""
    path_parts = urlparse(source_url).path.strip("/").split("/")
    if len(path_parts) < 4 or path_parts[2] != "main":
        raise click.ClickException(f"Unexpected raw GitHub source URL: {source_url}")

    owner, repository = path_parts[:2]
    api_url = f"https://api.github.com/repos/{owner}/{repository}/commits/main"
    try:
        with urllib.request.urlopen(api_url, timeout=30) as response:
            return json.load(response)["sha"]
    except (OSError, json.JSONDecodeError, KeyError) as error:
        raise click.ClickException(f"Could not resolve main commit for {owner}/{repository}.") from error


@click.command("download-inputs")
@click.argument("target_version", type=click.Choice(sorted(SOURCES)))
def main(target_version: str) -> None:
    """Download PEP and whatsnew source documents."""
    for category, urls in SOURCES[target_version].items():
        out_dir = Path(__file__).parents[5] / "datasets" / f"python{target_version}" / "input" / category
        out_dir.mkdir(parents=True, exist_ok=True)
        commits_by_repository = {}
        documents = {}
        for name, url in urls.items():
            repository = "/".join(urlparse(url).path.strip("/").split("/")[:2])
            if repository not in commits_by_repository:
                commits_by_repository[repository] = get_repository_commit(url)
            source_commit = commits_by_repository[repository]
            pinned_url = url.replace("/main/", f"/{source_commit}/", 1)

            dest = out_dir / f"{name}.rst"
            logger.info("Python %s: Downloading %s", target_version, name)
            urllib.request.urlretrieve(pinned_url, dest)
            documents[dest.name] = {
                "source_url": url,
                "source_commit": source_commit,
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            }

        manifest = {"target_python_version": target_version, "documents": documents}
        (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")


if __name__ == "__main__":
    main()
