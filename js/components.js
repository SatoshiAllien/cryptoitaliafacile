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
        <span class="logo-tagline">La crypto, spiegata facile</span>
      </span>
    </a>`;
}

function renderNavLinks(base) {
  return SITE_CONFIG.nav.map(item => {
    if (item.children) {
      const children = item.children.map(c =>
        `<a href="${base}${c.href}" class="dropdown-link">${c.label}</a>`
      ).join('');
      return `
        <div class="nav-item nav-item--dropdown">
          <a href="${base}${item.href}" class="nav-link">${item.label} <span class="nav-caret">▾</span></a>
          <div class="dropdown-menu">${children}</div>
        </div>`;
    }
    return `<a href="${base}${item.href}" class="nav-link">${item.label}</a>`;
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
          <button class="search-toggle" id="open-search" aria-label="Cerca">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" opacity="0.7"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
          </button>
          <a href="${base}newsletter/index.html" class="btn btn-primary btn-sm header-cta">Newsletter</a>
          <button class="menu-toggle" id="menu-toggle" aria-label="Menu" aria-expanded="false">
            <span></span><span></span><span></span>
          </button>
        </div>
      </div>
      <div class="search-bar" id="search-bar" hidden>
        <div class="container">
          <div class="search-bar-inner">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" opacity="0.7"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
            <input type="search" id="header-search" placeholder="Cerca guide, tips, termini… (es. seed phrase, staking ADA)" autocomplete="off">
            <button class="search-close" id="search-close" aria-label="Chiudi ricerca">✕</button>
          </div>
          <div class="search-suggestions" id="search-suggestions"></div>
        </div>
      </div>
    </header>
    <div class="mobile-nav" id="mobile-nav" aria-hidden="true">
      <div class="mobile-nav-backdrop" id="mobile-nav-backdrop"></div>
      <div class="mobile-nav-panel">
        <div class="mobile-nav-header">
          <strong>Menu</strong>
          <button id="mobile-nav-close" aria-label="Chiudi">✕</button>
        </div>
        <div class="mobile-search">
          <input type="search" id="mobile-search" placeholder="Cerca…" autocomplete="off">
        </div>
        <nav class="mobile-nav-links">
          ${SITE_CONFIG.nav.map(item => {
            if (item.children) {
              return `
                <details class="mobile-accordion">
                  <summary>${item.label}</summary>
                  <div class="mobile-accordion-body">
                    <a href="${base}${item.href}">Tutte le guide</a>
                    ${item.children.map(c => `<a href="${base}${c.href}">${c.label}</a>`).join('')}
                  </div>
                </details>`;
            }
            return `<a href="${base}${item.href}" class="mobile-nav-link">${item.label}</a>`;
          }).join('')}
          <a href="${base}glossario/index.html" class="mobile-nav-link">Glossario</a>
          <a href="${base}newsletter/index.html" class="mobile-nav-link mobile-nav-link--cta">Newsletter gratis</a>
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
            <p>Guide pratiche e spiegazioni semplici sul mondo crypto. 100% educativo, zero hype.</p>
            <div class="social-links">${social}</div>
          </div>
          <div class="footer-col">
            <h4>Guide</h4>
            <div class="footer-links">
              <a href="${base}guide/index.html?filter=principianti">Principianti</a>
              <a href="${base}sicurezza/index.html">Sicurezza</a>
              <a href="${base}cardano/index.html">Cardano</a>
              <a href="${base}guide/index.html?filter=defi">DeFi & Staking</a>
              <a href="${base}guide/index.html?filter=avanzate">Avanzate</a>
            </div>
          </div>
          <div class="footer-col">
            <h4>Risorse</h4>
            <div class="footer-links">
              <a href="${base}glossario/index.html">Glossario</a>
              <a href="${base}strumenti/index.html">Strumenti</a>
              <a href="${base}trend/index.html">Trend</a>
              <a href="${base}crypto-tips/index.html">Crypto Tips</a>
              <a href="${base}newsletter/index.html">Newsletter</a>
            </div>
          </div>
          <div class="footer-col">
            <h4>Legale</h4>
            <div class="footer-links">
              <a href="${base}chi-siamo/index.html">Chi siamo</a>
              <a href="${base}contatti/index.html">Contatti</a>
              <a href="${base}privacy.html">Privacy</a>
              <a href="${base}cookie.html">Cookie</a>
              <a href="${base}disclaimer.html">Disclaimer</a>
            </div>
          </div>
        </div>
        <div class="footer-disclaimer">
          I contenuti di CryptoFacile sono a scopo puramente educativo e non costituiscono consulenza finanziaria. Investire in crypto comporta rischi.
        </div>
        <div class="footer-bottom">
          <span>© ${SITE_CONFIG.year} CryptoFacile.com — ${SITE_CONFIG.tagline}</span>
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

  return `<nav class="breadcrumb" aria-label="Breadcrumb"><a href="${base}index.html">Home</a><span class="breadcrumb-sep">›</span>${crumbs}</nav>`;
}

function renderArticleCard(article, base) {
  const diffClass = `badge--${article.difficulty}`;
  const diffLabel = { beginner: 'Principiante', intermediate: 'Intermedio', advanced: 'Avanzato' }[article.difficulty] || 'Principiante';
  return `
    <a href="${base}articolo.html?slug=${article.slug}" class="article-card article-card--${article.difficulty}">
      <div class="article-card-accent"></div>
      <div class="article-card-body">
        <div class="article-card-top">
          <span class="badge ${diffClass}">${diffLabel}</span>
          <span class="article-meta">${article.readTime} min</span>
        </div>
        <h3 class="article-card-title">${article.title}</h3>
        <p class="article-card-excerpt">${article.excerpt}</p>
        <span class="article-card-link">Leggi la guida →</span>
      </div>
    </a>`;
}

function renderTipCard(tip, base) {
  return `
    <a href="${base}articolo.html?slug=${tip.slug}" class="tip-card">
      <span class="tip-marker" aria-hidden="true"></span>
      <div>
        <h3>${tip.title}</h3>
        <p>${tip.excerpt}</p>
      </div>
    </a>`;
}

function renderTrendCard(trend, base) {
  const tags = (trend.tags || []).map(t => `<span class="tag">${t}</span>`).join('');
  return `
    <a href="${base}articolo.html?slug=${trend.slug}" class="trend-card">
      <div class="trend-card-header">
        <span class="trend-date">Aggiornato ${trend.date}</span>
      </div>
      <h3>${trend.title}</h3>
      <p>${trend.excerpt}</p>
      <div class="trend-tags">${tags}</div>
      <span class="trend-cta">Spiegazione semplice →</span>
    </a>`;
}

function injectLayout() {
  const headerEl = document.getElementById('site-header');
  const footerEl = document.getElementById('site-footer');
  if (headerEl) headerEl.innerHTML = renderHeader();
  if (footerEl) footerEl.innerHTML = renderFooter();
}