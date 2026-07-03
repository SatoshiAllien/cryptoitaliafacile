const NAV_ICON_MAP = {
  'guide/index.html': 'guide',
  'crypto-tips/index.html': 'tips',
  'trend/index.html': 'trends',
  'news/index.html': 'news',
  'sicurezza/index.html': 'security',
  'cardano/index.html': 'cardano',
  'strumenti/index.html': 'tools',
  'chat/index.html': 'satoshi'
};

const SOCIAL_ICON_MAP = {
  instagram: 'instagram',
  facebook: 'facebook',
  x: 'x',
  linkedin: 'linkedin'
};

const CATEGORY_ICON_MAP = {
  principianti: 'book',
  sicurezza: 'shield',
  bitcoin: 'bitcoin',
  ethereum: 'ethereum',
  'smart-contract': 'lock',
  cardano: 'cardano',
  defi: 'chart',
  trend: 'trends',
  strumenti: 'tools'
};

function iconUrl(name) {
  const base = typeof getBasePath === 'function' ? getBasePath() : '';
  const ver = (typeof SITE_CONFIG !== 'undefined' && SITE_CONFIG.assetVersion)
    ? `?v=${SITE_CONFIG.assetVersion}`
    : '';
  return `${base}icons/${name}.svg${ver}`;
}

function iconImg(name, opts = {}) {
  const size = opts.size || 24;
  const className = opts.className || 'site-icon';
  const alt = opts.alt || '';
  const hidden = alt ? '' : ' aria-hidden="true"';
  return `<img src="${iconUrl(name)}" class="${className}" width="${size}" height="${size}" alt="${alt}" loading="lazy" decoding="async"${hidden}>`;
}

function navIcon(href, size = 22, className = 'site-icon site-icon--nav') {
  const name = NAV_ICON_MAP[href];
  return name ? iconImg(name, { size, className }) : '';
}

function navTabIcon(href) {
  const name = NAV_ICON_MAP[href];
  if (!name) return '';
  return `<span class="nav-tab-icon">${iconImg(name, { size: 16, className: 'site-icon site-icon--nav-tab' })}</span>`;
}

function socialIcon(id, size = 20) {
  const name = SOCIAL_ICON_MAP[id];
  return name ? iconImg(name, { size, className: 'site-icon site-icon--social' }) : '';
}

function categoryIcon(id, size = 28) {
  const name = CATEGORY_ICON_MAP[id];
  return name ? iconImg(name, { size, className: 'site-icon category-icon-img' }) : '';
}