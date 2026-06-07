/* v7.8 — Smart per-slide video autoplay
   - When a slide enters viewport, play all its videos (muted+inline)
   - When it leaves, pause them. Frees decode budget for the active slide.
   - Also kicks initial slide on load.
*/
(function(){
  function safePlay(v){
    if (!v) return;
    try {
      v.muted = true;
      v.playsInline = true;
      v.setAttribute('playsinline','');
      v.setAttribute('webkit-playsinline','');
      const p = v.play();
      if (p && typeof p.catch === 'function') p.catch(()=>{});
    } catch(e){}
  }
  function safePause(v){
    if (!v) return;
    try { v.pause(); } catch(e){}
  }
  function init(){
    const deck = document.getElementById('deck');
    if (!deck) return;
    const slides = Array.from(deck.querySelectorAll('.slide'));
    const io = new IntersectionObserver((entries)=>{
      entries.forEach(entry=>{
        const vids = entry.target.querySelectorAll('video');
        if (entry.isIntersecting && entry.intersectionRatio >= 0.35){
          vids.forEach(safePlay);
        } else if (entry.intersectionRatio < 0.1) {
          vids.forEach(safePause);
        }
      });
    }, { root: deck, threshold: [0, 0.1, 0.35, 0.5, 1.0] });
    slides.forEach(s => io.observe(s));
    // Kick the first slide explicitly
    setTimeout(()=>{
      const first = slides[0];
      if (first) first.querySelectorAll('video').forEach(safePlay);
      // Also force-play any in-viewport video right now
      slides.forEach(s=>{
        const r = s.getBoundingClientRect();
        if (r.left < window.innerWidth && r.right > 0){
          s.querySelectorAll('video').forEach(safePlay);
        }
      });
    }, 250);
    // User-gesture unlock: any click anywhere starts/resumes videos in visible slide
    document.addEventListener('click', ()=>{
      slides.forEach(s=>{
        const r = s.getBoundingClientRect();
        if (r.left < window.innerWidth && r.right > 0){
          s.querySelectorAll('video').forEach(safePlay);
        }
      });
    }, { once: true });
  }
  if (document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
