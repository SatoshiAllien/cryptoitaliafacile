const SITE_CONFIG = {
  name: 'CryptoFacile',
  domain: 'cryptofacile.com',
  tagline: 'La crypto, spiegata facile.',
  description: 'Guide pratiche, tips e spiegazioni semplici sul mondo crypto. Per principianti e non solo.',
  year: 2026,
  email: 'info@cryptofacile.com',

  teacher: {
    name: 'Stefano',
    title: 'Insegnante crypto professionale',
    photo: 'assets/img/teacher.jpg',
    quote: 'Ti accompagno passo dopo passo nel mondo crypto — con parole semplici, esempi pratici e zero hype. Il mio obiettivo è che tu capisca davvero, non che compri alla cieca.',
    badges: [
      'Guide passo-passo',
      'Sicurezza prima di tutto',
      'Linguaggio semplice',
      'Per principianti'
    ],
    href: 'chi-siamo/index.html'
  },

  colors: {
    primary: '#00C896',
    secondary: '#4F8CFF',
    coral: '#FF7B6B',
    yellow: '#FFC93C',
    purple: '#9B6DFF'
  },

  trustBadges: [
    '100% educativo',
    'Sicurezza prima di tutto',
    'Passo dopo passo',
    'Zero hype'
  ],

  nav: [
    {
      label: 'Guide',
      href: 'guide/index.html',
      children: [
        { label: 'Principianti', href: 'guide/index.html?filter=principianti' },
        { label: 'Avanzate', href: 'guide/index.html?filter=avanzate' },
        { label: 'DeFi & Staking', href: 'guide/index.html?filter=defi' },
        { label: 'Wallet', href: 'guide/index.html?filter=wallet' }
      ]
    },
    { label: 'Crypto Tips', href: 'crypto-tips/index.html' },
    { label: 'Trend', href: 'trend/index.html' },
    { label: 'Sicurezza', href: 'sicurezza/index.html' },
    { label: 'Cardano', href: 'cardano/index.html' },
    { label: 'Strumenti', href: 'strumenti/index.html' }
  ],

  categories: [
    { id: 'principianti', label: 'Principianti', abbr: 'P', href: 'guide/index.html?filter=principianti', color: '#00C896', bg: '#D4FFF3' },
    { id: 'sicurezza', label: 'Sicurezza', abbr: 'S', href: 'sicurezza/index.html', color: '#FF7B6B', bg: '#FFE8E5' },
    { id: 'cardano', label: 'Cardano', iconImg: 'assets/img/cardano-ada.png', href: 'cardano/index.html', color: '#4F8CFF', bg: '#E8F0FF' },
    { id: 'defi', label: 'DeFi & Staking', abbr: 'D', href: 'guide/index.html?filter=defi', color: '#9B6DFF', bg: '#F0E8FF' },
    { id: 'trend', label: 'Trend', abbr: 'T', href: 'trend/index.html', color: '#FFC93C', bg: '#FFF5D6' },
    { id: 'strumenti', label: 'Strumenti', abbr: 'St', href: 'strumenti/index.html', color: '#38BDF8', bg: '#E0F7FE' }
  ],

  pathColors: ['#00C896', '#4F8CFF', '#FFC93C', '#9B6DFF', '#FF7B6B'],

  social: {
    twitter: { url: 'https://twitter.com/cryptofacile', label: 'X' },
    telegram: { url: 'https://t.me/cryptofacile', label: 'TG' },
    youtube: { url: 'https://youtube.com/@cryptofacile', label: 'YT' }
  },

  beginnerPath: [
    { step: 1, title: 'Capire le basi', desc: 'Cos\'è una blockchain e come funziona', href: 'articolo.html?slug=blockchain-5-minuti' },
    { step: 2, title: 'Creare un account', desc: 'Revolut + registrazione su Kraken', href: 'articolo.html?slug=iniziare-exchange-revolut-kraken' },
    { step: 3, title: 'Primo acquisto', desc: 'Comprare i primi 20€ di Bitcoin', href: 'articolo.html?slug=comprare-bitcoin-prima-volta' },
    { step: 4, title: 'Wallet personale', desc: 'Trasferire crypto su wallet tuo', href: 'articolo.html?slug=creare-wallet-sicuro' },
    { step: 5, title: 'Proteggere tutto', desc: 'Seed phrase e sicurezza base', href: 'articolo.html?slug=proteggere-seed-phrase' }
  ],

  cardanoLogo: 'assets/img/cardano-ada.png',
  heroBackground: 'assets/img/crypto-hero-bg.png',

  affiliates: [
    {
      id: 'revolut',
      name: 'Revolut',
      initial: 'R',
      badge: 'GRATIS',
      badgeType: 'free',
      tagline: 'Il conto che usiamo davvero',
      headline: 'Apri Revolut in 5 minuti — zero costi',
      hook: 'Bonifici SEPA velocissimi verso Kraken. La banca che non blocca le crypto.',
      perks: ['Conto base gratuito', 'Bonifici SEPA in 1 giorno', 'Carta virtuale inclusa'],
      cta: 'Apri Revolut GRATIS →',
      href: 'https://revolut.com/referral/?referral-code=stefan2ayd!JUN1-26-AR&geo-redirect',
      accent: '#0075EB',
      accentLight: '#E8F4FF'
    },
    {
      id: 'kraken',
      name: 'Kraken',
      initial: 'K',
      badge: 'BONUS',
      badgeType: 'bonus',
      tagline: 'Exchange consigliato ai principianti',
      headline: 'Registrati su Kraken — bonus referral attivo',
      hook: 'Exchange regolamentato dal 2011. Deposito SEPA gratuito, fee basse, massima affidabilità.',
      perks: ['Deposito SEPA gratis', 'Fee tra le più basse', 'Supporto in italiano'],
      cta: 'Ottieni il bonus Kraken →',
      code: '3h8q8cf5',
      href: 'https://invite.kraken.com/JDNW/pql7tac5',
      accent: '#5741D9',
      accentLight: '#F0EBFF'
    }
  ],

  tools: [
    { name: 'Ledger', desc: 'Hardware wallet per massima sicurezza', category: 'Wallet', href: '#' },
    { name: 'Revolut', desc: 'Conto per bonifici SEPA verso exchange', category: 'Fintech', href: 'https://revolut.com/referral/?referral-code=stefan2ayd!JUN1-26-AR&geo-redirect', affiliate: true },
    { name: 'Kraken', desc: 'Exchange regolamentato e affidabile', category: 'Exchange', href: 'https://invite.kraken.com/JDNW/pql7tac5', affiliate: true },
    { name: 'Eternl', desc: 'Wallet Cardano consigliato', category: 'Cardano', href: '#' }
  ]
};

function getSiteRoot() {
  const path = window.location.pathname;
  const repoRoots = ['cryptoitaliafacile', 'cryptofacile'];
  for (const root of repoRoots) {
    const marker = `/${root}`;
    const idx = path.indexOf(marker);
    if (idx !== -1) return `${path.substring(0, idx + marker.length)}/`;
  }
  return '/';
}

function getAssetUrl(relativePath) {
  const root = getSiteRoot();
  const clean = relativePath.replace(/^\//, '');
  return root === '/' ? `${getBasePath()}${clean}` : `${root}${clean}`;
}

function getBasePath() {
  const path = window.location.pathname;
  const repoRoots = ['cryptoitaliafacile', 'cryptofacile'];

  for (const root of repoRoots) {
    const marker = `/${root}/`;
    if (path.includes(marker)) {
      const sub = path.split(marker)[1] || '';
      const levels = sub.split('/').filter(Boolean).length - (sub.endsWith('.html') ? 1 : 0);
      return levels > 0 ? '../'.repeat(levels) : '';
    }
    if (path === `/${root}` || path === `/${root}/` || path === `/${root}/index.html`) {
      return '';
    }
  }

  const segments = path.split('/').filter(Boolean);
  const htmlIdx = segments.findIndex(s => s.endsWith('.html'));
  const depth2 = htmlIdx > 0 ? htmlIdx : (segments.length > 0 && !segments[segments.length - 1].endsWith('.html') ? segments.length : 0);
  return depth2 > 0 ? '../'.repeat(depth2) : '';
}