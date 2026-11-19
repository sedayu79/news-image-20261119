#!/usr/bin/env python3
"""Copy the entry image to the output directory.

The image itself is drawn by draw.py (Pillow, run locally when the
entry was built). This program is the only thing the sandbox runs, and
it needs nothing but the standard library: it reads entry.png next to
this file and writes it, byte for byte, to the directory the
MAKEFUN_OUTPUT_DIR environment variable names.
"""
import os

_HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(_HERE, "entry.png"), "rb") as src:
        data = src.read()
    with open(os.path.join(out_dir, "entry.png"), "wb") as dst:
        dst.write(data)


if __name__ == "__main__":
    main()
