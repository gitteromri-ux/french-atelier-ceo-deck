#!/usr/bin/env python3
"""v7.7 restructure:
- Delete slides 4,5,6,14 (1-based original indices)
- Split slide 8 (Formal vs Spoken, 6 phones) into 2 slides (3 + 3)
- Split slide 9 (Homonyms, varies) into 2 slides
- Slide 12 (Beauty IG): change headline + ensure FA branding caption
- Move slide 16 'Thought Leadership' divider: rename to 'Email Marketing'
- Insert new 'Thought Leadership' divider after emails (before slide 40)
- Insert Welcome / Nurture flow openers before email groups
- Ensure all videos have poster + preload + width/height for smooth playback
"""
import re
import sys
from pathlib import Path

WEB = Path(__file__).parent
HTML = WEB / 'index.html'
src = HTML.read_text()

# Split on slide openings
parts = re.split(r'(<section class="slide)', src)
head = parts[0]
slides = []
for i in range(1, len(parts), 2):
    slides.append(parts[i] + parts[i+1])

# Slide is closed by </section>. Each slide string here goes from <section class="slide... up to (but NOT including) next <section. So it ends in </section>\n etc. Good.

# Print count
print(f"Original slide count: {len(slides)}")

# Build new ordering (1-based indices -> 0-based)
# Original 1..52.
# Delete: 4,5,6,14
# Split: 8 -> 8a + 8b, 9 -> 9a + 9b
# Move: 16 (Thought Leadership) becomes Email Marketing divider
# Insert: new Thought Leadership divider before slide 40 (Quora/Reddit intro)

def cut_phones(slide_html, start, end):
    """Return slide html with format-multi-cards from index [start, end). Renumber so it fits."""
    # find format-multi-grid block
    m = re.search(r'(<div class="format-multi-grid[^"]*">)(.*?)(</div>\s*</div>\s*</section>)', slide_html, re.DOTALL)
    if not m:
        return slide_html
    grid_open = m.group(1)
    grid_inner = m.group(2)
    tail = m.group(3)
    # Split into cards
    cards = re.findall(r'<div class="format-multi-card">.*?</div>\s*</div>', grid_inner, re.DOTALL)
    if not cards:
        return slide_html
    subset = cards[start:end]
    new_grid = grid_open.replace('format-multi-grid--6', f'format-multi-grid--{len(subset)}') + '\n' + '\n'.join(subset) + '\n' + tail
    return slide_html[:m.start()] + new_grid + slide_html[m.end():]

# Build slide-8a and 8b
slide_8 = slides[7]
slide_8a = cut_phones(slide_8, 0, 3)
slide_8b = cut_phones(slide_8, 3, 6)
# Rename slide 8b eyebrow with "(part 2)"
slide_8b = slide_8b.replace('FORMAL VS SPOKEN', 'FORMAL VS SPOKEN · PART 2', 1)
slide_8a = slide_8a.replace('FORMAL VS SPOKEN', 'FORMAL VS SPOKEN · PART 1', 1)

# slide 9 (homonyms) — same treatment
slide_9 = slides[8]
# Count cards
cards_9 = re.findall(r'<div class="format-multi-card">', slide_9)
n9 = len(cards_9)
print(f"Slide 9 (Homonyms) has {n9} cards")
half = n9 // 2 if n9 > 3 else n9
if n9 > 3:
    slide_9a = cut_phones(slide_9, 0, half)
    slide_9b = cut_phones(slide_9, half, n9)
    slide_9a = slide_9a.replace('HOMONYMS', 'HOMONYMS · PART 1', 1)
    slide_9b = slide_9b.replace('HOMONYMS', 'HOMONYMS · PART 2', 1)
else:
    slide_9a = slide_9
    slide_9b = None

# Slide 12 Beauty IG — change headline + ensure FA branding under each video
slide_12 = slides[11]
slide_12 = re.sub(
    r'<h2 class="title title--md">Seven IG references\..*?</h2>',
    '<h2 class="title title--md">Celebrating the Beauty of French Culture. <span class="title-sub">Like no other brand.</span></h2>',
    slide_12, flags=re.DOTALL)
slide_12 = slide_12.replace('CHAPTER 02 · ORGANIC · BEAUTY · IG REFERENCES', 'CHAPTER 02 · ORGANIC · BEAUTY · OUR FORMAT')
# Add FA branding badge overlay inside each ig-phone if not present already
def add_fa_badge(html):
    # Add a badge div right after <div class="phone-notch"></div>
    return re.sub(
        r'(<div class="phone-frame[^"]*phone-frame--ig[^"]*">\s*<div class="phone-notch"></div>)',
        r'\1\n            <div class="fa-brand-badge">FA</div>',
        html
    ) if 'phone-frame--ig' in html else re.sub(
        r'(<div class="ig-phone">\s*<div class="phone-frame[^"]*">\s*<div class="phone-notch"></div>)',
        r'\1\n            <div class="fa-brand-badge">FA</div>',
        html
    )
slide_12 = add_fa_badge(slide_12)

# Slide 16: rename Thought Leadership -> Email Marketing
slide_16 = slides[15]
slide_16 = slide_16.replace('Thought Leadership', 'Email Marketing')

# Build new Thought Leadership divider (clone slide 16 then change title)
tl_divider = '''<section class="slide slide--dark slide--divider">
  <div class="slide__inner">
    <div class="chapter-num">CHAPTER 04</div>
    <h2 class="divider-title">Thought Leadership</h2>
    <div class="divider-sub">Reddit · Quora · Pinterest · Medium · Stack Exchange · Telegram</div>
  </div>
</section>
'''

# Insert Welcome flow opener (before slide 17) and Nurture flow opener (before slide 23)
welcome_opener = '''<section class="slide slide--dark slide--divider slide--flow-opener">
  <div class="slide__inner">
    <div class="chapter-num">CHAPTER 03 · EMAIL MARKETING</div>
    <h2 class="divider-title">Welcome Flow</h2>
    <div class="divider-sub">6 emails · onboarding · first 14 days</div>
  </div>
</section>
'''

nurture_opener = '''<section class="slide slide--dark slide--divider slide--flow-opener">
  <div class="slide__inner">
    <div class="chapter-num">CHAPTER 03 · EMAIL MARKETING</div>
    <h2 class="divider-title">Nurture &amp; Conversion Flow</h2>
    <div class="divider-sub">15 emails · cultural immersion · cohort close</div>
  </div>
</section>
'''

# Compose new order (0-indexed source):
# 1 -> slides[0] cover
# 2 -> slides[1] Paid Media divider
# 3 -> slides[2] Paid duo
# 4,5,6 DELETED (slides[3,4,5])
# 7 -> slides[6] Organic Content divider
# 8 -> slide_8a + slide_8b
# 9 -> slide_9a (+ slide_9b)
# 10 -> slides[9] Tourism
# 11 -> slides[10] History
# 12 -> slide_12 Beauty (modified)
# 13 -> slides[12] Beauty & Visual
# 14 DELETED (slides[13] Breakfast in production)
# 15 -> slides[14] Performance closer
# 16 -> slide_16 (renamed Email Marketing divider)
# Welcome opener
# 17-22 -> slides[16..21]
# Nurture opener
# 23-37 -> slides[22..36]
# (Insert Thought Leadership divider here)
# 38 slides[37] site
# 39 slides[38] key pages
# 40 slides[39] QR intro 60 posts
# 41-46 slides[40..45] platforms
# 47 slides[46] performance closer
# 48 slides[47] Bastille divider
# 49 slides[48] Bastille campaign
# 50 slides[49] The Ask divider
# 51 slides[50] Ask
# 52 slides[51] Closing

new_order = []
new_order.append(slides[0])              # cover
new_order.append(slides[1])              # Paid Media divider
new_order.append(slides[2])              # Paid duo
# skip 3,4,5
new_order.append(slides[6])              # Organic divider
new_order.append(slide_8a)
new_order.append(slide_8b)
new_order.append(slide_9a)
if slide_9b: new_order.append(slide_9b)
new_order.append(slides[9])              # Tourism
new_order.append(slides[10])             # History
new_order.append(slide_12)               # Beauty IG (modified)
new_order.append(slides[12])             # Beauty & Visual
# skip slides[13] (Breakfast)
new_order.append(slides[14])             # Organic performance closer
new_order.append(slide_16)               # Email Marketing divider (renamed)
new_order.append(welcome_opener)
for i in range(16, 22):                  # Welcome emails (slides[16..21])
    new_order.append(slides[i])
new_order.append(nurture_opener)
for i in range(22, 37):                  # Nurture emails (slides[22..36])
    new_order.append(slides[i])
new_order.append(tl_divider)             # new Thought Leadership divider
new_order.append(slides[37])             # site
new_order.append(slides[38])             # key pages
new_order.append(slides[39])             # 60 posts intro
for i in range(40, 46):                  # platforms (Reddit..Telegram)
    new_order.append(slides[i])
new_order.append(slides[46])             # 60 posts performance closer
new_order.append(slides[47])             # Bastille divider
new_order.append(slides[48])             # Bastille campaign
new_order.append(slides[49])             # The Ask divider
new_order.append(slides[50])             # Ask
new_order.append(slides[51])             # Closing

print(f"New slide count: {len(new_order)}")

# Reassemble HTML
new_html = head + ''.join(new_order)

# Renumber the "X / Y" indicator in nav-bar
new_html = re.sub(r'<span id="tot">\d+</span>', f'<span id="tot">{len(new_order)}</span>', new_html)
new_html = re.sub(r'(\d+)\s*/\s*52', f'\\1 / {len(new_order)}', new_html)

# Update Welcome/Nurture email eyebrow numbering inside the kept slides:
# We need to renumber EMAIL 01..06 (Welcome) and EMAIL 01..15 (Nurture) — but they already are. Skip.

# Add preload="metadata" to all videos that don't have it
new_html = re.sub(r'<video\b(?![^>]*preload=)', '<video preload="metadata"', new_html)

# Ensure all <video> tags inside .format-multi or .beauty-ig or .paid-duo have explicit dims to help layout — skip, CSS handles it.

HTML.write_text(new_html)
print(f"Wrote {HTML} ({len(new_html)} bytes)")
