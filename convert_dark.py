#!/usr/bin/env python3
"""
Convert specific slides from cream to dark in the FA deck.
Strategy: convert structural/intro/closer slides, keep video mockups and email mockups cream.
"""

import re

with open('index.html', 'r') as f:
    content = f.read()

# Extract all section class strings for pre-count
sections_before = re.findall(r'<section class=\"([^\"]+)\"', content)
dark_before = sum(1 for c in sections_before if 'slide--dark' in c)
cream_before = sum(1 for c in sections_before if 'slide--cream' in c)
print(f"BEFORE: {dark_before} dark / {cream_before} cream / {len(sections_before)} total")

# We'll split on section boundaries and process each one
# Strategy: track section index, apply targeted replacements

# Split into sections preserving everything
# Each section starts with <section class="slide..."> and ends with </section>
# We operate on the full sections list by index

section_pattern = re.compile(r'(<section class=")(slide[^"]+)(")', )

# Identify sections by their eyebrow/title content
# We'll split, process, and rejoin

# Split the HTML into parts: before first section, then alternating [class_string, rest_of_section]
# More robust: find all section start positions
starts = [m.start() for m in re.finditer(r'<section class="slide', content)]
ends_marker = '</section>'

# Build list of (start, end) for each section
section_spans = []
for i, start in enumerate(starts):
    if i + 1 < len(starts):
        # Find the </section> before the next <section
        end = content.rfind('</section>', start, starts[i+1]) + len('</section>')
    else:
        end = content.rfind('</section>') + len('</section>')
    section_spans.append((start, end))

print(f"\nFound {len(section_spans)} sections")

# Extract section HTML and their classes
sections = []
for start, end in section_spans:
    sec_html = content[start:end]
    cls_match = re.match(r'<section class="([^"]+)"', sec_html)
    classes = cls_match.group(1) if cls_match else ''
    sections.append({'html': sec_html, 'classes': classes, 'start': start, 'end': end})

# Print each section with a snippet of its content for identification
for i, sec in enumerate(sections, 1):
    # Get eyebrow or first heading
    eyebrow = re.search(r'class="eyebrow[^"]*">([^<]+)<', sec['html'])
    title = re.search(r'<h[12][^>]*>([^<]+)', sec['html'])
    ch_title = re.search(r'class="ch-title">([^<]+)', sec['html'])
    cover = re.search(r'class="cover-h1">([^<]+)', sec['html'])
    display = re.search(r'class="display[^"]*">([^<]+)', sec['html'])
    
    label = ''
    if eyebrow:
        label = eyebrow.group(1)[:60]
    elif ch_title:
        label = f'CH-TITLE: {ch_title.group(1)}'
    elif cover:
        label = f'COVER: {cover.group(1)}'
    elif display:
        label = f'DISPLAY: {display.group(1)}'
    elif title:
        label = title.group(1)[:60]
    
    print(f"  Slide {i:02d} [{sec['classes']}]  {label}")

# ============================================================
# CONVERSION DECISIONS
# Convert to dark (cream -> dark):
#   02: Agenda slide (chapter overview intro)
#   08: Five locked formats intro (format intro)
#   14: Organic performance closer / stat hero  
#   16: Email lifecycle overview (email flow intro)
#   34: Quora/Reddit strategy intro (chapter intro)
#   37: Quora/Reddit performance / stat hero
#   06: Paid media chapter closer / stat hero ($420K)
#
# Keep cream:
#   04: Charline videos (video frames need cream)
#   05: CPL chart (chart reads better on cream)
#   09-13: All vidgrid slides (phone frames need cream)
#   17-31: All email mockup slides (white email cards need cream)
#   32: Site walkthrough (video needs cream)
#   33: Site key pages grid (screenshots need cream)
#   35: Quora topic map (data grid needs cream)
#   36: Quora examples (text cards need cream)
# ============================================================

# Slides to convert (1-indexed)
TO_DARK = {2, 6, 8, 14, 16, 34, 37}

print(f"\nConverting slides: {sorted(TO_DARK)} to dark")

new_content = content
offset = 0  # track position shifts after replacements

for i, sec in enumerate(sections, 1):
    if i in TO_DARK:
        old_classes = sec['classes']
        # Replace slide--cream with slide--dark
        if 'slide--cream' in old_classes:
            new_classes = old_classes.replace('slide--cream', 'slide--dark')
            old_tag = f'<section class="{old_classes}"'
            new_tag = f'<section class="{new_classes}"'
            # Replace in new_content (only the first occurrence matching exactly)
            new_content = new_content.replace(old_tag, new_tag, 1)
            print(f"  Slide {i:02d}: '{old_classes}' -> '{new_classes}'")
        else:
            print(f"  Slide {i:02d}: already dark or no cream class: {old_classes}")

# Write result
with open('index.html', 'w') as f:
    f.write(new_content)

print("\n✓ index.html updated")

# Verify
with open('index.html', 'r') as f:
    result = f.read()

sections_after = re.findall(r'<section class="([^"]+)"', result)
dark_after = sum(1 for c in sections_after if 'slide--dark' in c)
cream_after = sum(1 for c in sections_after if 'slide--cream' in c)

print(f"\nAFTER:  {dark_after} dark / {cream_after} cream / {len(sections_after)} total")
print(f"Dark %: {dark_after/len(sections_after)*100:.1f}%")

print("\nFinal slide list:")
for i, cls in enumerate(sections_after, 1):
    marker = "🌑" if 'slide--dark' in cls else "🌕"
    print(f"  Slide {i:02d} {marker} {cls}")
