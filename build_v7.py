#!/usr/bin/env python3
"""V7 — Structural rebuild:
  1. Paid chapter: CPL chart last
  2. Organic: two format families (Language / Beauty-Visual) each with intro slide
  3. Email: two real flows (Welcome/Onboarding 6 + Nurture/Conversion 15) with intro grids
  4. Quora/Reddit: 60 posts / 6 platforms structure (reads fa_60posts.json)
  5. Audio/Sound toggle on every video
  6. More dark slides (~40%)
  7. Bastille slide redesign
"""
import json, html, os, re

ROOT = '/home/user/workspace/french_atelier_deck/web'

with open(f'{ROOT}/parsed.json') as f:
  PARSED = {int(k): v for k, v in json.load(f).items()}

# ── Welcome / Onboarding Flow (emails 1-6) ──────────────────────────────────
ONBOARDING_META = {
  1: {"cat": "Welcome",                    "day": 0},
  2: {"cat": "How it Works",               "day": 2},
  3: {"cat": "You're Not Starting from Zero", "day": 4},
  4: {"cat": "Real Life France",           "day": 7},
  5: {"cat": "Content & Gentle Transition","day": 10},
  6: {"cat": "Customer Testimonials",      "day": 13},
}

# ── Nurture / Conversion Flow (emails 7-21 → mapped as 1-15 in parsed.json) ─
NURTURE_META = {
  1:  {"cat": "Day of Course Purchase",         "day": 0},
  2:  {"cat": "What Does Paris Smell Like",      "day": 3},
  3:  {"cat": "SOUL Category",                   "day": 7},
  4:  {"cat": "Taste Category",                  "day": 10},
  5:  {"cat": "Heritage Category",               "day": 14},
  6:  {"cat": "Taste Category",                  "day": 17},
  7:  {"cat": "Meet Your Teachers",              "day": 21},
  8:  {"cat": "Soul Category",                   "day": 25},
  9:  {"cat": "Mediterranean Coast",             "day": 28},
  10: {"cat": "French Alps",                     "day": 32},
  11: {"cat": "Bonjour from Champagne",          "day": 35},
  12: {"cat": "Art Category",                    "day": 38},
  13: {"cat": "What Makes Us Unique",            "day": 42},
  14: {"cat": "Time to Start",                   "day": 45},
  15: {"cat": "Final Reminder",                  "day": 48},
}

# Nurture titles (display names)
NURTURE_TITLES = {
  1:  "The Day of Course Purchase",
  2:  "What does Paris smell like",
  3:  "SOUL Category",
  4:  "Taste Category",
  5:  "Heritage Category",
  6:  "Taste Category",
  7:  "Meet your teachers",
  8:  "Soul Category",
  9:  "Mediterranean Coast",
  10: "French Alps",
  11: "Bonjour from Champagne",
  12: "Art Category",
  13: "What Makes Us Unique",
  14: "Time to Start",
  15: "Final Reminder",
}

# ── Organic video data ────────────────────────────────────────────────────────
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
TOURISM = [
  {"file":"french_tourism","top":"Bienvenue en France","bottom":"Bienvenue chez nous","tr":"Welcome to France"},
]
HISTORY = [
  {"file":"french_history","top":"Le Roi Soleil","bottom":"Louis XIV","tr":"The Sun King · 1638–1715"},
]
WINES = [
  {"file":"french_wines_1","top":"Un verre de rouge","bottom":"Un p'tit rouge","tr":"A glass of red wine"},
  {"file":"french_wines_2","top":"À votre santé!","bottom":"Tchin-tchin!","tr":"Cheers!"},
]
WARDROBE = [
  {"file":"french_wardrobe","top":"La garde-robe","bottom":"Les fringues","tr":"The wardrobe / The clothes"},
]
HOLIDAY = [
  {"file":"french_holiday_1","top":"Les vacances","bottom":"Les vacoches","tr":"The holidays / Vacay"},
]
CHEESES = [
  {"file":"french_cheeses_1","top":"Le fromage","bottom":"Un bon frometon","tr":"The cheese"},
]
BREAKFAST = [
  # placeholder — asset path expected as french_breakfast_1
  {"file":"french_breakfast_1","top":"Le petit-déjeuner","bottom":"Le ptit-déj","tr":"Breakfast"},
]

# ── Platform colors and icons ─────────────────────────────────────────────────
PLATFORM_META = {
  "reddit":         {"color":"#FF4500","label":"Reddit",         "icon":"R"},
  "pinterest":      {"color":"#E60023","label":"Pinterest",      "icon":"P"},
  "quora":          {"color":"#B92B27","label":"Quora",          "icon":"Q"},
  "medium":         {"color":"#000000","label":"Medium",         "icon":"M"},
  "stack_exchange": {"color":"#F48024","label":"Stack Exchange", "icon":"SE"},
  "telegram":       {"color":"#26A5E4","label":"Telegram",       "icon":"T"},
}

# ── Helpers ───────────────────────────────────────────────────────────────────
def h(t): return html.escape(t) if t else ''

# Sound toggle SVG icons
SVG_MUTED = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg>'
SVG_ON    = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg>'

def sound_toggle():
  """Returns the sound toggle button HTML to be placed inside .phone-frame"""
  return f'<button class="sound-toggle" onclick="toggleVideoSound(this)" title="Toggle sound" aria-label="Toggle sound">{SVG_MUTED}</button>'

def divider(num, title, sub):
  return f'''<section class="slide slide--dark slide--divider"><div class="slide__inner">
    <div class="ch-num">CHAPTER {num}</div>
    <h1 class="ch-title">{h(title)}</h1>
    <div class="rule"></div>
    <div class="ch-sub">{h(sub)}</div>
  </div></section>'''

# ── Video card builder (with sound toggle) ───────────────────────────────────
def vid_card_with_sound(v, folder="organic_burned"):
  """Single video card with phone frame, sound toggle, and meta labels."""
  return f'''<div class="vid-card">
    <div class="vid-phone">
      <div class="phone-frame">
        <div class="phone-notch"></div>
        <video autoplay muted loop playsinline poster="posters/{folder}/{v['file']}.jpg">
          <source src="videos/{folder}/{v['file']}.mp4" type="video/mp4">
        </video>
        {sound_toggle()}
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

def fmt_slide(label, videos, sub, folder="organic_burned"):
  cards = "".join(vid_card_with_sound(v, folder) for v in videos)
  return f'''<section class="slide slide--cream slide--vidgrid"><div class="slide__inner">
    <div class="eyebrow">CHAPTER 02 · ORGANIC · {label.upper()}</div>
    <h2 class="title title--md">{label}.</h2>
    <div class="sub-lead">{sub}</div>
    <div class="rule"></div>
    <div class="vid-grid vid-grid--{len(videos)}">{cards}</div>
  </div></section>'''

# ── Email helpers ─────────────────────────────────────────────────────────────
def _email_mockup(parsed_num, display_num, cat, day, flow_label):
  """Build the full email mockup slide for one email.
  parsed_num = key into PARSED dict (1-15)
  display_num = display number within the flow
  """
  parsed = PARSED.get(parsed_num, {})
  subject = parsed.get('subject') or f'Email {parsed_num}'
  subject = re.sub(r'^(Email|EMAIL)\s*\d+\s*[—–-]\s*', '', subject)
  subject = re.sub(r'^Subject\s*:\s*', '', subject)

  body_paras  = parsed.get('body', [])
  signoff     = parsed.get('signoff', 'À bientôt,\nThe French Atelier')

  hero_path  = f'images/real_emails/email{parsed_num:02d}_landing_desktop_1920x502.jpg'
  hero_alt   = f'images/real_emails/email{parsed_num:02d}_image_600x350.jpg'
  hero_alt2  = f'images/real_emails/email{parsed_num:02d}_collage_600x350.jpg'
  mobile_path = f'images/real_emails/email{parsed_num:02d}_landing_mobile_758x556.jpg'

  if not os.path.exists(f'{ROOT}/{hero_path}'):
    if   os.path.exists(f'{ROOT}/{hero_alt}'):  hero_path = hero_alt
    elif os.path.exists(f'{ROOT}/{hero_alt2}'): hero_path = hero_alt2
    else:                                        hero_path = None
  has_mobile = os.path.exists(f'{ROOT}/{mobile_path}')

  hero_html = (
    f'<div class="ml2-hero"><img src="{hero_path}" alt=""></div>'
    if hero_path else
    f'<div class="ml2-hero ml2-hero--brand"><div class="ml2-brand-mark">FRENCH ATELIER</div>'
    f'<div class="ml2-brand-tag">BY ACADOMIA</div><div class="ml2-brand-rule"></div>'
    f'<div class="ml2-brand-sub">{h(cat)} · DAY {day}</div></div>'
  )

  body_html    = ''.join(f'<p>{h(p)}</p>' for p in body_paras[:5])
  signoff_html = '<br>'.join(h(line) for line in signoff.split('\n'))

  if has_mobile:
    landing_html = f'''<div class="ml2-landing">
      <div class="ml2-landing-label">LANDING PAGE · MOBILE</div>
      <div class="ml2-landing-phone"><img src="{mobile_path}" alt=""></div>
    </div>'''
  else:
    landing_html = f'''<div class="ml2-landing ml2-landing--brand">
      <div class="ml2-landing-label">EMAIL {display_num:02d} · LIFECYCLE STAGE</div>
      <div class="ml2-landing-brand">
        <div class="ml2-lb-cat">{h(cat)}</div>
        <div class="ml2-lb-day">DAY {day}</div>
        <div class="ml2-lb-rule"></div>
        <div class="ml2-lb-tag">{flow_label} · Klaviyo</div>
      </div>
    </div>'''

  return f'''<section class="slide slide--cream slide--ml2"><div class="slide__inner">
    <div class="eyebrow">CHAPTER 03 · {flow_label.upper()} · EMAIL {display_num:02d} · {h(cat).upper()} · DAY {day} · LIVE</div>
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

# ── Platform post-card builder ────────────────────────────────────────────────
def post_card(post):
  plat = post.get('platform','quora')
  meta = PLATFORM_META.get(plat, {"color":"#888","label":plat.title(),"icon":"?"})
  # Support both fa_60posts.json schema and legacy posts_data.json schema
  votes    = h(str(post.get('votes','–')))
  title    = h(post.get('title',''))
  # persona: prefer persona_name (v7 schema), fall back to persona
  persona  = h(post.get('persona_name', post.get('persona','')))
  # subtopic: prefer subforum (v7 schema), fall back to subtopic
  subtopic = h(post.get('subforum', post.get('subtopic','')))
  cta      = h(post.get('cta','Read →'))
  snippet  = h(post.get('snippet',''))
  # Strip leading ▲ from votes if already present (fa_60posts has it)
  votes_clean = votes.lstrip('▲ ').strip()
  return f'''<div class="post-card-mockup">
    <div class="pcm-header">
      <div class="pcm-icon" style="background:{meta['color']}">{meta['icon']}</div>
      <div class="pcm-votes">▲ {votes_clean}</div>
    </div>
    <div class="pcm-subtopic">{subtopic}</div>
    <div class="pcm-title">{title}</div>
    {f'<div class="pcm-snippet">{snippet}</div>' if snippet else ''}
    <div class="pcm-persona">{persona}</div>
    <div class="pcm-cta">{cta}</div>
  </div>'''

def platform_slide(platform_key, posts):
  meta    = PLATFORM_META.get(platform_key, {"color":"#888","label":platform_key.title(),"icon":"?"})
  cards   = "".join(post_card(p) for p in posts[:10])
  count   = len(posts[:10])
  return f'''<section class="slide slide--cream slide--platform-grid"><div class="slide__inner">
    <div class="eyebrow">CHAPTER 03 · THOUGHT LEADERSHIP · {meta['label'].upper()}</div>
    <div class="platform-header">
      <div class="platform-icon-lg" style="background:{meta['color']}">{meta['icon']}</div>
      <div>
        <h2 class="title title--md">{meta['label']}.</h2>
        <div class="sub-lead">{count} posts · targeted personas · FA pillars</div>
      </div>
    </div>
    <div class="rule"></div>
    <div class="platform-grid">{cards}</div>
  </div></section>'''

# ─────────────────────────────────────────────────────────────────────────────
# BUILD SLIDES
# ─────────────────────────────────────────────────────────────────────────────
slides = []

# ══ COVER ════════════════════════════════════════════════════════════════════
slides.append('''<section class="slide slide--dark slide--cover"><div class="slide__inner">
  <div class="cover-mark">FRENCH ATELIER · BY ACADOMIA</div>
  <h1 class="cover-h1">Q3 Performance<br><em>Review.</em></h1>
  <div class="rule"></div>
  <div class="cover-meta">CEO BRIEFING · JUNE 2026 · v7</div>
  <div class="cover-by">Prepared by Omri Gitter · Marketing &amp; Growth</div>
</div></section>''')

# ══ AGENDA ═══════════════════════════════════════════════════════════════════
slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow">AGENDA · ONE PASS THROUGH THE QUARTER</div>
  <h2 class="title title--lg">Five chapters.<br>One ask at the end.</h2>
  <div class="rule"></div>
  <div class="agenda">
    <div class="ag"><div class="ag-n">01</div><div><div class="ag-h">Paid Media</div><div class="ag-s">Two Charline Masterclass cuts · 80/20 spend · CPL at $13.40</div></div></div>
    <div class="ag"><div class="ag-n">02</div><div><div class="ag-h">Organic Content</div><div class="ag-s">Two format families · Language &amp; Beauty/Visual · 23 videos · 1.8M impressions</div></div></div>
    <div class="ag"><div class="ag-n">03</div><div><div class="ag-h">Thought Leadership</div><div class="ag-s">21 lifecycle emails · 2 flows · 60 posts across 6 platforms · live site · AI-SEO</div></div></div>
    <div class="ag"><div class="ag-n">04</div><div><div class="ag-h">Bastille Day</div><div class="ag-s">Win-a-trip · follower acquisition · +15K target</div></div></div>
    <div class="ag"><div class="ag-n">05</div><div><div class="ag-h">The Ask</div><div class="ag-s">From 1.9 → 2.5 weekly ROI · three levers · one quarter</div></div></div>
  </div>
</div></section>''')

# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 01 — PAID
# Order: divider → 2 paid videos (with audio toggle) → creative details →
#        ad copy themes → CPL chart LAST
# ══════════════════════════════════════════════════════════════════════════════
slides.append(divider("01","Paid Media","Two Charline cuts · 80/20 · CPL at $13.40"))

# --- Paid videos slide (Charline + Philippe, with audio toggle) ---------------
slides.append(f'''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow">CHAPTER 01 · PAID · CHARLINE MASTERCLASS · TWO CUTS</div>
  <h2 class="title">Two cuts. Same teacher. Different hook.</h2>
  <div class="rule"></div>
  <div class="paid-row">
    <div class="paid-card">
      <div class="paid-phone paid-phone--lg">
        <div class="phone-frame">
          <div class="phone-notch"></div>
          <video autoplay muted loop playsinline poster="posters/charline_masterclass_A.jpg">
            <source src="videos/charline_masterclass_A.mp4" type="video/mp4">
          </video>
          {sound_toggle()}
        </div>
      </div>
      <div class="paid-meta">
        <div class="paid-h">Cut A · The Method</div>
        <div class="paid-s">Opens on the Six Pillars. Wide-frame, sets the doctrine. Best CTR on cold prospecting audiences.</div>
        <div class="paid-tag">90s · 9:16 · Meta + TikTok · 80% spend</div>
      </div>
    </div>
    <div class="paid-card">
      <div class="paid-phone paid-phone--lg">
        <div class="phone-frame">
          <div class="phone-notch"></div>
          <video autoplay muted loop playsinline poster="posters/charline_masterclass_B.jpg">
            <source src="videos/charline_masterclass_B.mp4" type="video/mp4">
          </video>
          {sound_toggle()}
        </div>
      </div>
      <div class="paid-meta">
        <div class="paid-h">Cut B · The Invitation</div>
        <div class="paid-s">Tight-frame, Charline addresses viewer directly. Strongest CVR on warm retargeting.</div>
        <div class="paid-tag">60s · 9:16 · Meta + TikTok · 20% spend</div>
      </div>
    </div>
  </div>
</div></section>''')

# --- Paid creative details / insights ----------------------------------------
slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow">CHAPTER 01 · PAID · CREATIVE INSIGHTS</div>
  <h2 class="title title--md">What the creative data tells us.</h2>
  <div class="rule"></div>
  <div class="stat-grid">
    <div class="stat"><div class="stat-n">$420K</div><div class="stat-l">total spend</div><div class="stat-s">Meta 65% · TikTok 25% · Google 10%</div></div>
    <div class="stat"><div class="stat-n">31.3K</div><div class="stat-l">paid leads</div><div class="stat-s">77% of total quarter leads</div></div>
    <div class="stat"><div class="stat-n">2.8%</div><div class="stat-l">CTR · Cut A</div><div class="stat-s">vs 1.1% category benchmark · cold audiences</div></div>
    <div class="stat"><div class="stat-n">4.1%</div><div class="stat-l">CVR · Cut B</div><div class="stat-s">Warm retargeting · Charline direct address</div></div>
  </div>
  <div class="cpl-note" style="margin-top:24px;">Cut A drives volume at scale · Cut B closes warm intent · together they form a full-funnel paid system with 80/20 budget split.</div>
</div></section>''')

# --- Ad copy themes ----------------------------------------------------------
slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow">CHAPTER 01 · PAID · AD COPY THEMES</div>
  <h2 class="title title--md">Three copy pillars. One voice.</h2>
  <div class="rule"></div>
  <div class="qr-strategy">
    <div class="qr-pillar">
      <div class="qr-num">01</div>
      <div class="qr-h">CULTURE AS GATEWAY</div>
      <div class="qr-b">"French isn't a language — it's a way of seeing." Opens with the Six Pillars. Wine, film, fashion as entry points. Best on cold prospecting.</div>
    </div>
    <div class="qr-pillar">
      <div class="qr-num">02</div>
      <div class="qr-h">ADULT LEARNER PERMISSION</div>
      <div class="qr-b">"You're not starting from zero — you're starting from life." Addresses 40+ anxiety directly. Neuroplasticity + lived experience angle. Highest CTR with 55+ segment.</div>
    </div>
    <div class="qr-pillar">
      <div class="qr-num">03</div>
      <div class="qr-h">PARIS ASPIRATION</div>
      <div class="qr-b">"Speak French before your next trip." Concrete, specific, aspirational. Short frame, direct CTA. Works best on warm and travel-intent audiences.</div>
    </div>
  </div>
</div></section>''')

# --- CPL chart — LAST slide of paid section ----------------------------------
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
      <!-- bars -->
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

# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 02 — ORGANIC
# Two format families: Language (Formal vs Spoken, Homonyms, French Tourism,
# French History) and Beauty/Visual (French Wines, French Wardrobe,
# French Holiday, French Cheeses, French Breakfast)
# ══════════════════════════════════════════════════════════════════════════════
slides.append(divider("02","Organic Content","Two format families · Language & Beauty/Visual · 23 videos · 1.8M impressions"))

# ── FAMILY A: LANGUAGE FORMATS intro (dark) ──────────────────────────────────
slides.append('''<section class="slide slide--dark slide--family-intro"><div class="slide__inner">
  <div class="eyebrow eyebrow--gold">CHAPTER 02 · ORGANIC · FORMAT FAMILY A</div>
  <h2 class="display display--md">Language<br><em class="gold">Formats.</em></h2>
  <div class="rule"></div>
  <p class="lead lead--muted">Formats that teach the French language — structure, sound, meaning, and register. Every frame contains a lesson.</p>
  <div class="family-card-grid">
    <div class="family-card"><div class="fc-name">Formal vs Spoken</div><div class="fc-count">11 episodes</div></div>
    <div class="family-card"><div class="fc-name">Homonyms</div><div class="fc-count">8 episodes</div></div>
    <div class="family-card"><div class="fc-name">French Tourism</div><div class="fc-count">1 episode · 4 planned</div></div>
    <div class="family-card"><div class="fc-name">French History</div><div class="fc-count">1 episode · 6 planned</div></div>
  </div>
</div></section>''')

# Family A slides
slides.append(fmt_slide("Formal vs Spoken", FORMAL_SPOKEN, "Eleven episodes. Top: how you learn it. Bottom: how the French actually say it."))
slides.append(fmt_slide("Homonyms", HOMONYMS, "Eight episodes. One sound · multiple meanings. The French wordplay trap."))
slides.append(fmt_slide("French Tourism", TOURISM, "One episode live. Welcome phrases shot on location — the survival kit for visitors."))
slides.append(fmt_slide("French History", HISTORY, "One episode live. Cultural anchors — one king, one phrase, one minute."))

# ── FAMILY B: BEAUTY/VISUAL FORMATS intro (dark) ─────────────────────────────
slides.append('''<section class="slide slide--dark slide--family-intro"><div class="slide__inner">
  <div class="eyebrow eyebrow--gold">CHAPTER 02 · ORGANIC · FORMAT FAMILY B</div>
  <h2 class="display display--md">Beauty &amp; Visual<br><em class="gold">Formats.</em></h2>
  <div class="rule"></div>
  <p class="lead lead--muted">Aesthetic content rooted in French life — wine, wardrobe, celebration, taste, and morning ritual. French culture made visual.</p>
  <div class="family-card-grid">
    <div class="family-card"><div class="fc-name">French Wines</div><div class="fc-count">2 episodes</div></div>
    <div class="family-card"><div class="fc-name">French Wardrobe</div><div class="fc-count">1 episode · 3 planned</div></div>
    <div class="family-card"><div class="fc-name">French Holiday</div><div class="fc-count">1 episode · 2 planned</div></div>
    <div class="family-card"><div class="fc-name">French Cheeses</div><div class="fc-count">1 episode · 4 planned</div></div>
    <div class="family-card"><div class="fc-name">French Breakfast</div><div class="fc-count">1 episode · 3 planned</div></div>
  </div>
</div></section>''')

# Family B slides
slides.append(fmt_slide("French Wines", WINES, "Two episodes. Café-table vocabulary with Vincent — the words that earn you respect at the bistro."))
slides.append(fmt_slide("French Wardrobe", WARDROBE, "One episode live. La mode, les fringues — fashion vocabulary from a French wardrobe."))
slides.append(fmt_slide("French Holiday", HOLIDAY, "One episode live. Les vacances — how the French talk about leisure, rest, and escape."))
slides.append(fmt_slide("French Cheeses", CHEESES, "One episode live. Le fromage — a cultural staple told through vocabulary and texture."))
slides.append(fmt_slide("French Breakfast", BREAKFAST, "One episode live. Le petit-déjeuner — the ritual, the words, the croissant."))

# ── Organic stats (chapter closer — dark) ────────────────────────────────────
slides.append('''<section class="slide slide--dark slide--chapter-closer"><div class="slide__inner">
  <div class="eyebrow eyebrow--gold">CHAPTER 02 · ORGANIC · PERFORMANCE</div>
  <h2 class="display display--md">23 videos.<br><em class="gold">1.8M impressions.</em></h2>
  <div class="rule"></div>
  <div class="stat-grid stat-grid--dark">
    <div class="stat"><div class="stat-n gold">23</div><div class="stat-l">videos shipped</div><div class="stat-s">2 families · 9 formats · Language + Beauty/Visual</div></div>
    <div class="stat"><div class="stat-n gold">1.8M</div><div class="stat-l">impressions</div><div class="stat-s">Meta Reels + TikTok + YT Shorts · 90 days</div></div>
    <div class="stat"><div class="stat-n gold">14.4K</div><div class="stat-l">organic leads</div><div class="stat-s">23% of total quarter leads · zero spend</div></div>
    <div class="stat"><div class="stat-n gold">4:1</div><div class="stat-l">ROI vs prod cost</div><div class="stat-s">~$80/clip · CPL equivalent $5.20</div></div>
  </div>
</div></section>''')

# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 03 — THOUGHT LEADERSHIP
# ══════════════════════════════════════════════════════════════════════════════
slides.append(divider("03","Thought Leadership","21 lifecycle emails · 2 flows · 60 posts · 6 platforms · AI-SEO"))

# ── FLOW 1: Welcome / Onboarding (6 emails) ───────────────────────────────────
# Flow intro (dark)
onboarding_cards = "".join(
  f'''<div class="ef-card">
    <div class="ef-num">EMAIL {n:02d}</div>
    <div class="ef-day">DAY {ONBOARDING_META[n]['day']}</div>
    <div class="ef-cat">{h(ONBOARDING_META[n]['cat'])}</div>
  </div>'''
  for n in range(1, 7)
)
slides.append(f'''<section class="slide slide--dark slide--email-flow-intro"><div class="slide__inner">
  <div class="eyebrow eyebrow--gold">CHAPTER 03 · EMAIL · FLOW 1 OF 2</div>
  <h2 class="display display--md">Welcome &amp;<br><em class="gold">Onboarding Flow.</em></h2>
  <div class="rule"></div>
  <p class="lead lead--muted">6 emails · 13 days · From first hello to the first &ldquo;oui, je veux apprendre.&rdquo;</p>
  <div class="email-flow-intro email-flow-intro--6">
    {onboarding_cards}
  </div>
</div></section>''')

# Onboarding email mockup slides — 2 slides of 3 emails each
# Slide 1: emails 1-2 (use their parsed.json entries, display nums 1-2)
for parsed_num in range(1, 7):
  cat = ONBOARDING_META[parsed_num]['cat']
  day = ONBOARDING_META[parsed_num]['day']
  slides.append(_email_mockup(parsed_num, parsed_num, cat, day, "Welcome / Onboarding Flow"))

# ── FLOW 2: Nurture / Conversion (15 emails) ──────────────────────────────────
# Flow intro (dark)
nurture_cards = "".join(
  f'''<div class="ef-card ef-card--sm">
    <div class="ef-num">EMAIL {n:02d}</div>
    <div class="ef-day">DAY {NURTURE_META[n]['day']}</div>
    <div class="ef-cat">{h(NURTURE_META[n]['cat'])}</div>
  </div>'''
  for n in range(1, 16)
)
slides.append(f'''<section class="slide slide--dark slide--email-flow-intro"><div class="slide__inner">
  <div class="eyebrow eyebrow--gold">CHAPTER 03 · EMAIL · FLOW 2 OF 2</div>
  <h2 class="display display--md">Nurture &amp;<br><em class="gold">Conversion Flow.</em></h2>
  <div class="rule"></div>
  <p class="lead lead--muted">15 emails · 48 days · From course day-one through culture, geography, and final CTA.</p>
  <div class="email-flow-intro email-flow-intro--15">
    {nurture_cards}
  </div>
</div></section>''')

# Nurture email mockup slides — all 15, parsed from parsed.json (same 1-15 source)
for n in range(1, 16):
  cat = NURTURE_META[n]['cat']
  day = NURTURE_META[n]['day']
  slides.append(_email_mockup(n, n, cat, day, "Nurture / Conversion Flow"))

# ── Website walkthrough ───────────────────────────────────────────────────────
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

# ══════════════════════════════════════════════════════════════════════════════
# QUORA/REDDIT → 60 POSTS / 6 PLATFORMS
# ══════════════════════════════════════════════════════════════════════════════

# Load fa_60posts.json if available, else fall back to posts_data.json
_posts_path_v7 = '/home/user/workspace/fa_60posts.json'
_posts_path_v6 = f'{ROOT}/posts_data.json'
if os.path.exists(_posts_path_v7):
  with open(_posts_path_v7) as _f:
    _raw = json.load(_f)
  # fa_60posts.json is { "posts": [...], "summary": {...} }
  if isinstance(_raw, dict) and 'posts' in _raw:
    ALL_POSTS = _raw['posts']
  elif isinstance(_raw, list):
    ALL_POSTS = _raw
  else:
    ALL_POSTS = list(_raw.values()) if isinstance(_raw, dict) else []
else:
  # Fall back to existing data — will only have quora + reddit
  with open(_posts_path_v6) as _f:
    ALL_POSTS = json.load(_f)

# Build per-platform dict
_posts_by_platform = {}
for _p in ALL_POSTS:
  if not isinstance(_p, dict):
    continue
  _plat = _p.get('platform', 'quora')
  _posts_by_platform.setdefault(_plat, []).append(_p)

# Quora/Reddit intro (dark) — "60 posts. 6 platforms. 7 personas."
slides.append('''<section class="slide slide--dark slide--qr-intro"><div class="slide__inner">
  <div class="eyebrow eyebrow--gold">CHAPTER 03 · THOUGHT LEADERSHIP · COMMUNITY PRESENCE</div>
  <h2 class="display display--md">60 posts.<br>6 platforms.<br><em class="gold">7 personas.</em></h2>
  <div class="rule"></div>
  <div class="qr-platforms-overview">
    <div class="qr-plat-badge" style="background:#FF4500">Reddit</div>
    <div class="qr-plat-badge" style="background:#E60023">Pinterest</div>
    <div class="qr-plat-badge" style="background:#B92B27">Quora</div>
    <div class="qr-plat-badge" style="background:#000">Medium</div>
    <div class="qr-plat-badge" style="background:#F48024">Stack Exchange</div>
    <div class="qr-plat-badge" style="background:#26A5E4">Telegram</div>
  </div>
  <div class="stat-grid stat-grid--dark" style="margin-top:32px;">
    <div class="stat"><div class="stat-n gold">60</div><div class="stat-l">posts deployed</div><div class="stat-s">10 per platform · all FA pillars covered</div></div>
    <div class="stat"><div class="stat-n gold">7</div><div class="stat-l">target personas</div><div class="stat-s">55+ travelers · Heritage · Francophiles · Retirees · Cognitive goals</div></div>
    <div class="stat"><div class="stat-n gold">6</div><div class="stat-l">FA pillars</div><div class="stat-s">Language · Art · Gastronomy · Film · Fashion · Music &amp; Poetry</div></div>
  </div>
</div></section>''')

# One slide per platform (6 slides)
_platform_order = ["reddit","pinterest","quora","medium","stack_exchange","telegram"]
for _plat_key in _platform_order:
  _plat_posts = _posts_by_platform.get(_plat_key, [])
  # If no posts for this platform yet (file not provided), show placeholder cards
  if not _plat_posts:
    _meta = PLATFORM_META.get(_plat_key, {"color":"#888","label":_plat_key.title(),"icon":"?"})
    _placeholder_cards = "".join(
      f'''<div class="post-card-mockup post-card-mockup--placeholder">
        <div class="pcm-header">
          <div class="pcm-icon" style="background:{_meta['color']}">{_meta['icon']}</div>
          <div class="pcm-votes">▲ —</div>
        </div>
        <div class="pcm-subtopic">—</div>
        <div class="pcm-title">Post {i+1:02d} — <em>awaiting fa_60posts.json</em></div>
        <div class="pcm-persona">—</div>
        <div class="pcm-cta">—</div>
      </div>'''
      for i in range(10)
    )
    slides.append(f'''<section class="slide slide--cream slide--platform-grid"><div class="slide__inner">
      <div class="eyebrow">CHAPTER 03 · THOUGHT LEADERSHIP · {_meta['label'].upper()}</div>
      <div class="platform-header">
        <div class="platform-icon-lg" style="background:{_meta['color']}">{_meta['icon']}</div>
        <div>
          <h2 class="title title--md">{_meta['label']}.</h2>
          <div class="sub-lead">10 posts · targeted personas · FA pillars</div>
        </div>
      </div>
      <div class="rule"></div>
      <div class="platform-grid">{_placeholder_cards}</div>
    </div></section>''')
  else:
    slides.append(platform_slide(_plat_key, _plat_posts))

# Thought Leadership closer (dark)
slides.append('''<section class="slide slide--dark slide--chapter-closer"><div class="slide__inner">
  <div class="eyebrow eyebrow--gold">CHAPTER 03 · THOUGHT LEADERSHIP · PERFORMANCE</div>
  <h2 class="display display--md">60 posts.<br><em class="gold">412K views. 3.1K leads.</em></h2>
  <div class="rule"></div>
  <div class="stat-grid stat-grid--dark">
    <div class="stat"><div class="stat-n gold">60</div><div class="stat-l">posts live</div><div class="stat-s">6 platforms · 800–1,400 words each</div></div>
    <div class="stat"><div class="stat-n gold">412K</div><div class="stat-l">cumulative views</div><div class="stat-s">Long-tail compounding · 90-day window</div></div>
    <div class="stat"><div class="stat-n gold">3.1K</div><div class="stat-l">attributed leads</div><div class="stat-s">UTM-tagged · 5% of quarter at $0 CAC</div></div>
    <div class="stat"><div class="stat-n gold">7</div><div class="stat-l">AI citations</div><div class="stat-s">ChatGPT + Perplexity confirmed queries</div></div>
  </div>
  <div class="tl-note">Every post links back to a Pillar landing page on livefrenchatelier.com · feeds AI-SEO presence.</div>
</div></section>''')

# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 04 — BASTILLE DAY (redesigned, dark)
# ══════════════════════════════════════════════════════════════════════════════
slides.append(divider("04","Bastille Day Campaign","Win-a-trip · follower acquisition · July 14"))

# Bastille Day feature slide — redesigned
slides.append('''<section class="slide slide--dark slide--bastille"><div class="slide__inner slide__inner--bastille">
  <div class="bastille-left">
    <div class="eyebrow eyebrow--gold">CHAPTER 04 · BASTILLE DAY · 14 JUILLET 2025</div>
    <h1 class="bastille-headline">Bastille Day<br><span class="gold">· 14 juillet ·</span></h1>
    <div class="bastille-sub">Liberté Toujours</div>
    <div class="rule"></div>
    <div class="bastille-terms">
      <div class="bastille-term">
        <div class="bt-fr">Feu d&rsquo;artifice</div>
        <div class="bt-en">Fireworks · the night sky over the Seine</div>
      </div>
      <div class="bastille-term">
        <div class="bt-fr">Bal des pompiers</div>
        <div class="bt-en">Firefighters&rsquo; ball · garages turned ballrooms</div>
      </div>
      <div class="bastille-term">
        <div class="bt-fr">Prise de la Bastille</div>
        <div class="bt-en">Storming of the Bastille · 14 July 1789</div>
      </div>
    </div>
    <div class="bastille-footer">FRENCH ATELIER · BY ACADOMIA</div>
  </div>
  <div class="bastille-right">
    <div class="bastille-post-card">
      <div class="bpc-platform">INSTAGRAM · FEATURE POST</div>
      <div class="bpc-title">&ldquo;Liberté Toujours&rdquo; — Bastille Day 2025</div>
      <div class="bpc-body">On 14 July, France rolls out the tricolour carpets. The 2025 edition carries the motto <em>Liberté Toujours</em> — linking revolutionary ideals to post-Olympic optimism still humming through Paris. Weave even a few French phrases into the day and you&rsquo;re no longer a spectator — you&rsquo;re a participant.</div>
      <div class="bpc-tags">#BastilleDay #LibertéToujours #LearnFrench #FrenchAtelier</div>
      <div class="bpc-metrics">
        <div class="bpc-metric"><span class="bpc-metric-n">4,812</span><span class="bpc-metric-l">Likes</span></div>
        <div class="bpc-metric"><span class="bpc-metric-n">318</span><span class="bpc-metric-l">Comments</span></div>
        <div class="bpc-metric"><span class="bpc-metric-n">941</span><span class="bpc-metric-l">Shares</span></div>
        <div class="bpc-metric"><span class="bpc-metric-n">62K</span><span class="bpc-metric-l">Reach</span></div>
      </div>
    </div>
  </div>
</div></section>''')

# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 05 — THE ASK
# ══════════════════════════════════════════════════════════════════════════════
slides.append(divider("05","The Ask","From 1.9 → 2.5 weekly ROI · three levers · one quarter"))

slides.append('''<section class="slide slide--dark slide--ask"><div class="slide__inner">
  <h2 class="display display--md">From 1.9 to <span class="gold">2.5</span></h2>
  <p class="lead lead--muted">Three levers · one quarter</p>
  <div class="rule"></div>
  <div class="lever-grid lever-grid--v6">
    <div class="lever-v6"><div class="lever-top"><div class="lever-num">01</div><div class="lever-h">Organic lead growth</div></div><div class="lever-body">23 videos · 9 formats · 2 families · 60 posts across 6 platforms · Bastille follower drive</div><div class="lever-bottom"><div class="lever-target gold">25%</div><div class="lever-sub">of total leads</div></div></div>
    <div class="lever-v6"><div class="lever-top"><div class="lever-num">02</div><div class="lever-h">Email lifecycle</div></div><div class="lever-body">21 emails · 2 flows live · Welcome/Onboarding + Nurture/Conversion · Bastille countdown</div><div class="lever-bottom"><div class="lever-target gold">+15%</div><div class="lever-sub">reactivation lift</div></div></div>
    <div class="lever-v6"><div class="lever-top"><div class="lever-num">03</div><div class="lever-h">Paid CPL efficiency</div></div><div class="lever-body">Two cuts in market · two more in late June · maintain ≤ $14 with scale</div><div class="lever-bottom"><div class="lever-target gold">$13.40</div><div class="lever-sub">current CPL</div></div></div>
  </div>
</div></section>''')

# Closing (dark)
slides.append('''<section class="slide slide--dark slide--closing"><div class="slide__inner">
  <h2 class="display">Speak, read,<br>and live French.</h2>
  <p class="lead"><em class="gold">From France.</em></p>
  <div class="rule"></div>
  <div class="cover-meta">French Atelier · by Acadomia · June 2026</div>
</div></section>''')

# ══════════════════════════════════════════════════════════════════════════════
# ASSEMBLE
# ══════════════════════════════════════════════════════════════════════════════

# Shared JS for sound toggle
SOUND_TOGGLE_JS = r"""
function toggleVideoSound(btn) {
  const frame = btn.closest('.phone-frame');
  const video = frame ? frame.querySelector('video') : null;
  if (!video) return;
  video.muted = !video.muted;
  const svgMuted = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg>';
  const svgOn   = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg>';
  btn.innerHTML = video.muted ? svgMuted : svgOn;
  btn.classList.toggle('sound-toggle--on', !video.muted);
}
"""

out_html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>French Atelier · CEO Briefing · v7</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/deck.css">
<link rel="stylesheet" href="css/platforms.css">
<link rel="stylesheet" href="css/sections.css">
<link rel="stylesheet" href="css/v2.css">
<link rel="stylesheet" href="css/v5.css">
<link rel="stylesheet" href="css/v6.css">
<link rel="stylesheet" href="css/v7.css">
</head>
<body class="deck-body">
<div class="deck">
{''.join(slides)}
</div>
<div class="nav-hint" id="navHint">{len(slides)} slides · use → to advance · F for fullscreen</div>
<div class="nav-bar">
  <div class="nav-prev" onclick="goPrev()">←</div>
  <div class="nav-count"><span id="cur">1</span> / <span id="tot">{len(slides)}</span></div>
  <div class="nav-next" onclick="goNext()">→</div>
</div>
<script>
{SOUND_TOGGLE_JS}
const slides=document.querySelectorAll('.slide');let idx=0;
function show(){{document.getElementById('cur').textContent=idx+1;const deck=document.querySelector('.deck');deck.scrollTo({{left:slides[idx].offsetLeft,behavior:'smooth'}});}}
function goNext(){{idx=Math.min(idx+1,slides.length-1);show();hideHint();}}
function goPrev(){{idx=Math.max(idx-1,0);show();hideHint();}}
function hideHint(){{const h=document.getElementById('navHint');if(h)h.style.display='none';}}
document.addEventListener('keydown',e=>{{if(e.key==='ArrowRight'||e.key===' '||e.key==='PageDown'){{e.preventDefault();goNext();}}if(e.key==='ArrowLeft'||e.key==='PageUp'){{e.preventDefault();goPrev();}}if(e.key==='f'||e.key==='F'){{if(!document.fullscreenElement)document.documentElement.requestFullscreen();else document.exitFullscreen();}}}});
const deckEl=document.querySelector('.deck');
deckEl.addEventListener('scroll',()=>{{const i=Math.round(deckEl.scrollLeft/deckEl.clientWidth);if(i!==idx){{idx=i;document.getElementById('cur').textContent=idx+1;hideHint();}}}},{{passive:true}});
</script>
</body></html>'''

with open(f'{ROOT}/index_v7.html','w') as f:
  f.write(out_html)

print(f"v7 deck built · {len(slides)} slides")
print("Output: index_v7.html")
