const SITE_CONFIG = {
  name: 'The Little Satoshi News',
  domain: 'cryptofacile.com',
  siteUrl: 'https://satoshiallien.github.io/cryptoitaliafacile/',
  tagline: 'Notizie e crypto, facili e semplici.',
  legacyBrand: {
    name: 'CryptoFacile',
    tagline: 'La crypto spiegata facile'
  },
  description: 'Notizie crypto e guide spiegate in modo facile e semplice. Per principianti e non solo.',
  year: 2026,
  assetVersion: '20260621-satoshi-bot',
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
    primary: '#00f0ff',
    secondary: '#ff2a6d',
    coral: '#ff2a6d',
    yellow: '#fcee0a',
    purple: '#bd00ff'
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
    { label: 'News', href: 'news/index.html' },
    { label: 'Sicurezza', href: 'sicurezza/index.html' },
    { label: 'Cardano', href: 'cardano/index.html' },
    { label: 'Strumenti', href: 'strumenti/index.html' },
    { label: 'Parla con Satoshi', href: 'chat/index.html', highlight: true }
  ],

  categories: [
    { id: 'principianti', label: 'Principianti', abbr: 'P', href: 'guide/index.html?filter=principianti', color: '#00f0ff', bg: 'rgba(0,240,255,0.08)' },
    { id: 'sicurezza', label: 'Sicurezza', abbr: 'S', href: 'sicurezza/index.html', color: '#ff2a6d', bg: 'rgba(255,42,109,0.08)' },
    { id: 'bitcoin', label: 'Bitcoin', iconImg: 'assets/img/bitcoin-btc.png', href: 'bitcoin/index.html', color: '#F7931A', bg: 'rgba(247,147,26,0.1)' },
    { id: 'ethereum', label: 'Ethereum', iconImg: 'assets/img/ethereum-eth.svg', href: 'ethereum/index.html', color: '#627EEA', bg: 'rgba(98,126,234,0.1)' },
    { id: 'smart-contract', label: 'Smart Contract', abbr: 'SC', href: 'smart-contract/index.html', color: '#10B981', bg: 'rgba(16,185,129,0.1)' },
    { id: 'cardano', label: 'Cardano', iconImg: 'assets/img/cardano-ada.png', href: 'cardano/index.html', color: '#3b82f6', bg: 'rgba(59,130,246,0.08)' },
    { id: 'defi', label: 'DeFi & Staking', abbr: 'D', href: 'guide/index.html?filter=defi', color: '#bd00ff', bg: 'rgba(189,0,255,0.08)' },
    { id: 'trend', label: 'Trend', abbr: 'T', href: 'trend/index.html', color: '#fcee0a', bg: 'rgba(252,238,10,0.08)' },
    { id: 'strumenti', label: 'Strumenti', abbr: 'St', href: 'strumenti/index.html', color: '#00f0ff', bg: 'rgba(0,240,255,0.06)' }
  ],

  pathColors: ['#00f0ff', '#ff2a6d', '#fcee0a', '#bd00ff', '#3b82f6'],

  social: [
    {
      id: 'x',
      name: 'X',
      handle: '@TheRiser100x',
      url: 'https://x.com/TheRiser100x',
      color: '#E7E9EA',
      desc: 'Notizie rapide, analisi crypto e aggiornamenti in tempo reale.'
    },
    {
      id: 'facebook',
      name: 'Facebook',
      handle: 'The Little Satoshi News',
      url: 'https://www.facebook.com/profile.php?id=61591151756348',
      color: '#1877F2',
      desc: 'Guide brevi, aggiornamenti e community crypto in italiano.'
    },
    {
      id: 'instagram',
      name: 'Instagram',
      handle: '@krown.82',
      url: 'https://www.instagram.com/krown.82/',
      color: '#E1306C',
      desc: 'Tips visivi, caroselli educativi e storie sulla sicurezza crypto.'
    },
    {
      id: 'tiktok',
      name: 'TikTok',
      handle: '@cryptofacile',
      url: 'https://www.tiktok.com/@cryptofacile',
      color: '#00f0ff',
      desc: 'Video brevi: crypto spiegata in 60 secondi, zero hype.'
    },
    {
      id: 'youtube',
      name: 'YouTube',
      handle: '@cryptofacile',
      url: 'https://www.youtube.com/@cryptofacile',
      color: '#FF0000',
      desc: 'Tutorial passo-passo e guide approfondite in video.'
    }
  ],

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

  satoshiAi: {
    name: 'Satoshi',
    title: 'Parla con Satoshi',
    subtitle: 'Assistente AI crypto — powered by Steven AI',
    tagline: 'Chiedi qualsiasi cosa su Bitcoin, DeFi, sicurezza e Web3',
    apiUrl: '',
    productionApiUrl: '',
    useLocalFallback: true,
    chatPage: 'chat/index.html',
    avatar: 'assets/img/welcome-bitcoin-boss.png',
    suggestions: [
      'Cos\'è Bitcoin spiegato semplice?',
      'Come iniziare con le crypto?',
      'Come proteggere il mio wallet?',
      'Cos\'è Cardano e Midnight?'
    ],
    features: [
      'Risposte in italiano, zero gergo',
      'Guide crypto personalizzate',
      'Sicurezza e best practice',
      'Aggiornato su trend e news'
    ]
  },

  tools: [
    { name: 'Ledger', desc: 'Hardware wallet per massima sicurezza', category: 'Wallet', href: '#' },
    { name: 'Revolut', desc: 'Conto per bonifici SEPA verso exchange', category: 'Fintech', href: 'https://revolut.com/referral/?referral-code=stefan2ayd!JUN1-26-AR&geo-redirect', affiliate: true },
    { name: 'Kraken', desc: 'Exchange regolamentato e affidabile', category: 'Exchange', href: 'https://invite.kraken.com/JDNW/pql7tac5', affiliate: true },
    { name: 'Eternl', desc: 'Wallet Cardano consigliato', category: 'Cardano', href: '#' }
  ]
};

function getSocial(id) {
  return (SITE_CONFIG.social || []).find(s => s.id === id);
}

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