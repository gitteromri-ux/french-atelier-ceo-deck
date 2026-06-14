/**
 * French Atelier · CEO Deck · deck_nav.js
 * Minimal, self-contained horizontal navigation for the .deck strip.
 * The deck is a horizontal flex strip (slide = 100vw) with
 * scroll-snap-type: x mandatory. This gives users who only have a
 * vertical mouse wheel a way to move between slides, plus arrow keys.
 * Trackpad horizontal-swipe and the (hidden) scrollbar already work
 * natively — this only ADDS input methods, it never blocks them.
 *
 * Desktop only: on mobile (<=900px) the deck scrolls vertically and
 * native touch handles everything, so we no-op there.
 */
(function () {
  'use strict';

  var deck = document.querySelector('.deck');
  if (!deck) return;

  var DESKTOP = function () { return window.matchMedia('(min-width: 769px)').matches; };

  function slideWidth() { return deck.clientWidth || window.innerWidth; }

  function currentIndex() {
    return Math.round(deck.scrollLeft / slideWidth());
  }

  function goTo(idx) {
    var slides = deck.querySelectorAll('.slide');
    var max = slides.length - 1;
    if (idx < 0) idx = 0;
    if (idx > max) idx = max;
    deck.scrollTo({ left: idx * slideWidth(), behavior: 'smooth' });
  }

  /* ─── VERTICAL WHEEL → HORIZONTAL SCROLL (mouse users) ─── */
  var wheelLock = false;
  deck.addEventListener('wheel', function (e) {
    if (!DESKTOP()) return; // mobile: let native vertical scroll work

    // If a slide's inner content is itself vertically scrollable and not
    // yet at its scroll limit, let the inner content scroll first.
    var inner = e.target.closest && e.target.closest('.slide');
    if (inner && e.deltaY !== 0) {
      var canInnerScroll =
        inner.scrollHeight > inner.clientHeight + 2 &&
        ((e.deltaY > 0 && inner.scrollTop + inner.clientHeight < inner.scrollHeight - 1) ||
         (e.deltaY < 0 && inner.scrollTop > 1));
      if (canInnerScroll) return; // don't hijack — inner scroll handles it
    }

    // Convert the dominant wheel delta into a single snap step.
    var delta = Math.abs(e.deltaX) > Math.abs(e.deltaY) ? e.deltaX : e.deltaY;
    if (delta === 0) return;
    e.preventDefault();
    if (wheelLock) return;
    wheelLock = true;
    goTo(currentIndex() + (delta > 0 ? 1 : -1));
    setTimeout(function () { wheelLock = false; }, 450);
  }, { passive: false });

  /* ─── KEYBOARD NAVIGATION ─── */
  document.addEventListener('keydown', function (e) {
    if (!DESKTOP()) return;
    var tag = (e.target.tagName || '').toLowerCase();
    if (tag === 'input' || tag === 'textarea') return;
    switch (e.key) {
      case 'ArrowRight':
      case 'ArrowDown':
      case 'PageDown':
      case ' ':
        e.preventDefault();
        goTo(currentIndex() + 1);
        break;
      case 'ArrowLeft':
      case 'ArrowUp':
      case 'PageUp':
        e.preventDefault();
        goTo(currentIndex() - 1);
        break;
      case 'Home':
        e.preventDefault();
        goTo(0);
        break;
      case 'End':
        e.preventDefault();
        goTo(deck.querySelectorAll('.slide').length - 1);
        break;
    }
  });
})();
