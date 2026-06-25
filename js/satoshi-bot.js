/**
 * Satoshi Bot — motore chat locale per il web
 * Funziona su GitHub Pages senza server. Con API attiva usa Steven AI.
 */
(function (global) {
  'use strict';

  const KNOWLEDGE = [
    {
      keys: ['bitcoin', 'btc', 'satoshi', 'cos\'è bitcoin', 'cosè bitcoin', 'che cos\'è bitcoin'],
      reply: 'Bitcoin è la prima criptovaluta decentralizzata: nessuna banca o governo la controlla. Funziona su una blockchain pubblica dove le transazioni sono verificate da migliaia di nodi.\n\nPunti chiave:\n• Massimo 21 milioni di BTC — scarsità programmata\n• Puoi inviarlo a chiunque, ovunque, 24/7\n• La chiave privata = proprietà dei tuoi bitcoin\n\nPer iniziare: apri un account su un exchange regolamentato (es. Kraken), compra una piccola somma e impara prima di investire di più.'
    },
    {
      keys: ['iniziare', 'principianti', 'da zero', 'come inizio', 'come cominciare', 'primo passo'],
      reply: 'Percorso consigliato per iniziare:\n\n1. Capire le basi (cos\'è blockchain)\n2. Aprire Revolut + account Kraken\n3. Comprare i primi 20€ di Bitcoin\n4. Creare un wallet personale\n5. Proteggere seed phrase e 2FA\n\nTutto spiegato passo-passo sul sito nella sezione Guide → Principianti.'
    },
    {
      keys: ['wallet', 'portafoglio', 'seed', 'seed phrase', 'chiave privata', 'hardware wallet', 'ledger'],
      reply: 'Il wallet è dove custodisci le tue crypto. Regole d\'oro:\n\n• Mai condividere la seed phrase (12-24 parole)\n• Nessuno legittimo te la chiederà mai\n• Per somme importanti: hardware wallet (Ledger, Trezor)\n• Attiva sempre 2FA su exchange e app\n• Fai backup offline della seed — mai su cloud o screenshot\n\nHot wallet = comodo ma online. Cold wallet = massima sicurezza offline.'
    },
    {
      keys: ['sicurezza', 'proteggere', 'truffa', 'scam', 'phishing', '2fa', 'autenticazione'],
      reply: 'Sicurezza crypto — checklist essenziale:\n\n✓ 2FA su tutti gli account (app, non SMS)\n✓ Seed phrase solo su carta, in luogo sicuro\n✓ Diffida di messaggi su Telegram/WhatsApp che promettono guadagni\n✓ Verifica sempre URL degli exchange (bookmark ufficiali)\n✓ Mai inviare crypto a "supporto tecnico"\n✓ Aggiorna wallet e app regolarmente\n\nSe qualcosa sembra troppo bello per essere vero, è una truffa.'
    },
    {
      keys: ['exchange', 'kraken', 'revolut', 'comprare', 'acquistare', 'bonifico', 'sepa'],
      reply: 'Per comprare crypto in Italia in modo sicuro:\n\n1. Revolut — conto per bonifici SEPA verso exchange\n2. Kraken — exchange regolamentato dal 2011, deposito SEPA gratis\n\nFlusso: Revolut → bonifico SEPA → Kraken → acquisto BTC/ETH\n\nInizia con piccole somme. Impara il processo prima di aumentare gli importi. Guida completa sul sito: "Iniziare con Revolut + Kraken".'
    },
    {
      keys: ['cardano', 'ada', 'midnight', 'staking ada', 'eternl'],
      reply: 'Cardano è una blockchain proof-of-stake fondata su ricerca accademica. ADA è la sua moneta nativa.\n\n• Staking: delega i tuoi ADA a un pool e ricevi ricompense (~3-4% annuo)\n• Non perdi il controllo dei token in staking\n• Wallet consigliato: Eternl\n• Midnight: nuova chain Cardano per privacy e smart contract\n\nTrovi guide dedicate nella sezione Cardano del sito.'
    },
    {
      keys: ['ethereum', 'eth', 'smart contract', 'defi', 'staking'],
      reply: 'Ethereum è la piattaforma principale per smart contract e DeFi.\n\n• ETH: moneta nativa per pagare le commissioni (gas)\n• DeFi: finanza decentralizzata (prestiti, swap, yield) — rischio elevato\n• Staking ETH: blocchi i token per validare la rete\n\nAttenzione: DeFi e staking hanno rischi (bug smart contract, impermanent loss). Impara prima di mettere capitali significativi.'
    },
    {
      keys: ['blockchain', 'blocchi', 'distributed ledger'],
      reply: 'La blockchain è un registro digitale distribuito: una catena di blocchi collegati tra loro, ognuno con un timestamp e le transazioni validate.\n\n• Decentralizzata: nessun punto unico di controllo\n• Immutabile: modificare un blocco richiede consenso di tutta la rete\n• Trasparente: tutte le transazioni sono pubbliche\n\nÈ la tecnologia dietro Bitcoin, Ethereum, Cardano e migliaia di altri progetti.'
    },
    {
      keys: ['nft', 'token', 'altcoin', 'shitcoin', 'meme coin'],
      reply: 'Token e altcoin:\n\n• Token: asset digitali su una blockchain esistente (es. ERC-20 su Ethereum)\n• Altcoin: qualsiasi crypto che non è Bitcoin\n• NFT: token non fungibili — proprietà digitale unica\n\nRegola pratica: capisci il progetto prima di comprare. La maggior parte degli altcoin non batte Bitcoin nel lungo periodo. Diffida di meme coin e hype sui social.'
    },
    {
      keys: ['trend', 'mica', 'regolamentazione', 'normativa', 'legge crypto'],
      reply: 'Trend e regolamentazione crypto in Europa:\n\n• MiCA (Markets in Crypto-Assets): nuova normativa UE per exchange e stablecoin\n• Le piattaforme regolamentate (Kraken, Coinbase) sono più sicure\n• Le stablecoin saranno soggette a requisiti più stringenti\n• KYC obbligatorio su exchange legali\n\nSegui la sezione Trend del sito per aggiornamenti spiegati in modo semplice.'
    },
    {
      keys: ['ciao', 'salve', 'buongiorno', 'buonasera', 'hey', 'hello', 'chi sei', 'presentati'],
      reply: 'Ciao! Sono Satoshi, l\'assistente AI di CryptoItaliaFacile — The Little Satoshi News.\n\nTi aiuto con domande su Bitcoin, sicurezza, wallet, exchange, Cardano, DeFi e Web3. Rispondo in italiano, con parole semplici e zero hype.\n\nChiedimi qualsiasi cosa, oppure prova uno dei suggerimenti qui sotto!'
    },
    {
      keys: ['grazie', 'perfetto', 'ok grazie', 'thanks'],
      reply: 'Prego! Se hai altre domande su crypto, sono qui. Buon stacking! 🟠'
    },
    {
      keys: [
        'avvio automato post', 'function9', 'funzione 9', 'auto post',
        'pubblicazione automatica', 'post automatici', 'automazione social',
        'pubblica automaticamente', 'scheduler post'
      ],
      reply: 'Avvio automato post (funzione 9) — pubblica su Instagram @krown.82 e Facebook ogni 30 minuti, dalle 07:00 alle 22:00 (ora di Roma), fino a 20 post+story al giorno per piattaforma.\n\nCome attivarlo:\n1. Apri CryptoItaliaFacile - Pubblica\n2. Scegli [9] Avvio automato post\n3. Il sistema configura cron WSL, GitHub Actions e la coda 14 giorni\n\nComandi utili:\n• [1] Pubblica ORA — pubblicazione immediata\n• [3] Stato coda — vedi pending/pubblicati\n• [6] Aggiorna token — quando il token Meta scade\n• [7] Reset circuit breaker — dopo errori API\n\nIl piano articoli è in data/publish-queue.json.'
    }
  ];

  const DEFAULT_REPLY = 'Ottima domanda! Posso aiutarti con:\n\n• Bitcoin e blockchain\n• Come iniziare con le crypto\n• Sicurezza e wallet\n• Exchange (Kraken, Revolut)\n• Cardano e staking\n• DeFi e trend\n\nRiformula la domanda con più dettagli, oppure esplora le guide su cryptoitaliafacile.com';

  function normalize(text) {
    return (text || '').toLowerCase()
      .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
      .replace(/[^\w\s']/g, ' ');
  }

  function scoreMatch(message, keys) {
    const norm = normalize(message);
    let best = 0;
    for (const key of keys) {
      const k = normalize(key);
      if (norm.includes(k)) best = Math.max(best, k.length + 10);
      const words = k.split(/\s+/).filter(Boolean);
      const hits = words.filter(w => w.length > 2 && norm.includes(w)).length;
      if (hits > 0) best = Math.max(best, hits * 4);
    }
    return best;
  }

  function findReply(message) {
    let best = null;
    let bestScore = 0;
    for (const entry of KNOWLEDGE) {
      const s = scoreMatch(message, entry.keys);
      if (s > bestScore) {
        bestScore = s;
        best = entry;
      }
    }
    return bestScore >= 4 ? best.reply : DEFAULT_REPLY;
  }

  /** Simula streaming per UX più naturale */
  async function streamReply(text, onToken, delayMs) {
    const delay = delayMs || 12;
    const words = text.split(/(\s+)/);
    let acc = '';
    for (const w of words) {
      acc += w;
      onToken(w);
      await new Promise(r => setTimeout(r, delay));
    }
    return acc;
  }

  global.SatoshiBot = {
    findReply,
    streamReply,
    isLocalMode: true
  };
})(typeof window !== 'undefined' ? window : global);