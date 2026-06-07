"""
v7.8 restructure:
1) Remove the slide--site (livefrenchatelier site mockup) slide
2) Consolidate 21 emails (6 welcome + 15 nurture) into 11 slides (2 per slide)
   with redesigned side-by-side full email cards (no more empty right column)
3) Keep all other slides intact
4) Output written back to index.html
"""
import re
from bs4 import BeautifulSoup

INDEX = "/home/user/workspace/french_atelier_deck/web/index.html"
with open(INDEX, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")
slides = soup.select(".deck .slide") or soup.select(".slide")
print(f"Found {len(slides)} slides")

# 1) Find and remove the slide--site (livefrenchatelier site mockup)
site_slides = soup.select(".slide--site")
print(f"  Removing {len(site_slides)} site slides")
for s in site_slides:
    s.decompose()

# Also remove the immediate next slide which is "Every page audited." (site grid)
# That's the "slide--cream" right after, with site-grid inside.
for slide in soup.select(".slide"):
    inner = slide.find("div", class_="slide__inner")
    if inner and inner.find("div", class_="site-grid"):
        print("  Removing site-grid (key pages) slide")
        slide.decompose()
        break

# 2) Collect all ml2 email slides
email_slides = soup.select(".slide--ml2")
print(f"Found {len(email_slides)} email slides")

# Parse each email into a dict
emails = []
for es in email_slides:
    eb = es.find("div", class_="eyebrow").get_text() if es.find("div", class_="eyebrow") else ""
    title = es.find("h2", class_="title").get_text(strip=True) if es.find("h2", class_="title") else ""
    subj = es.find("div", class_="ml2-subj").get_text(strip=True) if es.find("div", class_="ml2-subj") else title
    body_div = es.find("div", class_="ml2-body")
    body_paras = []
    if body_div:
        for p in body_div.find_all("p"):
            body_paras.append(p.get_text(strip=True))
    # extract day & flow from eyebrow
    # CHAPTER 03 · WELCOME / ONBOARDING FLOW · EMAIL 01 · WELCOME · DAY 0 · LIVE
    parts = [p.strip() for p in eb.split("·")]
    flow = "Welcome" if "WELCOME" in eb.upper() and "WELCOME" in (parts[1] if len(parts) > 1 else "") else ("Nurture" if "NURTURE" in eb.upper() else "Welcome")
    # Day
    day = ""
    for p in parts:
        if "DAY" in p.upper():
            day = p.strip()
            break
    # email number
    enum = ""
    for p in parts:
        m = re.match(r"EMAIL\s+(\d+)", p.strip(), re.I)
        if m:
            enum = m.group(1)
            break
    emails.append({
        "title": title,
        "subj": subj,
        "body": body_paras,
        "flow": flow,
        "day": day,
        "enum": enum,
        "eyebrow_full": eb,
    })

print(f"Parsed {len(emails)} emails")

def email_card_html(e, slot_idx):
    """Build one full email card (no right column placeholder)."""
    body_html = "".join(f"<p>{p}</p>" for p in e["body"])
    return f'''
      <div class="email-card-v78">
        <div class="email-card-v78__chrome">
          <div class="email-card-v78__dots"><span></span><span></span><span></span></div>
          <div class="email-card-v78__app">Inbox · The French Atelier</div>
          <div class="email-card-v78__stage">{e["flow"].upper()} · {e["day"]}</div>
        </div>
        <div class="email-card-v78__meta">
          <div class="email-card-v78__from">
            <div class="email-card-v78__avatar">FA</div>
            <div>
              <div class="email-card-v78__from-name">The French Atelier</div>
              <div class="email-card-v78__from-addr">hello@frenchatelier.com</div>
            </div>
          </div>
          <div class="email-card-v78__time">Today · 9:14 AM</div>
        </div>
        <div class="email-card-v78__subj">{e["subj"]}</div>
        <div class="email-card-v78__hero">
          <div class="email-card-v78__brand">FRENCH ATELIER</div>
          <div class="email-card-v78__tag">BY ACADOMIA</div>
          <div class="email-card-v78__rule"></div>
          <div class="email-card-v78__sub">EMAIL {e["enum"]} · {e["flow"]} · {e["day"]}</div>
        </div>
        <div class="email-card-v78__body">
          {body_html}
          <p class="email-card-v78__signoff">— The French Atelier team</p>
        </div>
      </div>
    '''

def email_pair_slide(e_left, e_right, flow_name, pair_idx):
    """Build a slide with two emails side-by-side."""
    if e_right is None:
        cards = email_card_html(e_left, 0)
        grid_class = "email-pair-v78--single"
    else:
        cards = email_card_html(e_left, 0) + email_card_html(e_right, 1)
        grid_class = "email-pair-v78"
    eyebrow = f"CHAPTER 03 · {flow_name.upper()} FLOW · EMAILS {e_left['enum']}{'–' + e_right['enum'] if e_right else ''} · LIVE"
    if e_right:
        title_text = f"{e_left['title']} <span class=\"email-pair-v78__sep\">·</span> {e_right['title']}"
    else:
        title_text = e_left["title"]
    return f'''<section class="slide slide--cream slide--email-pair"><div class="slide__inner">
  <div class="eyebrow">{eyebrow}</div>
  <h2 class="title title--md">{title_text}</h2>
  <div class="rule"></div>
  <div class="{grid_class}">
    {cards}
  </div>
</div></section>'''

# Build new email slides: 2 per slide
welcome_emails = [e for e in emails if e["flow"] == "Welcome"]
nurture_emails = [e for e in emails if e["flow"] == "Nurture"]
print(f"Welcome: {len(welcome_emails)}, Nurture: {len(nurture_emails)}")

new_email_html_blocks = []
for i in range(0, len(welcome_emails), 2):
    left = welcome_emails[i]
    right = welcome_emails[i+1] if i+1 < len(welcome_emails) else None
    new_email_html_blocks.append(email_pair_slide(left, right, "Welcome", i//2))
for i in range(0, len(nurture_emails), 2):
    left = nurture_emails[i]
    right = nurture_emails[i+1] if i+1 < len(nurture_emails) else None
    new_email_html_blocks.append(email_pair_slide(left, right, "Nurture", i//2))

print(f"New email slide count: {len(new_email_html_blocks)} (was {len(email_slides)})")

# Now: replace the FIRST email slide's HTML with all new email slides concatenated,
# then remove all the rest.
new_email_combined = "\n".join(new_email_html_blocks)
new_email_soup = BeautifulSoup(new_email_combined, "html.parser")
new_email_sections = new_email_soup.find_all("section", class_="slide")

if email_slides:
    insert_pos = email_slides[0]
    # Insert new sections in forward order before the first old email slide
    for s in new_email_sections:
        insert_pos.insert_before(s)
    # Remove all old email slides
    for old in email_slides:
        old.decompose()

# Write out
out_html = str(soup)
with open(INDEX, "w", encoding="utf-8") as f:
    f.write(out_html)

# Final count
soup2 = BeautifulSoup(out_html, "html.parser")
final_slides = soup2.select(".slide")
print(f"\nFinal slide count: {len(final_slides)}")
for i, s in enumerate(final_slides[:60], 1):
    eb = s.find(class_="eyebrow")
    t = s.find("h2")
    label = (eb.get_text(strip=True)[:60] if eb else "") + " | " + (t.get_text(strip=True)[:50] if t else "")
    print(f"  {i:2d}. {label}")
