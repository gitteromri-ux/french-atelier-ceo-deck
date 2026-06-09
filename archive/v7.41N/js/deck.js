/**
 * French Atelier · CEO Deck · deck.js
 * Handles: slide counting, dot nav, keyboard navigation,
 *          scroll-based counter, fullscreen toggle, PDF button.
 */

(function () {
  'use strict';

  /* ─── ELEMENTS ─── */
  const deck        = document.getElementById('deck');
  const header      = document.getElementById('header');
  const dotNav      = document.getElementById('dotNav');
  const counter     = document.getElementById('slideCounter');
  const btnFS       = document.getElementById('btnFullscreen');

  /* ─── COLLECT SLIDES ─── */
  const slides = Array.from(deck.querySelectorAll('.slide'));
  const total  = slides.length;

  /* ─── STATE ─── */
  let current     = 0;
  let isScrolling = false;

  /* ─── SLIDE COUNTER TEXT ─── */
  function updateCounter(idx) {
    if (counter) counter.textContent = `${idx + 1} / ${total}`;
  }

  /* ─── HEADER THEME ─── */
  function updateHeaderTheme(idx) {
    const slide = slides[idx];
    if (!slide) return;
    if (slide.classList.contains('slide--dark')) {
      header.classList.add('header--dark');
    } else {
      header.classList.remove('header--dark');
    }
  }

  /* ─── BUILD DOT NAVIGATION ─── */
  function buildDots() {
    if (!dotNav) return;
    dotNav.innerHTML = '';
    slides.forEach((slide, i) => {
      const btn = document.createElement('button');
      btn.className = 'dot-nav__dot' + (i === 0 ? ' is-active' : '');
      btn.setAttribute('aria-label', `Go to slide ${i + 1}`);
      btn.setAttribute('title', `Slide ${i + 1}`);
      btn.dataset.index = i;
      btn.addEventListener('click', () => goTo(i));
      dotNav.appendChild(btn);
    });
  }

  /* ─── UPDATE ACTIVE DOT ─── */
  function updateDots(idx) {
    const dots = dotNav ? dotNav.querySelectorAll('.dot-nav__dot') : [];
    dots.forEach((d, i) => {
      d.classList.toggle('is-active', i === idx);
    });
  }

  /* ─── NAVIGATE TO SLIDE ─── */
  function goTo(idx, smooth = true) {
    if (idx < 0 || idx >= total) return;
    current = idx;
    const target = slides[idx];

    deck.scrollTo({
      left: target.offsetLeft,
      behavior: smooth ? 'smooth' : 'instant',
    });

    updateCounter(idx);
    updateDots(idx);
    updateHeaderTheme(idx);
  }

  /* ─── KEYBOARD NAVIGATION ─── */
  document.addEventListener('keydown', (e) => {
    switch (e.key) {
      case 'ArrowRight':
      case 'ArrowDown':
      case 'PageDown':
        e.preventDefault();
        goTo(current + 1);
        break;
      case 'ArrowLeft':
      case 'ArrowUp':
      case 'PageUp':
        e.preventDefault();
        goTo(current - 1);
        break;
      case 'Home':
        e.preventDefault();
        goTo(0);
        break;
      case 'End':
        e.preventDefault();
        goTo(total - 1);
        break;
      case 'f':
      case 'F':
        toggleFullscreen();
        break;
    }
  });

  /* ─── SCROLL OBSERVER — track current slide ─── */
  function onScroll() {
    if (isScrolling) return;
    const scrollLeft   = deck.scrollLeft;
    const slideWidth   = deck.clientWidth;
    const nearest      = Math.round(scrollLeft / slideWidth);
    const clamped      = Math.max(0, Math.min(total - 1, nearest));
    if (clamped !== current) {
      current = clamped;
      updateCounter(clamped);
      updateDots(clamped);
      updateHeaderTheme(clamped);
    }
  }

  deck.addEventListener('scroll', onScroll, { passive: true });

  /* ─── INTERSECTION OBSERVER — more accurate current slide ─── */
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting && entry.intersectionRatio >= 0.5) {
          const idx = slides.indexOf(entry.target);
          if (idx !== -1 && idx !== current) {
            current = idx;
            updateCounter(idx);
            updateDots(idx);
            updateHeaderTheme(idx);
          }
        }
      });
    },
    { root: deck, threshold: 0.5 }
  );

  slides.forEach((s) => io.observe(s));

  /* ─── FULLSCREEN ─── */
  function toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen?.().catch(() => {});
    } else {
      document.exitFullscreen?.().catch(() => {});
    }
  }

  document.addEventListener('fullscreenchange', () => {
    if (btnFS) {
      const inFS = !!document.fullscreenElement;
      btnFS.setAttribute('aria-label', inFS ? 'Exit fullscreen' : 'Enter fullscreen');
      btnFS.innerHTML = inFS
        ? `<svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
             <path d="M5 1H1v4M11 1h4v4M1 11v4h4M15 11v4h-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
           </svg>`
        : `<svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
             <path d="M1 1h4M1 1v4M15 1h-4M15 1v4M1 15h4M1 15v-4M15 15h-4M15 15v-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
           </svg>`;
    }
  });

  if (btnFS) {
    btnFS.addEventListener('click', toggleFullscreen);
  }

  /* ─── TOUCH SWIPE ─── */
  let touchStartX = 0;
  let touchStartY = 0;

  deck.addEventListener('touchstart', (e) => {
    touchStartX = e.touches[0].clientX;
    touchStartY = e.touches[0].clientY;
  }, { passive: true });

  deck.addEventListener('touchend', (e) => {
    const dx = e.changedTouches[0].clientX - touchStartX;
    const dy = e.changedTouches[0].clientY - touchStartY;
    if (Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > 40) {
      goTo(dx < 0 ? current + 1 : current - 1);
    }
  }, { passive: true });

  /* ─── INIT ─── */
  function init() {
    updateCounter(0);
    buildDots();
    updateHeaderTheme(0);
  }

  // Run once fonts + layout are ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
