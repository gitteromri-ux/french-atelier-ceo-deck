/* ===================================================
   Sound Toggle Module — French Atelier Deck
   =================================================== */

window.toggleVideoSound = function(btn) {
  const wrap = btn.closest('.video-wrap');
  const vid = wrap.querySelector('video');
  if (!vid) return;
  vid.muted = !vid.muted;
  btn.classList.toggle('is-on', !vid.muted);
  if (!vid.muted) { vid.play().catch(()=>{}); }
};

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
