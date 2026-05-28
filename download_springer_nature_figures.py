#!/usr/bin/env python
"""Download Springer Nature HTML figure PNGs for an article DOI.

Example:
  python download_springer_nature_figures.py 10.1038/s41467-024-53523-8 out --count 5
"""

from __future__ import annotations

import argparse
import re
import urllib.request
from pathlib import Path


def asset_prefix_from_doi(doi: str) -> str:
    match = re.search(r"s(\d+)-(\d{3,4})-(\d+)-\d+", doi)
    if not match:
        raise ValueError(f"Cannot infer Springer Nature asset prefix from DOI: {doi}")
    journal_code, year_token, article = match.groups()
    year = year_token if len(year_token) == 4 else f"20{year_token[-2:]}"
    return f"{journal_code}_{year}_{article}"


def download_figures(doi: str, output_dir: Path, count: int) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    doi_suffix = doi.split("/", 1)[1] if "/" in doi else doi
    encoded_doi = doi_suffix.replace("/", "%2F")
    prefix = asset_prefix_from_doi(doi)
    saved: list[Path] = []
    for index in range(1, count + 1):
        url = (
            "https://media.springernature.com/full/springer-static/image/"
            f"art%3A10.1038%2F{encoded_doi}/MediaObjects/{prefix}_Fig{index}_HTML.png"
        )
        dest = output_dir / f"Fig{index}_HTML.png"
        urllib.request.urlretrieve(url, dest)
        saved.append(dest)
    return saved


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("doi")
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--count", type=int, default=8)
    args = parser.parse_args()
    for path in download_figures(args.doi, args.output_dir, args.count):
        print(path)


if __name__ == "__main__":
    main()
