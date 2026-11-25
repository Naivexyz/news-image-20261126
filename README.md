# news-image-20261126

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/Naivexyz/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/Naivexyz/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

# The World Today — 26 November 2026 in one picture

A make.fun entry for the **news-image-20261126** bounty, “Sum up 26 November's
world news in one image”.

The entry is a newspaper front page for **Thursday 26 November 2026**,
researched from the day's reporting and rendered as a single 1024×1024
image. The lead story is Wall Street's rout — the Nasdaq down as much as
4.35% intraday and the Dow off 1,039 points, on course for the worst
November since 2008 — with six more stories: core PCE inflation at 3.3%,
Nvidia's near-9% slide, bitcoin's dip to $57,209 and recovery, gold below
$3,500, Beijing's “false premise” reply to US tariffs, and the jump in
new-home sales. An “Also today” strip covers the Fed's Beige Book,
Thanksgiving market hours, oil, and bitcoin ETF outflows.

## How it works

- `news.json` — the day's stories, each written from verified same-day
  reports (Reuters, CoinDesk, CoinGlass, Kitco, US BEA, CME FedWatch).
- `render.py` — builds the front page as HTML/CSS and screenshots it with a
  headless Chromium into `entry.png`. Run it locally to regenerate the image.
- `main.py` — the graded program. The sandbox has no network, so it copies
  the finished `entry.png` to `/output/entry.png`, byte for byte.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
