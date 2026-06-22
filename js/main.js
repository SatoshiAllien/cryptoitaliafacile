let articlesData = null;

async function loadArticles() {
  if (articlesData) return articlesData;
  const base = getBasePath();
  const v = (typeof SITE_CONFIG !== 'undefined' && SITE_CONFIG.assetVersion) ? `?v=${SITE_CONFIG.assetVersion}` : '';
  const res = await fetch(`${base}data/articles.json${v}`);
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
    case 'bitcoin': return articles.filter(a => a.category === 'bitcoin' || (a.tags || []).some(tag => tag.toLowerCase().includes('bitcoin')));
    case 'ethereum': return articles.filter(a => a.category === 'ethereum' || (a.tags || []).some(tag => tag.toLowerCase().includes('ethereum')));
    case 'smart-contract': return articles.filter(a => a.category === 'smart-contract' || (a.tags || []).some(tag => tag.toLowerCase().includes('smart contract')));
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

function initNavActive() {
  const path = window.location.pathname;
  const routes = [
    { href: 'chat/index.html', test: () => path.includes('/chat/') },
    { href: 'crypto-tips/index.html', test: () => path.includes('/crypto-tips/') },
    { href: 'trend/index.html', test: () => path.includes('/trend/') },
    { href: 'news/index.html', test: () => path.includes('/news/') },
    { href: 'sicurezza/index.html', test: () => path.includes('/sicurezza/') },
    { href: 'cardano/index.html', test: () => path.includes('/cardano/') },
    { href: 'strumenti/index.html', test: () => path.includes('/strumenti/') },
    { href: 'guide/index.html', test: () => path.includes('/guide/') }
  ];
  const active = routes.find(r => r.test())?.href || null;
  document.querySelectorAll('[data-nav-href]').forEach(el => {
    el.classList.toggle('nav-tab--active', el.getAttribute('data-nav-href') === active);
  });
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
  const results = articlesData.articles.filter(a => {
    const loc = localizeArticle(a);
    return loc.title.toLowerCase().includes(q) ||
      loc.excerpt.toLowerCase().includes(q) ||
      (a.tags || []).some(tag => tag.toLowerCase().includes(q));
  }).slice(0, limit);

  const glossary = (articlesData.glossary || []).filter(g => {
    const loc = localizeGlossary(g);
    return g.term.toLowerCase().includes(q) || loc.definition.toLowerCase().includes(q);
  }).slice(0, 3);

  let html = results.map(a => {
    const loc = localizeArticle(a);
    return `
    <a href="${base}articolo.html?slug=${a.slug}" class="search-result-item">
      <span class="search-result-type">${a.category}</span>
      <strong>${loc.title}</strong>
    </a>`;
  }).join('');

  glossary.forEach(g => {
    const loc = localizeGlossary(g);
    html += `<a href="${base}glossario/index.html#${g.term.toLowerCase().replace(/\s+/g, '-')}" class="search-result-item">
      <span class="search-result-type">${t('pages.glossary.glossaryLabel')}</span>
      <strong>${g.term}</strong> — ${loc.definition.substring(0, 80)}…
    </a>`;
  });

  if (!html) html = `<p style="padding:0.75rem 1rem;color:var(--text-muted)">${t('ui.noResults')}</p>`;
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

  document.querySelectorAll('.hospitality-timeline-item:not([data-timeline-watched])').forEach((el, i) => {
    el.dataset.timelineWatched = '1';
    el.style.transitionDelay = `${i * 0.12}s`;
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
        alert(t('pages.newsletter.thanks'));
        input.value = '';
      }
    });
  });
}

async function initHomepage() {
  if (document.body.dataset.page !== 'home') return;
  const base = getBasePath();

  const trustEl = document.getElementById('trust-badges');
  if (trustEl) {
    const badges = t('trust');
    trustEl.innerHTML = (Array.isArray(badges) ? badges : SITE_CONFIG.trustBadges).map(b =>
      `<span class="trust-badge">${b}</span>`
    ).join('');
  }

  try {
    await loadArticles();
  } catch (_) { /* articoli non critici per homepage */ }

  const affiliateGrid = document.getElementById('affiliate-grid');
  if (affiliateGrid && SITE_CONFIG.affiliates) {
    affiliateGrid.innerHTML = SITE_CONFIG.affiliates.map(a => {
      const loc = t(`affiliates.${a.id}`) || {};
      return `
      <a href="${a.href}" class="affiliate-card affiliate-card--${a.badgeType} fade-in" target="_blank" rel="noopener noreferrer sponsored" style="--aff-accent:${a.accent};--aff-accent-light:${a.accentLight}">
        <div class="affiliate-card-top">
          <span class="affiliate-card-initial">${a.initial || a.name[0]}</span>
          <span class="affiliate-card-badge affiliate-card-badge--${a.badgeType}">${a.badge}</span>
        </div>
        <span class="affiliate-card-tagline">${loc.tagline || a.tagline}</span>
        <h3 class="affiliate-card-headline">${loc.headline || a.headline}</h3>
        <p class="affiliate-card-hook">${loc.hook || a.hook}</p>
        <ul class="affiliate-card-perks">
          ${(loc.perks || a.perks).map(p => `<li>✓ ${p}</li>`).join('')}
        </ul>
        ${a.code ? `<div class="affiliate-card-code">${loc.code || 'Codice'}: <strong>${a.code}</strong></div>` : ''}
        <span class="affiliate-card-cta">${loc.cta || a.cta}</span>
      </a>`;
    }).join('');
  }

  const catGrid = document.getElementById('category-grid');
  if (catGrid) {
    catGrid.innerHTML = SITE_CONFIG.categories.map(c => `
      <a href="${base}${c.href}" class="category-card fade-in" style="--cat-color:${c.color};--cat-bg:${c.bg}">
        <span class="category-icon">${c.iconImg
          ? `<img src="${base}${c.iconImg}" alt="${c.label}" class="category-icon-img" width="28" height="28" loading="lazy" />`
          : `<span class="category-abbr">${c.abbr || c.label[0]}</span>`}</span>
        <span class="category-label">${t(`categories.${c.id}`) || c.label}</span>
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
    const pathTr = t('path') || [];
    path.innerHTML = SITE_CONFIG.beginnerPath.map((s, i) => `
      <a href="${base}${s.href}" class="path-step fade-in" style="--step-color:${SITE_CONFIG.pathColors[i]}">
        <span class="path-number">${s.step}</span>
        <div class="path-content">
          <h3>${pathTr[i]?.title || s.title}</h3>
          <p>${pathTr[i]?.desc || s.desc}</p>
        </div>
        <span class="path-arrow">→</span>
      </a>`).join('');
  }

  const tools = document.getElementById('tools-grid');
  if (tools) {
    const toolKeys = { Ledger: 'ledger', Revolut: 'revolut', Kraken: 'kraken', Eternl: 'eternl' };
    tools.innerHTML = SITE_CONFIG.tools.map(tool => {
      const key = toolKeys[tool.name];
      const loc = key ? t(`tools.${key}`) : null;
      return `
      <div class="tool-card fade-in${tool.affiliate ? ' tool-card--affiliate' : ''}">
        <div class="tool-category">${loc?.cat || tool.category}${tool.affiliate ? ' <span class="tool-affiliate-tag">BONUS</span>' : ''}</div>
        <h3>${tool.name}</h3>
        <p>${loc?.desc || tool.desc}</p>
        <a href="${tool.href}" class="btn btn-ghost btn-sm"${tool.affiliate ? ' target="_blank" rel="noopener noreferrer sponsored"' : ''}>${tool.affiliate ? t('ui.getBonus') : t('ui.discover')}</a>
      </div>`;
    }).join('');
  }

  const homeSocial = document.getElementById('home-social-links');
  if (homeSocial && SITE_CONFIG.social) {
    homeSocial.innerHTML = renderSocialLinks();
  }

  initHeroSocialIcons();
}

function initHeroSocialIcons() {
  const el = document.getElementById('hero-social-icons');
  if (!el || !SITE_CONFIG.social) return;
  const base = getBasePath();
  const order = ['instagram', 'facebook', 'x'];
  el.innerHTML = order.map(id => {
    const s = getSocial(id);
    if (!s) return '';
    const iconFile = `${base}assets/img/social/icon-${id}.svg`;
    return `<a href="${s.url}" class="hero-social-icon hero-social-icon--${id}" data-label="${s.handle || s.name}" target="_blank" rel="noopener noreferrer" aria-label="${s.name}">
      <img src="${iconFile}" alt="" width="24" height="24" loading="eager" decoding="async">
    </a>`;
  }).join('');
}

function initHubI18n() {
  const hub = document.body.dataset.hub;
  if (!hub) return;
  const hubData = t(`hubs.${hub}`);
  if (!hubData || typeof hubData !== 'object') return;
  const h1 = document.querySelector('.page-hero h1, .page-hero-brand h1');
  const desc = document.querySelector('.page-hero > p, .page-hero-brand p');
  if (h1) h1.textContent = hubData.title;
  if (desc) desc.textContent = hubData.desc;
  const toolsH2 = document.querySelector('#tools-grid')?.closest('section')?.querySelector('h2');
  if (hub === 'strumenti' && toolsH2 && hubData.toolsSection) toolsH2.textContent = hubData.toolsSection;
  const filterMap = {
    guide: 'ui.all', principianti: 'nav.principianti', avanzate: 'nav.avanzate',
    defi: 'nav.defi', wallet: 'nav.wallet', sicurezza: 'nav.sicurezza'
  };
  document.querySelectorAll('.filter-btn').forEach(btn => {
    const key = filterMap[btn.dataset.filter];
    if (key) btn.textContent = t(key);
  });
  initStrumentiTools();
}

function initStrumentiTools() {
  if (document.body.dataset.hub !== 'strumenti') return;
  const tools = document.getElementById('tools-grid');
  if (!tools || !SITE_CONFIG.tools) return;
  const toolKeys = { Ledger: 'ledger', Revolut: 'revolut', Kraken: 'kraken', Eternl: 'eternl' };
  const base = getBasePath();
  tools.innerHTML = SITE_CONFIG.tools.map(tool => {
    const key = toolKeys[tool.name];
    const loc = key ? t(`tools.${key}`) : null;
    return `
      <div class="tool-card fade-in${tool.affiliate ? ' tool-card--affiliate' : ''}">
        <div class="tool-category">${loc?.cat || tool.category}${tool.affiliate ? ` <span class="tool-affiliate-tag">${t('messages.bonus')}</span>` : ''}</div>
        <h3>${tool.name}</h3>
        <p>${loc?.desc || tool.desc}</p>
        <a href="${tool.href}" class="btn btn-ghost btn-sm"${tool.affiliate ? ' target="_blank" rel="noopener noreferrer sponsored"' : ''}>${tool.affiliate ? t('ui.getBonus') : t('ui.discover')}</a>
      </div>`;
  }).join('');
}

async function initHubPage() {
  const hub = document.body.dataset.hub;
  if (!hub) return;
  await loadArticles();
  const base = getBasePath();
  const params = new URLSearchParams(window.location.search);
  const hubFilterMap = {
    guide: 'guide', tips: 'tip', trend: 'trend', sicurezza: 'sicurezza',
    bitcoin: 'bitcoin', ethereum: 'ethereum', 'smart-contract': 'smart-contract',
    cardano: 'cardano', strumenti: 'strumenti'
  };
  const filter = params.get('filter') || hubFilterMap[hub] || hub;

  const grid = document.getElementById('hub-articles');
  if (!grid) return;

  function render(filterKey) {
    const items = getArticlesByFilter(filterKey);
    grid.innerHTML = items.length
      ? items.map(a => hub === 'tips' ? renderTipCard(a, base) : renderArticleCard(a, base)).join('')
      : `<p style="color:var(--text-muted)">${t('messages.noArticles')}</p>`;
    document.querySelectorAll('.filter-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.filter === filterKey);
    });
  }

  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', () => render(btn.dataset.filter));
  });

  render(filter);
}

async function initGlossary() {
  if (document.body.dataset.page !== 'glossary') return;
  await loadArticles();
  const grid = document.getElementById('glossary-grid');
  const alpha = document.getElementById('glossary-alpha');
  if (!grid || !articlesData.glossary) return;

  const terms = [...articlesData.glossary].sort((a, b) => a.term.localeCompare(b.term, getLang() === 'en' ? 'en' : 'it'));
  const letters = [...new Set(terms.map(t => t.term[0].toUpperCase()))].sort();

  if (alpha) {
    alpha.innerHTML = `<button class="active" data-letter="all">${t('pages.glossary.all')}</button>` +
      letters.map(l => `<button data-letter="${l}">${l}</button>`).join('');
    alpha.addEventListener('click', e => {
      if (e.target.tagName !== 'BUTTON') return;
      const letter = e.target.dataset.letter;
      alpha.querySelectorAll('button').forEach(b => b.classList.toggle('active', b === e.target));
      renderGlossary(letter === 'all' ? terms : terms.filter(t => t.term[0].toUpperCase() === letter));
    });
  }

  function renderGlossary(list) {
    grid.innerHTML = list.map(g => {
      const loc = localizeGlossary(g);
      return `
      <div class="glossary-item" id="${g.term.toLowerCase().replace(/\s+/g, '-')}">
        <div class="glossary-term">${g.term}</div>
        <p class="glossary-def">${loc.definition}</p>
      </div>`;
    }).join('');
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
  const items = articlesData.articles.filter(a => {
    const loc = localizeArticle(a);
    return loc.title.toLowerCase().includes(q) || loc.excerpt.toLowerCase().includes(q);
  });

  container.innerHTML = items.length
    ? items.map(a => {
        const loc = localizeArticle(a);
        return `
        <a href="${base}articolo.html?slug=${a.slug}" class="search-page-result">
          <span class="badge badge--${a.difficulty}">${a.category}</span>
          <h3>${loc.title}</h3>
          <p>${loc.excerpt}</p>
        </a>`;
      }).join('')
    : `<p style="color:var(--text-muted);padding:2rem 0">${t('pages.search.noResults')} "<strong>${query}</strong>". ${t('pages.search.tryOther')}</p>`;
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

function initSocialPage() {
  if (document.body.dataset.page !== 'social') return;
  const grid = document.getElementById('social-grid');
  if (!grid || !SITE_CONFIG.social) return;
  grid.innerHTML = SITE_CONFIG.social.map(s => renderSocialCard(s)).join('');
  initFadeIn();
}

function initFacebookLinks() {
  const fb = getSocial('facebook');
  if (!fb) return;
  document.querySelectorAll('[data-facebook-link]').forEach(el => {
    el.href = fb.url;
    el.setAttribute('aria-label', fb.name);
    if (el.dataset.facebookText === 'handle') el.textContent = fb.handle;
    else if (el.dataset.facebookText === 'name') el.textContent = fb.name;
    if (!el.target) {
      el.target = '_blank';
      el.rel = 'noopener noreferrer';
    }
  });
}

function initInstagramLinks() {
  const ig = getSocial('instagram');
  if (!ig) return;
  document.querySelectorAll('[data-instagram-link]').forEach(el => {
    el.href = ig.url;
    el.setAttribute('aria-label', ig.name);
    if (!el.target) {
      el.target = '_blank';
      el.rel = 'noopener noreferrer';
    }
  });
  document.querySelectorAll('[data-instagram-handle]').forEach(el => {
    el.textContent = ig.handle;
  });
}

function loadScript(src) {
  return new Promise((resolve, reject) => {
    if (document.querySelector(`script[src="${src}"]`)) { resolve(); return; }
    const s = document.createElement('script');
    s.src = src;
    s.onload = resolve;
    s.onerror = reject;
    document.head.appendChild(s);
  });
}

async function loadSatoshiChat() {
  if (typeof initSatoshiChat === 'function') { initSatoshiChat(); return; }
  const base = getBasePath();
  const v = (typeof SITE_CONFIG !== 'undefined' && SITE_CONFIG.assetVersion) ? `?v=${SITE_CONFIG.assetVersion}` : '';
  await loadScript(`${base}js/satoshi-bot.js${v}`);
  await loadScript(`${base}js/satoshi-chat.js${v}`);
  if (typeof initSatoshiChat === 'function') initSatoshiChat();
}

async function bootApp() {
  try {
    await loadCryptoBackground();
    initCryptoBackground();
  } catch (_) { /* background non critico */ }
  try { await loadSatoshiChat(); } catch (_) { /* chat non critico */ }
  injectLayout();
  initNavActive();
  initFacebookLinks();
  initInstagramLinks();
  initMobileNav();
  initSearchBar();
  initI18n();
  initFadeIn();
  initNewsletter();
  await initHomepage();
  await initHubPage();
  initHubI18n();
  await initGlossary();
  await initSearchPage();
  initSocialPage();
  if (typeof initBitcoinNewsSession === 'function') await initBitcoinNewsSession();
  if (typeof initNewsHomePreview === 'function') await initNewsHomePreview();
  if (typeof initNewsHub === 'function') await initNewsHub();
  applyPageTranslations();
  initFadeIn();
  if (typeof initSatoshiChat === 'function') initSatoshiChat();
}

document.addEventListener('DOMContentLoaded', bootApp);

window.addEventListener('langchange', async () => {
  injectLayout();
  initNavActive();
  initFacebookLinks();
  initInstagramLinks();
  initMobileNav();
  initSearchBar();
  initI18n();
  await initHomepage();
  await initHubPage();
  initHubI18n();
  await initGlossary();
  await initSearchPage();
  initSocialPage();
  if (typeof initBitcoinNewsSession === 'function') await initBitcoinNewsSession();
  if (typeof initNewsHomePreview === 'function') await initNewsHomePreview();
  if (typeof initNewsHub === 'function') await initNewsHub();
  applyPageTranslations();
  initFadeIn();
  if (typeof initSatoshiChat === 'function') initSatoshiChat();
});