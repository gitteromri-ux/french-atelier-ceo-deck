#!/usr/bin/env python3
"""
Fix: revert slides 4 (Charline videos) and 5 (CPL chart) back to cream.
These were accidentally converted to dark by the previous script.
We use precise content-based targeting.
"""

with open('index.html', 'r') as f:
    content = f.read()

# Slide 4: Charline Masterclass Two Cuts — contains "CHARLINE MASTERCLASS · TWO CUTS"
# Slide 5: CPL chart — contains "COST PER LEAD · TREND"

# Both currently have class="slide slide--dark"
# We need to replace the class string ONLY for these specific sections

# Strategy: find the exact section opening tag just before the identifying eyebrow text

charline_marker = '<section class="slide slide--dark"><div class="slide__inner">\n  <div class="eyebrow">CHAPTER 01 · PAID · CHARLINE MASTERCLASS · TWO CUTS</div>'
charline_fix    = '<section class="slide slide--cream"><div class="slide__inner">\n  <div class="eyebrow">CHAPTER 01 · PAID · CHARLINE MASTERCLASS · TWO CUTS</div>'

cpl_marker = '<section class="slide slide--dark"><div class="slide__inner">\n  <div class="eyebrow">CHAPTER 01 · PAID · COST PER LEAD · TREND</div>'
cpl_fix    = '<section class="slide slide--cream"><div class="slide__inner">\n  <div class="eyebrow">CHAPTER 01 · PAID · COST PER LEAD · TREND</div>'

if charline_marker in content:
    content = content.replace(charline_marker, charline_fix, 1)
    print("✓ Fixed slide 04 (Charline videos) back to cream")
else:
    print("✗ ERROR: Could not find Charline marker")

if cpl_marker in content:
    content = content.replace(cpl_marker, cpl_fix, 1)
    print("✓ Fixed slide 05 (CPL chart) back to cream")
else:
    print("✗ ERROR: Could not find CPL marker")

with open('index.html', 'w') as f:
    f.write(content)

print("\n✓ index.html updated")

# Verify final state
import re
sections = re.findall(r'<section class="([^"]+)"', content)
dark = sum(1 for c in sections if 'slide--dark' in c)
cream = sum(1 for c in sections if 'slide--cream' in c)
print(f"\nFINAL: {dark} dark / {cream} cream / {len(sections)} total")
print(f"Dark %: {dark/len(sections)*100:.1f}%  Cream %: {cream/len(sections)*100:.1f}%")
print()
for i, c in enumerate(sections, 1):
    status = "DARK " if 'slide--dark' in c else "cream"
    print(f"  Slide {i:02d} [{status}] {c}")
