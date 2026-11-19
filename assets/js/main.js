/* ==========================================================
   DERAPEST — scripts communs à toutes les pages
   Les coordonnées se modifient dans build/data.py (puis relancer le build).
   ========================================================== */
const $ = (s, c = document) => c.querySelector(s);
const $$ = (s, c = document) => [...c.querySelectorAll(s)];
const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const WA_NUMBER = document.body.dataset.wa;
const waUrl = (text) => `https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(text)}`;

/* ---------- Préloader : une seule fois par visite ---------- */
(function preloader() {
  const el = $('#preloader');
  const ready = () => {
    document.body.classList.remove('is-loading');
    document.body.classList.add('is-ready');
  };
  const skip = document.documentElement.classList.contains('pl-skip');
  if (!el || skip || reduced) {
    if (el) el.remove();
    setTimeout(ready, 40);
    try { sessionStorage.setItem('dp-seen', '1'); } catch (e) {}
    return;
  }
  const bar = $('#preloaderBar');
  const count = $('#preloaderCount');
  const MIN = 1800;
  const start = performance.now();
  let loaded = document.readyState === 'complete';
  let finished = false;
  window.addEventListener('load', () => (loaded = true));
  setTimeout(() => (loaded = true), 5000);

  const finish = () => {
    if (finished) return;
    finished = true;
    el.classList.add('is-done');
    ready();
    try { sessionStorage.setItem('dp-seen', '1'); } catch (e) {}
    setTimeout(() => el.remove(), 1300);
  };
  const tick = (now) => {
    if (finished) return;
    const t = Math.min((now - start) / MIN, 1);
    let p = 1 - Math.pow(1 - t, 3);
    if (!loaded) p = Math.min(p, 0.92);
    bar.style.transform = `scaleX(${p})`;
    count.textContent = Math.round(p * 100);
    if (p >= 1) return setTimeout(finish, 250);
    requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
  setTimeout(finish, 6500); // sécurité : ne jamais bloquer le site
})();

/* ---------- Header ---------- */
const header = $('#header');
const heroImg = $('.hero__bg img');
let lastY = 0;
const topbar = $('#topbar');
const onScroll = () => {
  const y = window.scrollY;
  header.classList.toggle('is-scrolled', y > 40);
  if (topbar) topbar.classList.toggle('is-hidden', y > 40);
  const menuOpen = document.body.classList.contains('menu-open');
  header.classList.toggle('is-hidden', !menuOpen && y > 600 && y > lastY + 2);
  if (y < lastY - 2) header.classList.remove('is-hidden');
  lastY = y;
  if (heroImg && !reduced && y < window.innerHeight) heroImg.style.translate = `0 ${y * 0.12}px`;
};
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

/* ---------- Menu mobile + sous-menus ---------- */
const burger = $('#burger');
const nav = $('#nav');
const mobileQuery = window.matchMedia('(max-width: 960px)');
const setMenu = (open) => {
  document.body.classList.toggle('menu-open', open);
  burger.setAttribute('aria-expanded', open);
  burger.setAttribute('aria-label', open ? 'Fermer le menu' : 'Ouvrir le menu');
  if (!open) $$('.nav__dd.is-open').forEach((d) => d.classList.remove('is-open'));
};
burger.addEventListener('click', () => setMenu(!document.body.classList.contains('menu-open')));
$$('.nav__toggle').forEach((t) =>
  t.addEventListener('click', () => {
    const dd = t.parentElement;
    const open = !dd.classList.contains('is-open');
    $$('.nav__dd').forEach((o) => o !== dd && o.classList.remove('is-open'));
    dd.classList.toggle('is-open', open);
    t.setAttribute('aria-expanded', open);
  })
);
nav.addEventListener('click', (e) => e.target.closest('a') && setMenu(false));
window.addEventListener('keydown', (e) => {
  if (e.key !== 'Escape') return;
  setMenu(false);
  if (document.activeElement && nav.contains(document.activeElement)) document.activeElement.blur();
});
mobileQuery.addEventListener('change', () => setMenu(false));

/* ---------- Apparition au scroll ---------- */
const reveals = $$('.reveal');
if ('IntersectionObserver' in window && !reduced) {
  const io = new IntersectionObserver(
    (entries) => entries.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
    }),
    { threshold: 0.1, rootMargin: '0px 0px -5% 0px' }
  );
  reveals.forEach((el) => io.observe(el));
} else {
  reveals.forEach((el) => el.classList.add('is-in'));
}

/* ---------- Carrousel des nuisibles (accueil) ---------- */
const pests = $('#pests');
if (pests) {
  const prev = $('#pestPrev');
  const next = $('#pestNext');
  const step = () => (pests.querySelector('.pest').offsetWidth + 16) * (window.innerWidth > 960 ? 2 : 1);
  const sync = () => {
    prev.disabled = pests.scrollLeft < 8;
    next.disabled = pests.scrollLeft > pests.scrollWidth - pests.clientWidth - 8;
  };
  prev.addEventListener('click', () => pests.scrollBy({ left: -step(), behavior: 'smooth' }));
  next.addEventListener('click', () => pests.scrollBy({ left: step(), behavior: 'smooth' }));
  pests.addEventListener('scroll', sync, { passive: true });
  window.addEventListener('resize', sync);
  sync();
}

/* ---------- FAQ : une seule réponse ouverte ---------- */
$$('.faq').forEach((faq) => {
  const items = $$('details', faq);
  items.forEach((d) => d.addEventListener('toggle', () => {
    if (d.open) items.forEach((o) => o !== d && (o.open = false));
  }));
});

/* ---------- Formulaire de devis → WhatsApp ---------- */
const form = $('#quoteForm');
if (form) {
  const error = $('#formError');
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const d = Object.fromEntries(new FormData(form));
    let ok = true;
    ['nom', 'tel'].forEach((n) => {
      const bad = !d[n].trim();
      form.elements[n].classList.toggle('is-invalid', bad);
      if (bad) ok = false;
    });
    error.hidden = ok;
    if (!ok) return form.querySelector('.is-invalid').focus();
    const lines = [
      'Bonjour Derapest, je souhaite un devis.',
      '',
      `Prestation : ${d.prestation}`,
      `Profil : ${d.profil}`,
      `Nom : ${d.nom.trim()}`,
      `Téléphone : ${d.tel.trim()}`,
      d.zone ? `Département : ${d.zone}` : null,
      d.ville.trim() ? `Ville : ${d.ville.trim()}` : null,
      d.message.trim() ? `Situation : ${d.message.trim()}` : null,
    ].filter((l) => l !== null);
    window.open(waUrl(lines.join('\n')), '_blank', 'noopener');
  });
  form.addEventListener('input', (e) => e.target.classList.remove('is-invalid'));
}

/* ---------- Promesses : défilement une par une sur mobile ---------- */
if (topbar) {
  const items = $$('li', topbar);
  let i = 0;
  items[0].classList.add('is-current');
  if (items.length > 1 && !reduced) setInterval(() => {
    const prevItem = items[i];
    prevItem.classList.remove('is-current');
    prevItem.classList.add('is-leaving');
    setTimeout(() => prevItem.classList.remove('is-leaving'), 500);
    i = (i + 1) % items.length;
    items[i].classList.add('is-current');
  }, 3200);
}

/* ---------- Bulle WhatsApp : rappel après quelques secondes ---------- */
const wa = $('.wa');
if (wa) setTimeout(() => {
  wa.classList.add('is-hint');
  setTimeout(() => wa.classList.remove('is-hint'), 4500);
}, 7000);

/* ---------- Carte 3D : inclinaison au survol + liens départements ---------- */
const zStage = $('#zmapStage');
if (zStage) {
  const tilt = $('#zmapTilt');
  if (!reduced && window.matchMedia('(hover: hover)').matches) {
    zStage.addEventListener('pointermove', (e) => {
      const r = zStage.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width - 0.5;
      const py = (e.clientY - r.top) / r.height - 0.5;
      tilt.style.setProperty('--rx', `${38 - py * 14}deg`);
      tilt.style.setProperty('--rz', `${-12 + px * 10}deg`);
    });
    zStage.addEventListener('pointerleave', () => {
      tilt.style.removeProperty('--rx');
      tilt.style.removeProperty('--rz');
    });
  }
  // survol d'une pastille = département mis en avant sur la carte (et inversement)
  const deps = $$('.zmap__dep');
  const chips = $$('.zmap__chip');
  const link = (href, on) => {
    deps.forEach((d) => d.getAttribute('href') === href && d.classList.toggle('is-hot', on));
    chips.forEach((c) => c.getAttribute('href') === href && c.classList.toggle('is-hot', on));
  };
  [...deps, ...chips].forEach((el) => {
    el.addEventListener('pointerenter', () => link(el.getAttribute('href'), true));
    el.addEventListener('pointerleave', () => link(el.getAttribute('href'), false));
  });
}

/* ---------- Carrousels : défilement auto droite → gauche + glisser ---------- */
$$('.slider').forEach((track) => {
  const items = [...track.children];
  if (items.length < 2) return;
  const delay = +track.dataset.autoplay || 3500;
  const stepSize = () => items[0].getBoundingClientRect().width + parseFloat(getComputedStyle(track).columnGap || 16);
  const maxScroll = () => track.scrollWidth - track.clientWidth;

  // points de navigation
  const dots = document.createElement('div');
  dots.className = 'slider-dots';
  const btns = items.map((_, i) => {
    const b = document.createElement('button');
    b.type = 'button';
    b.setAttribute('aria-label', `Aller à l'élément ${i + 1}`);
    b.addEventListener('click', () => { goTo(i); pause(); });
    dots.appendChild(b);
    return b;
  });
  track.after(dots);
  const current = () => Math.round(track.scrollLeft / stepSize());
  const syncDots = () => {
    const last = track.scrollLeft >= maxScroll() - 4;
    const idx = last ? items.length - 1 : current();
    btns.forEach((b, i) => b.classList.toggle('is-active', i === idx));
  };
  const goTo = (i) => track.scrollTo({ left: Math.min(i * stepSize(), maxScroll()), behavior: 'smooth' });
  track.addEventListener('scroll', syncDots, { passive: true });
  syncDots();

  // autoplay (en pause au survol, au toucher, hors écran, ou si mouvement réduit)
  let paused = false, resumeT, visible = false;
  const pause = () => { paused = true; clearTimeout(resumeT); resumeT = setTimeout(() => (paused = false), 6000); };
  track.addEventListener('pointerenter', (e) => e.pointerType === 'mouse' && (paused = true));
  track.addEventListener('pointerleave', (e) => e.pointerType === 'mouse' && (paused = false));
  track.addEventListener('touchstart', pause, { passive: true });
  track.addEventListener('focusin', pause);
  if ('IntersectionObserver' in window) new IntersectionObserver(([e]) => (visible = e.isIntersecting), { threshold: 0.3 }).observe(track);
  if (!reduced) setInterval(() => {
    if (paused || !visible || document.hidden || maxScroll() < 8) return;
    if (track.scrollLeft >= maxScroll() - 4) track.scrollTo({ left: 0, behavior: 'smooth' });
    else goTo(current() + 1);
  }, delay);

  // glisser à la souris (le doigt et le trackpad fonctionnent nativement)
  let startX = 0, startLeft = 0, down = false, moved = false;
  track.addEventListener('pointerdown', (e) => {
    if (e.pointerType !== 'mouse' || e.button !== 0) return;
    down = true; moved = false; startX = e.clientX; startLeft = track.scrollLeft;
  });
  window.addEventListener('pointermove', (e) => {
    if (!down) return;
    const dx = e.clientX - startX;
    if (!moved && Math.abs(dx) > 5) { moved = true; track.classList.add('is-dragging'); }
    if (moved) track.scrollLeft = startLeft - dx;
  });
  window.addEventListener('pointerup', () => {
    if (!down) return;
    down = false;
    if (moved) {
      track.classList.remove('is-dragging');
      goTo(current());
      pause();
    }
  });
  track.addEventListener('dragstart', (e) => e.preventDefault());
});
