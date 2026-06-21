/**
 * Immagini clickbait per post Facebook — mappa articolo → thumbnail
 */
const FB_IMAGE_BASE = 'assets/img/facebook/posts/';

const FB_IMAGE_DEFAULTS = {
  guide: 'guide.jpg',
  tip: 'tip.jpg',
  trend: 'trend.jpg',
  tutorial: 'guide.jpg',
  cardano: 'cardano.jpg',
  sicurezza: 'sicurezza.jpg',
  bitcoin: 'bitcoin.jpg',
  ethereum: 'ethereum.jpg'
};

const FB_IMAGE_BY_TAG = {
  bitcoin: 'bitcoin.jpg',
  btc: 'bitcoin.jpg',
  exchange: 'exchange.jpg',
  revolut: 'exchange.jpg',
  kraken: 'exchange.jpg',
  wallet: 'wallet.jpg',
  'seed phrase': 'sicurezza.jpg',
  sicurezza: 'sicurezza.jpg',
  phishing: 'sicurezza.jpg',
  truffe: 'sicurezza.jpg',
  cardano: 'cardano.jpg',
  ada: 'cardano.jpg',
  ethereum: 'ethereum.jpg',
  eth: 'ethereum.jpg',
  defi: 'defi.jpg',
  uniswap: 'defi.jpg',
  staking: 'ethereum.jpg',
  ledger: 'wallet.jpg',
  metamask: 'wallet.jpg',
  '#bitcoin': 'bitcoin.jpg',
  '#ethereum': 'ethereum.jpg',
  '#defi': 'defi.jpg',
  '#etf': 'bitcoin.jpg',
  '#layer2': 'ethereum.jpg',
  '#stablecoin': 'defi.jpg'
};

const FB_CLICKBAIT_HOOKS = {
  guide: '🔥 GUIDA GRATIS — Non saltare questo:',
  tip: '⚡ TIP DA APPLICARE SUBITO:',
  trend: '📈 TREND HOT — Cosa devi sapere:',
  tutorial: '🎓 TUTORIAL PASSO-PASSO:',
  cardano: '🔷 CARDANO — Lo spieghiamo facile:',
  sicurezza: '🚨 ATTENZIONE — Evita questo errore:',
  bitcoin: '₿ BITCOIN — Guida che ti serve:',
  ethereum: '⟠ ETHEREUM — Spiegato semplice:'
};

function getFacebookStoryImageFile(article) {
  if (!article) return FB_IMAGE_DEFAULTS.guide;
  if (article.fbStoryImage) return article.fbStoryImage;
  return getFacebookImageFile(article);
}

function getFacebookImageFile(article) {
  if (!article) return FB_IMAGE_DEFAULTS.guide;
  if (article.fbImage) return article.fbImage;

  for (const rawTag of (article.tags || [])) {
    const tag = String(rawTag).toLowerCase().replace(/^#+/, '').trim();
    if (FB_IMAGE_BY_TAG[tag]) return FB_IMAGE_BY_TAG[tag];
    if (FB_IMAGE_BY_TAG[`#${tag}`]) return FB_IMAGE_BY_TAG[`#${tag}`];
  }

  if (article.category === 'cardano') return FB_IMAGE_DEFAULTS.cardano;
  if (article.category === 'sicurezza') return FB_IMAGE_DEFAULTS.sicurezza;
  if (article.category === 'tip') return FB_IMAGE_DEFAULTS.tip;
  if (article.category === 'trend') return FB_IMAGE_DEFAULTS.trend;

  const title = (article.title || '').toLowerCase();
  const slug = (article.slug || '').toLowerCase();
  if (title.includes('bitcoin') || slug.includes('bitcoin')) return 'bitcoin.jpg';
  if (title.includes('ethereum') || slug.includes('ethereum')) return 'ethereum.jpg';
  if (title.includes('cardano') || slug.includes('cardano') || slug.includes('ada')) return 'cardano.jpg';
  if (title.includes('exchange') || slug.includes('exchange') || slug.includes('revolut') || slug.includes('kraken')) return 'exchange.jpg';
  if (title.includes('wallet') || slug.includes('wallet') || slug.includes('seed')) return 'wallet.jpg';
  if (title.includes('sicurezz') || slug.includes('sicurezz') || slug.includes('phishing') || slug.includes('truff')) return 'sicurezza.jpg';
  if (title.includes('defi') || slug.includes('defi') || slug.includes('uniswap') || slug.includes('aave')) return 'defi.jpg';

  return FB_IMAGE_DEFAULTS[article.category] || FB_IMAGE_DEFAULTS.guide;
}

function getFacebookImageUrl(article) {
  const file = FB_IMAGE_BASE + getFacebookImageFile(article);
  if (typeof getAssetUrl === 'function') return getAssetUrl(file);
  const base = (typeof SITE_CONFIG !== 'undefined' && SITE_CONFIG.siteUrl)
    ? SITE_CONFIG.siteUrl.replace(/\/?$/, '/')
    : 'https://satoshiallien.github.io/cryptoitaliafacile/';
  return `${base}${file}`;
}

function getFacebookImageAbsoluteUrl(article) {
  const base = (typeof SITE_CONFIG !== 'undefined' && SITE_CONFIG.siteUrl)
    ? SITE_CONFIG.siteUrl.replace(/\/?$/, '/')
    : 'https://satoshiallien.github.io/cryptoitaliafacile/';
  return `${base}${FB_IMAGE_BASE}${getFacebookImageFile(article)}`;
}

function getFacebookClickbaitHook(article) {
  const cat = article?.category || 'guide';
  return FB_CLICKBAIT_HOOKS[cat] || FB_CLICKBAIT_HOOKS.guide;
}