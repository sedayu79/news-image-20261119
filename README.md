# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/sedayu79/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/sedayu79/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A dark "top 6" briefing poster summing up Thursday 19 November 2026,
built for the make.fun bounty "Sum up 19 November's world news in one image".

## The image

`entry.png` (1024×1024) leads with the date and a hero story — the
Trump–Xi–Putin trilateral in Shenzhen at the APEC summit — then counts
down stories 02–06: Israel's ground operation in central Gaza, the
Crimean Bridge hit for a third day, Anthropic's $81.3bn IPO (the largest
ever), GTA VI launching worldwide, and Hakeem Jeffries set to become the
first African-American Speaker of the U.S. House — plus an "Also today"
strip (Voyager 1's one-light-day milestone; Cyclone Akvan's expected
landfall between Machilipatnam and Puri; US–Iran clashes continuing).
Every fact is as reported on the day; nothing is invented.

## How it was made

- `draw.py` draws the image with Pillow (DejaVu fonts) on the builder's
  machine. Run it again with `python3 draw.py` to reproduce `entry.png`.
- `main.py` is the entrypoint the sandbox runs: standard library only, it
  copies `entry.png` to the output directory byte for byte, so both runs
  produce identical bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Verify

```sh
mkdir -p /tmp/out1 /tmp/out2
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
sha256sum /tmp/out1/entry.png /tmp/out2/entry.png
```
