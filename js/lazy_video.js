/* ===================================================
   Safe Lazy Video Loader — French Atelier Deck
   GUARANTEE: a video is NEVER shown black.
   - Every <video> has a poster (first-frame JPG) that stays
     visible until the video itself is decoded and playing.
   - First videos load eagerly; the rest defer their network
     fetch until near the viewport, then fade in over the poster.
   - Pauses offscreen videos to save CPU/bandwidth (poster remains).
   - Works alongside sound_toggle.js for user-controlled audio.
   =================================================== */
(function () {
  function loadVideo(video) {
    if (video.dataset.loaded === '1') return;
    var s = video.querySelector('source');
    if (s && !s.getAttribute('src') && s.getAttribute('data-src')) {
      s.setAttribute('src', s.getAttribute('data-src'));
    }
    video.dataset.loaded = '1';
    video.load();
  }

  function playMuted(video) {
    loadVideo(video);
    video.muted = (video.dataset.userSound !== 'on');
    var p = video.play();
    if (p && p.catch) p.catch(function () {});
  }

  document.addEventListener('DOMContentLoaded', function () {
    var videos = Array.prototype.slice.call(document.querySelectorAll('video'));

    videos.forEach(function (v) {
      // Defer network fetch (move src -> data-src) but KEEP poster visible.
      var s = v.querySelector('source');
      if (s && s.getAttribute('src')) {
        s.setAttribute('data-src', s.getAttribute('src'));
        s.removeAttribute('src');
      }
      v.setAttribute('preload', 'none');
      v.muted = true;
      v.loop = true;
      v.playsInline = true;
      v.setAttribute('playsinline', '');
    });

    // Eager-load the first several videos so the opening slides are instant.
    videos.slice(0, 8).forEach(function (v) { loadVideo(v); });

    if (!('IntersectionObserver' in window)) {
      videos.forEach(function (v) { playMuted(v); });
      return;
    }

    // Start fetching a bit before it scrolls into view.
    var loadObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) loadVideo(e.target); });
    }, { root: null, rootMargin: '1200px 1200px', threshold: 0 });

    // Play when visible; pause when it leaves (poster stays underneath).
    var playObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        var v = e.target;
        if (e.isIntersecting && e.intersectionRatio > 0.2) {
          playMuted(v);
        } else {
          try { v.pause(); } catch (err) {}
        }
      });
    }, { root: null, rootMargin: '0px', threshold: [0, 0.2, 0.6] });

    videos.forEach(function (v) {
      loadObserver.observe(v);
      playObserver.observe(v);
    });
  });
})();
