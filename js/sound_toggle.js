/* ===================================================
   Sound Toggle Module — French Atelier Deck
   =================================================== */

function toggleVideoSound(btn) {
  const wrap = btn.closest('.tv-frame') || btn.closest('.phone-frame') || btn.closest('.browser-body--video') || btn.closest('.video-wrap') || btn.parentElement;
  const vid = wrap ? wrap.querySelector('video') : null;
  if (!vid) return;
  // Mute every OTHER video on the page first so only one plays audio at a time
  document.querySelectorAll('video').forEach(v => {
    if (v !== vid) {
      v.muted = true;
      const otherCard = v.closest('.paid-duo-card');
      if (otherCard) otherCard.classList.remove('sound-on');
      const otherBtn = v.parentElement && v.parentElement.querySelector('.sound-toggle');
      if (otherBtn) otherBtn.classList.remove('is-on');
    }
  });
  vid.muted = !vid.muted;
  btn.classList.toggle('is-on', !vid.muted);
  const card = btn.closest('.paid-duo-card');
  if (card) card.classList.toggle('sound-on', !vid.muted);
  btn.setAttribute('data-muted', vid.muted ? 'true' : 'false');
  if (!vid.muted) { vid.volume = 1.0; }
  vid.play().catch(()=>{});
}
window.toggleVideoSound = toggleVideoSound;

// On load, ensure all videos are muted + autoplay + loop + playsinline
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('video').forEach(v => {
    v.muted = true;
    v.autoplay = true;
    v.loop = true;
    v.playsInline = true;
    v.setAttribute('playsinline', '');
    v.play().catch(()=>{});
  });
});
