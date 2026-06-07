"""
Move Nurture & Conversion Flow divider to position right before first Nurture email slide.
Also: rename "Welcome Flow" → "Welcome / Onboarding Flow" for consistency.
"""
from bs4 import BeautifulSoup
INDEX = "/home/user/workspace/french_atelier_deck/web/index.html"
with open(INDEX, "r", encoding="utf-8") as f:
    html = f.read()
soup = BeautifulSoup(html, "html.parser")
slides = soup.select(".slide")

# Find slides
nurture_divider = None
first_nurture_email = None
for s in slides:
    h = s.find("h2")
    eb = s.find(class_="eyebrow")
    if h and "Nurture" in h.get_text() and "Flow" in h.get_text():
        nurture_divider = s
    if eb and "NURTURE FLOW · EMAILS 01" in eb.get_text():
        first_nurture_email = s

print(f"Nurture divider: {nurture_divider is not None}, first nurture email: {first_nurture_email is not None}")

if nurture_divider and first_nurture_email and nurture_divider is not first_nurture_email:
    # Move nurture_divider so it appears directly before first_nurture_email
    nurture_divider.extract()
    first_nurture_email.insert_before(nurture_divider)
    print("Moved nurture divider before first nurture email")

# Rename Welcome Flow heading
for s in slides:
    h = s.find("h2")
    if h and h.get_text(strip=True) == "Welcome Flow":
        h.string = "Welcome / Onboarding Flow"
        print("Renamed Welcome Flow")
        break

with open(INDEX, "w", encoding="utf-8") as f:
    f.write(str(soup))

# Final order print
soup2 = BeautifulSoup(open(INDEX).read(), "html.parser")
for i, s in enumerate(soup2.select(".slide")[:42], 1):
    eb = s.find(class_="eyebrow")
    t = s.find("h2")
    print(f"  {i:2d}. {(eb.get_text(strip=True)[:55] if eb else '').ljust(57)} | {t.get_text(strip=True)[:50] if t else ''}")
