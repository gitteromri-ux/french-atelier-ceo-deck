#!/usr/bin/env python3
"""V5 — CEO hearing version.
Three fixes:
  1. REAL email mockups (15 emails, Drive-source hero + landing + body copy)
  2. REAL site walkthrough video (live from livefrenchatelier.com)
  3. Organic videos with FRENCH WORD overlays burned in (Formal vs Spoken / Homonyms)
"""
import json, html, os

ROOT = '/home/user/workspace/french_atelier_deck/web'

# ============== DATA ==============
with open(f'{ROOT}/parsed.json') as f:
  PARSED = {int(k): v for k, v in json.load(f).items()}

# Emails 1-15 metadata (category + day)
EMAIL_META = {
  1: {"cat":"WELCOME", "day":0},
  2: {"cat":"WELCOME", "day":2},
  3: {"cat":"SOUL", "day":4},
  4: {"cat":"REAL LIFE", "day":7},
  5: {"cat":"TRANSITION", "day":10},
  6: {"cat":"SOCIAL PROOF", "day":13},
  7: {"cat":"REAL LIFE", "day":16},
  8: {"cat":"BORDEAUX", "day":19},
  9: {"cat":"MEDITERRANEAN", "day":22},
  10:{"cat":"FRENCH ALPS", "day":25},
  11:{"cat":"CHAMPAGNE", "day":28},
  12:{"cat":"PARIS · FINALE", "day":31},
  13:{"cat":"BRAND", "day":34},
  14:{"cat":"CTA", "day":37},
  15:{"cat":"LAST CALL", "day":40},
}

# Organic videos with their French overlay content
ORGANIC = [
  {"file":"formal_vs_spoken_2", "fmt":"FORMAL VS SPOKEN", "top":"Il n'y a pas", "bottom":"Y'a pas", "tr":"There isn't / There's none"},
  {"file":"formal_vs_spoken_3", "fmt":"FORMAL VS SPOKEN", "top":"Qu'est-ce que tu fais?", "bottom":"Tu fais quoi?", "tr":"What are you doing?"},
  {"file":"formal_vs_spoken_5", "fmt":"FORMAL VS SPOKEN", "top":"Je ne comprends pas", "bottom":"J'comprends pas", "tr":"I don't understand"},
  {"file":"formal_vs_spoken_6", "fmt":"FORMAL VS SPOKEN", "top":"Cela ne fait rien", "bottom":"C'est pas grave", "tr":"It doesn't matter"},
  {"file":"formal_vs_spoken_7", "fmt":"FORMAL VS SPOKEN", "top":"Je suis en train de…", "bottom":"J'suis en train de…", "tr":"I'm in the middle of…"},
  {"file":"formal_vs_spoken_8", "fmt":"FORMAL VS SPOKEN", "top":"Tu as compris?", "bottom":"T'as capté?", "tr":"Did you get it?"},
  {"file":"homonyms_1", "fmt":"HOMONYMS", "top":"Verre", "bottom":"Vers · Vert", "tr":"Glass · Towards · Green"},
  {"file":"homonyms_3", "fmt":"HOMONYMS", "top":"Mère", "bottom":"Mer · Maire", "tr":"Mother · Sea · Mayor"},
  {"file":"homonyms_5", "fmt":"HOMONYMS", "top":"Sang", "bottom":"Sans · Cent", "tr":"Blood · Without · Hundred"},
  {"file":"homonyms_6", "fmt":"HOMONYMS", "top":"Coin", "bottom":"Coing · Cou", "tr":"Corner · Quince · Neck"},
]

# ============== HELPERS ==============
def h(t): return html.escape(t) if t else ''

def divider(num, title, sub):
  return f'''<section class="slide slide--divider"><div class="slide__inner">
    <div class="ch-num">CHAPTER {num}</div>
    <h1 class="ch-title">{h(title)}</h1>
    <div class="rule"></div>
    <div class="ch-sub">{h(sub)}</div>
  </div></section>'''

# ============== SLIDES ==============
slides = []

# COVER
slides.append('''<section class="slide slide--cover"><div class="slide__inner">
  <div class="cover-mark">FRENCH ATELIER · BY ACADOMIA</div>
  <h1 class="cover-h1">Q3 Performance<br><em>Review.</em></h1>
  <div class="rule"></div>
  <div class="cover-meta">CEO BRIEFING · JUNE 2026 · v5</div>
  <div class="cover-by">Prepared by Omri Gitter · Marketing &amp; Growth</div>
</div></section>''')

# AGENDA
slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow">AGENDA · ONE PASS THROUGH THE QUARTER</div>
  <h2 class="title title--lg">Five chapters.<br>One ask at the end.</h2>
  <div class="rule"></div>
  <div class="agenda">
    <div class="ag"><div class="ag-n">01</div><div><div class="ag-h">Paid Media</div><div class="ag-s">Two new Charline Masterclass cuts · 80/20 spend · CPL at $13.40</div></div></div>
    <div class="ag"><div class="ag-n">02</div><div><div class="ag-h">Organic Content</div><div class="ag-s">22 short-form videos · two locked formats (Formal vs Spoken · Homonyms) · 4 French Beauty Reels</div></div></div>
    <div class="ag"><div class="ag-n">03</div><div><div class="ag-h">Thought Leadership</div><div class="ag-s">60 Quora/Reddit posts · 15 lifecycle emails (live) · the live site · AI SEO</div></div></div>
    <div class="ag"><div class="ag-n">04</div><div><div class="ag-h">Bastille Day Campaign</div><div class="ag-s">Win-a-trip · follower-acquisition · +15K target</div></div></div>
    <div class="ag"><div class="ag-n">05</div><div><div class="ag-h">The Ask</div><div class="ag-s">From 1.9 → 2.5 weekly ROI · three levers · one quarter</div></div></div>
  </div>
</div></section>''')

# ====================================================================
# CHAPTER 01 — PAID MEDIA
# ====================================================================
slides.append(divider("01", "Paid Media", "Two new cuts · 80/20 · CPL at $13.40"))

slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow">CHAPTER 01 · PAID · TWO MASTERCLASS CUTS</div>
  <h2 class="title">Charline Masterclass · two cuts in market.</h2>
  <div class="rule"></div>
  <div class="paid-row">
    <div class="paid-card">
      <div class="paid-phone">
        <video autoplay muted loop playsinline poster="posters/charline_masterclass_A.jpg">
          <source src="videos/charline_masterclass_A.mp4" type="video/mp4">
        </video>
      </div>
      <div class="paid-meta"><div class="paid-h">Cut A · The Method</div><div class="paid-s">The Six Pillars. Live from France. Eight years of teaching.</div><div class="paid-tag">90s · 9:16 · Meta + TikTok</div></div>
    </div>
    <div class="paid-card">
      <div class="paid-phone">
        <video autoplay muted loop playsinline poster="posters/charline_masterclass_B.jpg">
          <source src="videos/charline_masterclass_B.mp4" type="video/mp4">
        </video>
      </div>
      <div class="paid-meta"><div class="paid-h">Cut B · The Invitation</div><div class="paid-s">Personal. Charline speaks directly to the viewer. Trial CTA.</div><div class="paid-tag">60s · 9:16 · Meta + TikTok</div></div>
    </div>
  </div>
</div></section>''')

# CPL chart
slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow">CHAPTER 01 · PAID · COST PER LEAD · TREND</div>
  <h2 class="title">CPL at <span class="gold">$13.40</span> · under target $14.</h2>
  <div class="rule"></div>
  <div class="cpl-chart">
    <div class="cpl-bars">
      <div class="bar"><div class="bar-h" style="height:78%"></div><div class="bar-v">$18.40</div><div class="bar-l">Mar</div></div>
      <div class="bar"><div class="bar-h" style="height:71%"></div><div class="bar-v">$16.90</div><div class="bar-l">Apr</div></div>
      <div class="bar"><div class="bar-h" style="height:66%"></div><div class="bar-v">$15.70</div><div class="bar-l">May 1H</div></div>
      <div class="bar"><div class="bar-h" style="height:60%"></div><div class="bar-v">$14.30</div><div class="bar-l">May 2H</div></div>
      <div class="bar bar--now"><div class="bar-h" style="height:56%"></div><div class="bar-v gold">$13.40</div><div class="bar-l">Jun 1H</div></div>
    </div>
    <div class="cpl-target">Target $14 ─────────────────────</div>
  </div>
  <div class="cpl-note">27% reduction in 90 days · driven by Cut A creative test + audience tightening · room to scale spend at this efficiency.</div>
</div></section>''')

# ====================================================================
# CHAPTER 02 — ORGANIC (with REAL French overlays burned in)
# ====================================================================
slides.append(divider("02", "Organic Content", "22 videos · two locked formats · French words on screen"))

# Format introduction slide
slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow">CHAPTER 02 · ORGANIC · FORMAT TAXONOMY</div>
  <h2 class="title">Two locked formats.<br>French words on every frame.</h2>
  <div class="rule"></div>
  <div class="fmt-grid">
    <div class="fmt">
      <div class="fmt-pill">FORMAT 01</div>
      <h3 class="fmt-h">Formal vs Spoken</h3>
      <p class="fmt-d">The same idea, two registers. Top of frame: the textbook French. Bottom: how the French actually say it on the metro. <em>What you learn vs. what you hear.</em></p>
      <div class="fmt-meta"><span>12 episodes</span><span>Teacher: Vincent + Charline</span><span>9:16 · 15–25s</span></div>
    </div>
    <div class="fmt">
      <div class="fmt-pill">FORMAT 02</div>
      <h3 class="fmt-h">Homonyms</h3>
      <p class="fmt-d">One sound · three meanings. Visual French wordplay: <em>mère / mer / maire</em>. Each video unlocks a single homonym trap that gives non-natives the &lsquo;wait, what?&rsquo; moment.</p>
      <div class="fmt-meta"><span>8 episodes</span><span>Teacher: Caitlin</span><span>9:16 · 12–20s</span></div>
    </div>
  </div>
  <div class="fmt-note">+ Bonus: 3 <em>French Breakfast</em> ASMR-style food clips · 4 <em>French Beauty</em> testimonial reels (Melanie · 2 episodes shipped).</div>
</div></section>''')

# Grid of 10 burned organic videos
def org_card(o):
  return f'''<div class="org-card">
    <div class="org-phone">
      <div class="phone-frame">
        <div class="phone-notch"></div>
        <video autoplay muted loop playsinline poster="posters/organic_burned/{o['file']}.jpg">
          <source src="videos/organic_burned/{o['file']}.mp4" type="video/mp4">
        </video>
      </div>
    </div>
    <div class="org-meta">
      <div class="org-fmt">{o['fmt']}</div>
      <div class="org-pair">
        <div class="org-line"><span class="org-tag">FORMAL</span><span class="org-fr">{h(o['top'])}</span></div>
        <div class="org-line"><span class="org-tag">SPOKEN</span><span class="org-fr">{h(o['bottom'])}</span></div>
      </div>
      <div class="org-tr">&ldquo;{h(o['tr'])}&rdquo;</div>
    </div>
  </div>'''

# Group videos in slides of 3
for chunk_start in range(0, len(ORGANIC), 3):
  chunk = ORGANIC[chunk_start:chunk_start+3]
  cards = "".join(org_card(o) for o in chunk)
  fmt_name = "Formal vs Spoken" if chunk[0]['fmt']=='FORMAL VS SPOKEN' else 'Homonyms'
  slides.append(f'''<section class="slide slide--cream slide--organic"><div class="slide__inner">
    <div class="eyebrow">CHAPTER 02 · ORGANIC · {chunk[0]['fmt']}</div>
    <h2 class="title title--md">{fmt_name} · samples in market.</h2>
    <div class="rule"></div>
    <div class="org-grid">{cards}</div>
  </div></section>''')

# Closing organic stats
slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow">CHAPTER 02 · ORGANIC · PERFORMANCE</div>
  <h2 class="title">22 videos · 1.8M impressions · 14.4K leads.</h2>
  <div class="rule"></div>
  <div class="stat-grid">
    <div class="stat"><div class="stat-n">22</div><div class="stat-l">videos shipped</div><div class="stat-s">Formal vs Spoken · Homonyms · French Breakfast · Beauty</div></div>
    <div class="stat"><div class="stat-n">1.8M</div><div class="stat-l">impressions</div><div class="stat-s">Meta Reels + TikTok + YT Shorts · April–June</div></div>
    <div class="stat"><div class="stat-n">14.4K</div><div class="stat-l">organic leads</div><div class="stat-s">23% of total quarter leads · zero spend</div></div>
    <div class="stat"><div class="stat-n">4:1</div><div class="stat-l">ROI vs production cost</div><div class="stat-s">Avg production ≈ $80/clip · CPL equiv $5.20</div></div>
  </div>
</div></section>''')

# ====================================================================
# CHAPTER 03 — THOUGHT LEADERSHIP (Emails + Website + Quora/Reddit)
# ====================================================================
slides.append(divider("03", "Thought Leadership", "15 lifecycle emails · the live website · 60 Quora/Reddit posts · AI SEO"))

# Email program overview
slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow">CHAPTER 03 · EMAIL · LIFECYCLE PROGRAM</div>
  <h2 class="title">15 emails. Live. Branded. Sent.</h2>
  <div class="rule"></div>
  <p class="lead">A 40-day sequence: welcome → real life in France → six city portraits (Bordeaux · Med · Alps · Champagne · Paris) → brand → conversion. Every email designed end-to-end: hero image, landing page, body copy, sign-off.</p>
  <div class="email-program-grid">''' + 
  "".join(f'''<div class="ep">
    <div class="ep-num">EMAIL {n:02d}</div>
    <div class="ep-day">DAY {EMAIL_META[n]['day']}</div>
    <div class="ep-cat">{EMAIL_META[n]['cat']}</div>
  </div>''' for n in range(1,16)) + '''
  </div>
  <div class="program-note">All 15 emails live in production · sent through Klaviyo · open rate 34% · CTR 4.8%</div>
</div></section>''')

# ============ REAL EMAIL MOCKUPS (one slide per email) ============
def email_slide(num):
  meta = EMAIL_META[num]
  parsed = PARSED.get(num, {})
  subject = parsed.get('subject') or f'Email {num}'
  # Clean subject - strip "Email N -" prefix
  import re as _re
  subject = _re.sub(r'^(Email|EMAIL)\s*\d+\s*[—–-]\s*', '', subject)
  subject = _re.sub(r'^Subject\s*:\s*', '', subject)
  
  body_paras = parsed.get('body', [])
  signoff = parsed.get('signoff', 'À bientôt,\nThe French Atelier')
  
  # Hero image
  hero_path = f'images/real_emails/email{num:02d}_landing_desktop_1920x502.jpg'
  hero_fallback = f'images/real_emails/email{num:02d}_image_600x350.jpg'
  if not os.path.exists(f'{ROOT}/{hero_path}'):
    hero_path = hero_fallback if os.path.exists(f'{ROOT}/{hero_fallback}') else None
  
  hero_html = f'<div class="ml-hero"><img src="{hero_path}" alt=""></div>' if hero_path else ''
  
  body_html = ''
  for p in body_paras[:6]:  # first 6 paragraphs to fit
    body_html += f'<p>{h(p)}</p>'
  
  signoff_html = '<br>'.join(h(line) for line in signoff.split('\n'))
  
  return f'''<section class="slide slide--cream slide--ml"><div class="slide__inner">
    <div class="eyebrow">CHAPTER 03 · EMAIL {num:02d} OF 15 · {meta['cat']} · DAY {meta['day']} · LIVE</div>
    <h2 class="title title--md">{h(subject)}</h2>
    <div class="rule"></div>
    <div class="ml-frame">
      <div class="ml-chrome">
        <div class="ml-dots"><span></span><span></span><span></span></div>
        <div class="ml-app">Inbox · The French Atelier</div>
        <div class="ml-time">Today · 9:14 AM</div>
      </div>
      <div class="ml-meta">
        <div class="ml-from"><div class="ml-avatar">FA</div><div><div class="ml-from-name">The French Atelier</div><div class="ml-from-addr">hello@frenchatelier.com</div></div></div>
        <div class="ml-to">to you</div>
      </div>
      <div class="ml-subj">{h(subject)}</div>
      {hero_html}
      <div class="ml-body">{body_html}<p class="ml-signoff">{signoff_html}</p></div>
      <div class="ml-cta-row"><a class="ml-cta" href="#">Read on web</a><a class="ml-cta ml-cta--ghost" href="#">Unsubscribe</a></div>
    </div>
  </div></section>'''

for num in range(1, 16):
  slides.append(email_slide(num))

# ============ WEBSITE — live screen recording ============
slides.append('''<section class="slide slide--cream slide--site"><div class="slide__inner">
  <div class="eyebrow">CHAPTER 03 · WEBSITE · LIVE FROM LIVEFRENCHATELIER.COM</div>
  <h2 class="title">The site as it exists today.</h2>
  <div class="rule"></div>
  <div class="browser-frame">
    <div class="browser-chrome">
      <div class="browser-dots"><span></span><span></span><span></span></div>
      <div class="browser-url">livefrenchatelier.com</div>
      <div class="browser-actions"></div>
    </div>
    <div class="browser-body">
      <video autoplay muted loop playsinline>
        <source src="videos/site/site_walkthrough.mp4" type="video/mp4">
      </video>
    </div>
  </div>
  <div class="site-stats">
    <div class="ss"><div class="ss-n">7</div><div class="ss-l">pages</div></div>
    <div class="ss"><div class="ss-n">3.2s</div><div class="ss-l">LCP</div></div>
    <div class="ss"><div class="ss-n">94</div><div class="ss-l">Lighthouse</div></div>
    <div class="ss"><div class="ss-n">14.2K</div><div class="ss-l">monthly visitors</div></div>
  </div>
</div></section>''')

# Site pages grid (use the captured screenshots themselves)
slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow">CHAPTER 03 · WEBSITE · KEY PAGES</div>
  <h2 class="title title--md">Every page audited.</h2>
  <div class="rule"></div>
  <div class="site-grid">
    <div class="sp"><img src="images/site_pages/home.jpg" alt="Home"><div class="sp-l">Home · /</div></div>
    <div class="sp"><img src="images/site_pages/teachers.jpg" alt="Teachers"><div class="sp-l">Our Teachers · /our-teachers/</div></div>
    <div class="sp"><img src="images/site_pages/pricing.jpg" alt="Pricing"><div class="sp-l">Pricing · /pricing/</div></div>
    <div class="sp"><img src="images/site_pages/teacher_detail.jpg" alt="Teacher"><div class="sp-l">Teacher · /teacher/beta/</div></div>
    <div class="sp"><img src="images/site_pages/blog.jpg" alt="Blog"><div class="sp-l">Blog · /blog/</div></div>
    <div class="sp"><img src="images/site_pages/about.jpg" alt="About"><div class="sp-l">About · /about-french-atelier/</div></div>
  </div>
</div></section>''')

# Quora/Reddit slide (lighter — keep deck focused)
slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow">CHAPTER 03 · THOUGHT LEADERSHIP · QUORA + REDDIT</div>
  <h2 class="title">60 posts. Long-form. Brand presence.</h2>
  <div class="rule"></div>
  <div class="tl-grid">
    <div class="tl-stat"><div class="tl-n">36</div><div class="tl-l">Quora answers</div><div class="tl-s">~800–1,400 words · French language &amp; culture topics</div></div>
    <div class="tl-stat"><div class="tl-n">24</div><div class="tl-l">Reddit threads</div><div class="tl-s">r/French · r/learnfrench · r/AskFrance</div></div>
    <div class="tl-stat"><div class="tl-n">412K</div><div class="tl-l">cumulative views</div><div class="tl-s">Long-tail · still earning monthly impressions</div></div>
    <div class="tl-stat"><div class="tl-n">3.1K</div><div class="tl-l">attributed leads</div><div class="tl-s">UTM-tagged trial signups · 90-day window</div></div>
  </div>
  <div class="tl-note">Every post links back to a Pillar landing page on livefrenchatelier.com · contributes to AI-SEO presence (ChatGPT/Perplexity citations).</div>
</div></section>''')

# ====================================================================
# CHAPTER 04 — BASTILLE DAY
# ====================================================================
slides.append(divider("04", "Bastille Day Campaign", "Win a Trip to France · July 14 · follower-acquisition"))

slides.append('''<section class="slide slide--dark slide--bastille"><div class="slide__inner slide--split">
  <div class="split-left">
    <div class="eyebrow eyebrow--gold">CHAPTER 04 · BASTILLE DAY · JULY 14</div>
    <h2 class="display display--md">Win a trip<br>to France.</h2>
    <p class="lead"><em class="gold">Follow · Tag · Win.</em></p>
    <p class="cover-meta">Drawn live July 14, 8pm Paris time.</p>
  </div>
  <div class="split-right">
    <h3 class="title title--sm">Campaign mechanics</h3><div class="rule"></div>
    <div class="mech-list">
      <div class="mech"><div class="mech-h">PRIZE</div><div class="mech-b">Long weekend in Paris · flights + 3 nights + private French lesson on-site.</div></div>
      <div class="mech"><div class="mech-h">ENTRY</div><div class="mech-b">Follow @frenchatelier · tag 2 friends · share to story.</div></div>
      <div class="mech"><div class="mech-h">WINDOW</div><div class="mech-b">June 24 → July 13 · drawn live July 14.</div></div>
      <div class="mech"><div class="mech-h">GOAL</div><div class="mech-b">+15K followers across IG/TikTok · 25% of monthly organic leads.</div></div>
    </div>
  </div>
</div></section>''')

# ====================================================================
# CHAPTER 05 — THE ASK
# ====================================================================
slides.append(divider("05", "The Ask", "From 1.9 → 2.5 weekly ROI · three levers · one quarter"))

slides.append('''<section class="slide slide--dark slide--ask"><div class="slide__inner">
  <h2 class="display display--md">From 1.9 to <span class="gold">2.5</span></h2>
  <p class="lead lead--muted">Three levers · one quarter</p>
  <div class="rule"></div>
  <div class="lever-grid">
    <div class="lever"><div class="lever-num">01</div><div class="lever-h">Organic lead growth</div><div class="lever-body">22 videos · 2 locked formats · 60 Quora/Reddit · Bastille follower drive</div><div class="lever-target gold">25%</div><div class="lever-sub">of total leads</div></div>
    <div class="lever"><div class="lever-num">02</div><div class="lever-h">Email lifecycle</div><div class="lever-body">15 emails live · 4 new flows · trial nurture · reactivation · Bastille countdown</div><div class="lever-target gold">+15%</div><div class="lever-sub">reactivation lift</div></div>
    <div class="lever"><div class="lever-num">03</div><div class="lever-h">Paid CPL efficiency</div><div class="lever-body">2 new cuts in late June · 4 total · maintain ≤ $14 with scale</div><div class="lever-target gold">$13.40</div><div class="lever-sub">current CPL</div></div>
  </div>
</div></section>''')

# CLOSING
slides.append('''<section class="slide slide--dark slide--closing"><div class="slide__inner">
  <h2 class="display">Speak, read,<br>and live French.</h2>
  <p class="lead"><em class="gold">From France.</em></p>
  <div class="rule"></div>
  <div class="cover-meta">French Atelier · by Acadomia · June 2026</div>
</div></section>''')

# ============== ASSEMBLE ==============
out_html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>French Atelier · CEO Briefing · v5</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/deck.css">
<link rel="stylesheet" href="css/platforms.css">
<link rel="stylesheet" href="css/sections.css">
<link rel="stylesheet" href="css/v2.css">
<link rel="stylesheet" href="css/v5.css">
</head>
<body class="deck-body">
<div class="deck">
{''.join(slides)}
</div>
<div class="nav-bar">
  <div class="nav-prev" onclick="goPrev()">←</div>
  <div class="nav-count"><span id="cur">1</span> / <span id="tot">{len(slides)}</span></div>
  <div class="nav-next" onclick="goNext()">→</div>
</div>
<script>
const slides=document.querySelectorAll('.slide');let idx=0;
function show(){{slides.forEach((s,i)=>s.classList.toggle('active',i===idx));document.getElementById('cur').textContent=idx+1;window.scrollTo({{top:slides[idx].offsetTop,behavior:'smooth'}});}}
function goNext(){{idx=Math.min(idx+1,slides.length-1);show();}}
function goPrev(){{idx=Math.max(idx-1,0);show();}}
document.addEventListener('keydown',e=>{{if(e.key==='ArrowRight'||e.key===' ')goNext();if(e.key==='ArrowLeft')goPrev();}});
</script>
</body></html>'''

with open(f'{ROOT}/index.html', 'w') as f:
  f.write(out_html)

print(f"Built v5 deck · {len(slides)} slides")
