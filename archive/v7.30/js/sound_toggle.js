/* ===================================================
   Sound Toggle Module — French Atelier Deck
   =================================================== */

function toggleVideoSound(btn) {
  const wrap = btn.closest('.phone-frame') || btn.closest('.browser-body--video') || btn.closest('.video-wrap') || btn.parentElement;
  const vid = wrap.querySelector('video');
  if (!vid) return;
  vid.muted = !vid.muted;
  btn.classList.toggle('is-on', !vid.muted);
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
