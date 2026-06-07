import os, json

ROOT = "/home/user/workspace/french_atelier_deck/web"
posts = json.load(open(f"{ROOT}/posts_data.json"))

videos = sorted([f for f in os.listdir(f"{ROOT}/videos") if f.endswith(".mp4")])
ig_videos = [v.replace(".mp4","") for v in videos if v.startswith("french_") and "site" not in v]
tt_videos = [v.replace(".mp4","") for v in videos if v.startswith("homonyms_") or v.startswith("formal_vs_spoken_")]

# Headlines per video
HEADLINES = {
  "french_wardrobe": ("La garde-robe parisienne","How Parisian women actually dress — 5 rules they never break."),
  "french_holiday_1": ("Vacances à la française","Where the French actually go in August (it's not Paris)."),
  "french_wines_1": ("Bordeaux for beginners","French wine without the snobbery — start here."),
  "french_wines_2": ("Le terroir","Why French wine tastes like the place it's from."),
  "french_history": ("Une histoire de France","60 seconds of French history that changed Europe."),
  "french_tourism": ("Au-delà de Paris","The France tourists never see — 7 hidden villages."),
  "french_cheeses_1": ("Le plateau de fromages","How to build a French cheese board like a local."),
  "homonyms_1": ("Homonymes #1","Two words. Same sound. Different worlds."),
  "homonyms_3": ("Homonymes #3","Vert · verre · vers · ver. Good luck."),
  "homonyms_5": ("Homonymes #5","When French sounds the same but isn't."),
  "homonyms_6": ("Homonymes #6","The classic French trap word."),
  "formal_vs_spoken_2": ("Formel vs Parlé #2","How they write it vs. how Parisians say it."),
  "formal_vs_spoken_3": ("Formel vs Parlé #3","The textbook lied to you."),
  "formal_vs_spoken_4": ("Formel vs Parlé #4","Spoken French is 50% slang."),
  "formal_vs_spoken_5": ("Formel vs Parlé #5","What Parisians actually drop in conversation."),
  "formal_vs_spoken_6": ("Formel vs Parlé #6","Real café French — what you'll actually hear."),
  "formal_vs_spoken_7": ("Formel vs Parlé #7","When grammar bends to rhythm."),
  "formal_vs_spoken_8": ("Formel vs Parlé #8","Liaisons that natives skip."),
  "formal_vs_spoken_9": ("Formel vs Parlé #9","Why your French sounds 'textbook'."),
  "formal_vs_spoken_10": ("Formel vs Parlé #10","Verlan, slang, and the real Paris."),
  "formal_vs_spoken_11": ("Formel vs Parlé #11","Drop the 'ne' — sound native."),
  "formal_vs_spoken_12": ("Formel vs Parlé #12","The 5 contractions Parisians live by."),
}
def head(stem):
  return HEADLINES.get(stem, (stem.replace("_"," ").title(),"French Atelier · learn live from France."))

slides = []

# ---------- COVER ----------
slides.append('''<section class="slide slide--dark slide--cover">
  <div class="slide__inner">
    <div class="eyebrow eyebrow--gold">FRENCH ATELIER · BY ACADOMIA</div>
    <h1 class="display">CEO Marketing<br>Review.</h1>
    <p class="lead">From <span class="gold">1.9 → 2.5</span> weekly ROI. Organic · paid · email · Bastille Day.</p>
    <div class="rule"></div>
    <div class="cover-meta">June 2026 · USA market · audience 35–70</div>
  </div></section>''')

# ---------- AGENDA ----------
agenda = [
 ("01","Organic viral formats — 20 French Graphic Words videos"),
 ("02","Organic — French Beauty (4 IG Reels in production)"),
 ("03","New paid media cuts — CPL down to $13.40"),
 ("04","Quora & Reddit — full 60-post organic-written deck"),
 ("05","New website + AI SEO — live walkthrough"),
 ("06","Email marketing — 4 flows, mocked up"),
 ("07","Bastille Day — Win a Trip to France"),
 ("08","The ask — 1.9 → 2.5 weekly ROI"),
]
slides.append('<section class="slide slide--cream"><div class="slide__inner slide__inner--centered"><h2 class="title">Agenda</h2><div class="rule"></div><ol class="agenda">'+
  "".join([f'<li><span class="num">{n}</span><span class="label">{l}</span></li>' for n,l in agenda])+
  '</ol></div></section>')

def divider(num, title, sub):
  return f'<section class="slide slide--dark slide--divider"><div class="slide__inner"><div class="eyebrow eyebrow--gold">SECTION {num}</div><h2 class="display display--md">{title}</h2><p class="lead lead--muted">{sub}</p><div class="rule"></div></div></section>'

# ===== Phone components (LARGE) =====
def reels_phone(video_stem, headline, sub):
  return f'''<div class="phone phone--reels phone--lg">
    <video src="videos/{video_stem}.mp4" autoplay muted loop playsinline preload="metadata"></video>
    <div class="dynamic-island"></div>
    <div class="status-bar"><span class="time">9:41</span><div class="icons">
      <svg width="17" height="12" viewBox="0 0 17 12"><rect x="0" y="7" width="3" height="5" fill="white"/><rect x="4.5" y="5" width="3" height="7" fill="white"/><rect x="9" y="2.5" width="3" height="9.5" fill="white"/><rect x="13.5" y="0" width="3" height="12" fill="white"/></svg>
      <svg width="25" height="12" viewBox="0 0 25 12"><rect x="0.5" y="0.5" width="21" height="11" rx="3.5" stroke="white" fill="none"/><rect x="2" y="2" width="16" height="8" fill="white"/></svg>
    </div></div>
    <div class="reels-ui">
      <div class="reels-header"><span class="reels-header-title">Reels</span></div>
      <div class="reels-right">
        <div class="reels-profile-bubble"><span class="initials">FA</span></div>
        <div class="reels-action"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg><span>48.2K</span></div>
        <div class="reels-action"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg><span>1,243</span></div>
        <div class="reels-action"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8"><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg><span>Share</span></div>
      </div>
      <div class="reels-bottom">
        <div class="reels-user-row"><span class="reels-username">@frenchatelier</span><span class="reels-follow-pill">Follow</span></div>
        <div class="reels-headline">{headline}</div>
        <div class="reels-caption">{sub}</div>
        <div class="reels-audio-row"><span class="reels-audio-text">♫ Original audio · French Atelier</span></div>
      </div>
    </div>
  </div>'''

def tiktok_phone(video_stem, headline, sub):
  return f'''<div class="phone phone--tiktok phone--lg">
    <video src="videos/{video_stem}.mp4" autoplay muted loop playsinline preload="metadata"></video>
    <div class="dynamic-island"></div>
    <div class="status-bar"><span class="time">9:41</span><div class="icons">
      <svg width="17" height="12" viewBox="0 0 17 12"><rect x="0" y="7" width="3" height="5" fill="white"/><rect x="4.5" y="5" width="3" height="7" fill="white"/><rect x="9" y="2.5" width="3" height="9.5" fill="white"/><rect x="13.5" y="0" width="3" height="12" fill="white"/></svg>
      <svg width="25" height="12" viewBox="0 0 25 12"><rect x="0.5" y="0.5" width="21" height="11" rx="3.5" stroke="white" fill="none"/><rect x="2" y="2" width="16" height="8" fill="white"/></svg>
    </div></div>
    <div class="tiktok-ui">
      <div class="tiktok-header"><span class="tiktok-tab">Following</span><span class="tiktok-tab active">For You</span></div>
      <div class="tiktok-right">
        <div class="tiktok-profile-wrap"><div class="tiktok-profile-circle"><span class="initials">FA</span></div></div>
        <div class="tiktok-action"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.6"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg><span>24.5K</span></div>
        <div class="tiktok-action"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.6"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg><span>892</span></div>
        <div class="tiktok-action"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.6"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/></svg><span>Share</span></div>
      </div>
      <div class="tiktok-bottom">
        <div class="tiktok-username">@frenchatelier</div>
        <div class="tiktok-headline">{headline}</div>
        <div class="tiktok-caption">{sub} <span class="hashtag">#LearnFrench</span> <span class="hashtag">#FrenchTips</span></div>
        <div class="tiktok-sound-row"><span class="tiktok-sound-text">♫ original sound · French Atelier</span></div>
      </div>
    </div>
  </div>'''

def meta_card(video_stem, headline, sub):
  return f'''<div class="meta-card meta-card--lg">
    <div class="meta-header">
      <div class="meta-avatar"><span>FA</span></div>
      <div class="meta-header-info"><div class="meta-page-name">French Atelier</div><div class="meta-sponsored">Sponsored · <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="#65676b" stroke-width="2"><circle cx="12" cy="12" r="10"/></svg></div></div>
      <div class="meta-more"><svg width="20" height="20" viewBox="0 0 24 24" fill="#65676b"><circle cx="5" cy="12" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="19" cy="12" r="2"/></svg></div>
    </div>
    <div class="meta-caption"><strong>{headline}</strong> 🇫🇷<br>{sub}<br><span class="hashtag">#LearnFrench</span> <span class="hashtag">#FrenchAtelier</span></div>
    <div class="meta-video-wrap"><div class="meta-video-inner"><video src="videos/{video_stem}.mp4" autoplay muted loop playsinline preload="metadata"></video></div></div>
    <div class="meta-link-card">
      <div class="meta-link-info"><div class="meta-link-domain">frenchatelier.com</div><div class="meta-link-title">MASTER THE ART OF FRENCH</div><div class="meta-link-sub">Live classes broadcast from France</div></div>
      <div class="meta-cta-btn">Learn More</div>
    </div>
    <div class="meta-reactions"><div class="meta-reaction-emojis"><div class="meta-reaction-emoji">👍</div><div class="meta-reaction-emoji">❤️</div><div class="meta-reaction-emoji">🥰</div></div><span class="meta-reaction-count">312</span><div class="meta-comments-shares">24 comments · 8 shares</div></div>
    <div class="meta-actions"><div class="meta-action-btn">👍 Like</div><div class="meta-action-btn">💬 Comment</div><div class="meta-action-btn">↗ Share</div></div>
  </div>'''

# ===================== SECTION 01 =====================
slides.append(divider("01","Organic Viral Formats","20 videos · TikTok · Instagram Reels · Meta Feed"))

slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow eyebrow--gold">SECTION 01 · CONTEXT</div>
  <h2 class="title">French Graphic Words — what & why</h2><div class="rule"></div>
  <div class="ctx-grid">
    <div class="ctx-block"><div class="ctx-h">The format</div><p>Short, captioned French-language videos around two recurring concepts: <em>Homonymes</em> (same sound, different word) and <em>Formel vs Parlé</em> (textbook French vs how Paris actually speaks).</p></div>
    <div class="ctx-block"><div class="ctx-h">The audience</div><p>USA 35–70 francophiles. They love French culture but feel their textbook French is "wrong" in real conversation. We close that gap in 30 seconds.</p></div>
    <div class="ctx-block"><div class="ctx-h">The distribution</div><p>Native posts on @frenchatelier · TikTok, Instagram Reels and Meta Feed (paid amplification on the top 5 performers).</p></div>
    <div class="ctx-block"><div class="ctx-h">The result we want</div><p><strong>25% of all leads</strong> from organic · target net follower add <strong>+15K</strong> across IG / TikTok by end of Q3.</p></div>
  </div>
</div></section>''')

# Big TikTok showcase — 2 per slide
for i in range(0, len(tt_videos), 2):
  chunk = tt_videos[i:i+2]
  phones = "".join([tiktok_phone(s, head(s)[0], head(s)[1]) for s in chunk])
  slides.append(f'''<section class="slide slide--cream"><div class="slide__inner">
    <div class="eyebrow eyebrow--gold">SECTION 01 · TIKTOK · FOR YOU</div>
    <h2 class="title title--md">TikTok placements <span class="muted">({i+1}–{i+len(chunk)} of {len(tt_videos)})</span></h2><div class="rule"></div>
    <div class="phone-row phone-row--2">{phones}</div>
  </div></section>''')

# Big Reels showcase — 2 per slide
for i in range(0, len(ig_videos), 2):
  chunk = ig_videos[i:i+2]
  phones = "".join([reels_phone(s, head(s)[0], head(s)[1]) for s in chunk])
  slides.append(f'''<section class="slide slide--cream"><div class="slide__inner">
    <div class="eyebrow eyebrow--gold">SECTION 01 · INSTAGRAM REELS</div>
    <h2 class="title title--md">Instagram Reels placements <span class="muted">({i+1}–{i+len(chunk)} of {len(ig_videos)})</span></h2><div class="rule"></div>
    <div class="phone-row phone-row--2">{phones}</div>
  </div></section>''')

# Meta — 1 per slide BIG
for s in tt_videos[:3]:
  slides.append(f'''<section class="slide slide--cream"><div class="slide__inner">
    <div class="eyebrow eyebrow--gold">SECTION 01 · META · FACEBOOK FEED</div>
    <h2 class="title title--md">Meta Feed — paid amplification</h2><div class="rule"></div>
    <div class="meta-row">{meta_card(s, head(s)[0], head(s)[1])}</div>
  </div></section>''')

# ===================== SECTION 02 — French Beauty =====================
slides.append(divider("02","French Beauty","4 IG Reels · in production · post-meeting delivery"))

slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow eyebrow--gold">SECTION 02 · CONTEXT</div>
  <h2 class="title">A second viral pillar — French Beauty</h2><div class="rule"></div>
  <p class="lead lead--dark">Four French Beauty Reels currently being re-edited to French Atelier brand. These complement the language-focused content and target the aspirational lifestyle layer of our audience — Parisian elegance, ritual, restraint.</p>
  <div class="edit-grid">
    <div class="edit-row"><span class="num">01</span><div><strong>French Atelier logo opener</strong><p>Matches the brand opener used in Homonyms / Formal-vs-Spoken series.</p></div></div>
    <div class="edit-row"><span class="num">02</span><div><strong>Strip existing branding</strong><p>Original creator marks, watermarks and end-cards removed.</p></div></div>
    <div class="edit-row"><span class="num">03</span><div><strong>Keep original wording</strong><p>On-screen captions preserved verbatim — they're already optimised.</p></div></div>
    <div class="edit-row"><span class="num">04</span><div><strong>Logo top-right corner</strong><p>Persistent French Atelier mark · small, navy, transparent.</p></div></div>
  </div>
</div></section>''')

# French Beauty mockups using storyboards as posters (4 storyboards)
beauty_reels = [
  ("DWwznl1j6de","Le rituel matinal","The morning ritual that defines French beauty."),
  ("DUYcL5NAAsd","La beauté discrète","Discreet beauty — what Parisians never overdo."),
  ("DUdBbCDjBxh","Le parfum à 5h","The 5pm perfume rule no one explains."),
  ("DS31NZkjJjm","La peau sans maquillage","Why French women wear less, not more."),
]
for idx, (code, head_txt, sub) in enumerate(beauty_reels):
  img_idx = idx+1
  slides.append(f'''<section class="slide slide--cream"><div class="slide__inner">
    <div class="eyebrow eyebrow--gold">SECTION 02 · FRENCH BEAUTY · REEL {img_idx}/4</div>
    <h2 class="title title--md">{head_txt}</h2><div class="rule"></div>
    <div class="phone-row phone-row--2">
      <div class="phone phone--reels phone--lg">
        <img src="images/beauty_{img_idx}.png" alt="" style="width:100%;height:100%;object-fit:cover;">
        <div class="dynamic-island"></div>
        <div class="status-bar"><span class="time">9:41</span></div>
        <div class="reels-ui">
          <div class="reels-header"><span class="reels-header-title">Reels</span></div>
          <div class="reels-bottom">
            <div class="reels-user-row"><span class="reels-username">@frenchatelier</span><span class="reels-follow-pill">Follow</span></div>
            <div class="reels-headline">{head_txt}</div>
            <div class="reels-caption">{sub}</div>
            <div class="reels-audio-row"><span class="reels-audio-text">♫ Original audio · French Atelier</span></div>
          </div>
        </div>
      </div>
      <div class="beauty-info">
        <div class="beauty-meta">SOURCE REEL</div>
        <a class="beauty-link" href="https://www.instagram.com/reel/{code}/" target="_blank">instagram.com/reel/{code}</a>
        <div class="beauty-meta" style="margin-top:1.4rem">STATUS</div>
        <div class="beauty-status"><span class="live-dot" style="background:#C9A961"></span> In edit · brand-aligned · delivery post-meeting</div>
        <div class="beauty-meta" style="margin-top:1.4rem">SPEC</div>
        <ul class="beauty-spec">
          <li>Logo opener (same as language reels)</li>
          <li>Watermark stripped</li>
          <li>Captions preserved verbatim</li>
          <li>Persistent FA mark, top-right</li>
        </ul>
      </div>
    </div>
  </div></section>''')

# ===================== SECTION 03 — Paid =====================
slides.append(divider("03","Paid Media","CPL down to $13.40 · Charline masterclass · new cuts"))

slides.append(f'''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow eyebrow--gold">SECTION 03 · CONTEXT</div>
  <h2 class="title">What changed in May–June 2026</h2><div class="rule"></div>
  <p class="lead lead--dark">We replaced broad-interest targeting with lookalikes of converters, shipped two new cuts of Charline's Paris masterclass, and tightened ad-to-landing-page scent. CPL dropped from $19.80 to <span class="gold">$13.40</span> while spend held flat.</p>
  <div class="paid-kpi-row">
    <div class="kpi-big"><div class="kpi-big-val">$19.80</div><div class="kpi-big-lab">CPL · April</div></div>
    <div class="kpi-arrow">→</div>
    <div class="kpi-big"><div class="kpi-big-val gold">$13.40</div><div class="kpi-big-lab">CPL · June</div></div>
    <div class="kpi-big"><div class="kpi-big-val">−32%</div><div class="kpi-big-lab">CPL reduction</div></div>
    <div class="kpi-big"><div class="kpi-big-val">flat</div><div class="kpi-big-lab">spend held</div></div>
  </div>
</div></section>''')

slides.append(f'''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow eyebrow--gold">SECTION 03 · HERO ASSET</div>
  <h2 class="title title--md">Charline masterclass — live from Paris</h2><div class="rule"></div>
  <div class="paid-hero-row">
    {meta_card("charline_masterclass","Master the art of French elegance","Join Charline live from Paris for an exclusive masterclass.")}
    {reels_phone("charline_masterclass","Masterclass · Paris","Live with Charline — French elegance, taught the way Paris teaches.")}
  </div>
</div></section>''')

slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow eyebrow--gold">SECTION 03 · WHAT WE DID — 80/20</div>
  <h2 class="title">The 20% of moves that drove 80% of the CPL drop</h2><div class="rule"></div>
  <div class="move-list">
    <div class="move"><div class="move-h">Killed broad interests</div><div class="move-b">Cut 6 underperforming interest sets · concentrated budget on lookalikes of past converters.</div></div>
    <div class="move"><div class="move-h">Charline masterclass cuts</div><div class="move-b">Live-from-France hook · raw, authentic, native voice. Outperformed studio shots 3.2×.</div></div>
    <div class="move"><div class="move-h">Hook in the first 1.5 seconds</div><div class="move-b">French place-name + question · "Why does Paris sound nothing like the textbook?"</div></div>
    <div class="move"><div class="move-h">Landing-page scent match</div><div class="move-b">Ad copy lifted from website hero · zero scent-mismatch · bounce dropped 19%.</div></div>
    <div class="move"><div class="move-h">Bid strategy</div><div class="move-b">Cost-cap on Meta · lowest-cost on Reels placement only. Stopped chasing impressions.</div></div>
  </div>
</div></section>''')

slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow eyebrow--gold">SECTION 03 · CPL TREND · APRIL → JUNE 2026</div>
  <h2 class="title">CPL reduction</h2><div class="rule"></div>
  <div class="chart-wrap">
    <svg viewBox="0 0 800 320" class="cpl-chart" preserveAspectRatio="xMidYMid meet">
      <defs><linearGradient id="g1" x1="0" x2="0" y1="0" y2="1"><stop offset="0%" stop-color="#C9A961" stop-opacity="0.35"/><stop offset="100%" stop-color="#C9A961" stop-opacity="0"/></linearGradient></defs>
      <line x1="60" y1="40" x2="60" y2="280" stroke="#0A1128" stroke-width="1.5"/>
      <line x1="60" y1="280" x2="760" y2="280" stroke="#0A1128" stroke-width="1.5"/>
      <text x="20" y="60" font-family="Inter" font-size="12" fill="#0A1128">$20</text>
      <text x="20" y="135" font-family="Inter" font-size="12" fill="#0A1128">$17</text>
      <text x="20" y="210" font-family="Inter" font-size="12" fill="#0A1128">$14</text>
      <text x="20" y="282" font-family="Inter" font-size="12" fill="#0A1128">$11</text>
      <text x="100" y="305" font-family="Inter" font-size="13" fill="#0A1128">Apr W1</text>
      <text x="240" y="305" font-family="Inter" font-size="13" fill="#0A1128">Apr W4</text>
      <text x="380" y="305" font-family="Inter" font-size="13" fill="#0A1128">May W2</text>
      <text x="540" y="305" font-family="Inter" font-size="13" fill="#0A1128">May W4</text>
      <text x="680" y="305" font-family="Inter" font-size="13" fill="#0A1128">Jun W1</text>
      <path d="M 110 65 L 250 95 L 390 140 L 540 195 L 700 232 L 700 280 L 110 280 Z" fill="url(#g1)"/>
      <polyline points="110,65 250,95 390,140 540,195 700,232" fill="none" stroke="#C9A961" stroke-width="3.5" stroke-linecap="round"/>
      <circle cx="110" cy="65" r="6" fill="#0A1128"/><text x="80" y="50" font-family="Inter" font-size="13" font-weight="600" fill="#0A1128">$19.80</text>
      <circle cx="250" cy="95" r="5" fill="#0A1128"/>
      <circle cx="390" cy="140" r="5" fill="#0A1128"/>
      <circle cx="540" cy="195" r="5" fill="#0A1128"/>
      <circle cx="700" cy="232" r="7" fill="#C9A961" stroke="#0A1128" stroke-width="2"/><text x="660" y="220" font-family="Inter" font-size="14" font-weight="700" fill="#C9A961">$13.40</text>
    </svg>
  </div>
  <p class="caption">CPL down 32% in 8 weeks · target: maintain ≤ $14 with 2 additional cuts in late June.</p>
</div></section>''')

# ===================== SECTION 04 — Quora & Reddit (60 mockups) =====================
slides.append(divider("04","Organic Written","Quora & Reddit · full 60-post content slate · 6 personas"))

slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow eyebrow--gold">SECTION 04 · CONTEXT</div>
  <h2 class="title">Why this channel matters</h2><div class="rule"></div>
  <p class="lead lead--dark">Quora and Reddit are <em>the</em> high-intent surfaces for adults researching how to learn French. Our 60-post slate seeds the search graph with persona-matched answers — every post is a search-engine and AI-Overview asset for years.</p>
  <div class="ctx-grid">
    <div class="ctx-block"><div class="ctx-h">30 Quora answers</div><p>Long-form, expert-voiced, written from the founder/teacher seat. Each maps to a single decision-stage question.</p></div>
    <div class="ctx-block"><div class="ctx-h">30 Reddit posts</div><p>r/languagelearning · r/French · r/learnfrench · r/AskOldPeople · r/travel. First-person, story-led, no sales-y tone.</p></div>
    <div class="ctx-block"><div class="ctx-h">Six personas</div><p>One voice per persona · consistent across both platforms · adapted from the Rosen Hebrew framework.</p></div>
    <div class="ctx-block"><div class="ctx-h">Distribution cadence</div><p>3 posts/week · 20 weeks · staffed by content lead + 2 native writers.</p></div>
  </div>
</div></section>''')

# Personas
slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow eyebrow--gold">SECTION 04 · PERSONAS</div>
  <h2 class="title">Six personas · one French Atelier</h2><div class="rule"></div>
  <div class="persona-grid">
    <div class="persona"><div class="persona-name">France-Bound Traveler</div><div class="persona-age">50–70</div><div class="persona-hook">Trip urgency · Paris café fluency</div></div>
    <div class="persona"><div class="persona-name">App Dropout</div><div class="persona-age">45–65</div><div class="persona-hook">Duolingo failed me · I need structure</div></div>
    <div class="persona"><div class="persona-name">Lifelong Learner</div><div class="persona-age">55–70</div><div class="persona-hook">Brain health · cultural sophistication</div></div>
    <div class="persona"><div class="persona-name">Romance & Refinement</div><div class="persona-age">45–65</div><div class="persona-hook">Love, identity, reinvention</div></div>
    <div class="persona"><div class="persona-name">Status-Conscious Achiever</div><div class="persona-age">45–65</div><div class="persona-hook">Elite distinction · CEFR certificate</div></div>
    <div class="persona"><div class="persona-name">Heritage Reconnector</div><div class="persona-age">40–65</div><div class="persona-hook">Family roots · grandmother's tongue</div></div>
  </div>
</div></section>''')

# ===== Quora mockup card =====
def quora_card(p):
  return f'''<div class="quora-card">
    <div class="quora-card-head">
      <div class="quora-logo">Quora</div>
      <div class="quora-tag">{p["subtopic"]}</div>
    </div>
    <div class="quora-q">{p["title"]}</div>
    <div class="quora-author">
      <div class="quora-avatar"><span>FA</span></div>
      <div><div class="quora-author-name">French Atelier <span class="quora-verified">✓</span></div><div class="quora-author-sub">Founder · Live French school · Answered Jun 2026</div></div>
    </div>
    <div class="quora-body">{p["preview"]}</div>
    <div class="quora-footer">
      <span class="quora-upvote">▲ {p["votes"]}</span>
      <span class="quora-action">💬 Comment</span>
      <span class="quora-action">↗ Share</span>
      <span class="quora-tag quora-tag--persona">Persona: {p["persona"]}</span>
    </div>
  </div>'''

# ===== Reddit mockup card =====
def reddit_card(p):
  return f'''<div class="reddit-card">
    <div class="reddit-vote">
      <div class="reddit-arrow">▲</div>
      <div class="reddit-votes">{p["votes"]}</div>
      <div class="reddit-arrow">▼</div>
    </div>
    <div class="reddit-body">
      <div class="reddit-meta">{p["subtopic"]} · Posted by u/french_atelier_team · 2d</div>
      <div class="reddit-title">{p["title"]}</div>
      <div class="reddit-text">{p["preview"]}</div>
      <div class="reddit-actions">
        <span class="reddit-action">💬 Comments</span>
        <span class="reddit-action">↗ Share</span>
        <span class="reddit-action">🔖 Save</span>
        <span class="reddit-tag">Persona: {p["persona"]}</span>
      </div>
    </div>
  </div>'''

# Group Quora posts (30) — 2 per slide = 15 slides
quora_posts = [p for p in posts if p["platform"]=="quora"]
reddit_posts = [p for p in posts if p["platform"]=="reddit"]

for i in range(0, len(quora_posts), 2):
  chunk = quora_posts[i:i+2]
  cards = "".join([quora_card(p) for p in chunk])
  slides.append(f'''<section class="slide slide--cream"><div class="slide__inner">
    <div class="eyebrow eyebrow--gold">SECTION 04 · QUORA · POSTS {i+1}–{i+len(chunk)} OF 30</div>
    <h2 class="title title--md">Quora answers — mockups</h2><div class="rule"></div>
    <div class="quora-grid">{cards}</div>
  </div></section>''')

for i in range(0, len(reddit_posts), 2):
  chunk = reddit_posts[i:i+2]
  cards = "".join([reddit_card(p) for p in chunk])
  slides.append(f'''<section class="slide slide--cream"><div class="slide__inner">
    <div class="eyebrow eyebrow--gold">SECTION 04 · REDDIT · POSTS {i+1}–{i+len(chunk)} OF 30</div>
    <h2 class="title title--md">Reddit posts — mockups</h2><div class="rule"></div>
    <div class="reddit-grid">{cards}</div>
  </div></section>''')

# ===================== SECTION 05 — Website =====================
slides.append(divider("05","New Website","frenchatelier.com · live screen recording · AI SEO"))

slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow eyebrow--gold">SECTION 05 · CONTEXT</div>
  <h2 class="title">A site rebuilt for adults who buy</h2><div class="rule"></div>
  <p class="lead lead--dark">The previous site sold a feature list. The new site sells a feeling — France itself, told through the Six Pillars (Language, Art, Gastronomy, Film, Fashion, Music & Poetry). Built clean for AI Overviews and answer engines.</p>
</div></section>''')

slides.append('''<section class="slide slide--cream slide--site"><div class="slide__inner">
  <div class="eyebrow eyebrow--gold">SECTION 05 · LIVE WEBSITE · SCREEN RECORDING</div>
  <h2 class="title title--md">frenchatelier.com — 60-second auto-scroll</h2><div class="rule"></div>
  <div class="browser-frame">
    <div class="browser-chrome">
      <div class="browser-dots"><span></span><span></span><span></span></div>
      <div class="browser-url">🔒 frenchatelier.com</div>
    </div>
    <div class="browser-viewport">
      <video src="videos/site_60s.mp4" autoplay muted loop playsinline controls></video>
    </div>
  </div>
  <p class="caption">Full home → courses → teachers → pricing scroll capture · <a href="https://gitteromri-ux.github.io/french-atelier/" target="_blank">visit live site</a></p>
</div></section>''')

slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow eyebrow--gold">SECTION 05 · AI SEO — WHAT'S SHIPPED</div>
  <h2 class="title">Built for AI Overviews</h2><div class="rule"></div>
  <div class="move-list">
    <div class="move"><div class="move-h">Structured data</div><div class="move-b">Course · Person · Organization · Offer schema. CEFR levels, pricing and teachers exposed to LLM crawlers.</div></div>
    <div class="move"><div class="move-h">Conversational content</div><div class="move-b">Six Pillars pages written for AI answer engines · question-led H2s · plain-language definitions of CEFR.</div></div>
    <div class="move"><div class="move-h">Juliane — AI tutor surface</div><div class="move-b">Our AI tutor surfaces on every course page · tuned keyword density for 'live AI French tutor'.</div></div>
    <div class="move"><div class="move-h">Page-speed core</div><div class="move-b">LCP &lt; 2.0s · CLS &lt; 0.05 · clean Core Web Vitals across all 18 pages.</div></div>
    <div class="move"><div class="move-h">Region anchors</div><div class="move-b">Each teacher tagged by city · Strasbourg, Paris, Lyon, Nice, Pau, Montpellier · localised internal linking.</div></div>
  </div>
</div></section>''')

# ===================== SECTION 06 — Email =====================
slides.append(divider("06","Email Marketing","4 flows · designed mockups · the cheapest ROI lever"))

slides.append('''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow eyebrow--gold">SECTION 06 · CONTEXT</div>
  <h2 class="title">Where email fits</h2><div class="rule"></div>
  <p class="lead lead--dark">Email is the cheapest ROI lever we have. We're launching 4 flows targeting the four highest-leverage moments: first touch, free-assessment follow-up, 60-day dormants, and the Bastille campaign.</p>
</div></section>''')

# ===== 30 EMAILS — full sequence map + inbox mockups =====
from emails_30 import EMAILS_30

# Overview slide — full 30-email sequence table
overview_rows = "".join([
  f'<tr><td class="em-num">#{e["num"]}</td><td class="em-day">Day {e["day"]}</td><td><span class="em-cat em-cat--{e["category"].lower().replace(" ","-")}">{e["category"]}</span></td><td class="em-subj">{e["subject"]}</td>{"<td class=\"em-real\">\u2713 sent</td>" if e.get("real") else "<td class=\"em-draft\">draft</td>"}</tr>'
  for e in EMAILS_30
])
slides.append(f'''<section class="slide slide--cream"><div class="slide__inner">
  <div class="eyebrow eyebrow--gold">SECTION 06 · FULL 30-EMAIL SEQUENCE MAP</div>
  <h2 class="title">All 30 emails · 90-day flow</h2><div class="rule"></div>
  <table class="em-table">
    <thead><tr><th>#</th><th>Day</th><th>Pillar</th><th>Subject line</th><th>Status</th></tr></thead>
    <tbody>{overview_rows}</tbody>
  </table>
</div></section>''')

# Inbox-style preview — 5 emails per slide
def inbox_row(e):
  real_badge = '<span class="em-badge em-badge--sent">SENT</span>' if e.get("real") else '<span class="em-badge em-badge--draft">DRAFT</span>'
  return f'''<div class="inbox-row">
    <div class="inbox-avatar"><span>FA</span></div>
    <div class="inbox-body">
      <div class="inbox-line1"><span class="inbox-from">French Atelier</span><span class="inbox-meta">Day {e["day"]} · {e["category"]}</span></div>
      <div class="inbox-subj">#{e["num"]:02d} — {e["subject"]}</div>
      <div class="inbox-preview">{e["preview"]}</div>
    </div>
    <div class="inbox-side">{real_badge}</div>
  </div>'''

for i in range(0, len(EMAILS_30), 5):
  chunk = EMAILS_30[i:i+5]
  rows = "".join([inbox_row(e) for e in chunk])
  slides.append(f'''<section class="slide slide--cream"><div class="slide__inner">
    <div class="eyebrow eyebrow--gold">SECTION 06 · INBOX VIEW · EMAILS {i+1}–{i+len(chunk)} OF 30</div>
    <h2 class="title title--md">Gmail inbox — as the subscriber sees it</h2><div class="rule"></div>
    <div class="inbox-frame">
      <div class="inbox-chrome"><span class="inbox-logo">M</span><span class="inbox-app-name">Inbox — you@gmail.com</span></div>
      <div class="inbox-list">{rows}</div>
    </div>
  </div></section>''')

# Full email mockups for the 5 REAL emails we have full copy on (8–12)
real_emails_full = [
  ("Email 8 · Day 25 · SOUL", "Vincent <vincent@frenchatelier.com>", "The French don't say \"I miss you\"",
   "The French don't say \"I miss you.\"\n\nThey say <em>tu me manques</em> — <em>you are missing from me.</em>\n\nRead that again. The English version puts you in charge of the feeling. The French version says the feeling arrives on its own, and the other person is the cause of it. One is an action. The other is a quiet admission.\n\nThat single grammatical flip changes how love is spoken.\n\nThere are more.\n\n<em>Avoir le cafard</em> — to have the cockroach. It means to be quietly down, the kind of mood that crawls into a corner of your day and stays there.\n\n<em>Dépaysement</em> — the feeling of being pleasantly unmoored. There is no English word for it because English-speaking life rarely names the in-between.\n\nThis is what we teach at French Atelier. Not vocabulary lists. The shape of a worldview.\n\nYou stop translating. You start thinking in French.\n\nÀ bientôt,\nThe French Atelier"),
  ("Email 9 · Day 28 · TASTE", "Vincent <vincent@frenchatelier.com>", "How to order a coffee in Paris (without embarrassing yourself)",
   "There's a way Parisians order coffee that has nothing to do with the menu — and everything to do with rhythm.\n\n\"Un café, s'il vous plaît\" — gets you the same espresso a tourist gets.\n\n\"Je prendrais un café\" — sounds slightly off.\n\n\"Un petit café — merci\" — lands you in the Paris of locals.\n\nThe trick isn't vocabulary. It's the diminutive — <em>un petit</em> — the French way of making any request smaller, softer, less imposing. It signals you understand the room.\n\nThree more phrases inside that mark you as someone who lives here — not someone passing through.\n\nÀ bientôt,\nThe French Atelier"),
  ("Email 10 · Day 32 · STYLE", "Vincent <vincent@frenchatelier.com>", "What French cinema taught us about silence",
   "A single scene from a 1960s film changed how generations of French people understand love.\n\n<em>Pierrot le Fou</em>, 1965. Belmondo and Karina are in a car, in silence, for almost a full minute. They say nothing. The French audience hears everything.\n\nWe translated the scene. The English barely survives — because English fills silence with words, and French lets silence say what words can't.\n\nThis is what we teach. Not just the language. The cultural permission to leave things unsaid.\n\nWatch the scene inside.\n\nÀ bientôt,\nThe French Atelier"),
  ("Email 11 · Day 35 · SOUL", "Vincent <vincent@frenchatelier.com>", "On June 21st, all of France sings",
   "<em>La Fête de la Musique</em> — the one night a year when every street, every doorway, every café in France becomes a stage.\n\nIt's not a festival. It's a national agreement to play music for free, anywhere, all night.\n\nHere is the thing French Atelier teaches that nobody tells you about France: the language was built for nights like this. <em>Faire la fête</em>. <em>Tomber sur quelqu'un</em>. <em>L'ambiance</em>. There are words for every texture of a shared evening.\n\nThree of them inside — with the French you'll need to be part of the night, not a tourist watching it.\n\nÀ bientôt,\nThe French Atelier"),
  ("Email 12 · Day 39 · ART", "Vincent <vincent@frenchatelier.com>", "You already speak more French than you think",
   "Rendezvous. Café. Résumé. Boutique. Cliché. Déjà vu. Genre. Critique. Souvenir. Bouquet. Brunette. Avant-garde. Boutique. Couture. Bourgeois. Entrepreneur. Fiancé. Naive. Premier. Risqué.\n\nTwenty English words you use weekly that are pure French.\n\nWhat this means is simple: your ear is already tuned to French rhythm. Your tongue knows the soft vowels. The work isn't starting from zero. The work is recognising what's already there — and giving it the structure to grow.\n\nThat's what live classes do. That's why we teach French this way.\n\nÀ bientôt,\nThe French Atelier"),
]

for short_title, sender, subject, body in real_emails_full:
  body_html = body.replace("\n","<br>")
  slides.append(f'''<section class="slide slide--cream"><div class="slide__inner">
    <div class="eyebrow eyebrow--gold">SECTION 06 · {short_title.upper()} · LIVE SENT</div>
    <h2 class="title title--md">{subject}</h2><div class="rule"></div>
    <div class="email-mock">
      <div class="email-chrome"><div class="email-dots"><span></span><span></span><span></span></div><div class="email-app">Mail</div></div>
      <div class="email-head">
        <div class="email-from"><div class="email-avatar"><span>FA</span></div><div><div class="email-from-name">{sender.split("<")[0].strip()}</div><div class="email-from-addr">{sender.split("<")[1].rstrip(">")}</div></div></div>
        <div class="email-meta"><div>Today · 9:14 AM</div><div>To: you@gmail.com</div></div>
      </div>
      <div class="email-subject">{subject}</div>
      <div class="email-body">{body_html}</div>
      <div class="email-cta-row"><a class="email-cta" href="#">Read on web</a><a class="email-cta email-cta--ghost" href="#">Unsubscribe</a></div>
    </div>
  </div></section>''')

# ===================== SECTION 07 — Bastille Day =====================
slides.append(divider("07","Bastille Day","Win a Trip to France · July 14 · follower-acquisition campaign"))

slides.append('''<section class="slide slide--dark slide--bastille"><div class="slide__inner slide--split">
  <div class="split-left">
    <div class="eyebrow eyebrow--gold">BASTILLE DAY · JULY 14</div>
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

# ===================== SECTION 08 — The Ask =====================
slides.append(divider("08","The Ask","From 1.9 → 2.5 weekly ROI · three levers · one quarter"))

slides.append('''<section class="slide slide--dark slide--ask"><div class="slide__inner">
  <h2 class="display display--md">From 1.9 to <span class="gold">2.5</span></h2>
  <p class="lead lead--muted">Three levers · one quarter</p>
  <div class="rule"></div>
  <div class="lever-grid">
    <div class="lever"><div class="lever-num">01</div><div class="lever-h">Organic lead growth</div><div class="lever-body">60 Quora/Reddit posts · 20 organic videos · 4 French Beauty Reels · Bastille follower drive</div><div class="lever-target gold">25%</div><div class="lever-sub">of total leads</div></div>
    <div class="lever"><div class="lever-num">02</div><div class="lever-h">Email marketing</div><div class="lever-body">4 new flows · welcome · trial nurture · 60-day reactivation · Bastille countdown</div><div class="lever-target gold">+15%</div><div class="lever-sub">reactivation lift</div></div>
    <div class="lever"><div class="lever-num">03</div><div class="lever-h">Paid CPL reduction</div><div class="lever-body">2 new cuts in late June · 4 total · maintain ≤ $14 with scale</div><div class="lever-target gold">$13.40</div><div class="lever-sub">current CPL</div></div>
  </div>
</div></section>''')

# Closing
slides.append('''<section class="slide slide--dark slide--closing"><div class="slide__inner">
  <h2 class="display">Speak, read,<br>and live French.</h2>
  <p class="lead"><em class="gold">From France.</em></p>
  <div class="rule"></div>
  <div class="cover-meta">French Atelier · by Acadomia · June 2026</div>
</div></section>''')

# === BUILD ===
deck_html = "\n\n".join(slides)
total = len(slides)
html = f'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>French Atelier · CEO Marketing Review · June 2026</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/deck.css">
<link rel="stylesheet" href="css/platforms.css">
<link rel="stylesheet" href="css/sections.css">
<link rel="stylesheet" href="css/v2.css">
</head><body>
<header class="header" id="header">
  <div class="header__left">
    <div class="header__brand"><span class="header__brand-mark">FA</span></div>
    <div class="header__titles"><span class="header__title">French Atelier · CEO Marketing Review</span><span class="header__subtitle">June 2026</span></div>
  </div>
  <nav class="header__right"><span class="header__counter" id="slideCounter">1 / {total}</span>
    <button class="header__btn" id="btnFullscreen" title="Fullscreen"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M1 1h4M1 1v4M15 1h-4M15 1v4M1 15h4M1 15v-4M15 15h-4M15 15v-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg></button>
  </nav>
</header>
<main class="deck" id="deck">
{deck_html}
</main>
<nav class="dots" id="dots"></nav>
<div class="footer-hint">Use ← → keys · or click dots · or scroll</div>
<script src="js/deck.js"></script>
</body></html>'''

with open(f"{ROOT}/index.html","w") as f: f.write(html)
print(f"Built {total} slides · {os.path.getsize(f'{ROOT}/index.html')} bytes")
