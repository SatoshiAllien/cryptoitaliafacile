const NAV_I18N = {
  'guide/index.html': 'nav.guide',
  'crypto-tips/index.html': 'nav.cryptoTips',
  'trend/index.html': 'nav.trend',
  'news/index.html': 'nav.news',
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
    <a href="${base}index.html" class="logo" aria-label="${SITE_CONFIG.name} — Home">
      <svg class="logo-icon" viewBox="0 0 40 40" width="36" height="36" aria-hidden="true">
        <rect x="4" y="4" width="32" height="32" rx="6" fill="#0a0a12" stroke="url(#logoGrad)" stroke-width="1.5"/>
        <defs><linearGradient id="logoGrad" x1="0" y1="0" x2="40" y2="40"><stop offset="0%" stop-color="#00f0ff"/><stop offset="100%" stop-color="#ff2a6d"/></linearGradient></defs>
        <text x="20" y="25" text-anchor="middle" font-family="Orbitron, Plus Jakarta Sans, sans-serif" font-weight="700" font-size="11" fill="#00f0ff">LS</text>
        <path d="M28 14 L32 10 L32 18 Z" fill="#fcee0a"/>
      </svg>
      <span class="logo-text">
        <span class="logo-name">${SITE_CONFIG.name}</span>
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

function renderHeaderSocialLink(id) {
  const s = getSocial(id);
  if (!s) return '';
  return `<a href="${s.url}" class="header-social header-social--${s.id}" aria-label="${s.name}" target="_blank" rel="noopener noreferrer" style="--social-color:${s.color}">${SOCIAL_ICONS[s.id] || s.name[0]}</a>`;
}

function renderMobileSocialLink(id) {
  const s = getSocial(id);
  if (!s) return '';
  return `<a href="${s.url}" class="mobile-nav-link" target="_blank" rel="noopener noreferrer">${SOCIAL_ICONS[s.id] || ''} ${s.name}</a>`;
}

function renderHeader() {
  const base = getBasePath();
  const headerSocialsHtml = ['x', 'facebook'].map(renderHeaderSocialLink).join('');
  const headerSocials = headerSocialsHtml ? `<div class="header-socials">${headerSocialsHtml}</div>` : '';
  return `
    <header class="header" id="header">
      <div class="container header-inner">
        ${renderLogo(base)}
        <nav class="nav-desktop" aria-label="Menu principale">
          ${renderNavLinks(base)}
        </nav>
        <div class="header-actions">
          ${headerSocials}
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
          ${['x', 'facebook'].map(renderMobileSocialLink).join('')}
          <a href="${base}newsletter/index.html" class="mobile-nav-link mobile-nav-link--cta">${t('nav.newsletterFree')}</a>
        </nav>
      </div>
    </div>`;
}

const SOCIAL_ICONS = {
  x: '<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>',
  facebook: '<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>',
  instagram: '<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>',
  tiktok: '<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M19.59 6.69a4.83 4.83 0 01-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 01-2.88 2.5 2.89 2.89 0 01-2.89-2.89 2.89 2.89 0 012.89-2.89c.28 0 .54.04.79.1V9.01a6.27 6.27 0 00-.79-.05 6.34 6.34 0 00-6.34 6.34 6.34 6.34 0 006.34 6.34 6.34 6.34 0 006.34-6.34V8.69a8.18 8.18 0 004.78 1.52V6.76a4.85 4.85 0 01-1.01-.07z"/></svg>',
  youtube: '<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M23.498 6.186a3.016 3.016 0 00-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 00.502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 002.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 002.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>'
};

function renderSocialLinks() {
  return (SITE_CONFIG.social || []).map(s =>
    `<a href="${s.url}" class="social-link social-link--${s.id}" aria-label="${s.name}" target="_blank" rel="noopener noreferrer" style="--social-color:${s.color}">${SOCIAL_ICONS[s.id] || s.name[0]}</a>`
  ).join('');
}

function renderSocialCard(s) {
  const desc = t(`pages.social.${s.id}.desc`) || s.desc;
  return `
    <a href="${s.url}" class="social-card fade-in" target="_blank" rel="noopener noreferrer" style="--social-color:${s.color}">
      <div class="social-card-icon">${SOCIAL_ICONS[s.id] || ''}</div>
      <div class="social-card-body">
        <span class="social-card-label">${t('pages.social.follow')}</span>
        <h2>${s.name}</h2>
        <p class="social-card-handle">${s.handle}</p>
        <p class="social-card-desc">${desc}</p>
        <span class="social-card-cta">${t('pages.social.cta')}</span>
      </div>
    </a>`;
}

function renderFooter() {
  const base = getBasePath();
  const social = renderSocialLinks();

  return `
    <footer class="footer">
      <div class="container">
        <div class="footer-grid">
          <div class="footer-col">
            <h4>${SITE_CONFIG.name}</h4>
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
              <a href="${base}news/index.html">${t('nav.news')}</a>
              <a href="${base}crypto-tips/index.html">${t('nav.cryptoTips')}</a>
              <a href="${base}newsletter/index.html">${t('nav.newsletter')}</a>
              <a href="${base}social/index.html">${t('nav.social')}</a>
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
          <span>© ${SITE_CONFIG.year} ${SITE_CONFIG.name} — ${t('tagline')}</span>
        </div>
      </div>
    </footer>`;
}

function getArticlePreviewSquareUrl(article) {
  if (!article) return '';
  const file = article.igImage || article.fbImage;
  if (!file) return '';
  const path = `assets/img/instagram/posts/${file}`;
  return typeof getAssetUrl === 'function' ? getAssetUrl(path) : path;
}

function getArticlePreviewHeroUrl(article) {
  if (!article) return '';
  const file = article.fbImage || article.igImage;
  if (!file) return '';
  const path = `assets/img/facebook/posts/${file}`;
  if (typeof getAssetUrl === 'function') return getAssetUrl(path);
  const base = (typeof SITE_CONFIG !== 'undefined' && SITE_CONFIG.siteUrl)
    ? SITE_CONFIG.siteUrl.replace(/\/?$/, '/')
    : 'https://satoshiallien.github.io/cryptoitaliafacile/';
  return `${base}${path}`;
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
  const previewUrl = typeof getArticlePreviewSquareUrl === 'function'
    ? getArticlePreviewSquareUrl(a)
    : '';
  const previewHtml = previewUrl
    ? `<div class="article-card-media"><img src="${previewUrl}" alt="" class="article-card-image" loading="lazy" width="400" height="400" decoding="async"></div>`
    : '<div class="article-card-accent"></div>';
  return `
    <a href="${base}articolo.html?slug=${a.slug}" class="article-card article-card--${a.difficulty}">
      ${previewHtml}
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
  const previewUrl = typeof getArticlePreviewSquareUrl === 'function'
    ? getArticlePreviewSquareUrl(t_)
    : '';
  const previewHtml = previewUrl
    ? `<img src="${previewUrl}" alt="" class="tip-card-image" loading="lazy" width="96" height="96" decoding="async">`
    : '<span class="tip-marker" aria-hidden="true"></span>';
  return `
    <a href="${base}articolo.html?slug=${t_.slug}" class="tip-card">
      ${previewHtml}
      <div>
        <h3>${t_.title}</h3>
        <p>${t_.excerpt}</p>
      </div>
    </a>`;
}

function renderTrendCard(trend, base) {
  const tr = localizeArticle(trend);
  const tags = (tr.tags || []).map(tag => `<span class="tag">${tag}</span>`).join('');
  const previewUrl = typeof getArticlePreviewSquareUrl === 'function'
    ? getArticlePreviewSquareUrl(tr)
    : '';
  const previewHtml = previewUrl
    ? `<div class="trend-card-media"><img src="${previewUrl}" alt="" class="trend-card-image" loading="lazy" width="320" height="180" decoding="async"></div>`
    : '';
  return `
    <a href="${base}articolo.html?slug=${tr.slug}" class="trend-card">
      ${previewHtml}
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