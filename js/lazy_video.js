/* ===================================================
   Safe Lazy Video Loader — French Atelier Deck
   GUARANTEE: a video is NEVER shown black, and NOTHING autoplays.
   - Every <video> shows its poster (first-frame JPG) until the
     viewer clicks it. No video plays on its own.
   - A gold play badge sits over each poster as an affordance.
   - Click toggles play/pause. Sound stays OFF until the per-video
     sound toggle is used (handled by sound_toggle.js).
   - Offscreen playing videos are paused (poster/last frame remains).
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

  function wrapWithBadge(video) {
    if (video.parentElement && video.parentElement.classList.contains('video-clickwrap')) return;
    var wrap = document.createElement('div');
    wrap.className = 'video-clickwrap';
    var parent = video.parentNode;
    parent.insertBefore(wrap, video);
    wrap.appendChild(video);
    var badge = document.createElement('button');
    badge.className = 'video-play-badge';
    badge.setAttribute('aria-label', 'Play video');
    badge.type = 'button';
    badge.innerHTML = '<span class="video-play-badge__tri"></span>';
    wrap.appendChild(badge);

    function play() {
      loadVideo(video);
      video.muted = (video.dataset.userSound !== 'on');
      var p = video.play();
      if (p && p.catch) p.catch(function () {});
    }
    function pause() { try { video.pause(); } catch (e) {} }

    badge.addEventListener('click', function (e) { e.stopPropagation(); play(); });
    video.addEventListener('click', function () {
      if (video.paused) play(); else pause();
    });
    video.addEventListener('playing', function () { wrap.classList.add('is-playing'); });
    video.addEventListener('pause', function () { wrap.classList.remove('is-playing'); });
    video.addEventListener('ended', function () { wrap.classList.remove('is-playing'); });
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
      v.removeAttribute('autoplay');
      v.muted = true;
      v.loop = true;
      v.playsInline = true;
      v.setAttribute('playsinline', '');
      wrapWithBadge(v);
    });

    // Pause videos that scroll fully offscreen (no autoplay on enter).
    if ('IntersectionObserver' in window) {
      var pauseObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) { try { e.target.pause(); } catch (err) {} }
        });
      }, { root: null, rootMargin: '0px', threshold: 0 });
      videos.forEach(function (v) { pauseObserver.observe(v); });
    }
  });
})();
