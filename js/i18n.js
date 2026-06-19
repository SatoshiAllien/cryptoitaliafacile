const I18N_STORAGE_KEY = 'cf_lang';

function flagImg(code) {
  const base = typeof getBasePath === 'function' ? getBasePath() : '';
  const src = `${base}assets/img/flag-${code}.svg`;
  return `<img src="${src}" class="lang-flag" width="22" height="15" alt="" loading="eager" decoding="async">`;
}

const TRANSLATIONS = {
  it: {
    tagline: 'La crypto, spiegata facile.',
    logoTagline: 'La crypto, spiegata facile',
    nav: {
      guide: 'Guide', cryptoTips: 'Crypto Tips', trend: 'Trend', sicurezza: 'Sicurezza',
      cardano: 'Cardano', strumenti: 'Strumenti', glossario: 'Glossario',
      principianti: 'Principianti', avanzate: 'Avanzate', defi: 'DeFi & Staking', wallet: 'Wallet',
      allGuides: 'Tutte le guide', newsletter: 'Newsletter', newsletterFree: 'Newsletter gratis',
      search: 'Cerca', menu: 'Menu', close: 'Chiudi', closeSearch: 'Chiudi ricerca'
    },
    ui: {
      home: 'Home', readGuide: 'Leggi la guida →', simpleExplanation: 'Spiegazione semplice →',
      updated: 'Aggiornato', beginner: 'Principiante', intermediate: 'Intermedio', advanced: 'Avanzato',
      discover: 'Scopri →', getBonus: 'Ottieni bonus →', all: 'Tutte', noResults: 'Nessun risultato trovato.',
      subscribe: 'Iscriviti gratis', emailPlaceholder: 'La tua email', emailAria: 'Email per newsletter',
      searchPlaceholder: 'Cerca guide, tips, termini… (es. seed phrase, staking ADA)',
      searchShort: 'Cerca…', langLabel: 'Lingua'
    },
    footer: {
      desc: 'Guide pratiche e spiegazioni semplici sul mondo crypto. 100% educativo, zero hype.',
      guides: 'Guide', resources: 'Risorse', legal: 'Legale', about: 'Chi siamo', contacts: 'Contatti',
      disclaimer: 'I contenuti di CryptoFacile sono a scopo puramente educativo e non costituiscono consulenza finanziaria. Investire in crypto comporta rischi.'
    },
    home: {
      welcome: 'Ciao! Sei nel posto giusto per imparare',
      heroTitle: 'La crypto,',
      heroHighlight: 'spiegata facile',
      heroDesc: 'Niente paura, niente gergo complicato. Guide passo-passo, tips pratici e spiegazioni chiare — pensate per chi inizia da zero.',
      ctaStart: 'Inizia da qui', ctaBonus: 'Bonus Revolut + Kraken', ctaSecurity: 'Sicurezza', ctaCardano: 'Cardano',
      reassure1t: 'Non serve essere esperti', reassure1d: 'Tutto spiegato con parole semplici',
      reassure2t: 'Vai con calma', reassure2d: 'Impara al tuo ritmo, senza fretta',
      reassure3t: 'Solo contenuti utili', reassure3d: 'Niente promesse, solo guide pratiche',
      teacherBadge: 'Insegnante', teacherLabel: 'Chi ti guida',
      teacherTitle: 'Insegnante crypto professionale',
      teacherQuote: 'Ti accompagno passo dopo passo nel mondo crypto — con parole semplici, esempi pratici e zero hype. Il mio obiettivo è che tu capisca davvero, non che compri alla cieca.',
      teacherB1: 'Guide passo-passo', teacherB2: 'Sicurezza prima di tutto', teacherB3: 'Linguaggio semplice', teacherB4: 'Per principianti',
      teacherCta: 'Scopri di più su di me →',
      offer: 'Offerta', affTitle: 'Vuoi comprare crypto oggi?',
      affSub: 'Usa i link che usiamo noi — bonus e zero costi extra per te',
      affLink: 'Guida completa →',
      affDisclaimer: 'Link referral: potremmo ricevere una piccola commissione se ti registri, senza costi aggiuntivi per te. Li usiamo realmente nelle nostre guide.',
      explore: 'Esplora', catTitle: 'Scegli da dove iniziare', catDesc: 'Ogni area è pensata per accompagnarti passo dopo passo',
      guidesLabel: 'Guide', guidesTitle: 'Guide più lette', guidesDesc: 'Le guide più utili per iniziare e approfondire', guidesLink: 'Vedi tutte le guide →',
      trendLabel: 'Trend', trendTitle: 'Trend crypto del momento', trendDesc: 'Macro trend spiegati in modo semplice', trendLink: 'Tutti i trend →',
      tipsLabel: 'Tips', tipsTitle: 'Crypto Tips', tipsDesc: 'Consigli brevi e pratici da applicare subito', tipsLink: 'Tutti i tips →',
      pathLabel: 'Percorso', pathTitle: 'Percorso principianti', pathDesc: '5 step semplici per passare da zero al tuo primo wallet',
      toolsTitle: 'Strumenti consigliati', toolsDesc: 'Wallet, exchange e strumenti che usiamo nelle nostre guide',
      nlTitle: '1 tip di sicurezza a settimana',
      nlDesc: 'Iscriviti alla newsletter gratuita e ricevi subito la Checklist Sicurezza Crypto — 25 punti da verificare oggi.',
      nlNote: 'Niente spam. Solo contenuti educativi. Cancellati quando vuoi.'
    },
    trust: ['100% educativo', 'Sicurezza prima di tutto', 'Passo dopo passo', 'Zero hype'],
    categories: {
      principianti: 'Principianti', sicurezza: 'Sicurezza', cardano: 'Cardano',
      defi: 'DeFi & Staking', trend: 'Trend', strumenti: 'Strumenti'
    },
    path: [
      { title: 'Capire le basi', desc: 'Cos\'è una blockchain e come funziona' },
      { title: 'Creare un account', desc: 'Revolut + registrazione su Kraken' },
      { title: 'Primo acquisto', desc: 'Comprare i primi 20€ di Bitcoin' },
      { title: 'Wallet personale', desc: 'Trasferire crypto su wallet tuo' },
      { title: 'Proteggere tutto', desc: 'Seed phrase e sicurezza base' }
    ],
    affiliates: {
      revolut: {
        tagline: 'Il conto che usiamo davvero', headline: 'Apri Revolut in 5 minuti — zero costi',
        hook: 'Bonifici SEPA velocissimi verso Kraken. La banca che non blocca le crypto.',
        perks: ['Conto base gratuito', 'Bonifici SEPA in 1 giorno', 'Carta virtuale inclusa'],
        cta: 'Apri Revolut GRATIS →'
      },
      kraken: {
        tagline: 'Exchange consigliato ai principianti', headline: 'Registrati su Kraken — bonus referral attivo',
        hook: 'Exchange regolamentato dal 2011. Deposito SEPA gratuito, fee basse, massima affidabilità.',
        perks: ['Deposito SEPA gratis', 'Fee tra le più basse', 'Supporto in italiano'],
        cta: 'Ottieni il bonus Kraken →', code: 'Code'
      }
    },
    tools: {
      ledger: { desc: 'Hardware wallet per massima sicurezza', cat: 'Wallet' },
      revolut: { desc: 'Conto per bonifici SEPA verso exchange', cat: 'Fintech' },
      kraken: { desc: 'Exchange regolamentato e affidabile', cat: 'Exchange' },
      eternl: { desc: 'Wallet Cardano consigliato', cat: 'Cardano' }
    },
    hubs: {
      guide: { title: 'Guide Crypto', desc: 'Guide passo-passo per imparare il mondo crypto senza complicazioni. Scegli il tuo livello e inizia.' },
      tips: { title: 'Crypto Tips', desc: 'Consigli brevi e pratici da applicare subito.' },
      trend: { title: 'Trend Crypto', desc: 'Macro trend spiegati in modo semplice, senza hype.' },
      sicurezza: { title: 'Sicurezza Crypto', desc: 'Proteggi wallet, seed phrase e account.' },
      cardano: { title: 'Cardano', desc: 'Tutto sull\'ecosistema ADA.' },
      strumenti: { title: 'Strumenti', desc: 'Wallet, exchange e tool consigliati.' }
    }
  },
  en: {
    tagline: 'Crypto, explained simply.',
    logoTagline: 'Crypto, explained simply',
    nav: {
      guide: 'Guides', cryptoTips: 'Crypto Tips', trend: 'Trends', sicurezza: 'Security',
      cardano: 'Cardano', strumenti: 'Tools', glossario: 'Glossary',
      principianti: 'Beginners', avanzate: 'Advanced', defi: 'DeFi & Staking', wallet: 'Wallet',
      allGuides: 'All guides', newsletter: 'Newsletter', newsletterFree: 'Free newsletter',
      search: 'Search', menu: 'Menu', close: 'Close', closeSearch: 'Close search'
    },
    ui: {
      home: 'Home', readGuide: 'Read guide →', simpleExplanation: 'Simple explanation →',
      updated: 'Updated', beginner: 'Beginner', intermediate: 'Intermediate', advanced: 'Advanced',
      discover: 'Discover →', getBonus: 'Get bonus →', all: 'All', noResults: 'No results found.',
      subscribe: 'Subscribe free', emailPlaceholder: 'Your email', emailAria: 'Email for newsletter',
      searchPlaceholder: 'Search guides, tips, terms… (e.g. seed phrase, staking ADA)',
      searchShort: 'Search…', langLabel: 'Language'
    },
    footer: {
      desc: 'Practical guides and simple explanations about crypto. 100% educational, zero hype.',
      guides: 'Guides', resources: 'Resources', legal: 'Legal', about: 'About us', contacts: 'Contact',
      disclaimer: 'CryptoFacile content is for educational purposes only and does not constitute financial advice. Investing in crypto involves risks.'
    },
    home: {
      welcome: 'Hi! You\'re in the right place to learn',
      heroTitle: 'Crypto,',
      heroHighlight: 'explained simply',
      heroDesc: 'No fear, no complicated jargon. Step-by-step guides, practical tips and clear explanations — designed for complete beginners.',
      ctaStart: 'Start here', ctaBonus: 'Revolut + Kraken bonus', ctaSecurity: 'Security', ctaCardano: 'Cardano',
      reassure1t: 'No expertise needed', reassure1d: 'Everything explained in plain language',
      reassure2t: 'Take your time', reassure2d: 'Learn at your own pace',
      reassure3t: 'Useful content only', reassure3d: 'No promises — just practical guides',
      teacherBadge: 'Teacher', teacherLabel: 'Your guide',
      teacherTitle: 'Professional crypto teacher',
      teacherQuote: 'I walk you through crypto step by step — with simple words, practical examples and zero hype. My goal is for you to truly understand, not buy blindly.',
      teacherB1: 'Step-by-step guides', teacherB2: 'Security first', teacherB3: 'Simple language', teacherB4: 'For beginners',
      teacherCta: 'Learn more about me →',
      offer: 'Offer', affTitle: 'Want to buy crypto today?',
      affSub: 'Use the same links we use — bonuses and no extra cost for you',
      affLink: 'Full guide →',
      affDisclaimer: 'Referral links: we may earn a small commission if you sign up, at no extra cost to you. We actually use these in our guides.',
      explore: 'Explore', catTitle: 'Choose where to start', catDesc: 'Each section is designed to guide you step by step',
      guidesLabel: 'Guides', guidesTitle: 'Most read guides', guidesDesc: 'The most useful guides to start and go deeper', guidesLink: 'See all guides →',
      trendLabel: 'Trends', trendTitle: 'Crypto trends right now', trendDesc: 'Macro trends explained simply', trendLink: 'All trends →',
      tipsLabel: 'Tips', tipsTitle: 'Crypto Tips', tipsDesc: 'Short, practical advice you can use right away', tipsLink: 'All tips →',
      pathLabel: 'Path', pathTitle: 'Beginner path', pathDesc: '5 simple steps from zero to your first wallet',
      toolsTitle: 'Recommended tools', toolsDesc: 'Wallets, exchanges and tools we use in our guides',
      nlTitle: '1 security tip per week',
      nlDesc: 'Subscribe to the free newsletter and get the Crypto Security Checklist — 25 points to verify today.',
      nlNote: 'No spam. Educational content only. Unsubscribe anytime.'
    },
    trust: ['100% educational', 'Security first', 'Step by step', 'Zero hype'],
    categories: {
      principianti: 'Beginners', sicurezza: 'Security', cardano: 'Cardano',
      defi: 'DeFi & Staking', trend: 'Trends', strumenti: 'Tools'
    },
    path: [
      { title: 'Learn the basics', desc: 'What a blockchain is and how it works' },
      { title: 'Create an account', desc: 'Revolut + Kraken registration' },
      { title: 'First purchase', desc: 'Buy your first €20 of Bitcoin' },
      { title: 'Personal wallet', desc: 'Transfer crypto to your own wallet' },
      { title: 'Protect everything', desc: 'Seed phrase and basic security' }
    ],
    affiliates: {
      revolut: {
        tagline: 'The account we actually use', headline: 'Open Revolut in 5 minutes — zero fees',
        hook: 'Fast SEPA transfers to Kraken. The bank that doesn\'t block crypto.',
        perks: ['Free basic account', 'SEPA transfers in 1 day', 'Virtual card included'],
        cta: 'Open Revolut FREE →'
      },
      kraken: {
        tagline: 'Recommended exchange for beginners', headline: 'Sign up on Kraken — referral bonus active',
        hook: 'Regulated exchange since 2011. Free SEPA deposits, low fees, maximum reliability.',
        perks: ['Free SEPA deposit', 'Among the lowest fees', 'Reliable support'],
        cta: 'Get Kraken bonus →', code: 'Code'
      }
    },
    tools: {
      ledger: { desc: 'Hardware wallet for maximum security', cat: 'Wallet' },
      revolut: { desc: 'Account for SEPA transfers to exchanges', cat: 'Fintech' },
      kraken: { desc: 'Regulated and reliable exchange', cat: 'Exchange' },
      eternl: { desc: 'Recommended Cardano wallet', cat: 'Cardano' }
    },
    hubs: {
      guide: { title: 'Crypto Guides', desc: 'Step-by-step guides to learn crypto without complications. Pick your level and start.' },
      tips: { title: 'Crypto Tips', desc: 'Short, practical tips you can apply right away.' },
      trend: { title: 'Crypto Trends', desc: 'Macro trends explained simply, without hype.' },
      sicurezza: { title: 'Crypto Security', desc: 'Protect wallets, seed phrases and accounts.' },
      cardano: { title: 'Cardano', desc: 'Everything about the ADA ecosystem.' },
      strumenti: { title: 'Tools', desc: 'Recommended wallets, exchanges and tools.' }
    }
  }
};

const ARTICLE_EN = {
  'iniziare-exchange-revolut-kraken': { title: 'Getting started with exchanges: Revolut + Kraken guide for beginners', excerpt: 'Crypto exchanges explained simply: why use Revolut, how to sign up on Kraken and make your first safe purchase.' },
  'lightning-network-guida': { title: 'Lightning Network explained simply: sats, wallets and Satoshi Wallet', excerpt: 'What Lightning is, how sats work, which wallets to use and how to pay with the Satoshi Wallet merchant map.' },
  'comprare-bitcoin-prima-volta': { title: 'How to buy Bitcoin for the first time (complete 2026 guide)', excerpt: 'Exchange, identity verification, first purchase and security: everything step by step.' },
  'creare-wallet-sicuro': { title: 'How to create a secure crypto wallet in 10 minutes', excerpt: 'Hot wallet, cold wallet and basic setup to protect your crypto.' },
  'proteggere-seed-phrase': { title: 'How to protect your seed phrase: methods and mistakes to avoid', excerpt: 'The golden rule of crypto security: keeping your 12-24 recovery words safe.' },
  'blockchain-5-minuti': { title: 'Blockchain in 5 minutes: how it works', excerpt: 'The basics of blockchain explained without technical jargon.' },
  'cardano-spiegato': { title: 'Cardano explained: what is ADA', excerpt: 'The Cardano ecosystem, staking and why it matters.' }
};

function getLang() {
  return localStorage.getItem(I18N_STORAGE_KEY) || 'it';
}

function setLang(lang) {
  localStorage.setItem(I18N_STORAGE_KEY, lang);
  document.documentElement.lang = lang;
}

function t(key) {
  const lang = getLang();
  const parts = key.split('.');
  let val = TRANSLATIONS[lang];
  for (const p of parts) {
    val = val?.[p];
  }
  if (val === undefined && lang !== 'it') {
    val = TRANSLATIONS.it;
    for (const p of parts) val = val?.[p];
  }
  return val ?? key;
}

function localizeArticle(article) {
  if (getLang() !== 'en' || !article?.slug) return article;
  const en = ARTICLE_EN[article.slug];
  if (!en) return article;
  return { ...article, title: en.title, excerpt: en.excerpt };
}

function renderLangSwitcher() {
  const lang = getLang();
  return `
    <div class="lang-switcher" role="group" aria-label="${t('ui.langLabel')}">
      <button type="button" class="lang-btn${lang === 'it' ? ' lang-btn--active' : ''}" data-lang="it" aria-pressed="${lang === 'it'}" title="Italiano">
        ${flagImg('it')}<span class="lang-code">IT</span>
      </button>
      <button type="button" class="lang-btn${lang === 'en' ? ' lang-btn--active' : ''}" data-lang="en" aria-pressed="${lang === 'en'}" title="English">
        ${flagImg('en')}<span class="lang-code">EN</span>
      </button>
    </div>`;
}

function applyPageTranslations() {
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.dataset.i18n;
    const val = t(key);
    if (typeof val === 'string') el.textContent = val;
  });
  document.querySelectorAll('[data-i18n-html]').forEach(el => {
    const val = t(el.dataset.i18nHtml);
    if (typeof val === 'string') el.innerHTML = val;
  });
  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
    el.placeholder = t(el.dataset.i18nPlaceholder);
  });
  document.querySelectorAll('[data-i18n-aria]').forEach(el => {
    el.setAttribute('aria-label', t(el.dataset.i18nAria));
  });
  const titleKey = document.body.dataset.i18nTitle;
  if (titleKey) document.title = t(titleKey);
}

function initLangSwitcher() {
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const lang = btn.dataset.lang;
      if (lang === getLang()) return;
      setLang(lang);
      window.dispatchEvent(new CustomEvent('langchange', { detail: { lang } }));
    });
  });
}

function initI18n() {
  document.documentElement.lang = getLang();
  initLangSwitcher();
  applyPageTranslations();
}