/* ===================================================
   Sound Toggle Module — French Atelier Deck (click-to-play)
   - NOTHING autoplays. Videos play only when the viewer clicks
     them (handled by lazy_video.js click-to-play badges).
   - Sound is OFF by default. The per-video sound-toggle button
     enables audio for that one video and mutes all others.
   =================================================== */

function _muteAllExcept(keepVid){
  document.querySelectorAll('video').forEach(v => {
    if (v !== keepVid) {
      v.muted = true;
      v.dataset.userSound = 'off';
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
  vid.dataset.userSound = vid.muted ? 'off' : 'on';
  btn.classList.toggle('is-on', !vid.muted);
  const card = btn.closest('.paid-duo-card');
  if (card) card.classList.toggle('sound-on', !vid.muted);
  btn.setAttribute('data-muted', vid.muted ? 'true' : 'false');
  if (!vid.muted) { vid.volume = 1.0; }
  // Enabling sound also starts playback for this one video (user gesture).
  vid.play().catch(()=>{});
}
window.toggleVideoSound = toggleVideoSound;

document.addEventListener('DOMContentLoaded', () => {
  // Establish safe defaults: muted, looping, NO autoplay.
  document.querySelectorAll('video').forEach(v => {
    v.muted = true;
    v.dataset.userSound = v.dataset.userSound || 'off';
    v.autoplay = false;
    v.removeAttribute('autoplay');
    v.loop = true;
    v.playsInline = true;
    v.setAttribute('playsinline', '');
  });
});
