/* ===================================================
   Sound Toggle Module — French Atelier Deck v8.1
   - Per-video toggle (mutes others)
   - Active-slide audio: only the slide in view plays sound (after user enables)
   - One-tap "Enable sound" overlay to satisfy browser autoplay policy
   =================================================== */

let SOUND_ENABLED = false;

function _muteAllExcept(keepVid){
  document.querySelectorAll('video').forEach(v => {
    if (v !== keepVid) {
      v.muted = true;
      const c = v.closest('.paid-duo-card');
      if (c) c.classList.remove('sound-on');
      const b = v.parentElement && v.parentElement.querySelector('.sound-toggle');
      if (b) { b.classList.remove('is-on'); b.setAttribute('data-muted','true'); }
    }
  });
}

function toggleVideoSound(btn) {
  const wrap = btn.closest('.tv-frame') || btn.closest('.phone-frame') || btn.closest('.browser-body--video') || btn.closest('.video-wrap') || btn.parentElement;
  const vid = wrap ? wrap.querySelector('video') : null;
  if (!vid) return;
  _muteAllExcept(vid);
  vid.muted = !vid.muted;
  btn.classList.toggle('is-on', !vid.muted);
  const card = btn.closest('.paid-duo-card');
  if (card) card.classList.toggle('sound-on', !vid.muted);
  btn.setAttribute('data-muted', vid.muted ? 'true' : 'false');
  if (!vid.muted) { vid.volume = 1.0; SOUND_ENABLED = true; }
  vid.play().catch(()=>{});
}
window.toggleVideoSound = toggleVideoSound;

function _enableAudioGlobally(){
  if (SOUND_ENABLED) return;
  SOUND_ENABLED = true;
  document.querySelectorAll('video').forEach(v => { v.volume = 1.0; });
  // Pick the slide most in view and unmute its first video
  let bestVid = null, bestRatio = 0;
  document.querySelectorAll('.slide').forEach(slide => {
    const r = slide.getBoundingClientRect();
    const vh = window.innerHeight;
    const visible = Math.max(0, Math.min(r.bottom, vh) - Math.max(r.top, 0));
    const ratio = visible / Math.max(1, vh);
    if (ratio > bestRatio) {
      const v = slide.querySelector('video');
      if (v) { bestRatio = ratio; bestVid = v; }
    }
  });
  if (bestVid){
    _muteAllExcept(bestVid);
    bestVid.muted = false;
    bestVid.volume = 1.0;
    bestVid.play().catch(()=>{});
    const slide = bestVid.closest('.slide');
    if (slide){
      const card = bestVid.closest('.paid-duo-card');
      if (card) card.classList.add('sound-on');
      const btn = bestVid.parentElement && bestVid.parentElement.querySelector('.sound-toggle');
      if (btn) { btn.classList.add('is-on'); btn.setAttribute('data-muted','false'); }
    }
  }
  const ov = document.getElementById('sound-enable-overlay');
  if (ov) ov.remove();
}

document.addEventListener('DOMContentLoaded', () => {
  // Ensure base autoplay attributes
  document.querySelectorAll('video').forEach(v => {
    v.muted = true;
    v.autoplay = true;
    v.loop = true;
    v.playsInline = true;
    v.setAttribute('playsinline', '');
    v.play().catch(()=>{});
  });

  // One-tap "Enable sound" overlay
  if (!document.getElementById('sound-enable-overlay')){
    const ov = document.createElement('button');
    ov.id = 'sound-enable-overlay';
    ov.type = 'button';
    ov.innerHTML = '🔊 Tap for sound';
    ov.style.cssText = [
      'position:fixed','right:20px','bottom:20px','z-index:99999',
      'background:rgba(10,17,40,0.92)','color:#fff','border:none',
      'padding:12px 18px','border-radius:999px','font:600 14px/1 system-ui,-apple-system,Segoe UI,sans-serif',
      'cursor:pointer','box-shadow:0 8px 24px rgba(0,0,0,0.25)','letter-spacing:0.3px'
    ].join(';');
    ov.addEventListener('click', _enableAudioGlobally);
    document.body.appendChild(ov);
  }

  // Auto-unmute active slide once sound is enabled
  if ('IntersectionObserver' in window){
    const io = new IntersectionObserver(entries => {
      if (!SOUND_ENABLED) return;
      entries.forEach(e => {
        if (e.isIntersecting && e.intersectionRatio > 0.55){
          const v = e.target.querySelector('video');
          if (v){
            _muteAllExcept(v);
            v.muted = false;
            v.volume = 1.0;
            v.play().catch(()=>{});
            const btn = v.parentElement && v.parentElement.querySelector('.sound-toggle');
            if (btn){ btn.classList.add('is-on'); btn.setAttribute('data-muted','false'); }
            const card = v.closest('.paid-duo-card');
            if (card) card.classList.add('sound-on');
          }
        }
      });
    }, { threshold: [0, 0.55, 0.8] });
    document.querySelectorAll('.slide').forEach(s => io.observe(s));
  }

  // Any user click anywhere unlocks audio (safety net)
  const unlock = () => { _enableAudioGlobally(); document.removeEventListener('click', unlock, true); };
  document.addEventListener('click', unlock, true);
});
