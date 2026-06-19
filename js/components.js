const NAV_I18N = {
  'guide/index.html': 'nav.guide',
  'crypto-tips/index.html': 'nav.cryptoTips',
  'trend/index.html': 'nav.trend',
  'sicurezza/index.html': 'nav.sicurezza',
  'cardano/index.html': 'nav.cardano',
  'strumenti/index.html': 'nav.strumenti',
  'guide/index.html?filter=principianti': 'nav.principianti',
  'guide/index.html?filter=avanzate': 'nav.avanzate',
  'guide/index.html?filter=defi': 'nav.defi',
  'guide/index.html?filter=wallet': 'nav.wallet'
};

function navLabel(href) {
  return t(NAV_I18N[href] || href);
}

function renderLogo(base) {
  return `
    <a href="${base}index.html" class="logo" aria-label="CryptoFacile — Home">
      <svg class="logo-icon" viewBox="0 0 40 40" width="36" height="36" aria-hidden="true">
        <circle cx="20" cy="20" r="18" fill="#00C896" opacity="0.2"/>
        <circle cx="20" cy="20" r="16" fill="url(#logoGrad)"/>
        <defs><linearGradient id="logoGrad" x1="0" y1="0" x2="40" y2="40"><stop offset="0%" stop-color="#00C896"/><stop offset="100%" stop-color="#4F8CFF"/></linearGradient></defs>
        <text x="20" y="25" text-anchor="middle" font-family="Plus Jakarta Sans, Inter, sans-serif" font-weight="700" font-size="14" fill="#fff">CF</text>
        <path d="M28 14 L32 10 L32 18 Z" fill="#FFC93C"/>
      </svg>
      <span class="logo-text">
        <span class="logo-name">CryptoFacile</span>
        <span class="logo-tagline">${t('logoTagline')}</span>
      </span>
    </a>`;
}

function renderNavLinks(base) {
  return SITE_CONFIG.nav.map(item => {
    if (item.children) {
      const children = item.children.map(c =>
        `<a href="${base}${c.href}" class="dropdown-link">${navLabel(c.href)}</a>`
      ).join('');
      return `
        <div class="nav-item nav-item--dropdown">
          <a href="${base}${item.href}" class="nav-link">${navLabel(item.href)} <span class="nav-caret">▾</span></a>
          <div class="dropdown-menu">${children}</div>
        </div>`;
    }
    return `<a href="${base}${item.href}" class="nav-link">${navLabel(item.href)}</a>`;
  }).join('');
}

function renderHeader() {
  const base = getBasePath();
  return `
    <header class="header" id="header">
      <div class="container header-inner">
        ${renderLogo(base)}
        <nav class="nav-desktop" aria-label="Menu principale">
          ${renderNavLinks(base)}
        </nav>
        <div class="header-actions">
          <button class="search-toggle" id="open-search" aria-label="${t('nav.search')}">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
          </button>
          <div class="header-lang" id="header-lang">${renderLangSwitcher()}</div>
          <a href="${base}newsletter/index.html" class="btn btn-primary btn-sm header-cta">${t('nav.newsletter')}</a>
          <button class="menu-toggle" id="menu-toggle" aria-label="Menu" aria-expanded="false">
            <span></span><span></span><span></span>
          </button>
        </div>
      </div>
      <div class="search-bar" id="search-bar" hidden>
        <div class="container">
          <div class="search-bar-inner">
            <svg class="search-bar-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
            <input type="search" id="header-search" placeholder="${t('ui.searchPlaceholder')}" autocomplete="off">
            <div class="search-bar-lang">${renderLangSwitcher()}</div>
            <button class="search-close" id="search-close" aria-label="${t('nav.closeSearch')}">✕</button>
          </div>
          <div class="search-suggestions" id="search-suggestions"></div>
        </div>
      </div>
    </header>
    <div class="mobile-nav" id="mobile-nav" aria-hidden="true">
      <div class="mobile-nav-backdrop" id="mobile-nav-backdrop"></div>
      <div class="mobile-nav-panel">
        <div class="mobile-nav-header">
          <strong>${t('nav.menu')}</strong>
          <div class="mobile-nav-header-actions">
            ${renderLangSwitcher()}
            <button id="mobile-nav-close" aria-label="${t('nav.close')}">✕</button>
          </div>
        </div>
        <div class="mobile-search">
          <input type="search" id="mobile-search" placeholder="${t('ui.searchShort')}" autocomplete="off">
        </div>
        <nav class="mobile-nav-links">
          ${SITE_CONFIG.nav.map(item => {
            if (item.children) {
              return `
                <details class="mobile-accordion">
                  <summary>${navLabel(item.href)}</summary>
                  <div class="mobile-accordion-body">
                    <a href="${base}${item.href}">${t('nav.allGuides')}</a>
                    ${item.children.map(c => `<a href="${base}${c.href}">${navLabel(c.href)}</a>`).join('')}
                  </div>
                </details>`;
            }
            return `<a href="${base}${item.href}" class="mobile-nav-link">${navLabel(item.href)}</a>`;
          }).join('')}
          <a href="${base}glossario/index.html" class="mobile-nav-link">${t('nav.glossario')}</a>
          <a href="${base}newsletter/index.html" class="mobile-nav-link mobile-nav-link--cta">${t('nav.newsletterFree')}</a>
        </nav>
      </div>
    </div>`;
}

function renderFooter() {
  const base = getBasePath();
  const social = Object.values(SITE_CONFIG.social).map(s =>
    `<a href="${s.url}" class="social-link" aria-label="${s.label}" target="_blank" rel="noopener">${s.label}</a>`
  ).join('');

  return `
    <footer class="footer">
      <div class="container">
        <div class="footer-grid">
          <div class="footer-col">
            <h4>CryptoFacile</h4>
            <p>${t('footer.desc')}</p>
            <div class="social-links">${social}</div>
          </div>
          <div class="footer-col">
            <h4>${t('footer.guides')}</h4>
            <div class="footer-links">
              <a href="${base}guide/index.html?filter=principianti">${t('nav.principianti')}</a>
              <a href="${base}sicurezza/index.html">${t('nav.sicurezza')}</a>
              <a href="${base}cardano/index.html">${t('nav.cardano')}</a>
              <a href="${base}guide/index.html?filter=defi">${t('nav.defi')}</a>
              <a href="${base}guide/index.html?filter=avanzate">${t('nav.avanzate')}</a>
            </div>
          </div>
          <div class="footer-col">
            <h4>${t('footer.resources')}</h4>
            <div class="footer-links">
              <a href="${base}glossario/index.html">${t('nav.glossario')}</a>
              <a href="${base}strumenti/index.html">${t('nav.strumenti')}</a>
              <a href="${base}trend/index.html">${t('nav.trend')}</a>
              <a href="${base}crypto-tips/index.html">${t('nav.cryptoTips')}</a>
              <a href="${base}newsletter/index.html">${t('nav.newsletter')}</a>
            </div>
          </div>
          <div class="footer-col">
            <h4>${t('footer.legal')}</h4>
            <div class="footer-links">
              <a href="${base}chi-siamo/index.html">${t('footer.about')}</a>
              <a href="${base}contatti/index.html">${t('footer.contacts')}</a>
              <a href="${base}privacy.html">Privacy</a>
              <a href="${base}cookie.html">Cookie</a>
              <a href="${base}disclaimer.html">Disclaimer</a>
            </div>
          </div>
        </div>
        <div class="footer-disclaimer">${t('footer.disclaimer')}</div>
        <div class="footer-bottom">
          <span>© ${SITE_CONFIG.year} CryptoFacile.com — ${t('tagline')}</span>
        </div>
      </div>
    </footer>`;
}

function renderBreadcrumb(items) {
  const base = getBasePath();
  const crumbs = items.map((item, i) => {
    if (i === items.length - 1) {
      return `<span aria-current="page">${item.label}</span>`;
    }
    return `<a href="${base}${item.href}">${item.label}</a>`;
  }).join('<span class="breadcrumb-sep">›</span>');

  return `<nav class="breadcrumb" aria-label="Breadcrumb"><a href="${base}index.html">${t('ui.home')}</a><span class="breadcrumb-sep">›</span>${crumbs}</nav>`;
}

function renderArticleCard(article, base) {
  const a = localizeArticle(article);
  const diffClass = `badge--${a.difficulty}`;
  const diffLabel = { beginner: t('ui.beginner'), intermediate: t('ui.intermediate'), advanced: t('ui.advanced') }[a.difficulty] || t('ui.beginner');
  return `
    <a href="${base}articolo.html?slug=${a.slug}" class="article-card article-card--${a.difficulty}">
      <div class="article-card-accent"></div>
      <div class="article-card-body">
        <div class="article-card-top">
          <span class="badge ${diffClass}">${diffLabel}</span>
          <span class="article-meta">${a.readTime} min</span>
        </div>
        <h3 class="article-card-title">${a.title}</h3>
        <p class="article-card-excerpt">${a.excerpt}</p>
        <span class="article-card-link">${t('ui.readGuide')}</span>
      </div>
    </a>`;
}

function renderTipCard(tip, base) {
  const t_ = localizeArticle(tip);
  return `
    <a href="${base}articolo.html?slug=${t_.slug}" class="tip-card">
      <span class="tip-marker" aria-hidden="true"></span>
      <div>
        <h3>${t_.title}</h3>
        <p>${t_.excerpt}</p>
      </div>
    </a>`;
}

function renderTrendCard(trend, base) {
  const tr = localizeArticle(trend);
  const tags = (tr.tags || []).map(tag => `<span class="tag">${tag}</span>`).join('');
  return `
    <a href="${base}articolo.html?slug=${tr.slug}" class="trend-card">
      <div class="trend-card-header">
        <span class="trend-date">${t('ui.updated')} ${tr.date}</span>
      </div>
      <h3>${tr.title}</h3>
      <p>${tr.excerpt}</p>
      <div class="trend-tags">${tags}</div>
      <span class="trend-cta">${t('ui.simpleExplanation')}</span>
    </a>`;
}

function injectLayout() {
  const headerEl = document.getElementById('site-header');
  const footerEl = document.getElementById('site-footer');
  if (headerEl) headerEl.innerHTML = renderHeader();
  if (footerEl) footerEl.innerHTML = renderFooter();
  initLangSwitcher();
}