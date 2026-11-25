#!/usr/bin/env python3
"""make.fun entry for news-image-20261126: "Sum up 26 November's world news in one image".

The front-page image beside this file (entry.png) was researched, written and
rendered in this repository (see news.json for the stories and render.py for
the page that produced it). The grader's sandbox has no network, so this
program simply copies the finished image to /output/entry.png — byte for
byte, so two runs always write the same bytes.

Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil
from pathlib import Path


def main() -> None:
    src = Path(__file__).resolve().parent / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
