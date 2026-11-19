#!/usr/bin/env python3
"""Draw entry.png: a dark "top 6" briefing poster summing up
Thursday 19 November 2026. Pure Pillow, deterministic output.
Run: python3 draw.py  -> writes entry.png next to this file.

Design (deliberately unlike the 17/18 Nov newspaper grids):
a dark navy briefing board, one big hero story on top, then a
numbered 02-06 countdown. Only facts from the verified 19 Nov list.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (13, 22, 38)
CARD = (26, 40, 64)
CARD2 = (20, 32, 52)
INK = (245, 242, 234)
MUTED = (184, 192, 204)
GOLD = (232, 184, 75)
RED = (224, 90, 78)
BLUE = (96, 165, 250)
GREEN = (74, 184, 122)
PURPLE = (178, 132, 232)
TEAL = (64, 196, 188)
RULE = (232, 184, 75)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
F_KICK = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 24)
F_DATE = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 62)
F_SUB = ImageFont.truetype(FONT_DIR + "DejaVuSans.ttf", 24)
F_TAG = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 20)
F_HERO = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 38)
F_HERO_BODY = ImageFont.truetype(FONT_DIR + "DejaVuSans.ttf", 25)
F_NUM = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 44)
F_HEAD = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 27)
F_BODY = ImageFont.truetype(FONT_DIR + "DejaVuSans.ttf", 22)
F_ALSO = ImageFont.truetype(FONT_DIR + "DejaVuSans.ttf", 21)
F_ALSO_B = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 21)
F_FOOT = ImageFont.truetype(FONT_DIR + "DejaVuSans.ttf", 19)

# (number, tag, tag colour, headline, one factual line)
ROWS = [
    ("02", "GAZA", RED,
     "Israel launches ground operation in central Gaza",
     "Tens of thousands flee their tents as troops move in."),
    ("03", "UKRAINE", BLUE,
     "Crimean Bridge hit for a third day",
     "Traffic closed after the latest attack on the bridge."),
    ("04", "BUSINESS", GREEN,
     "Anthropic IPO at $81.3bn",
     "The largest IPO ever; shares priced at $83."),
    ("05", "GAMES", PURPLE,
     "GTA VI launches worldwide",
     "Players return to Vice City after a 13-year wait."),
    ("06", "USA", TEAL,
     "Jeffries set to be first African-American Speaker",
     "Hakeem Jeffries to lead the U.S. House of Representatives."),
]

ALSO = [
    "Voyager 1 reaches a one-light-day milestone, NASA confirms.",
    "Cyclone Akvan set to make landfall between Machilipatnam and Puri.",
    "US-Iran clashes continue; Iran struck Kuwait and Bahrain on 18 Nov.",
]


def wrap(draw, text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    mx = 40

    # --- header ---
    kick = "THE WORLD IN ONE DAY  \u2022  THURSDAY"
    d.text((mx, 30), kick, font=F_KICK, fill=GOLD)
    date = "19 NOVEMBER 2026"
    d.text((mx, 58), date, font=F_DATE, fill=INK)
    d.line([(mx, 138), (W - mx, 138)], fill=GOLD, width=4)

    # --- hero story 01 ---
    hy = 158
    d.rounded_rectangle([mx, hy, W - mx, hy + 182], radius=14, fill=CARD)
    d.rectangle([mx, hy, mx + 8, hy + 182], fill=GOLD)
    d.text((mx + 26, hy + 16), "01  \u2022  SUMMIT IN SHENZHEN", font=F_TAG, fill=GOLD)
    hero_head = "Trump, Xi and Putin meet in Shenzhen"
    lines = wrap(d, hero_head, F_HERO, W - 2 * mx - 52)
    yy = hy + 48
    for line in lines:
        d.text((mx + 26, yy), line, font=F_HERO, fill=INK)
        yy += 44
    hero_body = ("Trilateral talks at the APEC summit focus on nuclear "
                 "issues and Ukraine.")
    blines = wrap(d, hero_body, F_HERO_BODY, W - 2 * mx - 52)
    for line in blines:
        d.text((mx + 26, yy + 4), line, font=F_HERO_BODY, fill=MUTED)
        yy += 30

    # --- numbered rows 02-06 ---
    ry = hy + 186 + 16
    row_h = 94
    for num, tag, color, head, body in ROWS:
        d.rounded_rectangle([mx, ry, W - mx, ry + row_h - 10], radius=10,
                            fill=CARD2)
        d.text((mx + 18, ry + 20), num, font=F_NUM, fill=color)
        tx = mx + 104
        d.text((tx, ry + 12), tag, font=F_TAG, fill=color)
        hlines = wrap(d, head, F_HEAD, W - mx - tx - 16)[:1]
        d.text((tx, ry + 34), hlines[0], font=F_HEAD, fill=INK)
        blines = wrap(d, body, F_BODY, W - mx - tx - 16)[:1]
        d.text((tx, ry + 64), blines[0], font=F_BODY, fill=MUTED)
        ry += row_h

    # --- also today strip ---
    sy = ry + 10
    d.line([(mx, sy), (W - mx, sy)], fill=GOLD, width=2)
    d.text((mx, sy + 10), "ALSO TODAY", font=F_ALSO_B, fill=GOLD)
    ay = sy + 38
    for item in ALSO:
        line = wrap(d, "\u2022  " + item, F_ALSO, W - 2 * mx)[0]
        d.text((mx, ay), line, font=F_ALSO, fill=MUTED)
        ay += 28

    foot = "Events as reported on 19 November 2026  \u2022  One day, in one picture."
    fw = d.textlength(foot, font=F_FOOT)
    d.text(((W - fw) / 2, H - 28), foot, font=F_FOOT, fill=(140, 148, 162))

    img.save("entry.png", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
