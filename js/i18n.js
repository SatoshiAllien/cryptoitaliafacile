const I18N_STORAGE_KEY = 'cf_lang';

function flagImg(code) {
  const base = typeof getBasePath === 'function' ? getBasePath() : '';
  const src = `${base}assets/img/flag-${code}.svg`;
  return `<img src="${src}" class="lang-flag" width="22" height="15" alt="" loading="eager" decoding="async">`;
}

const TRANSLATIONS = {
  it: {
    tagline: 'Notizie e crypto, facili e semplici.',
    logoTagline: 'Notizie e crypto, facili e semplici',
    nav: {
      guide: 'Guide', cryptoTips: 'Crypto Tips', trend: 'Trend', news: 'News', sicurezza: 'Sicurezza',
      cardano: 'Cardano', strumenti: 'Strumenti', glossario: 'Glossario',
      principianti: 'Principianti', avanzate: 'Avanzate', defi: 'DeFi & Staking', wallet: 'Wallet',
      allGuides: 'Tutte le guide', newsletter: 'Newsletter', newsletterFree: 'Newsletter gratis',
      satoshiAi: 'Parla con Satoshi',
      tabGuide: 'Guide', tabTips: 'Consigli', tabTrend: 'Trend', tabNews: 'Notizie',
      tabSecurity: 'Sicurezza', tabCardano: 'Cardano', tabTools: 'Strumenti', tabSatoshi: 'Satoshi',
      openSection: 'Apri sezione', satoshiSub: 'Assistente AI crypto', followUs: 'Seguici',
      social: 'Social', search: 'Cerca', menu: 'Menu', close: 'Chiudi', closeSearch: 'Chiudi ricerca'
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
      desc: 'Notizie crypto e guide spiegate in modo facile e semplice. 100% educativo, zero hype.',
      guides: 'Guide', resources: 'Risorse', legal: 'Legale', about: 'Chi siamo', founder: 'Il Fondatore', techLab: 'Tech Lab', hospitality: 'Ospitalità', contacts: 'Contatti',
      disclaimer: 'I contenuti di The Little Satoshi News sono a scopo puramente educativo e non costituiscono consulenza finanziaria. Investire in crypto comporta rischi.'
    },
    home: {
      cryptoFacileName: 'CryptoFacile',
      cryptoFacileTagline: 'La crypto spiegata facile',
      welcome: 'Ciao! Sei nel posto giusto per imparare',
      welcomeLabel: 'Benvenuto',
      welcomeBadge: 'Breaking News',
      welcomeTitle: 'Benvenuto in The Little Satoshi News',
      welcomeLead: 'La voce indipendente di chi vive le crypto dal 2015, con mentalità da patriot 🇺🇸, radici italiane 🇮🇹 e occhi laser puntati sul futuro.',
      welcomeP1: 'Qui non trovi rumore, hype o propaganda. Trovi verità, analisi, cultura Bitcoin e aggiornamenti reali, raccontati da chi ha attraversato ogni ciclo e continua a costruire per il prossimo.',
      welcomeP2: 'E soprattutto: le crypto spiegate in modo facile, intuitivo e senza tecnicismi inutili. Perché capire è potere.',
      welcomeListTitle: 'Cosa trovi qui:',
      welcomeLi1: 'Notizie crypto spiegate in modo chiaro e diretto',
      welcomeLi2: 'Analisi su Bitcoin, cicli, macro e narrativa',
      welcomeLi3: 'Focus su Cardano e Midnight, le reti che stanno cambiando il gioco',
      welcomeLi4: 'Meme, cultura e riflessioni per chi stacka sats e libertà',
      welcomeLi5: 'Guide semplici e intuitive per muoverti nel mondo Web3 senza confusione',
      welcomeP3: 'Questo è il posto per chi non segue la massa. Per chi vuole capire, non farsi manipolare. Per chi costruisce, non aspetta.',
      welcomeClosing1: 'Stacking truth.',
      welcomeClosing2: 'Stacking memes.',
      heroTitle: 'Notizie e crypto,',
      heroHighlight: 'facili e semplici',
      heroDesc: 'Notizie aggiornate e crypto spiegate in modo facile e semplice. Niente gergo, niente hype — solo guide chiare per chi inizia da zero.',
      ctaStart: 'Inizia da qui', ctaBonus: 'Bonus Revolut + Kraken', ctaSecurity: 'Sicurezza', ctaCardano: 'Cardano', ctaInstagram: 'Instagram', ctaFacebook: 'Facebook',
      instagramLabel: 'Instagram', instagramTitle: 'Seguici su Instagram',
      instagramDesc: 'Tips visivi, caroselli educativi e storie sulla sicurezza crypto — ogni giorno contenuti freschi per imparare senza hype.',
      instagramCta: 'Segui @krown.82 →',
      instagramLi1: 'Caroselli e tips in formato verticale',
      instagramLi2: 'Storie e highlights su sicurezza e trend',
      instagramLi3: 'Crypto spiegata in 60 secondi',
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
      socialLabel: 'Social', socialTitle: 'Seguici sui social',
      socialDesc: 'Tips, notizie e aggiornamenti su X, Facebook, Instagram e TikTok.',
      socialLink: 'Tutti i profili →',
      nlTitle: '1 tip di sicurezza a settimana',
      nlDesc: 'Iscriviti alla newsletter gratuita e ricevi subito la Checklist Sicurezza Crypto — 25 punti da verificare oggi.',
      nlNote: 'Niente spam. Solo contenuti educativi. Cancellati quando vuoi.',
      aiLabel: 'Assistente AI',
      aiTitle: 'Parla con Satoshi',
      aiDesc: 'Il tuo assistente AI crypto personale. Chiedi qualsiasi cosa su Bitcoin, sicurezza, DeFi e Web3 — risposte chiare in italiano.',
      aiCta: 'Inizia a chattare',
      aiFeature1: 'Italiano, zero gergo',
      aiFeature2: 'Guide personalizzate',
      aiFeature3: 'Sicurezza crypto',
      aiFeature4: 'Steven AI'
    },
    founder: {
      label: 'Il Creatore di CryptoItaliaFacile',
      title: 'Chi è il Fondatore',
      subtitle: 'Rendere il mondo crypto comprensibile, sicuro e accessibile a tutti.',
      name: 'Stefano Davide Ciancimino',
      role: 'Fondatore di CryptoItaliaFacile · Fraud & Risk Analyst · Blockchain Researcher · AI Specialist',
      bio: 'Oltre 8 anni in PayPal tra antifrode e risk operations. Ricercatore blockchain dal 2017. Creo contenuti educativi chiari per rendere Bitcoin, DeFi e Web3 accessibili a tutti — con sicurezza e zero hype.',
      badge: 'Fondatore',
      stat1: 'anni in PayPal',
      stat2: 'ricerca blockchain',
      stat3: 'educativo, zero hype',
      p1: 'Autorevolezza',
      p2: 'Esperienza reale',
      p3: 'Missione educativa',
      p4: 'Sicurezza prima di tutto',
      cta: 'Scopri il fondatore →',
      ctaContact: 'Contatta il Fondatore',
      ctaLinkedin: 'Segui su LinkedIn',
      ctaConsult: 'Richiedi una consulenza'
    },
    techLab: {
      label: 'Il Mio Spazio Tecnologico',
      title: 'Tech Lab Personale',
      subtitle: 'Sperimentazione, hardware custom e AI locali — competenze reali oltre il mondo crypto.',
      homeHeadline: 'Hobby Tecnologici & Progetti Personali',
      homeDesc: 'Build PC avanzati, ambienti multi‑OS, modelli AI in locale con Ollama e GPU NVIDIA, automazioni PowerShell e scripting Linux. Un laboratorio dove passione tecnica e metodo professionale si incontrano.',
      pill1: 'Build PC',
      pill2: 'AI Locale',
      pill3: 'Multi‑OS',
      pill4: 'Scripting',
      cta: 'Esplora il Tech Lab →'
    },
    hospitality: {
      label: 'Esperienze Globali & Passione per l\'Arte del Servizio',
      title: 'Dall\'Estero alla Mixology',
      subtitle: '10+ anni tra hotel, bar e turismo internazionale — UK, Sudafrica e Italia.',
      homeHeadline: 'La Mia Storia nel Mondo dell\'Ospitalità',
      homeDesc: 'Da commis de rang in Sicilia a bartender al Royal Shakespeare Company in UK, passando per resort 5 stelle e Sudafrica. Formazione AIBES, mixology, sommelier e HACCP — un percorso che ha forgiato disciplina, calma e cura del dettaglio.',
      stat1: 'anni',
      stat2: 'continenti',
      stat3: 'barman',
      cta: 'Leggi la storia completa →'
    },
    newsHub: {
      filterAll: 'Tutte',
      filterX: 'Da X',
      filterTrend: 'Trend',
      filterTips: 'Tips',
      filterSite: 'Dal sito',
      items: 'notizie',
      exportAll: 'Esporta feed',
      exportTitle: 'Feed News — The Little Satoshi News',
      noItems: 'Nessuna notizia per questo filtro.',
      error: 'Impossibile caricare il feed news.',
      plusSite: '+ sito'
    },
    btcNews: {
      label: 'Sessione News',
      title: 'Sessione News Bitcoin',
      desc: 'Notizie in tempo reale da @BitcoinMagazine, @Strategy e @CPOfficialtx — pronte da leggere o ripubblicare.',
      homeTitle: 'News del momento',
      homeDesc: 'Tutte le notizie aggregate: X, trend crypto e aggiornamenti del sito.',
      filterAll: 'Tutte',
      openOnX: 'Apri su X',
      noItems: 'Nessuna news per questo filtro.',
      homeLink: 'Tutte le news →',
      items: 'notizie',
      updated: 'Aggiornato',
      exportAll: 'Esporta tutte le news',
      shareX: 'Condividi su X',
      readMore: 'Leggi →',
      readArticle: 'Leggi articolo',
      repost: 'Ripubblica',
      copied: 'Copiato!',
      exportedAll: 'Sessione esportata!',
      exported: 'Esportato',
      source: 'Fonte',
      copyPrompt: 'Copia il testo della news:',
      error: 'Impossibile caricare le news Bitcoin.',
      breaking: 'In evidenza',
      guidesLabel: 'Guide',
      guidesTitle: 'Tutte le guide Bitcoin',
      categories: {
        guide: 'Guida', tip: 'Tip', trend: 'Trend', tutorial: 'Tutorial',
        cardano: 'Cardano', sicurezza: 'Sicurezza', bitcoin: 'Bitcoin'
      }
    },
    trust: ['100% educativo', 'Sicurezza prima di tutto', 'Passo dopo passo', 'Zero hype'],
    categories: {
      principianti: 'Principianti', sicurezza: 'Sicurezza',
      bitcoin: 'Bitcoin', ethereum: 'Ethereum', 'smart-contract': 'Smart Contract',
      cardano: 'Cardano', defi: 'DeFi & Staking', trend: 'Trend', strumenti: 'Strumenti'
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
      tips: { title: 'Crypto Tips', desc: 'Consigli brevi e pratici da applicare subito. Niente fuffa, solo azioni concrete.' },
      trend: { title: 'Trend Crypto del Momento', desc: 'I macro trend che stanno plasmando il mondo crypto, spiegati senza hype.' },
      news: { title: 'News', desc: 'Tutte le notizie aggregate: feed X, trend crypto e aggiornamenti The Little Satoshi News.' },
      sicurezza: { title: 'Sicurezza & Protezione Wallet', desc: 'Proteggi le tue crypto. Guide su seed phrase, hardware wallet, phishing e best practice.', goldenRule: 'Regola d\'oro', goldenText: 'Nessuno legittimo ti chiederà mai la seed phrase. Nemmeno il "supporto tecnico".' },
      bitcoin: { title: 'Bitcoin', desc: 'Guide su BTC, acquisto, wallet, Lightning Network, halving e cultura Bitcoin spiegate in modo semplice.' },
      ethereum: { title: 'Ethereum', desc: 'Guide su ETH, staking, gas fee, wallet, Layer 2 e DeFi spiegate senza tecnicismi.' },
      'smart-contract': { title: 'Smart Contract', desc: 'Contratti intelligenti spiegati in modo chiaro: verifica, approvazioni, Solidity base e sicurezza DeFi.' },
      cardano: { title: 'Ecosistema Cardano', desc: 'Guide dedicate a ADA, staking, wallet Cardano, DeFi, governance e scalabilità.' },
      strumenti: { title: 'Strumenti Crypto', desc: 'Guide e confronti su wallet, exchange, hardware wallet e strumenti di monitoraggio.', toolsSection: 'Strumenti consigliati' }
    },
    pages: {
      about: {
        metaTitle: 'Chi siamo — The Little Satoshi News',
        metaDesc: 'Chi siamo: The Little Satoshi News è il portale educativo che spiega il mondo crypto in modo semplice e pratico.',
        label: 'Chi siamo', badge: 'Insegnante', alt: 'Stefano — Insegnante crypto professionale',
        role: 'Insegnante crypto professionale · Fondatore di The Little Satoshi News',
        quote: '"Ti accompagno passo dopo passo nel mondo crypto — con parole semplici, esempi pratici e zero hype. Il mio obiettivo è che tu capisca davvero, non che compri alla cieca."',
        mission: 'La nostra missione', mission1: 'nasce con un obiettivo semplice: rendere il mondo crypto accessibile a tutti, senza hype e senza complicazioni inutili.',
        mission2: 'Ispirato allo stile chiaro e pratico di Aranzulla, il nostro portale offre guide passo-passo, tips brevi e spiegazioni dei macro trend — tutto con un linguaggio che chiunque può capire.',
        mission3: 'Educare, non vendere. Ogni contenuto su The Little Satoshi News ha un solo scopo: aiutarti a capire e usare le criptovalute in sicurezza.',
        find: 'Cosa troverai', find1: 'Guide passo-passo per principianti e utenti avanzati',
        find2: 'Crypto Tips brevi e immediatamente applicabili', find3: 'Spiegazioni dei macro trend senza sensazionalismo',
        find4: 'Sezione dedicata all\'ecosistema Cardano', find5: 'Guide approfondite su sicurezza e protezione wallet',
        find6: 'Glossario con tutti i termini crypto', approach: 'Il nostro approccio', principles: 'I nostri principi',
        principlesText: 'Semplicità · Praticità · Sicurezza · Zero hype · 100% educativo',
        contact: 'Hai domande o suggerimenti?', contactLink: 'Contattaci'
      },
      contacts: {
        metaTitle: 'Contatti — The Little Satoshi News', metaDesc: 'Contatta il team di The Little Satoshi News per domande, suggerimenti o collaborazioni.',
        title: 'Contatti', intro: 'Hai una domanda, un suggerimento per una nuova guida o vuoi collaborare con noi? Scrivici!',
        name: 'Nome', email: 'Email', message: 'Messaggio', submit: 'Invia messaggio',
        or: 'Oppure scrivici a', thanks: 'Grazie per il messaggio! Ti risponderemo al più presto.'
      },
      newsletter: {
        metaTitle: 'Newsletter — The Little Satoshi News',
        metaDesc: 'Iscriviti alla newsletter The Little Satoshi News: 1 tip di sicurezza a settimana + Checklist Sicurezza Crypto gratis.',
        title: 'Newsletter The Little Satoshi News', intro: 'Iscriviti gratis e ricevi:',
        item1: '1 tip di sicurezza a settimana', item2: 'Nuove guide passo-passo',
        item3: 'Checklist Sicurezza Crypto (PDF) in regalo',
        thanks: 'Grazie! Ti abbiamo iscritto alla newsletter The Little Satoshi News. Controlla la tua email.'
      },
      search: {
        metaTitle: 'Cerca — The Little Satoshi News', metaDesc: 'Cerca guide, tips e termini crypto su The Little Satoshi News.',
        title: 'Cerca su The Little Satoshi News', desc: 'Trova guide, tips, trend e termini del glossario.',
        noResults: 'Nessun risultato per', tryOther: 'Prova con altri termini.'
      },
      glossary: {
        metaTitle: 'Glossario Crypto — The Little Satoshi News',
        metaDesc: 'Glossario crypto A-Z: tutti i termini del mondo criptovalute spiegati in modo semplice.',
        title: 'Glossario Crypto', desc: 'Tutti i termini del mondo crypto spiegati in parole semplici. Da A a Z.',
        all: 'Tutti', glossaryLabel: 'glossario'
      },
      social: {
        metaTitle: 'Social — The Little Satoshi News',
        metaDesc: 'Segui The Little Satoshi News su X, Facebook, Instagram, TikTok e YouTube. Guide crypto semplici ogni giorno.',
        title: 'Seguici sui social',
        desc: 'Tips, guide brevi e aggiornamenti sul mondo crypto. Scegli la piattaforma che preferisci.',
        follow: 'Seguici', cta: 'Vai al profilo →',
        x: { desc: 'Notizie rapide, analisi crypto e aggiornamenti in tempo reale.' },
        facebook: { desc: 'Guide brevi, aggiornamenti e community crypto in italiano.' },
        instagram: { desc: 'Tips visivi, caroselli educativi e storie sulla sicurezza crypto.' },
        tiktok: { desc: 'Video brevi: crypto spiegata in 60 secondi, zero hype.' },
        youtube: { desc: 'Tutorial passo-passo e guide approfondite in video.' }
      },
      article: {
        metaTitle: 'Articolo — The Little Satoshi News', metaDesc: 'Guida crypto su The Little Satoshi News',
        related: 'Guide correlate', nlTitle: 'Non perdere i prossimi aggiornamenti',
        nlDesc: 'Ricevi tips di sicurezza e nuove guide direttamente nella tua inbox.',
        toc: 'Indice', faq: 'Domande frequenti', readMin: 'min di lettura', updated: 'Aggiornato'
      },
      privacy: {
        metaTitle: 'Privacy Policy — The Little Satoshi News', title: 'Privacy Policy', updated: 'Ultimo aggiornamento: Giugno 2026',
        intro: 'The Little Satoshi News rispetta la tua privacy. Questa policy descrive come raccogliamo e utilizziamo i dati personali.',
        dataTitle: 'Dati raccolti', data: 'Raccogliamo solo i dati che ci fornisci volontariamente: indirizzo email (newsletter), nome e messaggio (modulo contatti), e dati di navigazione anonimi tramite cookie analitici.',
        useTitle: 'Utilizzo dei dati', use: 'I dati vengono utilizzati esclusivamente per inviare la newsletter, rispondere alle richieste di contatto e migliorare il sito.',
        rightsTitle: 'I tuoi diritti', rights: 'Hai diritto di accesso, rettifica, cancellazione e opposizione al trattamento dei tuoi dati. Contattaci a info@cryptofacile.com.'
      },
      disclaimer: {
        metaTitle: 'Disclaimer — The Little Satoshi News', title: 'Disclaimer', warning: 'Avviso importante',
        warningText: 'I contenuti di The Little Satoshi News sono forniti a scopo puramente educativo e informativo. Non costituiscono consulenza finanziaria, fiscale o legale.',
        risksTitle: 'Rischi', risks: 'L\'investimento in criptovalute comporta rischi significativi, inclusa la possibilità di perdere l\'intero capitale investito. I prezzi delle crypto sono altamente volatili.',
        affTitle: 'Affiliazioni', aff: 'Alcuni link presenti sul sito sono link di affiliazione. Questo significa che potremmo ricevere una commissione se acquisti un prodotto tramite i nostri link, senza costi aggiuntivi per te. Questo non influenza le nostre recensioni editoriali.',
        accuracyTitle: 'Accuratezza', accuracy: 'Ci impegniamo a mantenere i contenuti aggiornati e accurati, ma il mondo crypto evolve rapidamente. Verifica sempre le informazioni con fonti ufficiali prima di prendere decisioni.'
      },
      cookie: {
        metaTitle: 'Cookie Policy — The Little Satoshi News', title: 'Cookie Policy', updated: 'Ultimo aggiornamento: Giugno 2026',
        intro: 'The Little Satoshi News utilizza cookie tecnici necessari al funzionamento del sito e cookie analitici per comprendere come i visitatori utilizzano il portale.',
        typesTitle: 'Tipi di cookie', tech: 'Cookie tecnici', techDesc: 'necessari per la navigazione e il funzionamento del sito',
        analytics: 'Cookie analitici', analyticsDesc: 'raccolgono dati anonimi sull\'utilizzo del sito',
        manageTitle: 'Gestione dei cookie', manage: 'Puoi disabilitare i cookie dalle impostazioni del tuo browser. La disabilitazione dei cookie tecnici potrebbe limitare alcune funzionalità del sito.'
      }
    },
    meta: {
      homeTitle: 'The Little Satoshi News — Notizie e crypto, facili e semplici',
      homeDesc: 'Notizie crypto e guide spiegate in modo facile e semplice. Bitcoin, wallet, DeFi e sicurezza senza hype.',
      guideTitle: 'Guide Crypto — The Little Satoshi News',
      guideDesc: 'Guide crypto passo-passo per principianti e avanzati. Impara Bitcoin, wallet, DeFi, staking e molto altro su The Little Satoshi News.',
      tipsTitle: 'Crypto Tips — The Little Satoshi News', tipsDesc: 'Consigli brevi e pratici sul mondo crypto.',
      trendTitle: 'Trend Crypto — The Little Satoshi News', trendDesc: 'Macro trend crypto spiegati in modo semplice.',
      sicurezzaTitle: 'Sicurezza Crypto — The Little Satoshi News',
      sicurezzaDesc: 'Guide sulla sicurezza crypto: seed phrase, hardware wallet, phishing, backup e protezione del portafoglio.',
      cardanoTitle: 'Cardano — The Little Satoshi News',
      cardanoDesc: 'Tutto sull\'ecosistema Cardano: ADA, staking, wallet, DeFi, Catalyst e Hydra spiegati in modo semplice.',
      strumentiTitle: 'Strumenti Crypto — The Little Satoshi News',
      strumentiDesc: 'Confronti e guide su wallet, exchange, tracker e strumenti crypto consigliati.'
    },
    articleGeneric: {
      introSuffix: 'Questo articolo fa parte della sezione {cat} di The Little Satoshi News. Stiamo aggiornando il contenuto completo — nel frattempo, ecco una panoramica utile.',
      overview: 'Panoramica', overview2: 'In questa guida vedremo tutto ciò che serve per approfondire l\'argomento in modo pratico e sicuro, senza hype e con esempi concreti.',
      steps: 'Passi principali', step1t: 'Passo 1 — Preparazione', step1d: 'Raccogli le informazioni necessarie e assicurati di aver compreso i rischi base prima di procedere.',
      step2t: 'Passo 2 — Esecuzione', step2d: 'Segui le istruzioni passo dopo passo, verificando ogni operazione prima di confermare.',
      step3t: 'Passo 3 — Verifica', step3d: 'Controlla che tutto sia andato a buon fine e conserva traccia dell\'operazione.',
      warning: 'Attenzione', warningText: 'Questo contenuto ha scopo educativo. Non costituisce consulenza finanziaria. Investire in crypto comporta rischi.',
      tips: 'Consigli pratici', tip1: 'Inizia sempre con piccole somme per fare pratica', tip2: 'Verifica le fonti ufficiali prima di ogni operazione',
      tip3: 'Non condividere mai seed phrase o chiavi private', tip4: 'Tieni traccia di ogni operazione per la dichiarazione fiscale',
      faq1q: 'Questo articolo è adatto ai principianti?', faq1a: 'Sì, The Little Satoshi News è pensato per chi si avvicina al mondo crypto. Se un termine non ti è chiaro, consulta il nostro glossario.',
      faq2q: 'Quando sarà aggiornato il contenuto completo?', faq2a: 'Stiamo pubblicando le guide complete progressivamente. Iscriviti alla newsletter per ricevere gli aggiornamenti.',
      catGuide: 'Guida passo-passo', catTip: 'Crypto Tip', catTrend: 'Trend crypto', catTutorial: 'Tutorial', catCardano: 'Cardano', catSicurezza: 'Sicurezza'
    },
    messages: { noArticles: 'Nessun articolo in questa categoria.', bonus: 'BONUS' }
  },
  en: {
    tagline: 'News and crypto, easy and simple.',
    logoTagline: 'News and crypto, easy and simple',
    nav: {
      guide: 'Guides', cryptoTips: 'Crypto Tips', trend: 'Trends', news: 'News', sicurezza: 'Security',
      cardano: 'Cardano', strumenti: 'Tools', glossario: 'Glossary',
      principianti: 'Beginners', avanzate: 'Advanced', defi: 'DeFi & Staking', wallet: 'Wallet',
      allGuides: 'All guides', newsletter: 'Newsletter', newsletterFree: 'Free newsletter',
      satoshiAi: 'Talk to Satoshi',
      tabGuide: 'Guides', tabTips: 'Tips', tabTrend: 'Trends', tabNews: 'News',
      tabSecurity: 'Security', tabCardano: 'Cardano', tabTools: 'Tools', tabSatoshi: 'Satoshi',
      openSection: 'Open section', satoshiSub: 'Crypto AI assistant', followUs: 'Follow us',
      social: 'Social', search: 'Search', menu: 'Menu', close: 'Close', closeSearch: 'Close search'
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
      guides: 'Guides', resources: 'Resources', legal: 'Legal', about: 'About us', founder: 'The Founder', techLab: 'Tech Lab', hospitality: 'Hospitality', contacts: 'Contact',
      disclaimer: 'The Little Satoshi News content is for educational purposes only and does not constitute financial advice. Investing in crypto involves risks.'
    },
    home: {
      cryptoFacileName: 'CryptoFacile',
      cryptoFacileTagline: 'Crypto explained the easy way',
      welcome: 'Hi! You\'re in the right place to learn',
      welcomeLabel: 'Welcome',
      welcomeBadge: 'Breaking News',
      welcomeTitle: 'Welcome to The Little Satoshi News',
      welcomeLead: 'The independent voice of someone who\'s lived crypto since 2015 — patriot mindset 🇺🇸, Italian roots 🇮🇹, and laser eyes on the future.',
      welcomeP1: 'No noise, hype or propaganda here. You get truth, analysis, Bitcoin culture and real updates — told by someone who\'s ridden every cycle and keeps building for the next.',
      welcomeP2: 'Above all: crypto explained simply, intuitively and without useless jargon. Because understanding is power.',
      welcomeListTitle: 'What you\'ll find here:',
      welcomeLi1: 'Crypto news explained clearly and directly',
      welcomeLi2: 'Analysis on Bitcoin, cycles, macro and narrative',
      welcomeLi3: 'Focus on Cardano and Midnight — networks changing the game',
      welcomeLi4: 'Memes, culture and reflections for those stacking sats and freedom',
      welcomeLi5: 'Simple, intuitive guides to navigate Web3 without confusion',
      welcomeP3: 'This is the place for those who don\'t follow the crowd. Who want to understand, not be manipulated. Who build, not wait.',
      welcomeClosing1: 'Stacking truth.',
      welcomeClosing2: 'Stacking memes.',
      heroTitle: 'News and crypto,',
      heroHighlight: 'easy and simple',
      heroDesc: 'Fresh crypto news and explanations the easy, simple way. No jargon, no hype — just clear guides for complete beginners.',
      ctaStart: 'Start here', ctaBonus: 'Revolut + Kraken bonus', ctaSecurity: 'Security', ctaCardano: 'Cardano', ctaInstagram: 'Instagram', ctaFacebook: 'Facebook',
      instagramLabel: 'Instagram', instagramTitle: 'Follow us on Instagram',
      instagramDesc: 'Visual tips, educational carousels and security stories — fresh content every day to learn without hype.',
      instagramCta: 'Follow @krown.82 →',
      instagramLi1: 'Vertical carousels and quick tips',
      instagramLi2: 'Stories and highlights on security and trends',
      instagramLi3: 'Crypto explained in 60 seconds',
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
      socialLabel: 'Social', socialTitle: 'Follow us on social',
      socialDesc: 'Tips, news and updates on X, Facebook, Instagram and TikTok.',
      socialLink: 'All profiles →',
      nlTitle: '1 security tip per week',
      nlDesc: 'Subscribe to the free newsletter and get the Crypto Security Checklist — 25 points to verify today.',
      nlNote: 'No spam. Educational content only. Unsubscribe anytime.',
      aiLabel: 'AI Assistant',
      aiTitle: 'Talk to Satoshi',
      aiDesc: 'Your personal crypto AI assistant. Ask anything about Bitcoin, security, DeFi and Web3 — clear answers in plain language.',
      aiCta: 'Start chatting',
      aiFeature1: 'Plain language, zero jargon',
      aiFeature2: 'Personalized guides',
      aiFeature3: 'Crypto security',
      aiFeature4: 'Steven AI'
    },
    founder: {
      label: 'The Creator of CryptoItaliaFacile',
      title: 'Meet the Founder',
      subtitle: 'Making crypto understandable, secure and accessible for everyone.',
      name: 'Stefano Davide Ciancimino',
      role: 'Founder of CryptoItaliaFacile · Fraud & Risk Analyst · Blockchain Researcher · AI Specialist',
      bio: '8+ years at PayPal in fraud prevention and risk operations. Independent blockchain researcher since 2017. I create clear educational content to make Bitcoin, DeFi and Web3 accessible — with security and zero hype.',
      badge: 'Founder',
      stat1: 'years at PayPal',
      stat2: 'blockchain research',
      stat3: 'educational, zero hype',
      p1: 'Authority',
      p2: 'Real experience',
      p3: 'Educational mission',
      p4: 'Security first',
      cta: 'Meet the founder →',
      ctaContact: 'Contact the Founder',
      ctaLinkedin: 'Follow on LinkedIn',
      ctaConsult: 'Request a consultation'
    },
    techLab: {
      label: 'My Technology Space',
      title: 'Personal Tech Lab',
      subtitle: 'Experimentation, custom hardware and local AI — real skills beyond the crypto world.',
      homeHeadline: 'Tech Hobbies & Personal Projects',
      homeDesc: 'Advanced PC builds, multi‑OS environments, local AI models with Ollama and NVIDIA GPU, PowerShell automation and Linux scripting. A lab where technical passion meets professional method.',
      pill1: 'PC Builds',
      pill2: 'Local AI',
      pill3: 'Multi‑OS',
      pill4: 'Scripting',
      cta: 'Explore the Tech Lab →'
    },
    hospitality: {
      label: 'Global Experiences & Passion for the Art of Service',
      title: 'From Abroad to Mixology',
      subtitle: '10+ years in hotels, bars and international tourism — UK, South Africa and Italy.',
      homeHeadline: 'My Story in the World of Hospitality',
      homeDesc: 'From commis de rang in Sicily to bartender at the Royal Shakespeare Company in the UK, through 5-star resorts and South Africa. AIBES training, mixology, sommelier and HACCP — a journey that forged discipline, calm and attention to detail.',
      stat1: 'years',
      stat2: 'continents',
      stat3: 'barman',
      cta: 'Read the full story →'
    },
    newsHub: {
      filterAll: 'All',
      filterX: 'From X',
      filterTrend: 'Trends',
      filterTips: 'Tips',
      filterSite: 'From site',
      items: 'stories',
      exportAll: 'Export feed',
      exportTitle: 'News Feed — The Little Satoshi News',
      noItems: 'No stories for this filter.',
      error: 'Could not load the news feed.',
      plusSite: '+ site'
    },
    btcNews: {
      label: 'News Session',
      title: 'Bitcoin News Session',
      desc: 'Live news from @BitcoinMagazine, @Strategy and @CPOfficialtx — ready to read or repost.',
      homeTitle: 'News right now',
      homeDesc: 'All aggregated news: X, crypto trends and site updates.',
      filterAll: 'All',
      openOnX: 'Open on X',
      noItems: 'No news for this filter.',
      homeLink: 'All news →',
      items: 'stories',
      updated: 'Updated',
      exportAll: 'Export all news',
      shareX: 'Share on X',
      readMore: 'Read →',
      readArticle: 'Read article',
      repost: 'Repost',
      copied: 'Copied!',
      exportedAll: 'Session exported!',
      exported: 'Exported',
      source: 'Source',
      copyPrompt: 'Copy the news text:',
      error: 'Could not load Bitcoin news.',
      breaking: 'Featured',
      guidesLabel: 'Guides',
      guidesTitle: 'All Bitcoin guides',
      categories: {
        guide: 'Guide', tip: 'Tip', trend: 'Trend', tutorial: 'Tutorial',
        cardano: 'Cardano', sicurezza: 'Security', bitcoin: 'Bitcoin'
      }
    },
    trust: ['100% educational', 'Security first', 'Step by step', 'Zero hype'],
    categories: {
      principianti: 'Beginners', sicurezza: 'Security',
      bitcoin: 'Bitcoin', ethereum: 'Ethereum', 'smart-contract': 'Smart Contract',
      cardano: 'Cardano', defi: 'DeFi & Staking', trend: 'Trends', strumenti: 'Tools'
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
      tips: { title: 'Crypto Tips', desc: 'Short, practical tips you can apply right away. No fluff — just concrete actions.' },
      trend: { title: 'Crypto Trends Right Now', desc: 'The macro trends shaping the crypto world, explained without hype.' },
      news: { title: 'News', desc: 'All news in one place: X feeds, crypto trends and The Little Satoshi News updates.' },
      sicurezza: { title: 'Security & Wallet Protection', desc: 'Protect your crypto. Guides on seed phrases, hardware wallets, phishing and best practices.', goldenRule: 'Golden rule', goldenText: 'No legitimate service will ever ask for your seed phrase. Not even "technical support".' },
      bitcoin: { title: 'Bitcoin', desc: 'Guides on BTC, buying, wallets, Lightning Network, halving and Bitcoin culture — explained simply.' },
      ethereum: { title: 'Ethereum', desc: 'Guides on ETH, staking, gas fees, wallets, Layer 2 and DeFi — without jargon.' },
      'smart-contract': { title: 'Smart Contracts', desc: 'Smart contracts explained clearly: verification, approvals, basic Solidity and DeFi security.' },
      cardano: { title: 'Cardano Ecosystem', desc: 'Guides dedicated to ADA, staking, Cardano wallets, DeFi, governance and scalability.' },
      strumenti: { title: 'Crypto Tools', desc: 'Guides and comparisons of wallets, exchanges, hardware wallets and monitoring tools.', toolsSection: 'Recommended tools' }
    },
    pages: {
      about: {
        metaTitle: 'About us — The Little Satoshi News',
        metaDesc: 'About us: The Little Satoshi News is the educational portal that explains the crypto world simply and practically.',
        label: 'About us', badge: 'Teacher', alt: 'Stefano — Professional crypto teacher',
        role: 'Professional crypto teacher · Founder of The Little Satoshi News',
        quote: '"I walk you through crypto step by step — with simple words, practical examples and zero hype. My goal is for you to truly understand, not buy blindly."',
        mission: 'Our mission', mission1: 'was born with a simple goal: make the crypto world accessible to everyone, without hype or unnecessary complications.',
        mission2: 'Inspired by Aranzulla\'s clear, practical style, our portal offers step-by-step guides, short tips and macro trend explanations — all in language anyone can understand.',
        mission3: 'Educate, not sell. Every piece of content on The Little Satoshi News has one purpose: help you understand and use cryptocurrencies safely.',
        find: 'What you\'ll find', find1: 'Step-by-step guides for beginners and advanced users',
        find2: 'Short, immediately applicable Crypto Tips', find3: 'Macro trend explanations without sensationalism',
        find4: 'Section dedicated to the Cardano ecosystem', find5: 'In-depth guides on security and wallet protection',
        find6: 'Glossary with all crypto terms', approach: 'Our approach', principles: 'Our principles',
        principlesText: 'Simplicity · Practicality · Security · Zero hype · 100% educational',
        contact: 'Questions or suggestions?', contactLink: 'Contact us'
      },
      contacts: {
        metaTitle: 'Contact — The Little Satoshi News', metaDesc: 'Contact the The Little Satoshi News team for questions, suggestions or collaborations.',
        title: 'Contact', intro: 'Have a question, a suggestion for a new guide, or want to collaborate? Write to us!',
        name: 'Name', email: 'Email', message: 'Message', submit: 'Send message',
        or: 'Or email us at', thanks: 'Thanks for your message! We\'ll get back to you soon.'
      },
      newsletter: {
        metaTitle: 'Newsletter — The Little Satoshi News',
        metaDesc: 'Subscribe to the The Little Satoshi News newsletter: 1 security tip per week + free Crypto Security Checklist.',
        title: 'The Little Satoshi News Newsletter', intro: 'Subscribe free and receive:',
        item1: '1 security tip per week', item2: 'New step-by-step guides',
        item3: 'Crypto Security Checklist (PDF) as a gift',
        thanks: 'Thanks! You\'re subscribed to the The Little Satoshi News newsletter. Check your email.'
      },
      search: {
        metaTitle: 'Search — The Little Satoshi News', metaDesc: 'Search guides, tips and crypto terms on The Little Satoshi News.',
        title: 'Search The Little Satoshi News', desc: 'Find guides, tips, trends and glossary terms.',
        noResults: 'No results for', tryOther: 'Try other terms.'
      },
      glossary: {
        metaTitle: 'Crypto Glossary — The Little Satoshi News',
        metaDesc: 'Crypto glossary A-Z: all cryptocurrency terms explained simply.',
        title: 'Crypto Glossary', desc: 'All crypto terms explained in plain language. From A to Z.',
        all: 'All', glossaryLabel: 'glossary'
      },
      social: {
        metaTitle: 'Social — The Little Satoshi News',
        metaDesc: 'Follow The Little Satoshi News on X, Facebook, Instagram, TikTok and YouTube. Simple crypto guides every day.',
        title: 'Follow us on social',
        desc: 'Tips, short guides and crypto updates. Pick your favourite platform.',
        follow: 'Follow us', cta: 'Go to profile →',
        x: { desc: 'Fast news, crypto analysis and real-time updates.' },
        facebook: { desc: 'Short guides, updates and an Italian crypto community.' },
        instagram: { desc: 'Visual tips, educational carousels and security stories.' },
        tiktok: { desc: 'Short videos: crypto explained in 60 seconds, zero hype.' },
        youtube: { desc: 'Step-by-step tutorials and in-depth video guides.' }
      },
      article: {
        metaTitle: 'Article — The Little Satoshi News', metaDesc: 'Crypto guide on The Little Satoshi News',
        related: 'Related guides', nlTitle: 'Don\'t miss the next updates',
        nlDesc: 'Get security tips and new guides straight to your inbox.',
        toc: 'Contents', faq: 'Frequently asked questions', readMin: 'min read', updated: 'Updated'
      },
      privacy: {
        metaTitle: 'Privacy Policy — The Little Satoshi News', title: 'Privacy Policy', updated: 'Last updated: June 2026',
        intro: 'The Little Satoshi News respects your privacy. This policy describes how we collect and use personal data.',
        dataTitle: 'Data collected', data: 'We only collect data you voluntarily provide: email address (newsletter), name and message (contact form), and anonymous browsing data via analytics cookies.',
        useTitle: 'Use of data', use: 'Data is used exclusively to send the newsletter, respond to contact requests and improve the site.',
        rightsTitle: 'Your rights', rights: 'You have the right to access, rectify, delete and object to processing of your data. Contact us at info@cryptofacile.com.'
      },
      disclaimer: {
        metaTitle: 'Disclaimer — The Little Satoshi News', title: 'Disclaimer', warning: 'Important notice',
        warningText: 'The Little Satoshi News content is provided for educational and informational purposes only. It does not constitute financial, tax or legal advice.',
        risksTitle: 'Risks', risks: 'Investing in cryptocurrencies involves significant risks, including the possibility of losing your entire invested capital. Crypto prices are highly volatile.',
        affTitle: 'Affiliations', aff: 'Some links on the site are affiliate links. This means we may receive a commission if you purchase a product through our links, at no extra cost to you. This does not influence our editorial reviews.',
        accuracyTitle: 'Accuracy', accuracy: 'We strive to keep content updated and accurate, but the crypto world evolves rapidly. Always verify information with official sources before making decisions.'
      },
      cookie: {
        metaTitle: 'Cookie Policy — The Little Satoshi News', title: 'Cookie Policy', updated: 'Last updated: June 2026',
        intro: 'The Little Satoshi News uses technical cookies necessary for site operation and analytics cookies to understand how visitors use the portal.',
        typesTitle: 'Types of cookies', tech: 'Technical cookies', techDesc: 'necessary for navigation and site operation',
        analytics: 'Analytics cookies', analyticsDesc: 'collect anonymous data on site usage',
        manageTitle: 'Cookie management', manage: 'You can disable cookies in your browser settings. Disabling technical cookies may limit some site features.'
      }
    },
    meta: {
      homeTitle: 'The Little Satoshi News — News and crypto, easy and simple',
      homeDesc: 'Crypto news and guides explained the easy and simple way. Bitcoin, wallets, DeFi and security without hype.',
      guideTitle: 'Crypto Guides — The Little Satoshi News',
      guideDesc: 'Step-by-step crypto guides for beginners and advanced users. Learn Bitcoin, wallets, DeFi, staking and more on The Little Satoshi News.',
      tipsTitle: 'Crypto Tips — The Little Satoshi News', tipsDesc: 'Short, practical tips about the crypto world.',
      trendTitle: 'Crypto Trends — The Little Satoshi News', trendDesc: 'Macro crypto trends explained simply.',
      sicurezzaTitle: 'Crypto Security — The Little Satoshi News',
      sicurezzaDesc: 'Crypto security guides: seed phrase, hardware wallet, phishing, backup and portfolio protection.',
      cardanoTitle: 'Cardano — The Little Satoshi News',
      cardanoDesc: 'Everything about the Cardano ecosystem: ADA, staking, wallets, DeFi, Catalyst and Hydra explained simply.',
      strumentiTitle: 'Crypto Tools — The Little Satoshi News',
      strumentiDesc: 'Comparisons and guides on wallets, exchanges, trackers and recommended crypto tools.'
    },
    articleGeneric: {
      introSuffix: 'This article is part of the {cat} section on The Little Satoshi News. We\'re updating the full content — in the meantime, here\'s a useful overview.',
      overview: 'Overview', overview2: 'In this guide we\'ll cover everything you need to explore the topic practically and safely, without hype and with concrete examples.',
      steps: 'Main steps', step1t: 'Step 1 — Preparation', step1d: 'Gather the necessary information and make sure you understand the basic risks before proceeding.',
      step2t: 'Step 2 — Execution', step2d: 'Follow the instructions step by step, verifying each operation before confirming.',
      step3t: 'Step 3 — Verification', step3d: 'Check that everything went well and keep a record of the operation.',
      warning: 'Warning', warningText: 'This content is for educational purposes. It does not constitute financial advice. Investing in crypto involves risks.',
      tips: 'Practical tips', tip1: 'Always start with small amounts to practice', tip2: 'Verify official sources before every operation',
      tip3: 'Never share seed phrases or private keys', tip4: 'Track every operation for tax reporting',
      faq1q: 'Is this article suitable for beginners?', faq1a: 'Yes, The Little Satoshi News is designed for those new to crypto. If a term isn\'t clear, check our glossary.',
      faq2q: 'When will the full content be updated?', faq2a: 'We\'re publishing complete guides progressively. Subscribe to the newsletter for updates.',
      catGuide: 'Step-by-step guide', catTip: 'Crypto Tip', catTrend: 'Crypto trend', catTutorial: 'Tutorial', catCardano: 'Cardano', catSicurezza: 'Security'
    },
    messages: { noArticles: 'No articles in this category.', bonus: 'BONUS' }
  }
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
  if (getLang() !== 'en' || !article) return article;
  return {
    ...article,
    title: article.titleEn || article.title,
    excerpt: article.excerptEn || article.excerpt,
    date: article.dateEn || article.date
  };
}

function localizeGlossary(entry) {
  if (getLang() !== 'en' || !entry) return entry;
  return { ...entry, definition: entry.definitionEn || entry.definition };
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
  document.querySelectorAll('[data-i18n-alt]').forEach(el => {
    el.alt = t(el.dataset.i18nAlt);
  });
  document.querySelectorAll('[data-i18n-href]').forEach(el => {
    const hrefKey = el.dataset.i18nHref;
    if (hrefKey.startsWith('mailto:') || hrefKey.startsWith('http')) el.href = hrefKey;
    else el.href = (typeof getBasePath === 'function' ? getBasePath() : '') + hrefKey;
  });
  const titleKey = document.body.dataset.i18nTitle;
  if (titleKey) document.title = t(titleKey);
  const descKey = document.body.dataset.i18nDesc;
  if (descKey) {
    const meta = document.querySelector('meta[name="description"]');
    if (meta) meta.content = t(descKey);
  }
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