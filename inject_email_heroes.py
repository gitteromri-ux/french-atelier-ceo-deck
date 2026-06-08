#!/usr/bin/env python3
"""Inject real email hero images into each email card, and add slide-13/36 fixes via CSS."""
import re
from pathlib import Path

WEB = Path("/home/user/workspace/french_atelier_deck/web")
HTML = WEB / "index.html"

# Map deck card position (1-21) -> hero image filename, OR None for stylized brand hero.
# Welcome (1-6): no real heroes, keep brand. Nurture (7-21): map to email03-15 by index.
HERO_MAP = {
    # Welcome 01-06 — no real hero images exist for these
    1: None, 2: None, 3: None, 4: None, 5: None, 6: None,
    # Nurture 01-15
    7: "email03_image_600x350.jpg",   # NURTURE DAY 0
    8: "email04_image_600x350.jpg",   # NURTURE DAY 1
    9: "email05_image_600x350.jpg",   # NURTURE DAY 3
    10: "email06_collage_600x350.jpg",
    11: "email07_image_600x350.jpg",
    12: "email08_image_600x350.jpg",  # The French don't say "I miss you"
    13: "email09_image_600x350.jpg",  # coffee
    14: "email10_image_600x350.jpg",  # cinema
    15: "email11_image_600x350.jpg",  # France sings
    16: "email12_image_600x350.jpg",  # already speak
    17: "email13_image_600x350.jpg",
    18: "email14_image_600x350.jpg",
    19: "email15_image_600x350.jpg",
    20: "email15_image_600x350.jpg",
    21: "email15_image_600x350.jpg",
}

html = HTML.read_text()

# Find all email-card-v78__hero blocks
hero_pattern = re.compile(
    r'(<div class="email-card-v78__hero">)(.*?)(</div>\s*<div class="email-card-v78__body">)',
    re.DOTALL
)

matches = list(hero_pattern.finditer(html))
print(f"Found {len(matches)} hero blocks")

def replace_hero(idx, match):
    inner = match.group(2)
    # extract sub text
    sub_match = re.search(r'<div class="email-card-v78__sub">(.*?)</div>', inner)
    sub = sub_match.group(1) if sub_match else ""
    
    img = HERO_MAP.get(idx)
    if img:
        # Real image with overlay
        new = f'''<div class="email-card-v78__hero email-card-v78__hero--img" style="background-image:url('images/real_emails/{img}');background-size:cover;background-position:center;">
<div class="email-card-v78__hero-overlay">
<div class="email-card-v78__brand">FRENCH ATELIER</div>
<div class="email-card-v78__tag">BY ACADOMIA</div>
<div class="email-card-v78__sub">{sub}</div>
</div>
</div>
<div class="email-card-v78__body">'''
    else:
        # Keep brand hero
        new = match.group(1) + inner + match.group(3)
    return new

# Replace sequentially with index
counter = [0]
def sub_fn(m):
    counter[0] += 1
    return replace_hero(counter[0], m)

new_html = hero_pattern.sub(sub_fn, html)
HTML.write_text(new_html)
print(f"Replaced {counter[0]} hero blocks. Real images injected for: {sum(1 for v in HERO_MAP.values() if v)}")
