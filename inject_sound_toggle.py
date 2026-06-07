#!/usr/bin/env python3
"""
inject_sound_toggle.py
======================
Modifies index.html to:
  1. Link sound_toggle.css in <head>
  2. Link sound_toggle.js before </body>
  3. Wrap every <video ...>...</video> block in <div class="video-wrap">...</div>
     (idempotent — skips videos already inside a .video-wrap)
  4. Inject the sound-toggle button HTML right before </div> of every .video-wrap
  5. Ensure every <video> tag has: muted autoplay loop playsinline attrs

After all modifications it verifies that the count of
  <button class="sound-toggle"  ==  <div class="video-wrap"
and prints a before/after spot-check of 20 lines around the first .video-wrap.
"""

import re
import sys

INDEX = "/home/user/workspace/french_atelier_deck/web/index.html"

SOUND_TOGGLE_BTN = (
    '<button class="sound-toggle" onclick="toggleVideoSound(this)" '
    'aria-label="Toggle sound" title="Click for sound">\n'
    '  <svg class="icon-mute" width="18" height="18" viewBox="0 0 24 24" fill="currentColor">'
    '<path d="M3 9v6h4l5 5V4L7 9H3zm13.59 3L19 9.59 17.59 8.17 15.17 10.59 '
    '12.76 8.17 11.34 9.59 13.76 12l-2.42 2.41 1.41 1.42L15.17 13.4l2.41 2.42 '
    '1.41-1.42L16.59 12z"/></svg>\n'
    '  <svg class="icon-on" width="18" height="18" viewBox="0 0 24 24" fill="currentColor">'
    '<path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 '
    '2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c'
    '4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg>\n'
    '</button>'
)

# ── helper: ensure a video tag has required attrs ──────────────────────────────
REQUIRED_ATTRS = ['muted', 'autoplay', 'loop', 'playsinline']

def ensure_video_attrs(video_open_tag: str) -> str:
    """Add missing boolean attrs to an opening <video ...> tag."""
    for attr in REQUIRED_ATTRS:
        # match attr as a whole word (not inside another word)
        if not re.search(r'\b' + attr + r'\b', video_open_tag):
            # Insert before the closing > or />
            video_open_tag = re.sub(r'(\s*/?>)\s*$', f' {attr}\\1', video_open_tag)
    return video_open_tag

# ── load ───────────────────────────────────────────────────────────────────────
with open(INDEX, 'r', encoding='utf-8') as f:
    html = f.read()

lines_before = html.splitlines()
print(f"[BEFORE] Total lines: {len(lines_before)}")
print(f"[BEFORE] <video>  count: {html.count('<video')}")
print(f"[BEFORE] video-wrap count: {html.count('class=\"video-wrap\"')}")
print(f"[BEFORE] sound-toggle count: {html.count('<button class=\"sound-toggle\"')}")

# ── 1. Add CSS link in <head> (after the last existing <link> in head) ─────────
CSS_LINK = '<link rel="stylesheet" href="css/sound_toggle.css">'
if CSS_LINK not in html:
    # Insert just before </head>
    html = html.replace('</head>', f'{CSS_LINK}\n</head>', 1)
    print("[STEP 1] CSS link injected.")
else:
    print("[STEP 1] CSS link already present — skipped.")

# ── 2. Add JS script before </body> ────────────────────────────────────────────
JS_SCRIPT = '<script src="js/sound_toggle.js"></script>'
if JS_SCRIPT not in html:
    html = html.replace('</body>', f'{JS_SCRIPT}\n</body>', 1)
    print("[STEP 2] JS script tag injected.")
else:
    print("[STEP 2] JS script tag already present — skipped.")

# ── 3+4+5. Wrap every <video>…</video> in .video-wrap and inject button ────────
# Strategy: use a single regex to find each <video ...>...</video> block,
# wrap it, fix attrs, and append the toggle button.
# We match the opening <video tag, all content until </video>, close tag.

# The pattern captures:
#   group 1 = everything from <video up to and including the matching </video>
VIDEO_BLOCK_RE = re.compile(
    r'(<video\b[^>]*>.*?</video>)',
    re.DOTALL | re.IGNORECASE
)

def wrap_and_fix(match):
    block = match.group(1)
    # Fix the opening tag attrs
    fixed_block = re.sub(
        r'(<video\b[^>]*>)',
        lambda m: ensure_video_attrs(m.group(1)),
        block,
        count=1,
        flags=re.IGNORECASE
    )
    return (
        '<div class="video-wrap">\n'
        + fixed_block + '\n'
        + SOUND_TOGGLE_BTN + '\n'
        + '</div>'
    )

# Run substitution
html_new = VIDEO_BLOCK_RE.sub(wrap_and_fix, html)
print(f"[STEP 3-5] Wrapped all <video>…</video> blocks in .video-wrap + injected button.")

html = html_new

# ── Verify counts ──────────────────────────────────────────────────────────────
wrap_count = html.count('class="video-wrap"')
btn_count  = html.count('<button class="sound-toggle"')

print(f"\n[VERIFY] <div class=\"video-wrap\"> count : {wrap_count}")
print(f"[VERIFY] <button class=\"sound-toggle\"> count : {btn_count}")

if wrap_count == btn_count:
    print(f"[VERIFY] ✓ COUNTS MATCH — {wrap_count} video wraps, {btn_count} buttons")
else:
    print("[VERIFY] ✗ COUNT MISMATCH — check logic")
    sys.exit(1)

# ── Spot check: 20 lines around first .video-wrap ──────────────────────────────
lines_after = html.splitlines()
first_wrap_line = None
for i, line in enumerate(lines_after):
    if 'class="video-wrap"' in line:
        first_wrap_line = i
        break

if first_wrap_line is not None:
    start = max(0, first_wrap_line - 5)
    end   = min(len(lines_after), first_wrap_line + 15)
    print(f"\n[SPOT CHECK] Lines {start+1}–{end} around first .video-wrap:")
    for ln_num, ln in enumerate(lines_after[start:end], start=start+1):
        print(f"  {ln_num:4d}: {ln}")

# ── write ──────────────────────────────────────────────────────────────────────
with open(INDEX, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n[DONE] index.html written — {len(lines_after)} lines total.")
