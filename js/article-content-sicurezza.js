const ARTICLE_CONTENT_SICUREZZA = {
  'seed-phrase-guida': {
    intro: 'La <strong>seed phrase</strong> (12 o 24 parole BIP39) è la chiave master del tuo wallet. Chi la possiede controlla i tuoi fondi. Questa guida spiega cos\'è, come viene generata e come conservarla senza errori fatali.',
    sections: [
      { id: 'cos-e-seed', title: 'Cos\'è la seed phrase', content: `
<p>Quando crei un wallet self-custody, il software genera una sequenza di parole in un ordine preciso. Da quella sequenza derivano tutte le chiavi private del portafoglio.</p>
<h3>Perché è così importante</h3>
<ul><li>È l'<strong>unico modo</strong> per recuperare il wallet se perdi telefono o computer</li><li>Non esiste "reset password" — senza seed, i fondi sono irrecuperabili</li><li>Chiunque legga la seed può svuotare il wallet</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'generazione', title: 'Come viene generata', content: `
<p>La generazione avviene <strong>sul tuo dispositivo</strong>, in un ambiente sicuro del wallet (Trust Wallet, MetaMask, Ledger, ecc.).</p>
<ol><li>Scegli "Crea nuovo wallet"</li><li>Il software genera entropia casuale e la converte in parole BIP39</li><li>Ti mostra le parole una sola volta — annotale subito</li><li>Verifica con il test di conferma del wallet</li></ol>
<div class="box box--danger"><span class="box-title">Mai</span>Generare o inserire la seed su siti web, moduli Google, chat Telegram o "supporto tecnico".</div>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'conservazione', title: 'Come conservarla correttamente', content: `
<p>Regola pratica: <strong>carta + metallo + luogo sicuro</strong>.</p>
<ul><li>Scrivi le parole su carta indelebile, senza abbreviazioni</li><li>Valuta una piastra in acciaio per resistere a fuoco e acqua</li><li>Crea almeno due copie in luoghi fisici diversi</li><li>Non numerare le copie in modo che sia ovvio che sono seed phrase</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'errori', title: 'Errori che costano caro', content: `
<ul><li>❌ Screenshot o foto della seed</li><li>❌ Salvataggio su cloud, email, Note, iCloud</li><li>❌ Digitare la seed su qualsiasi sito</li><li>❌ Condividere con familiari "per sicurezza" senza capire i rischi</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
    ],
    faq: [
      { q: 'Posso cambiare la seed phrase?', a: 'No. Per averne una nuova devi creare un nuovo wallet e trasferire i fondi.' },
      { q: '12 o 24 parole?', a: 'Entrambe sono valide. 24 parole offrono più entropia; 12 è lo standard più comune su mobile.' },
    ]
  },
  'hot-vs-cold-wallet': {
    intro: 'Hot wallet e cold wallet non sono la stessa cosa. Capire la differenza ti aiuta a usare lo strumento giusto per ogni somma e ogni operazione.',
    sections: [
      { id: 'differenza', title: 'La differenza in 30 secondi', content: `
<p><strong>Hot wallet</strong>: connesso a internet (app mobile, estensione browser). Comodo, veloce, più esposto.</p><p><strong>Cold wallet</strong>: chiavi offline (hardware wallet, paper wallet). Meno comodo, massima protezione per hodl.</p>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'quando-hot', title: 'Quando usare un hot wallet', content: `
<ul><li>Piccole somme per uso quotidiano</li><li>DeFi, NFT, operazioni frequenti</li><li>Test e apprendimento con importi minimi</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'quando-cold', title: 'Quando usare un cold wallet', content: `
<ul><li>Conservazione a lungo termine (Bitcoin, ETH, ADA)</li><li>Somme che non ti servono ogni giorno</li><li>Dopo aver accumulato su exchange — preleva verso cold</li></ul><div class="box box--tip"><span class="box-title">Regola pratica</span>Exchange per comprare. Hot per operare. Cold per conservare.</div>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'rischi', title: 'Rischi principali', content: `
<p>Hot: malware, phishing, approvazioni malevole. Cold: perdita fisica del device, seed non backuppata, acquisto device tampered.</p>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
    ],
    faq: [
      { q: 'Posso usare solo hot wallet?', a: 'Sì per iniziare, ma non per tutto il patrimonio. Diversifica quando le somme crescono.' },
      { q: 'Il cold wallet è difficile?', a: 'Ledger e Trezor sono pensati per principianti. Setup in 20-30 minuti.' },
    ]
  },
  'confronto-hardware-wallet': {
    intro: 'Ledger, Trezor e BitBox sono i tre hardware wallet più usati in Europa. Nessuno è "perfetto": la scelta dipende da budget, blockchain supportate e livello di privacy.',
    sections: [
      { id: 'panoramica', title: 'Perché un hardware wallet', content: `
<p>Un hardware wallet tiene le <strong>chiavi private offline</strong>. Anche se il PC è infetto, un attaccante non può firmare transazioni senza il dispositivo fisico e il PIN.</p><ul><li>Ideale per conservazione medio-lungo termine</li><li>Compatibile con MetaMask, Ledger Live, Trezor Suite</li><li>Acquista solo da sito ufficiale o rivenditore autorizzato</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'ledger', title: 'Ledger (Nano S Plus / Nano X)', content: `
<h3>Punti di forza</h3><ul><li>Supporto ampissimo di chain e token</li><li>App Ledger Live intuitiva</li><li>Nano X con Bluetooth (attenzione: più superficie d'attacco)</li></ul><h3>Attenzioni</h3><p>Storico leak dati clienti (email, indirizzi). Usa email dedicata e non cliccare link sospetti.</p>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'trezor', title: 'Trezor (Model One / Safe 3)', content: `
<h3>Punti di forza</h3><ul><li>Firmware open source</li><li>Trezor Suite pulita e trasparente</li><li>Ottimo per Bitcoin ed Ethereum</li></ul><h3>Attenzioni</h3><p>Model One non supporta alcune chain moderne. Verifica compatibilità prima dell'acquisto.</p>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'bitbox', title: 'BitBox (BitBox02)', content: `
<h3>Punti di forza</h3><ul><li>Produzione svizzera, focus privacy</li><li>Backup su microSD oltre alla seed</li><li>Interfaccia minimalista</li></ul><h3>Attenzioni</h3><p>Meno chain rispetto a Ledger. Ottimo se il tuo stack è BTC/ETH-centric.</p>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'scelta', title: 'Come scegliere', content: `
<ol><li>Elenca le crypto che detieni oggi e quelle previste</li><li>Confronta prezzo, display, connettività (USB-C, Bluetooth)</li><li>Verifica che il firmware sia aggiornabile</li><li>Ordina dal sito ufficiale — mai da marketplace sconosciuti</li></ol><div class="box box--warning"><span class="box-title">Attenzione</span>Device "già configurato" o con seed precompilata = truffa garantita.</div>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
    ],
    faq: [
      { q: 'Ledger o Trezor per principianti?', a: 'Entrambi vanno bene. Ledger ha più tutorial in italiano; Trezor punta su trasparenza open source.' },
      { q: 'Serve il modello più costoso?', a: 'No. Nano S Plus o Trezor Safe 3 bastano per la maggior parte degli utenti.' },
    ]
  },
  'difendersi-phishing': {
    intro: 'Il phishing è l\'attacco più comune nel mondo crypto. Non serve un hacker geniale: basta un link convincente e un momento di distrazione. Impara a riconoscerlo prima che sia tardi.',
    sections: [
      { id: 'cos-e', title: 'Cos\'è il phishing crypto', content: `
<p>Messaggi che imitano exchange, wallet, airdrop o "supporto tecnico" per rubare seed phrase, password o far firmare transazioni malevole.</p><h3>Canali frequenti</h3><ul><li>Email e SMS con link urgenti</li><li>Annunci Google/Facebook con URL simili</li><li>DM su Telegram, Discord, X</li><li>Siti clone di MetaMask, Ledger, Uniswap</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'segnali', title: 'Segnali di allarme', content: `
<ul><li>Urgenza: "Il tuo account verrà bloccato in 24 ore"</li><li>Richiesta di seed phrase o chiavi private</li><li>URL leggermente diversi (metamask.io vs metamask.com)</li><li>Promesse di raddoppio BTC o airdrop "esclusivi"</li><li>Assistenza non richiesta che ti contatta per primo</li></ul><div class="box box--danger"><span class="box-title">Regola d'oro</span>Nessuno legittimo ti chiederà mai la seed phrase. Nemmeno Ledger, MetaMask o Binance.</div>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'difesa', title: 'Come difendersi', content: `
<ol><li>Segna i siti ufficiali nei preferiti — non usare link da email</li><li>Verifica sempre l'URL carattere per carattere</li><li>Attiva 2FA con app authenticator (non SMS)</li><li>Usa un email dedicata per exchange e crypto</li><li>Controlla approvazioni token periodicamente</li></ol>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'cosa-fare', title: 'Se hai cliccato un link sospetto', content: `
<p><strong>Non inserire dati.</strong> Chiudi la pagina. Se hai digitato la seed: trasferisci subito i fondi su un nuovo wallet. Se hai collegato il wallet a un sito fake: revoca le approvazioni su revoke.cash o etherscan.io.</p>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
    ],
    faq: [
      { q: 'Come verifico se un sito è ufficiale?', a: 'Controlla il dominio esatto, certificato HTTPS, e confronta con i link dal sito ufficiale dell\'azienda su X o documentazione.' },
      { q: 'Il phishing colpisce solo i principianti?', a: 'No. Anche utenti esperti cadono in truffe sofisticate. La routine di verifica protegge tutti.' },
    ]
  },
  'approvazioni-smart-contract': {
    intro: 'Ogni volta che usi Uniswap, OpenSea o un protocollo DeFi, firmi <strong>approvazioni</strong> che permettono a uno smart contract di muovere i tuoi token. Capire cosa firmi è fondamentale per la sicurezza.',
    sections: [
      { id: 'cosa-sono', title: 'Cosa sono le approvazioni', content: `
<p>Un'approvazione (allowance) autorizza un contratto a prelevare un certo quantitativo di token dal tuo wallet senza chiedere ogni volta.</p><h3>Tipi</h3><ul><li><strong>Limitata</strong> — importo specifico (più sicura)</li><li><strong>Illimitata</strong> — accesso totale al token (rischiosa)</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'rischi', title: 'Rischi delle approvazioni aperte', content: `
<p>Se un contratto viene compromesso o era malevolo fin dall'inizio, può svuotare i token approvati — anche mesi dopo.</p><div class="box box--danger"><span class="box-title">Mai</span>Approva importi illimitati su protocolli che non conosci o non usi regolarmente.</div>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'verifica', title: 'Come verificare le approvazioni', content: `
<ol><li>Visita <strong>revoke.cash</strong> o Etherscan Token Approvals</li><li>Collega il wallet (solo su siti affidabili)</li><li>Controlla ogni rete: Ethereum, Polygon, BSC, Arbitrum</li><li>Revoca approvazioni vecchie o sospette</li></ol>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'buone-pratiche', title: 'Buone pratiche', content: `
<ul><li>Approva solo l'importo necessario per la singola operazione</li><li>Usa un wallet separato per DeFi sperimentale</li><li>Rivedi le approvazioni ogni 1-3 mesi</li><li>Prima di revocare, verifica fee di rete</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
    ],
    faq: [
      { q: 'Revocare un\'approvazione è pericoloso?', a: 'No, è una operazione standard. Costa solo la fee di rete della transazione di revoca.' },
      { q: 'Serve su tutte le chain?', a: 'Sì. Ogni rete ha approvazioni separate. Controlla Ethereum, L2 e sidechain dove hai operato.' },
    ]
  },
  'backup-wallet-321': {
    intro: 'La strategia <strong>3-2-1</strong> nasce nel mondo IT ma si applica perfettamente alle crypto: tre copie, due supporti, una off-site. È il minimo sindacale per non perdere tutto.',
    sections: [
      { id: 'strategia', title: 'La regola 3-2-1 spiegata', content: `
<ul><li><strong>3 copie</strong> della seed phrase o backup</li><li><strong>2 supporti diversi</strong> — es. carta + acciaio, o carta + microSD criptata</li><li><strong>1 copia off-site</strong> — luogo fisico diverso da casa (cassetta, parente fidato)</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'supporti', title: 'Supporti consigliati', content: `
<h3>Carta</h3><p>Economica, immediata. Usa penna indelebile, evita post-it.</p><h3>Metallo</h3><p>Piastre Cryptosteel, Billfodl: resistono a fuoco e allagamento.</p><h3>MicroSD (hardware wallet)</h3><p>BitBox supporta backup su scheda. Conserva la scheda come tesoro.</p>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'cosa-no', title: 'Cosa NON usare come backup', content: `
<ul><li>❌ Screenshot, foto, file digitali non criptati</li><li>❌ Cloud (iCloud, Google Drive, Dropbox)</li><li>❌ Email a te stesso</li><li>❌ Password manager per la seed (solo per password exchange)</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'test', title: 'Testa il backup', content: `
<p>Un backup non testato è un backup inutile. Una volta all'anno (o dopo ogni grande movimento):</p><ol><li>Recupera il wallet su un dispositivo pulito usando la seed</li><li>Verifica che gli indirizzi coincidano</li><li>Richiudi senza lasciare tracce sul device di test</li></ol>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
    ],
    faq: [
      { q: 'Tre copie non sono troppe?', a: 'No. Una può bruciare, una può bagnarsi, una può perdersi. La ridondanza è il punto.' },
      { q: 'Posso dare una copia a un familiare?', a: 'Solo se comprende che è come dare le chiavi di casa. Valuta passphrase aggiuntiva (BIP39 passphrase) per protezione extra.' },
    ]
  },
  'sicurezza-mobile': {
    intro: 'Il telefono è il wallet più usato dai principianti — e il più rubato, perso o infettato. Pochi accorgimenti riducono drasticamente il rischio.',
    sections: [
      { id: 'minaccia', title: 'Perché il mobile è a rischio', content: `
<ul><li>App malevole con permessi eccessivi</li><li>Telefono rubato o smarrito</li><li>Wi-Fi pubblico non sicuro</li><li>Backup cloud del telefono che include screenshot</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'protezione', title: 'Proteggi il dispositivo', content: `
<ol><li>PIN forte (6+ cifre) o passphrase — non solo impronta</li><li>Aggiornamenti OS sempre installati</li><li>Scarica wallet solo da App Store / Play Store ufficiale</li><li>Disattiva backup cloud per app wallet se possibile</li><li>Non fare jailbreak/root se usi wallet con fondi reali</li></ol>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'wallet-app', title: 'Configurazione wallet mobile', content: `
<ul><li>Attiva biometria <strong>oltre</strong> al PIN del wallet</li><li>Disattiva anteprima notifiche con importi</li><li>Non fare screenshot della seed — mai</li><li>Usa wallet con open source verificabile quando possibile</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'perso', title: 'Se perdi o ti rubano il telefono', content: `
<p>La seed phrase su carta ti salva. Installa il wallet su un nuovo device, importa la seed, verifica i fondi. Cambia password exchange e revoca sessioni attive.</p><div class="box box--warning"><span class="box-title">Senza seed</span>Se non hai backup della seed, i fondi sul telefono perso sono irrecuperabili.</div>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
    ],
    faq: [
      { q: 'Trust Wallet è sicuro?', a: 'È widely usato ma resta un hot wallet. Sicuro per piccole somme se segui le best practice. Per grandi importi usa hardware wallet.' },
      { q: 'Devo usare VPN?', a: 'Utile su Wi-Fi pubblico. A casa con rete affidabile è meno critico, ma non sostituisce buone abitudini.' },
    ]
  },
  'wallet-compromesso': {
    intro: 'Sospetti che qualcuno abbia accesso al tuo wallet? Ogni minuto conta. Segui questo piano d\'azione senza panico — ma senza perdere tempo.',
    sections: [
      { id: 'segnali', title: 'Segnali di compromissione', content: `
<ul><li>Transazioni che non hai autorizzato</li><li>Approvazioni sconosciute su revoke.cash</li><li>Login exchange da IP o paese insolito</li><li>Hai inserito la seed su un sito sospetto</li><li>Hai installato un'app o estensione non ufficiale</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'immediato', title: 'Azioni immediate (primi 15 minuti)', content: `
<ol><li><strong>Stop</strong> — non firmare altre transazioni</li><li>Se hai seed sicura altrove: crea <strong>nuovo wallet</strong> su device pulito</li><li>Trasferisci tutti i fondi al nuovo indirizzo con fee alte se serve velocità</li><li>Revoca tutte le approvazioni sul vecchio indirizzo</li></ol><div class="box box--danger"><span class="box-title">Priorità</span>Salvare i fondi prima di capire come è successo.</div>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'exchange', title: 'Se i fondi sono su exchange', content: `
<ol><li>Cambia password immediatamente</li><li>Revoca API key e sessioni attive</li><li>Attiva o verifica 2FA (authenticator, non SMS)</li><li>Contatta supporto ufficiale solo dal sito verificato</li><li>Preleva verso wallet self-custody se possibile</li></ol>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'dopo', title: 'Dopo l\'emergenza', content: `
<ul><li>Analizza come è avvenuta la compromissione</li><li>Sostituisci device o reinstalla OS se malware</li><li>Nuova seed phrase — non riutilizzare quella compromessa</li><li>Documenta per eventuale denuncia (polizia postale)</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
    ],
    faq: [
      { q: 'Posso recuperare fondi rubati?', a: 'Raramente. Le transazioni on-chain sono irreversibili. Agire in tempo è l\'unica difesa reale.' },
      { q: 'Devo denunciare?', a: 'Consigliato per truffe e phishing. Conserva hash transazioni, URL, screenshot.' },
    ]
  },
  'password-manager-crypto': {
    intro: 'Password manager e crypto vanno d\'accordo — ma con regole precise. Gestiscono le password degli exchange, non la seed phrase.',
    sections: [
      { id: 'perche', title: 'Perché usarne uno', content: `
<ul><li>Password uniche e lunghe per ogni exchange</li><li>Niente riutilizzo tra piattaforme</li><li>2FA backup codes archiviati in modo sicuro</li><li>Condivisione controllata in contesti familiari (vault)</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'scelta', title: 'Quale scegliere', content: `
<p>Opzioni affidabili: <strong>Bitwarden</strong> (open source), 1Password, KeePassXC (locale). Evita soluzioni sconosciute o "gratis" senza audit.</p><h3>Configurazione minima</h3><ol><li>Master password lunga (20+ caratteri) o passphrase</li><li>2FA sul vault stesso</li><li>Backup della chiave di recupero del PM in luogo fisico sicuro</li></ol>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'cosa-mettere', title: 'Cosa mettere nel password manager', content: `
<ul><li>✅ Login exchange, email crypto, API key label</li><li>✅ Backup codes 2FA</li><li>✅ Note su indirizzi wallet (pubblici) e PIN device</li><li>❌ Seed phrase — mai digitale</li><li>❌ Chiavi private raw</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'abitudini', title: 'Abitudini sicure', content: `
<p>Aggiorna password dopo breach noti. Non autocompletare su siti crypto da link email. Usa il PM solo su device che controlli.</p>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
    ],
    faq: [
      { q: 'Bitwarden è abbastanza sicuro?', a: 'Sì, con master password forte e 2FA. Il modello zero-knowledge protegge i dati anche se i server fossero compromessi.' },
      { q: 'Posso salvare la seed criptata nel PM?', a: 'Sconsigliato. Un errore di sync, malware o subpoena espone comunque un rischio inaccettabile.' },
    ]
  },
  'audit-sicurezza-portafoglio': {
    intro: 'Un audit di sicurezza non richiede competenze da hacker: è una checklist che verifichi dove custodisci crypto, come proteggi le chiavi e quali abitudini ti espongono al rischio.',
    sections: [
      { id: 'seed', title: 'Seed phrase e backup', content: `
<ul><li>□ Backup su carta/metallo, mai digitale</li><li>□ Almeno 2 copie in luoghi diversi</li><li>□ Test di recupero fatto negli ultimi 12 mesi</li><li>□ Nessuno oltre a te ha accesso non necessario</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'wallet-device', title: 'Wallet e dispositivi', content: `
<ul><li>□ Hot wallet solo per somme operative</li><li>□ Hardware wallet per conservazione principale</li><li>□ Firmware wallet aggiornato</li><li>□ PIN/biometria attivi su telefono e app</li><li>□ Nessuna app wallet da fonti non ufficiali</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'exchange', title: 'Exchange e account', content: `
<ul><li>□ 2FA authenticator (non SMS) su ogni exchange</li><li>□ Password uniche via password manager</li><li>□ Withdrawal whitelist attiva dove disponibile</li><li>□ Nessun fondo significativo lasciato su exchange a lungo</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'defi', title: 'DeFi e approvazioni', content: `
<ul><li>□ Approvazioni token riviste negli ultimi 3 mesi</li><li>□ Nessuna approvazione illimitata su protocolli inattivi</li><li>□ Wallet DeFi separato da wallet principale</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'abitudini', title: 'Abitudini e phishing', content: `
<ul><li>□ Siti ufficiali nei preferiti</li><li>□ Mai seed richiesta da "supporto"</li><li>□ Email dedicata per crypto</li><li>□ Sospetti segnalati e revoche fatte</li></ul><div class="box box--tip"><span class="box-title">Frequenza</span>Ripeti l'audit ogni 3-6 mesi o dopo ogni grande acquisto.</div>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
    ],
    faq: [
      { q: 'Quanto tempo richiede?', a: '30-45 minuti la prima volta, 15 minuti le volte successive.' },
      { q: 'Cosa fare se fallisco molti punti?', a: 'Priorità: seed backup, 2FA, spostare fondi da exchange a self-custody. Un punto alla volta.' },
    ]
  },
  'creare-wallet-sicuro': {
    intro: 'Un wallet è il posto dove conservi le tue crypto. Crearne uno sicuro richiede meno di 10 minuti, ma gli errori in questa fase possono costarti tutto.',
    sections: [
      { id: 'tipi-wallet', title: 'Hot wallet vs Cold wallet', content: `
<p>Ci sono due categorie principali:</p><ul><li><strong>Hot wallet</strong> — app o estensione browser, connessi a internet. Comodi per uso quotidiano.</li><li><strong>Cold wallet</strong> — dispositivo hardware offline. Massima sicurezza per conservazione a lungo termine.</li></ul><p>Per iniziare, un hot wallet va benissimo. Per somme importanti, considera un hardware wallet.</p>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'installazione', title: 'Passo 1: Installare il wallet', content: `
<p>Per principianti consigliamo <strong>Trust Wallet</strong> (mobile) o <strong>MetaMask</strong> (browser + mobile).</p><div class="step-block"><h3>Trust Wallet (smartphone)</h3><ol><li>Scarica solo dall'App Store o Google Play ufficiale</li><li>Apri l'app e seleziona "Crea nuovo wallet"</li><li>Imposta un PIN forte o attiva la biometria</li></ol></div><div class="box box--danger"><span class="box-title">Mai</span>Scaricare wallet da link ricevuti via email, Telegram o annunci. Solo store ufficiali.</div>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'seed-phrase', title: 'Passo 2: Salvare la seed phrase', content: `
<p>L'app ti mostrerà <strong>12 o 24 parole</strong> in un ordine preciso.</p><ol><li>Scrivile su <strong>carta</strong>, nell'ordine esatto</li><li>Verifica due volte ogni parola</li><li>Conservale in un posto sicuro</li><li>Fai una seconda copia in luogo diverso</li></ol><div class="box box--danger"><span class="box-title">Mai</span>Fotografare, screenshot, cloud, email o digitare la seed phrase.</div>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'verifica', title: 'Passo 3: Verificare il backup', content: `
<p>Il wallet ti chiederà di reinserire alcune parole per confermare il backup. Fallo con calma.</p>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'primo-uso', title: 'Passo 4: Primo utilizzo', content: `
<ul><li>Fai un <strong>test con pochi centesimi</strong></li><li>Verifica ricezione e invio</li><li>Controlla la transazione su block explorer</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
    ],
    faq: [
      { q: 'Cosa succede se perdo la seed phrase?', a: 'Perdi accesso permanente. Nessuno può recuperarle. La seed phrase È il tuo wallet.' },
      { q: 'Posso usare lo stesso wallet su più dispositivi?', a: 'Sì, importando la stessa seed. Ogni dispositivo in più è un rischio in più.' },
    ]
  },
  'proteggere-seed-phrase': {
    intro: 'La seed phrase è la chiave di tutto il tuo portafoglio crypto. Chi la possiede, possiede le tue crypto. Ecco come proteggerla correttamente.',
    sections: [
      { id: 'cosa-e', title: 'Cos\'è la seed phrase', content: `
<p>Sequenza di 12 o 24 parole BIP39 generata dal wallet. Ricrea le chiavi private e recupera l'accesso su qualsiasi device compatibile.</p>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'come-salvarla', title: 'Come salvarla correttamente', content: `
<p>Strategia <strong>3-2-1</strong>:</p><ul><li><strong>3 copie</strong></li><li><strong>2 supporti</strong> (carta + metallo)</li><li><strong>1 copia</strong> off-site</li></ul><div class="box box--tip"><span class="box-title">Consiglio</span>Piastre in acciaio resistono a fuoco e acqua meglio della carta.</div>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'errori', title: 'Errori da evitare', content: `
<ul><li>❌ Screenshot o foto</li><li>❌ Note digitali, email, cloud</li><li>❌ Condividere con "supporto tecnico"</li><li>❌ Digitare su siti web</li><li>❌ Una sola copia</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'emergenza', title: 'Cosa fare in emergenza', content: `
<p>Se sospetti compromissione:</p><ol><li>Crea <strong>nuovo wallet</strong></li><li>Trasferisci tutti i fondi</li><li>Non usare più il vecchio wallet</li></ol>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
    ],
    faq: [
      { q: 'Posso cambiare la seed phrase?', a: 'No. Per una nuova seed crea un nuovo wallet e trasferisci i fondi.' },
    ]
  },
  'hardware-wallet-ledger': {
    intro: 'Un Ledger Nano protegge le chiavi offline. Configurarlo correttamente al primo utilizzo è il passo più importante: la seed viene generata una sola volta.',
    sections: [
      { id: 'prima', title: 'Prima di iniziare', content: `
<ul><li>Ledger acquistato da ledger.com o rivenditore ufficiale</li><li>Cavo USB funzionante</li><li>PC pulito, senza estensioni sospette</li><li>Carta e penna per la seed — mai digitale</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'setup', title: 'Configurazione iniziale', content: `
<ol><li>Installa <strong>Ledger Live</strong> dal sito ufficiale</li><li>Collega il Nano e seleziona "Configura come nuovo dispositivo"</li><li>Scegli PIN (6-8 cifre, non data di nascita)</li><li>Annota le 24 parole nell'ordine mostrato sul device</li><li>Completa il test di verifica parole</li></ol><div class="box box--danger"><span class="box-title">Mai</span>Usare un Ledger con seed già fornita o "pre-configurato".</div>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'app', title: 'Installare app crypto', content: `
<p>In Ledger Live → Manager, installa le app per le chain che usi (Bitcoin, Ethereum, Cardano, ecc.). Ogni blockchain richiede la sua app sul device.</p>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'prima-tx', title: 'Prima transazione', content: `
<ol><li>Ricevi una piccola somma di test</li><li>Verifica indirizzo sul display del Ledger prima di condividere</li><li>Invia una piccola quantità per confermare invio</li><li>Collega a MetaMask se usi DeFi su Ethereum</li></ol>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'manutenzione', title: 'Manutenzione', content: `
<ul><li>Aggiorna firmware via Ledger Live regolarmente</li><li>Conserva seed su metallo oltre che carta</li><li>Non prestare il device</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
    ],
    faq: [
      { q: 'Nano S Plus o Nano X?', a: 'S Plus basta per USB desktop. Nano X se vuoi Bluetooth con mobile (valuta rischio extra).' },
      { q: 'Ledger è ancora sicuro dopo i leak?', a: 'Il device resta sicuro se seed non è compromessa. Usa email dedicata e diffida di phishing post-leak.' },
    ]
  },
  'cold-wallet-chiavi-offline': {
    intro: 'Un cold wallet con chiavi generate offline elimina il rischio che malware sul PC legga la seed durante la creazione. È un approccio avanzato ma accessibile con metodo e pazienza.',
    sections: [
      { id: 'perche-offline', title: 'Perché generare offline', content: `
<p>Su un PC connesso, malware può catturare schermo, clipboard o file durante la generazione. Un ambiente <strong>air-gapped</strong> (senza rete) riduce questa superficie a zero.</p>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'metodi', title: 'Metodi principali', content: `
<h3>Hardware wallet (consigliato)</h3><p>Ledger/Trezor generano seed nel chip sicuro. Il metodo più pratico per quasi tutti.</p><h3>Wallet su PC offline</h3><p>PC mai connesso + software come Electrum (BTC) o MyEtherWallet offline (ETH). Solo per utenti esperti.</p><h3>Paper wallet</h3><p>Chiave stampata su carta. Obsoleto per molti use case — sconsigliato ai principianti.</p>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'setup-offline', title: 'Setup air-gapped (avanzato)', content: `
<ol><li>Usa PC/live USB pulito mai connesso dopo download verificato</li><li>Verifica checksum del software (GPG, hash ufficiale)</li><li>Genera seed offline, scrivi su carta</li><li>Trasferisci solo indirizzi pubblici via QR su device secondo</li><li>Firma transazioni offline, broadcast da device online</li></ol>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
      { id: 'conservazione', title: 'Conservazione chiavi', content: `
<ul><li>Seed su carta + metallo, strategia 3-2-1</li><li>Mai fotografare chiavi private</li><li>Considera passphrase BIP39 aggiuntiva</li></ul><div class="box box--warning"><span class="box-title">Avanzato</span>Se non ti senti pronto, un hardware wallet standard è più che sufficiente.</div>
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>

      `},
    ],
    faq: [
      { q: 'Serve davvero l\'air-gap?', a: 'Per la maggior parte degli utenti no. Hardware wallet moderno offre sicurezza comparabile con meno complessità.' },
      { q: 'Paper wallet nel 2026?', a: 'Quasi sempre superato da hardware wallet. Evita salvo casi molto specifici.' },
    ]
  },

};
