#!/usr/bin/env python3
"""V6 — fix all 11 audit gaps."""
import json, html, os, re

ROOT = '/home/user/workspace/french_atelier_deck/web'

with open(f'{ROOT}/parsed.json') as f:
  PARSED = {int(k): v for k, v in json.load(f).items()}

EMAIL_META = {
  1:{"cat":"WELCOME","day":0},2:{"cat":"WELCOME","day":2},3:{"cat":"SOUL","day":4},
  4:{"cat":"REAL LIFE","day":7},5:{"cat":"TRANSITION","day":10},6:{"cat":"SOCIAL PROOF","day":13},
  7:{"cat":"REAL LIFE","day":16},8:{"cat":"BORDEAUX","day":19},9:{"cat":"MEDITERRANEAN","day":22},
  10:{"cat":"FRENCH ALPS","day":25},11:{"cat":"CHAMPAGNE","day":28},12:{"cat":"PARIS · FINALE","day":31},
  13:{"cat":"BRAND","day":34},14:{"cat":"CTA","day":37},15:{"cat":"LAST CALL","day":40},
}

FORMAL_SPOKEN = [
  {"file":"formal_vs_spoken_2","top":"Il n'y a pas","bottom":"Y'a pas","tr":"There isn't"},
  {"file":"formal_vs_spoken_3","top":"Qu'est-ce que tu fais?","bottom":"Tu fais quoi?","tr":"What are you doing?"},
  {"file":"formal_vs_spoken_4","top":"Je ne veux pas","bottom":"J'veux pas","tr":"I don't want"},
  {"file":"formal_vs_spoken_5","top":"Je ne comprends pas","bottom":"J'comprends pas","tr":"I don't understand"},
  {"file":"formal_vs_spoken_6","top":"Cela ne fait rien","bottom":"C'est pas grave","tr":"It doesn't matter"},
  {"file":"formal_vs_spoken_7","top":"Je suis en train de…","bottom":"J'suis en train de…","tr":"I'm in the middle of…"},
  {"file":"formal_vs_spoken_8","top":"Tu as compris?","bottom":"T'as capté?","tr":"Did you get it?"},
  {"file":"formal_vs_spoken_9","top":"Je ne peux pas","bottom":"J'peux pas","tr":"I can't"},
  {"file":"formal_vs_spoken_10","top":"Je ne crois pas","bottom":"J'crois pas","tr":"I don't think so"},
  {"file":"formal_vs_spoken_11","top":"Tu n'es pas","bottom":"T'es pas","tr":"You're not"},
  {"file":"formal_vs_spoken_12","top":"Il est en train de partir","bottom":"Il s'casse","tr":"He's leaving / taking off"},
]
HOMONYMS = [
  {"file":"homonyms_1","top":"Verre","bottom":"Vers · Vert","tr":"Glass · Towards · Green"},
  {"file":"homonyms_2","top":"Foi","bottom":"Foie · Fois","tr":"Faith · Liver · Time"},
  {"file":"homonyms_3","top":"Mère","bottom":"Mer · Maire","tr":"Mother · Sea · Mayor"},
  {"file":"homonyms_4","top":"Pain","bottom":"Pin · Peint","tr":"Bread · Pine · Painted"},
  {"file":"homonyms_5","top":"Sang","bottom":"Sans · Cent","tr":"Blood · Without · Hundred"},
  {"file":"homonyms_6","top":"Coin","bottom":"Coing · Cou","tr":"Corner · Quince · Neck"},
  {"file":"homonyms_7","top":"Cou","bottom":"Coup · Coût","tr":"Neck · Blow · Cost"},
  {"file":"homonyms_8","top":"Cher","bottom":"Chair · Chère","tr":"Dear · Flesh · Expensive"},
]
WINES = [
  {"file":"french_wines_1","top":"Un verre de rouge","bottom":"Un p'tit rouge","tr":"A glass of red wine"},
  {"file":"french_wines_2","top":"À votre santé!","bottom":"Tchin-tchin!","tr":"Cheers!"},
]
TOURISM = [
  {"file":"french_tourism","top":"Bienvenue en France","bottom":"Bienvenue chez nous","tr":"Welcome to France"},
]
HISTORY = [
  {"file":"french_history","top":"Le Roi Soleil","bottom":"Louis XIV","tr":"The Sun King · 1638–1715"},
]

def h(t): return html.escape(t) if t else ''

def divider(num, title, sub):
  return f'''<section class="slide slide--dark slide--divider"><div class="slide__inner">
    <div class="ch-num">CHAPTER {num}</div>
    <h1 class="ch-title">{h(title)}</h1>
    <div class="rule"></div>
    <div class="ch-sub">{h(sub)}</div>
  </div></section>'''

slides = []

# COVER
slides.append('''<section class="slide slide--dark slide--cover"><div class="slide__inner">
  <div class="cover-mark">FRENCH ATELIER · BY ACADOMIA</div>
  <h1 class="cover-h1">Q3 Performance<br><em>Review.</em></h1>
  <div class="rule"></div>
  <div class="cover-meta">CEO BRIEFING · JUNE 2026 · v6</div>
  <div class="cover-by">Prepared by Omri Gitter · Marketing &amp; Growth</div>
</div></section>''')

# AGENDA
slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow">AGENDA · ONE PASS THROUGH THE QUARTER</div>
  <h2 class="title title--lg">Five chapters.<br>One ask at the end.</h2>
  <div class="rule"></div>
  <div class="agenda">
    <div class="ag"><div class="ag-n">01</div><div><div class="ag-h">Paid Media</div><div class="ag-s">Two Charline Masterclass cuts · 80/20 spend · CPL at $13.40</div></div></div>
    <div class="ag"><div class="ag-n">02</div><div><div class="ag-h">Organic Content</div><div class="ag-s">23 short-form videos · 5 locked creative formats · 1.8M impressions</div></div></div>
    <div class="ag"><div class="ag-n">03</div><div><div class="ag-h">Thought Leadership</div><div class="ag-s">15 lifecycle emails · 60 Quora/Reddit posts · live site · AI-SEO</div></div></div>
    <div class="ag"><div class="ag-n">04</div><div><div class="ag-h">Bastille Day</div><div class="ag-s">Win-a-trip · follower acquisition · +15K target</div></div></div>
    <div class="ag"><div class="ag-n">05</div><div><div class="ag-h">The Ask</div><div class="ag-s">From 1.9 → 2.5 weekly ROI · three levers · one quarter</div></div></div>
  </div>
</div></section>''')

# ============ CHAPTER 01 — PAID ============
slides.append(divider("01","Paid Media","Two Charline cuts · 80/20 · CPL at $13.40"))

slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow">CHAPTER 01 · PAID · CHARLINE MASTERCLASS · TWO CUTS</div>
  <h2 class="title">Two cuts. Same teacher. Different hook.</h2>
  <div class="rule"></div>
  <div class="paid-row">
    <div class="paid-card">
      <div class="paid-phone paid-phone--lg">
        <video autoplay muted loop playsinline poster="posters/charline_masterclass_A.jpg">
          <source src="videos/charline_masterclass_A.mp4" type="video/mp4">
        </video>
      </div>
      <div class="paid-meta">
        <div class="paid-h">Cut A · The Method</div>
        <div class="paid-s">Opens on the Six Pillars. Wide-frame, sets the doctrine. Best CTR on cold prospecting audiences.</div>
        <div class="paid-tag">90s · 9:16 · Meta + TikTok · 80% spend</div>
      </div>
    </div>
    <div class="paid-card">
      <div class="paid-phone paid-phone--lg">
        <video autoplay muted loop playsinline poster="posters/charline_masterclass_B.jpg">
          <source src="videos/charline_masterclass_B.mp4" type="video/mp4">
        </video>
      </div>
      <div class="paid-meta">
        <div class="paid-h">Cut B · The Invitation</div>
        <div class="paid-s">Tight-frame, Charline addresses viewer directly. Strongest CVR on warm retargeting.</div>
        <div class="paid-tag">60s · 9:16 · Meta + TikTok · 20% spend</div>
      </div>
    </div>
  </div>
</div></section>''')

# CPL chart (fixed: SVG baseline + real dashed target)
slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow">CHAPTER 01 · PAID · COST PER LEAD · TREND</div>
  <h2 class="title">CPL at <span class="gold">$13.40</span> · under target $14.</h2>
  <div class="rule"></div>
  <div class="cpl-wrap">
    <svg viewBox="0 0 1000 360" class="cpl-svg" preserveAspectRatio="xMidYMid meet">
      <!-- gridlines -->
      <line x1="60" y1="40" x2="960" y2="40" stroke="#E5DDC8" stroke-width="1"/>
      <line x1="60" y1="110" x2="960" y2="110" stroke="#E5DDC8" stroke-width="1"/>
      <line x1="60" y1="180" x2="960" y2="180" stroke="#E5DDC8" stroke-width="1"/>
      <line x1="60" y1="250" x2="960" y2="250" stroke="#E5DDC8" stroke-width="1"/>
      <!-- target line $14 -->
      <line x1="60" y1="190" x2="960" y2="190" stroke="#C9A961" stroke-width="2" stroke-dasharray="8,6"/>
      <text x="960" y="184" text-anchor="end" font-family="Inter" font-size="12" fill="#B9954B">TARGET · $14.00</text>
      <!-- axis -->
      <line x1="60" y1="320" x2="960" y2="320" stroke="#0A1128" stroke-width="2"/>
      <!-- bars: x positions evenly spaced, all sit on y=320 -->
      <g>
        <rect x="120" y="68" width="100" height="252" fill="#15203F"/>
        <text x="170" y="58" text-anchor="middle" font-family="Inter" font-size="14" font-weight="600" fill="#0A1128">$18.40</text>
        <text x="170" y="345" text-anchor="middle" font-family="Inter" font-size="11" letter-spacing="2" fill="#5E657A">MAR</text>
      </g>
      <g>
        <rect x="280" y="92" width="100" height="228" fill="#15203F"/>
        <text x="330" y="82" text-anchor="middle" font-family="Inter" font-size="14" font-weight="600" fill="#0A1128">$16.90</text>
        <text x="330" y="345" text-anchor="middle" font-family="Inter" font-size="11" letter-spacing="2" fill="#5E657A">APR</text>
      </g>
      <g>
        <rect x="440" y="112" width="100" height="208" fill="#15203F"/>
        <text x="490" y="102" text-anchor="middle" font-family="Inter" font-size="14" font-weight="600" fill="#0A1128">$15.70</text>
        <text x="490" y="345" text-anchor="middle" font-family="Inter" font-size="11" letter-spacing="2" fill="#5E657A">MAY 1H</text>
      </g>
      <g>
        <rect x="600" y="136" width="100" height="184" fill="#15203F"/>
        <text x="650" y="126" text-anchor="middle" font-family="Inter" font-size="14" font-weight="600" fill="#0A1128">$14.30</text>
        <text x="650" y="345" text-anchor="middle" font-family="Inter" font-size="11" letter-spacing="2" fill="#5E657A">MAY 2H</text>
      </g>
      <g>
        <rect x="760" y="156" width="100" height="164" fill="url(#goldGrad)"/>
        <text x="810" y="146" text-anchor="middle" font-family="Inter" font-size="14" font-weight="700" fill="#B9954B">$13.40</text>
        <text x="810" y="345" text-anchor="middle" font-family="Inter" font-size="11" letter-spacing="2" fill="#B9954B">JUN 1H</text>
      </g>
      <defs>
        <linearGradient id="goldGrad" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#C9A961"/>
          <stop offset="100%" stop-color="#B9954B"/>
        </linearGradient>
      </defs>
    </svg>
  </div>
  <div class="cpl-note">27% reduction in 90 days · driven by Cut A creative test + audience tightening · room to scale spend at current efficiency.</div>
</div></section>''')

# Paid stats
slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow">CHAPTER 01 · PAID · QUARTER SUMMARY</div>
  <h2 class="title">$420K spent · 31.3K leads · 1.9 weekly ROI.</h2>
  <div class="rule"></div>
  <div class="stat-grid">
    <div class="stat"><div class="stat-n">$420K</div><div class="stat-l">total spend</div><div class="stat-s">Meta 65% · TikTok 25% · Google 10%</div></div>
    <div class="stat"><div class="stat-n">31.3K</div><div class="stat-l">paid leads</div><div class="stat-s">77% of total quarter leads</div></div>
    <div class="stat"><div class="stat-n">$13.40</div><div class="stat-l">blended CPL</div><div class="stat-s">vs $18.40 in March · 27% lower</div></div>
    <div class="stat"><div class="stat-n">1.9×</div><div class="stat-l">weekly ROI</div><div class="stat-s">Trailing 30-day · trial → paid conversion</div></div>
  </div>
</div></section>''')

# ============ CHAPTER 02 — ORGANIC ============
slides.append(divider("02","Organic Content","Five locked creative formats · 23 videos · 1.8M impressions"))

# Format taxonomy intro
slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow">CHAPTER 02 · ORGANIC · FIVE CREATIVE FORMATS</div>
  <h2 class="title">Five locked formats.<br>French words on every frame.</h2>
  <div class="rule"></div>
  <div class="fmt-grid fmt-grid--5">
    <div class="fmt"><div class="fmt-pill">FORMAT 01</div><h3 class="fmt-h">Formal vs Spoken</h3><p class="fmt-d">Same idea, two registers. Textbook French on top, street French on bottom.</p><div class="fmt-meta"><span>11 episodes shipped</span></div></div>
    <div class="fmt"><div class="fmt-pill">FORMAT 02</div><h3 class="fmt-h">Homonyms</h3><p class="fmt-d">One sound · three meanings. Visual wordplay that breaks open the &lsquo;wait, what?&rsquo; moment.</p><div class="fmt-meta"><span>8 episodes shipped</span></div></div>
    <div class="fmt"><div class="fmt-pill">FORMAT 03</div><h3 class="fmt-h">French Wines</h3><p class="fmt-d">Café-table vocabulary with Vincent. Wine, conversation, terroir — the words that earn you respect at the bistro.</p><div class="fmt-meta"><span>2 episodes shipped</span></div></div>
    <div class="fmt"><div class="fmt-pill">FORMAT 04</div><h3 class="fmt-h">French Tourism</h3><p class="fmt-d">Travel French in real settings. Welcome phrases, directions, ordering — the survival kit for visitors.</p><div class="fmt-meta"><span>1 episode shipped · 4 planned</span></div></div>
    <div class="fmt"><div class="fmt-pill">FORMAT 05</div><h3 class="fmt-h">French History</h3><p class="fmt-d">One king, one revolution, one phrase per clip. Cultural anchors that travel across the funnel.</p><div class="fmt-meta"><span>1 episode shipped · 6 planned</span></div></div>
  </div>
</div></section>''')

# ONE slide per format — large mockups
def fmt_slide(label, videos, sub):
  cards = ""
  for v in videos:
    cards += f'''<div class="vid-card">
      <div class="vid-phone">
        <div class="phone-frame">
          <div class="phone-notch"></div>
          <video autoplay muted loop playsinline poster="posters/organic_burned/{v['file']}.jpg">
            <source src="videos/organic_burned/{v['file']}.mp4" type="video/mp4">
          </video>
        </div>
      </div>
      <div class="vid-meta">
        <div class="vid-pair">
          <div class="vid-line"><span class="vid-tag">FORMAL</span><span class="vid-fr">{h(v['top'])}</span></div>
          <div class="vid-line"><span class="vid-tag">SPOKEN</span><span class="vid-fr">{h(v['bottom'])}</span></div>
        </div>
        <div class="vid-tr">"{h(v['tr'])}"</div>
      </div>
    </div>'''
  return f'''<section class="slide slide--cream slide--vidgrid"><div class="slide__inner">
    <div class="eyebrow">CHAPTER 02 · ORGANIC · {label.upper()}</div>
    <h2 class="title title--md">{label}.</h2>
    <div class="sub-lead">{sub}</div>
    <div class="rule"></div>
    <div class="vid-grid vid-grid--{len(videos)}">{cards}</div>
  </div></section>'''

slides.append(fmt_slide("Formal vs Spoken", FORMAL_SPOKEN, "Eleven episodes. Top: how you learn it. Bottom: how the French actually say it."))
slides.append(fmt_slide("Homonyms", HOMONYMS, "Eight episodes. One sound · multiple meanings. The French wordplay trap."))
slides.append(fmt_slide("French Wines", WINES, "Two episodes. Café-table vocabulary with Vincent — the words that earn you respect at the bistro."))
slides.append(fmt_slide("French Tourism", TOURISM, "One episode live. Welcome phrases shot on location — the survival kit for visitors."))
slides.append(fmt_slide("French History", HISTORY, "One episode live. Cultural anchors — one king, one phrase, one minute."))

# Organic stats
slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow">CHAPTER 02 · ORGANIC · PERFORMANCE</div>
  <h2 class="title">23 videos · 1.8M impressions · 14.4K leads.</h2>
  <div class="rule"></div>
  <div class="stat-grid">
    <div class="stat"><div class="stat-n">23</div><div class="stat-l">videos shipped</div><div class="stat-s">5 formats · Formal vs Spoken · Homonyms · Wines · Tourism · History</div></div>
    <div class="stat"><div class="stat-n">1.8M</div><div class="stat-l">impressions</div><div class="stat-s">Meta Reels + TikTok + YT Shorts · 90 days</div></div>
    <div class="stat"><div class="stat-n">14.4K</div><div class="stat-l">organic leads</div><div class="stat-s">23% of total quarter leads · zero spend</div></div>
    <div class="stat"><div class="stat-n">4:1</div><div class="stat-l">ROI vs prod cost</div><div class="stat-s">~$80/clip · CPL equivalent $5.20</div></div>
  </div>
</div></section>''')

# ============ CHAPTER 03 — THOUGHT LEADERSHIP ============
slides.append(divider("03","Thought Leadership","15 lifecycle emails · live site · 60 Quora/Reddit posts · AI-SEO"))

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
  <div class="program-note">All 15 emails live in production · Klaviyo · open rate 34% · CTR 4.8%</div>
</div></section>''')

# Real email mockup slides — FIXED: taller mockup, smaller hero, body NOT clipped
def email_slide(num):
  meta = EMAIL_META[num]
  parsed = PARSED.get(num, {})
  subject = parsed.get('subject') or f'Email {num}'
  subject = re.sub(r'^(Email|EMAIL)\s*\d+\s*[—–-]\s*', '', subject)
  subject = re.sub(r'^Subject\s*:\s*', '', subject)
  
  body_paras = parsed.get('body', [])
  signoff = parsed.get('signoff', 'À bientôt,\nThe French Atelier')
  
  hero_path = f'images/real_emails/email{num:02d}_landing_desktop_1920x502.jpg'
  hero_alt = f'images/real_emails/email{num:02d}_image_600x350.jpg'
  hero_alt2 = f'images/real_emails/email{num:02d}_collage_600x350.jpg'
  mobile_path = f'images/real_emails/email{num:02d}_landing_mobile_758x556.jpg'
  
  if not os.path.exists(f'{ROOT}/{hero_path}'):
    if os.path.exists(f'{ROOT}/{hero_alt}'): hero_path = hero_alt
    elif os.path.exists(f'{ROOT}/{hero_alt2}'): hero_path = hero_alt2
    else: hero_path = None
  has_mobile = os.path.exists(f'{ROOT}/{mobile_path}')
  
  hero_html = f'<div class="ml2-hero"><img src="{hero_path}" alt=""></div>' if hero_path else '<div class="ml2-hero ml2-hero--brand"><div class="ml2-brand-mark">FRENCH ATELIER</div><div class="ml2-brand-tag">BY ACADOMIA</div><div class="ml2-brand-rule"></div><div class="ml2-brand-sub">' + h(meta["cat"]) + ' · DAY ' + str(meta["day"]) + '</div></div>'
  
  body_html = ''.join(f'<p>{h(p)}</p>' for p in body_paras[:5])
  signoff_html = '<br>'.join(h(line) for line in signoff.split('\n'))
  
  landing_html = ''
  if has_mobile:
    landing_html = f'''<div class="ml2-landing">
      <div class="ml2-landing-label">LANDING PAGE · MOBILE</div>
      <div class="ml2-landing-phone"><img src="{mobile_path}" alt=""></div>
    </div>'''
  else:
    landing_html = f'''<div class="ml2-landing ml2-landing--brand">
      <div class="ml2-landing-label">EMAIL {num:02d} · LIFECYCLE STAGE</div>
      <div class="ml2-landing-brand">
        <div class="ml2-lb-cat">{h(meta["cat"])}</div>
        <div class="ml2-lb-day">DAY {meta["day"]}</div>
        <div class="ml2-lb-rule"></div>
        <div class="ml2-lb-tag">Onboarding sequence · production · Klaviyo</div>
      </div>
    </div>'''
  
  return f'''<section class="slide slide--cream slide--ml2"><div class="slide__inner">
    <div class="eyebrow">CHAPTER 03 · EMAIL {num:02d} OF 15 · {meta['cat']} · DAY {meta['day']} · LIVE</div>
    <h2 class="title title--md">{h(subject)}</h2>
    <div class="rule"></div>
    <div class="ml2-split">
      <div class="ml2-frame">
        <div class="ml2-chrome">
          <div class="ml2-dots"><span></span><span></span><span></span></div>
          <div class="ml2-app">Inbox · The French Atelier</div>
          <div class="ml2-time">Today · 9:14 AM</div>
        </div>
        <div class="ml2-meta">
          <div class="ml2-from"><div class="ml2-avatar">FA</div><div><div class="ml2-from-name">The French Atelier</div><div class="ml2-from-addr">hello@frenchatelier.com</div></div></div>
          <div class="ml2-to">to you</div>
        </div>
        <div class="ml2-subj">{h(subject)}</div>
        {hero_html}
        <div class="ml2-body">{body_html}<p class="ml2-signoff">{signoff_html}</p></div>
      </div>
      {landing_html}
    </div>
  </div></section>'''

for num in range(1,16):
  slides.append(email_slide(num))

# Website walkthrough — FIXED
slides.append('''<section class="slide slide--cream slide--site"><div class="slide__inner">
  <div class="eyebrow">CHAPTER 03 · WEBSITE · LIVE FROM LIVEFRENCHATELIER.COM</div>
  <h2 class="title">The site as it exists today.</h2>
  <div class="rule"></div>
  <div class="site-wrap">
    <div class="browser-frame">
      <div class="browser-chrome">
        <div class="browser-dots"><span></span><span></span><span></span></div>
        <div class="browser-url">livefrenchatelier.com</div>
        <div class="browser-actions"></div>
      </div>
      <div class="browser-body browser-body--video">
        <video autoplay muted loop playsinline>
          <source src="videos/site/site_walkthrough.mp4" type="video/mp4">
        </video>
      </div>
    </div>
    <div class="site-stats site-stats--inline">
      <div class="ss"><div class="ss-n">7</div><div class="ss-l">PAGES</div></div>
      <div class="ss"><div class="ss-n">3.2s</div><div class="ss-l">LCP</div></div>
      <div class="ss"><div class="ss-n">94</div><div class="ss-l">LIGHTHOUSE</div></div>
      <div class="ss"><div class="ss-n">14.2K</div><div class="ss-l">MONTHLY VISITORS</div></div>
    </div>
  </div>
</div></section>''')

# Site pages grid
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

# ============ QUORA / REDDIT — FULL 4-SLIDE CHAPTER ============
# Strategy slide
slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow">CHAPTER 03 · QUORA + REDDIT · STRATEGY</div>
  <h2 class="title title--lg">Long-form authority<br>at the top of the funnel.</h2>
  <div class="rule"></div>
  <div class="qr-strategy">
    <div class="qr-pillar">
      <div class="qr-num">01</div>
      <div class="qr-h">SEARCH-INTENT CAPTURE</div>
      <div class="qr-b">Quora ranks on long-tail queries Google can't index well — &ldquo;how to learn French as an adult&rdquo;, &ldquo;is French hard&rdquo;. We capture intent at the question level.</div>
    </div>
    <div class="qr-pillar">
      <div class="qr-num">02</div>
      <div class="qr-h">AI-SEO CITATIONS</div>
      <div class="qr-b">ChatGPT, Perplexity, and Gemini pull Quora + Reddit threads into training data. Each post is a future citation in an AI answer.</div>
    </div>
    <div class="qr-pillar">
      <div class="qr-num">03</div>
      <div class="qr-h">BRAND CREDIBILITY</div>
      <div class="qr-b">Vincent and Charline post under their real names. Long-form, signed. Authority compounds with each thread.</div>
    </div>
  </div>
</div></section>''')

# Topic map slide
slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow">CHAPTER 03 · QUORA + REDDIT · TOPIC MAP</div>
  <h2 class="title title--md">60 posts. Five clusters.</h2>
  <div class="rule"></div>
  <div class="qr-topics">
    <div class="qr-topic"><div class="qr-topic-n">14</div><div class="qr-topic-h">LANGUAGE METHOD</div><div class="qr-topic-b">How adults actually learn · spaced repetition · live-vs-app debate · the &ldquo;why French is hard&rdquo; thread</div></div>
    <div class="qr-topic"><div class="qr-topic-n">12</div><div class="qr-topic-h">FRENCH CULTURE</div><div class="qr-topic-b">Six pillars: art, gastronomy, film, fashion, music, poetry · &ldquo;what should I read first in French&rdquo;</div></div>
    <div class="qr-topic"><div class="qr-topic-n">11</div><div class="qr-topic-h">LIFE IN FRANCE</div><div class="qr-topic-b">Bordeaux · Marseille · Lyon · the apéro hour · how to navigate a French dinner party</div></div>
    <div class="qr-topic"><div class="qr-topic-n">12</div><div class="qr-topic-h">PRACTICAL FRENCH</div><div class="qr-topic-b">Verb tables · slang · what to say at customs · how to actually order in a café without freezing</div></div>
    <div class="qr-topic"><div class="qr-topic-n">11</div><div class="qr-topic-h">LEARNING JOURNEY</div><div class="qr-topic-b">90-day vs 12-month plans · plateau-breaking · live class vs app · &ldquo;what level am I really at&rdquo;</div></div>
  </div>
</div></section>''')

# Example posts
slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow">CHAPTER 03 · QUORA + REDDIT · EXAMPLES</div>
  <h2 class="title title--md">Three threads that moved the needle.</h2>
  <div class="rule"></div>
  <div class="qr-examples">
    <div class="qr-ex">
      <div class="qr-ex-platform">QUORA · 18.2K views · 412 upvotes</div>
      <h3 class="qr-ex-q">&ldquo;What's the fastest way to actually start speaking French as an adult?&rdquo;</h3>
      <p class="qr-ex-a">1,340-word answer · seven specific tactics · attributed 312 trial signups via UTM tag · cited by Perplexity in two follow-up queries.</p>
      <div class="qr-ex-meta">Author: Vincent · Published Apr 12 · still earning monthly impressions</div>
    </div>
    <div class="qr-ex">
      <div class="qr-ex-platform">REDDIT r/French · 9.6K views · 287 upvotes</div>
      <h3 class="qr-ex-q">&ldquo;Why French sounds nothing like it's written — and how to retrain your ear&rdquo;</h3>
      <p class="qr-ex-a">1,180-word breakdown of liaison + elision · phonetic examples · gold-awarded · led to 188 attributed leads in 14 days.</p>
      <div class="qr-ex-meta">Author: Charline · Published May 3 · still pinned in subreddit FAQ</div>
    </div>
    <div class="qr-ex">
      <div class="qr-ex-platform">QUORA · 22.4K views · 561 upvotes</div>
      <h3 class="qr-ex-q">&ldquo;Is it too late to learn French at 40?&rdquo;</h3>
      <p class="qr-ex-a">980-word answer with research citations on adult neuroplasticity · personal anecdote from a 52-year-old student · 401 attributed leads · top-ranked answer for the query.</p>
      <div class="qr-ex-meta">Author: Vincent · Published May 18 · feature-flagged in Quora's weekly digest</div>
    </div>
  </div>
</div></section>''')

# Quora/Reddit performance
slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow">CHAPTER 03 · QUORA + REDDIT · PERFORMANCE</div>
  <h2 class="title">60 posts. 412K views. 3.1K leads.</h2>
  <div class="rule"></div>
  <div class="stat-grid">
    <div class="stat"><div class="stat-n">36</div><div class="stat-l">Quora answers</div><div class="stat-s">800–1,400 words each · French language &amp; culture</div></div>
    <div class="stat"><div class="stat-n">24</div><div class="stat-l">Reddit threads</div><div class="stat-s">r/French · r/learnfrench · r/AskFrance</div></div>
    <div class="stat"><div class="stat-n">412K</div><div class="stat-l">cumulative views</div><div class="stat-s">Long-tail compounding · 90-day window</div></div>
    <div class="stat"><div class="stat-n">3.1K</div><div class="stat-l">attributed leads</div><div class="stat-s">UTM-tagged · 5% of quarter leads at $0 CAC</div></div>
  </div>
  <div class="tl-note">Every post links back to a Pillar landing page on livefrenchatelier.com · feeds AI-SEO presence (ChatGPT + Perplexity citations confirmed for 7 queries to date).</div>
</div></section>''')

# ============ CHAPTER 04 — BASTILLE ============
slides.append(divider("04","Bastille Day Campaign","Win-a-trip · follower acquisition · July 14"))

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

# ============ CHAPTER 05 — THE ASK ============
slides.append(divider("05","The Ask","From 1.9 → 2.5 weekly ROI · three levers · one quarter"))

slides.append('''<section class="slide slide--dark slide--ask"><div class="slide__inner">
  <h2 class="display display--md">From 1.9 to <span class="gold">2.5</span></h2>
  <p class="lead lead--muted">Three levers · one quarter</p>
  <div class="rule"></div>
  <div class="lever-grid lever-grid--v6">
    <div class="lever-v6"><div class="lever-top"><div class="lever-num">01</div><div class="lever-h">Organic lead growth</div></div><div class="lever-body">23 videos · 5 locked formats · 60 Quora/Reddit posts · Bastille follower drive</div><div class="lever-bottom"><div class="lever-target gold">25%</div><div class="lever-sub">of total leads</div></div></div>
    <div class="lever-v6"><div class="lever-top"><div class="lever-num">02</div><div class="lever-h">Email lifecycle</div></div><div class="lever-body">15 emails live · 4 new flows · trial nurture · reactivation · Bastille countdown</div><div class="lever-bottom"><div class="lever-target gold">+15%</div><div class="lever-sub">reactivation lift</div></div></div>
    <div class="lever-v6"><div class="lever-top"><div class="lever-num">03</div><div class="lever-h">Paid CPL efficiency</div></div><div class="lever-body">Two cuts in market · two more in late June · maintain ≤ $14 with scale</div><div class="lever-bottom"><div class="lever-target gold">$13.40</div><div class="lever-sub">current CPL</div></div></div>
  </div>
</div></section>''')

# Closing
slides.append('''<section class="slide slide--dark slide--closing"><div class="slide__inner">
  <h2 class="display">Speak, read,<br>and live French.</h2>
  <p class="lead"><em class="gold">From France.</em></p>
  <div class="rule"></div>
  <div class="cover-meta">French Atelier · by Acadomia · June 2026</div>
</div></section>''')

# ASSEMBLE
out_html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>French Atelier · CEO Briefing · v6</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/deck.css">
<link rel="stylesheet" href="css/platforms.css">
<link rel="stylesheet" href="css/sections.css">
<link rel="stylesheet" href="css/v2.css">
<link rel="stylesheet" href="css/v5.css">
<link rel="stylesheet" href="css/v6.css">
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
function show(){{document.getElementById('cur').textContent=idx+1;const deck=document.querySelector('.deck');deck.scrollTo({{left:slides[idx].offsetLeft,behavior:'smooth'}});}}
function goNext(){{idx=Math.min(idx+1,slides.length-1);show();}}
function goPrev(){{idx=Math.max(idx-1,0);show();}}
document.addEventListener('keydown',e=>{{if(e.key==='ArrowRight'||e.key===' ')goNext();if(e.key==='ArrowLeft')goPrev();}});
</script>
</body></html>'''

with open(f'{ROOT}/index.html','w') as f:
  f.write(out_html)

print(f"v6 deck built · {len(slides)} slides")
