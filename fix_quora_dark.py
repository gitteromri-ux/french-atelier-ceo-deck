#!/usr/bin/env python3
"""
Convert Quora Strategy (slide 34) and Quora Performance (slide 37) to dark.
Use content-based targeting to avoid incorrect replacements.
"""

with open('index.html', 'r') as f:
    content = f.read()

# Quora Strategy slide — unique eyebrow: "CHAPTER 03 · QUORA + REDDIT · STRATEGY"
qr_strategy_marker = '<section class="slide slide--cream"><div class="slide__inner">\n  <div class="eyebrow">CHAPTER 03 · QUORA + REDDIT · STRATEGY</div>'
qr_strategy_fix    = '<section class="slide slide--dark"><div class="slide__inner">\n  <div class="eyebrow">CHAPTER 03 · QUORA + REDDIT · STRATEGY</div>'

# Quora Performance slide — unique eyebrow: "CHAPTER 03 · QUORA + REDDIT · PERFORMANCE"
qr_perf_marker = '<section class="slide slide--cream"><div class="slide__inner">\n  <div class="eyebrow">CHAPTER 03 · QUORA + REDDIT · PERFORMANCE</div>'
qr_perf_fix    = '<section class="slide slide--dark"><div class="slide__inner">\n  <div class="eyebrow">CHAPTER 03 · QUORA + REDDIT · PERFORMANCE</div>'

if qr_strategy_marker in content:
    content = content.replace(qr_strategy_marker, qr_strategy_fix, 1)
    print("✓ Converted Quora Strategy slide to dark")
else:
    # Try with tab indentation
    qr_strategy_marker2 = '<section class="slide slide--cream"><div class="slide__inner">\n    <div class="eyebrow">CHAPTER 03 · QUORA + REDDIT · STRATEGY</div>'
    qr_strategy_fix2    = '<section class="slide slide--dark"><div class="slide__inner">\n    <div class="eyebrow">CHAPTER 03 · QUORA + REDDIT · STRATEGY</div>'
    if qr_strategy_marker2 in content:
        content = content.replace(qr_strategy_marker2, qr_strategy_fix2, 1)
        print("✓ Converted Quora Strategy slide to dark (variant 2)")
    else:
        print("✗ ERROR: Could not find Quora Strategy marker")
        # Debug: show context
        import re
        idx = content.find('QUORA + REDDIT · STRATEGY')
        if idx > 0:
            print(f"Context: {repr(content[idx-120:idx+50])}")

if qr_perf_marker in content:
    content = content.replace(qr_perf_marker, qr_perf_fix, 1)
    print("✓ Converted Quora Performance slide to dark")
else:
    qr_perf_marker2 = '<section class="slide slide--cream"><div class="slide__inner">\n    <div class="eyebrow">CHAPTER 03 · QUORA + REDDIT · PERFORMANCE</div>'
    qr_perf_fix2    = '<section class="slide slide--dark"><div class="slide__inner">\n    <div class="eyebrow">CHAPTER 03 · QUORA + REDDIT · PERFORMANCE</div>'
    if qr_perf_marker2 in content:
        content = content.replace(qr_perf_marker2, qr_perf_fix2, 1)
        print("✓ Converted Quora Performance slide to dark (variant 2)")
    else:
        print("✗ ERROR: Could not find Quora Performance marker")
        import re
        idx = content.find('QUORA + REDDIT · PERFORMANCE')
        if idx > 0:
            print(f"Context: {repr(content[idx-120:idx+50])}")

with open('index.html', 'w') as f:
    f.write(content)

print("\n✓ index.html updated")

# Verify
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
