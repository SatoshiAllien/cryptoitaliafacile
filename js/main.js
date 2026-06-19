let articlesData = null;

async function loadArticles() {
  if (articlesData) return articlesData;
  const base = getBasePath();
  const res = await fetch(`${base}data/articles.json`);
  articlesData = await res.json();
  return articlesData;
}

function getArticlesByFilter(filter) {
  if (!articlesData) return [];
  const { articles } = articlesData;
  switch (filter) {
    case 'popular': return articles.filter(a => a.popular);
    case 'tip': return articles.filter(a => a.category === 'tip');
    case 'trend': return articles.filter(a => a.category === 'trend');
    case 'guide': return articles.filter(a => a.category === 'guide');
    case 'sicurezza': return articles.filter(a => a.category === 'sicurezza' || a.subcategory === 'sicurezza');
    case 'cardano': return articles.filter(a => a.category === 'cardano');
    case 'strumenti': return articles.filter(a => a.tags?.includes('wallet') || a.tags?.includes('exchange'));
    case 'principianti': return articles.filter(a => a.subcategory === 'principianti' || (a.category === 'guide' && a.difficulty === 'beginner'));
    case 'avanzate': return articles.filter(a => a.subcategory === 'avanzate' || a.difficulty === 'advanced');
    case 'defi': return articles.filter(a => a.subcategory === 'defi' || a.tags?.includes('defi') || a.tags?.includes('staking'));
    case 'wallet': return articles.filter(a => a.subcategory === 'wallet' || a.tags?.includes('wallet'));
    case 'tutorial-principianti': return articles.filter(a => a.category === 'tutorial' && a.subcategory === 'principianti');
    case 'tutorial-avanzati': return articles.filter(a => a.category === 'tutorial' && a.subcategory === 'avanzate');
    default: return articles;
  }
}

function initMobileNav() {
  const toggle = document.getElementById('menu-toggle');
  const nav = document.getElementById('mobile-nav');
  const close = document.getElementById('mobile-nav-close');
  const backdrop = document.getElementById('mobile-nav-backdrop');
  if (!toggle || !nav) return;

  const open = () => { nav.setAttribute('aria-hidden', 'false'); toggle.setAttribute('aria-expanded', 'true'); document.body.style.overflow = 'hidden'; };
  const shut = () => { nav.setAttribute('aria-hidden', 'true'); toggle.setAttribute('aria-expanded', 'false'); document.body.style.overflow = ''; };

  toggle.addEventListener('click', open);
  close?.addEventListener('click', shut);
  backdrop?.addEventListener('click', shut);
}

function initSearchBar() {
  const openBtn = document.getElementById('open-search');
  const bar = document.getElementById('search-bar');
  const closeBtn = document.getElementById('search-close');
  const input = document.getElementById('header-search');
  const suggestions = document.getElementById('search-suggestions');

  if (!openBtn || !bar) return;

  openBtn.addEventListener('click', () => {
    bar.hidden = false;
    input?.focus();
  });
  closeBtn?.addEventListener('click', () => { bar.hidden = true; suggestions.innerHTML = ''; });

  let debounce;
  input?.addEventListener('input', () => {
    clearTimeout(debounce);
    debounce = setTimeout(() => performSearch(input.value, suggestions, 6), 200);
  });
  input?.addEventListener('keydown', e => {
    if (e.key === 'Enter' && input.value.trim()) {
      window.location.href = `${getBasePath()}cerca/index.html?q=${encodeURIComponent(input.value.trim())}`;
    }
  });
}

async function performSearch(query, container, limit = 20) {
  if (!query || query.length < 2) { container.innerHTML = ''; return; }
  await loadArticles();
  const base = getBasePath();
  const q = query.toLowerCase();
  const results = articlesData.articles.filter(a =>
    a.title.toLowerCase().includes(q) ||
    a.excerpt.toLowerCase().includes(q) ||
    (a.tags || []).some(t => t.toLowerCase().includes(q))
  ).slice(0, limit);

  const glossary = (articlesData.glossary || []).filter(g =>
    g.term.toLowerCase().includes(q) || g.definition.toLowerCase().includes(q)
  ).slice(0, 3);

  let html = results.map(a => `
    <a href="${base}articolo.html?slug=${a.slug}" class="search-result-item">
      <span class="search-result-type">${a.category}</span>
      <strong>${a.title}</strong>
    </a>`).join('');

  glossary.forEach(g => {
    html += `<a href="${base}glossario/index.html#${g.term.toLowerCase().replace(/\s+/g, '-')}" class="search-result-item">
      <span class="search-result-type">glossario</span>
      <strong>${g.term}</strong> — ${g.definition.substring(0, 80)}…
    </a>`;
  });

  if (!html) html = '<p style="padding:0.75rem 1rem;color:var(--text-muted)">Nessun risultato trovato.</p>';
  container.innerHTML = html;
}

let fadeObserver = null;

function initFadeIn() {
  if (!fadeObserver) {
    fadeObserver = new IntersectionObserver(entries => {
      entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
    }, { threshold: 0.05, rootMargin: '40px' });
  }

  document.querySelectorAll('.fade-in:not([data-fade-watched])').forEach(el => {
    el.dataset.fadeWatched = '1';
    fadeObserver.observe(el);
    const rect = el.getBoundingClientRect();
    if (rect.height > 0 && rect.top < window.innerHeight && rect.bottom > 0) {
      el.classList.add('visible');
    }
  });
}

function initNewsletter() {
  document.querySelectorAll('.newsletter-form').forEach(form => {
    form.addEventListener('submit', e => {
      e.preventDefault();
      const input = form.querySelector('input[type="email"]');
      if (input?.value) {
        alert('Grazie! Ti abbiamo iscritto alla newsletter CryptoFacile. Controlla la tua email.');
        input.value = '';
      }
    });
  });
}

async function initHomepage() {
  if (document.body.dataset.page !== 'home') return;
  await loadArticles();
  const base = getBasePath();

  const trustEl = document.getElementById('trust-badges');
  if (trustEl) {
    trustEl.innerHTML = SITE_CONFIG.trustBadges.map(b =>
      `<span class="trust-badge"><span class="trust-badge-icon">${b.icon}</span>${b.label}</span>`
    ).join('');
  }

  const teacherCard = document.getElementById('teacher-card');
  if (teacherCard && SITE_CONFIG.teacher) {
    const t = SITE_CONFIG.teacher;
    const photoUrl = getAssetUrl(t.photo);
    teacherCard.classList.add('visible');
    teacherCard.innerHTML = `
      <div class="teacher-photo-wrap">
        <img src="${photoUrl}" alt="${t.name} — ${t.title}" class="teacher-photo" width="280" height="280" loading="eager" decoding="async">
        <span class="teacher-photo-badge">🎓 Insegnante</span>
      </div>
      <div class="teacher-content">
        <span class="section-label">👨‍🏫 Chi ti guida</span>
        <h2>${t.name} — <span class="teacher-title">${t.title}</span></h2>
        <p class="teacher-quote">"${t.quote}"</p>
        <div class="teacher-badges">
          ${t.badges.map(b => `<span class="teacher-badge"><span class="teacher-badge-icon">${b.icon}</span>${b.label}</span>`).join('')}
        </div>
        <a href="${base}${t.href}" class="btn btn-primary btn-sm">Scopri di più su di me →</a>
      </div>`;
  }

  const affiliateGrid = document.getElementById('affiliate-grid');
  if (affiliateGrid && SITE_CONFIG.affiliates) {
    affiliateGrid.innerHTML = SITE_CONFIG.affiliates.map(a => `
      <a href="${a.href}" class="affiliate-card affiliate-card--${a.badgeType} fade-in" target="_blank" rel="noopener noreferrer sponsored" style="--aff-accent:${a.accent};--aff-accent-light:${a.accentLight}">
        <div class="affiliate-card-top">
          <span class="affiliate-card-icon">${a.icon}</span>
          <span class="affiliate-card-badge affiliate-card-badge--${a.badgeType}">${a.badge}</span>
        </div>
        <span class="affiliate-card-tagline">${a.tagline}</span>
        <h3 class="affiliate-card-headline">${a.headline}</h3>
        <p class="affiliate-card-hook">${a.hook}</p>
        <ul class="affiliate-card-perks">
          ${a.perks.map(p => `<li>✓ ${p}</li>`).join('')}
        </ul>
        ${a.code ? `<div class="affiliate-card-code">Codice: <strong>${a.code}</strong></div>` : ''}
        <span class="affiliate-card-cta">${a.cta}</span>
      </a>`).join('');
  }

  const catGrid = document.getElementById('category-grid');
  if (catGrid) {
    catGrid.innerHTML = SITE_CONFIG.categories.map(c => `
      <a href="${base}${c.href}" class="category-card fade-in" style="--cat-color:${c.color};--cat-bg:${c.bg}">
        <span class="category-icon">${c.iconImg
          ? `<img src="${base}${c.iconImg}" alt="${c.label}" class="category-icon-img" width="40" height="40" loading="lazy" />`
          : c.icon}</span>
        <span class="category-label">${c.label}</span>
      </a>`).join('');
  }

  const popular = document.getElementById('popular-guides');
  if (popular) {
    popular.innerHTML = getArticlesByFilter('popular').slice(0, 6)
      .map(a => renderArticleCard(a, base)).join('');
  }

  const trends = document.getElementById('trends-grid');
  if (trends) {
    trends.innerHTML = getArticlesByFilter('trend').slice(0, 4)
      .map(t => renderTrendCard(t, base)).join('');
  }

  const tips = document.getElementById('tips-list');
  if (tips) {
    tips.innerHTML = getArticlesByFilter('tip').slice(0, 8)
      .map(t => renderTipCard(t, base)).join('');
  }

  const path = document.getElementById('beginner-path');
  if (path) {
    path.innerHTML = SITE_CONFIG.beginnerPath.map((s, i) => `
      <a href="${base}${s.href}" class="path-step fade-in" style="--step-color:${SITE_CONFIG.pathColors[i]}">
        <span class="path-number">${s.step}</span>
        <div class="path-content">
          <h3>${s.title}</h3>
          <p>${s.desc}</p>
        </div>
        <span class="path-arrow">→</span>
      </a>`).join('');
  }

  const tools = document.getElementById('tools-grid');
  if (tools) {
    tools.innerHTML = SITE_CONFIG.tools.map(t => `
      <div class="tool-card fade-in${t.affiliate ? ' tool-card--affiliate' : ''}">
        <div class="tool-category">${t.category}${t.affiliate ? ' <span class="tool-affiliate-tag">BONUS</span>' : ''}</div>
        <h3>${t.name}</h3>
        <p>${t.desc}</p>
        <a href="${t.href}" class="btn btn-ghost btn-sm"${t.affiliate ? ' target="_blank" rel="noopener noreferrer sponsored"' : ''}>${t.affiliate ? 'Ottieni bonus →' : 'Scopri →'}</a>
      </div>`).join('');
  }
}

async function initHubPage() {
  const hub = document.body.dataset.hub;
  if (!hub) return;
  await loadArticles();
  const base = getBasePath();
  const params = new URLSearchParams(window.location.search);
  const hubFilterMap = { guide: 'guide', tips: 'tip', trend: 'trend', sicurezza: 'sicurezza', cardano: 'cardano', strumenti: 'strumenti' };
  const filter = params.get('filter') || hubFilterMap[hub] || hub;

  const grid = document.getElementById('hub-articles');
  if (!grid) return;

  function render(filterKey) {
    const items = getArticlesByFilter(filterKey);
    grid.innerHTML = items.length
      ? items.map(a => hub === 'tips' ? renderTipCard(a, base) : renderArticleCard(a, base)).join('')
      : '<p style="color:var(--text-muted)">Nessun articolo in questa categoria.</p>';
    document.querySelectorAll('.filter-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.filter === filterKey);
    });
  }

  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', () => render(btn.dataset.filter));
  });

  render(filter);
}

function initAboutPage() {
  const el = document.getElementById('about-teacher');
  const t = SITE_CONFIG.teacher;
  if (!el || !t) return;
  const base = getBasePath();
  const photoUrl = getAssetUrl(t.photo);
  el.classList.add('visible');
  el.innerHTML = `
    <div class="about-hero-inner">
      <div class="teacher-photo-wrap">
        <img src="${photoUrl}" alt="${t.name} — ${t.title}" class="teacher-photo" width="300" height="300" loading="eager" decoding="async">
        <span class="teacher-photo-badge">🎓 Insegnante</span>
      </div>
      <div>
        <span class="section-label">Chi siamo</span>
        <h1>${t.name}</h1>
        <p class="about-role">${t.title} · Fondatore di CryptoFacile</p>
        <p class="teacher-quote" style="margin-top:1rem;">"${t.quote}"</p>
        <div class="teacher-badges" style="margin-top:1.25rem;">
          ${t.badges.map(b => `<span class="teacher-badge"><span class="teacher-badge-icon">${b.icon}</span>${b.label}</span>`).join('')}
        </div>
      </div>
    </div>`;
}

async function initGlossary() {
  if (document.body.dataset.page !== 'glossary') return;
  await loadArticles();
  const grid = document.getElementById('glossary-grid');
  const alpha = document.getElementById('glossary-alpha');
  if (!grid || !articlesData.glossary) return;

  const terms = [...articlesData.glossary].sort((a, b) => a.term.localeCompare(b.term, 'it'));
  const letters = [...new Set(terms.map(t => t.term[0].toUpperCase()))].sort();

  if (alpha) {
    alpha.innerHTML = `<button class="active" data-letter="all">Tutti</button>` +
      letters.map(l => `<button data-letter="${l}">${l}</button>`).join('');
    alpha.addEventListener('click', e => {
      if (e.target.tagName !== 'BUTTON') return;
      const letter = e.target.dataset.letter;
      alpha.querySelectorAll('button').forEach(b => b.classList.toggle('active', b === e.target));
      renderGlossary(letter === 'all' ? terms : terms.filter(t => t.term[0].toUpperCase() === letter));
    });
  }

  function renderGlossary(list) {
    grid.innerHTML = list.map(g => `
      <div class="glossary-item" id="${g.term.toLowerCase().replace(/\s+/g, '-')}">
        <div class="glossary-term">${g.term}</div>
        <p class="glossary-def">${g.definition}</p>
      </div>`).join('');
  }
  renderGlossary(terms);
}

async function initSearchPage() {
  if (document.body.dataset.page !== 'search') return;
  await loadArticles();
  const input = document.getElementById('search-page-input');
  const results = document.getElementById('search-page-results');
  const params = new URLSearchParams(window.location.search);
  const q = params.get('q') || '';

  if (input) {
    input.value = q;
    if (q) showSearchResults(q, results);

    let debounce;
    input.addEventListener('input', () => {
      clearTimeout(debounce);
      debounce = setTimeout(() => {
        const val = input.value;
        const url = new URL(window.location);
        if (val) url.searchParams.set('q', val); else url.searchParams.delete('q');
        window.history.replaceState({}, '', url);
        showSearchResults(val, results);
      }, 300);
    });
  }
}

async function showSearchResults(query, container) {
  if (!container) return;
  if (!query || query.length < 2) { container.innerHTML = ''; return; }
  const base = getBasePath();
  const q = query.toLowerCase();
  const items = articlesData.articles.filter(a =>
    a.title.toLowerCase().includes(q) || a.excerpt.toLowerCase().includes(q)
  );

  container.innerHTML = items.length
    ? items.map(a => `
        <a href="${base}articolo.html?slug=${a.slug}" class="search-page-result">
          <span class="badge badge--${a.difficulty}">${a.category}</span>
          <h3>${a.title}</h3>
          <p>${a.excerpt}</p>
        </a>`).join('')
    : `<p style="color:var(--text-muted);padding:2rem 0">Nessun risultato per "<strong>${query}</strong>". Prova con altri termini.</p>`;
}

function loadCryptoBackground() {
  return new Promise((resolve, reject) => {
    if (window.initCryptoBackground) { resolve(); return; }
    const s = document.createElement('script');
    s.src = getBasePath() + 'js/crypto-background.js';
    s.onload = resolve;
    s.onerror = reject;
    document.head.appendChild(s);
  });
}

document.addEventListener('DOMContentLoaded', async () => {
  try {
    await loadCryptoBackground();
    initCryptoBackground();
  } catch (_) { /* background non critico */ }
  injectLayout();
  initMobileNav();
  initSearchBar();
  initFadeIn();
  initNewsletter();
  await initHomepage();
  await initHubPage();
  await initGlossary();
  await initSearchPage();
  initAboutPage();
  initFadeIn();
});