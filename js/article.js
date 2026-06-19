const ARTICLE_CONTENT = {
  'iniziare-exchange-revolut-kraken': {
    intro: 'Vuoi comprare le tue prime crypto ma non sai da dove iniziare? In questa guida ti spiego cos\'è un exchange, perché Revolut ti semplifica la vita, come scegliere una piattaforma affidabile e come fare il tuo primo acquisto su Kraken — passo dopo passo, senza hype.',
    sections: [
      { id: 'cos-e-exchange', title: 'Cos\'è un exchange crypto', content: `
        <p>Un <strong>exchange crypto</strong> è una piattaforma dove puoi comprare, vendere e scambiare criptovalute usando euro o altre valute tradizionali.</p>
        <h3>CEX vs DEX</h3>
        <ul>
          <li><strong>CEX (Centralized Exchange)</strong> — exchange centralizzato come Kraken, Coinbase o Binance. Un'azienda gestisce la piattaforma, custodisce temporaneamente i fondi e offre supporto. Ideale per chi inizia.</li>
          <li><strong>DEX (Decentralized Exchange)</strong> — exchange decentralizzato come Uniswap. Scambi peer-to-peer tramite smart contract, senza intermediario. Più avanzato.</li>
        </ul>
        <h3>Perché un principiante parte da un CEX</h3>
        <ul>
          <li>Interfaccia semplice e in italiano (su molti exchange)</li>
          <li>Deposito in euro con bonifico o carta</li>
          <li>Supporto clienti in caso di problemi</li>
          <li>Verifica identità (KYC) che offre un minimo di protezione normativa</li>
        </ul>
        <p><strong>Vantaggi:</strong> facilità, liquidità, metodi di pagamento familiari.</p>
        <p><strong>Limiti:</strong> non controlli direttamente le chiavi private; devi fidarti della piattaforma per i fondi depositati.</p>
        <div class="box box--tip"><span class="box-title">Regola d'oro</span>L'exchange serve per comprare e vendere. Per conservare crypto a lungo termine, trasferiscile su un wallet personale.</div>
      `},
      { id: 'perche-revolut', title: 'Perché serve un conto Revolut per iniziare', content: `
        <p>Non è obbligatorio, ma <strong>Revolut</strong> è uno degli strumenti più pratici per chi inizia con le crypto in Europa. Ecco perché.</p>
        <h3>Perché è utile</h3>
        <ul>
          <li><strong>Bonifici SEPA velocissimi</strong> verso exchange come Kraken (di solito 1 giorno lavorativo)</li>
          <li><strong>Conto multivaluta</strong> — euro, dollari e altre valute in un'unica app</li>
          <li><strong>Carta virtuale</strong> — utile per depositi con carta su alcuni exchange</li>
          <li><strong>App mobile intuitiva</strong> — tutto gestibile dal telefono</li>
        </ul>
        <h3>Perché è considerato sicuro</h3>
        <ul>
          <li>Regolamentato e con licenze bancarie/e-money in diversi Paesi UE</li>
          <li>Verifica identità obbligatoria (KYC)</li>
          <li>Protezioni standard per conti digitali europei</li>
          <li>Autenticazione a due fattori disponibile</li>
        </ul>
        <h3>Il problema delle banche tradizionali</h3>
        <p>Alcune banche italiane classici bloccano o rallentano bonifici verso exchange crypto. Revolut, essendo fintech nativa digitale, di solito non presenta questo problema — i bonifici SEPA verso Kraken arrivano senza intoppi.</p>
        <h3>Come aprire un conto Revolut</h3>
        <p>Puoi registrarti gratuitamente tramite link di invito. L'apertura del conto base è gratis e non ci sono costi obbligatori per iniziare. Revolut offre periodicamente bonus o cashback ai nuovi utenti — le promozioni variano nel tempo.</p>
        <p><strong>Link per aprire Revolut:</strong><br>
        <a href="https://revolut.com/referral/?referral-code=stefan2ayd!JUN1-26-AR&geo-redirect" target="_blank" rel="noopener noreferrer">revolut.com/referral — registrazione gratuita</a></p>
        <div class="box box--warning"><span class="box-title">Trasparenza</span>Questo è un link referral: se ti registri tramite questo link, potremmo ricevere un piccolo beneficio senza costi aggiuntivi per te. Lo includiamo perché lo usiamo realmente e lo riteniamo utile per chi inizia.</div>
      `},
      { id: 'scegliere-exchange', title: 'Come scegliere un exchange affidabile', content: `
        <p>Prima di depositare soldi, controlla questi criteri:</p>
        <ul>
          <li><strong>Sicurezza</strong> — 2FA obbligatorio, storico senza hack gravi, cold storage dei fondi</li>
          <li><strong>Licenze</strong> — regolamentato in UE o USA (MiCA in Europa)</li>
          <li><strong>Reputazione</strong> — anni di attività, recensioni, volume di scambi</li>
          <li><strong>Commissioni</strong> — spread, fee di deposito/prelievo, fee di trading</li>
          <li><strong>Facilità d'uso</strong> — interfaccia chiara per principianti</li>
          <li><strong>Metodi di deposito</strong> — bonifico SEPA (ideale con Revolut), carta, crypto</li>
        </ul>
        <p><strong>Kraken</strong> soddisfa questi criteri: è regolamentato, attivo dal 2011, con fee competitive e deposito SEPA gratuito. Per questo lo usiamo come esempio in questa guida.</p>
      `},
      { id: 'registrazione-exchange', title: 'Come registrarsi su un exchange', content: `
        <div class="step-block"><h3>Passo 1 — Crea l'account</h3>
        <p>Vai sul sito ufficiale dell'exchange (mai da link in email o Telegram). Inserisci email e crea una <strong>password unica e forte</strong> — non riutilizzare password di altri siti.</p></div>
        <div class="step-block"><h3>Passo 2 — Verifica email</h3>
        <p>Clicca il link di conferma che ricevi via email. Se non arriva, controlla lo spam.</p></div>
        <div class="step-block"><h3>Passo 3 — KYC (verifica identità)</h3>
        <p>Carica foto del documento d'identità e un selfie. È obbligatorio per legge su exchange regolamentati. I tempi vanno da pochi minuti a 24 ore.</p></div>
        <div class="step-block"><h3>Passo 4 — Attiva il 2FA</h3>
        <p>Subito dopo la registrazione, attiva l'<strong>autenticazione a due fattori</strong> con Google Authenticator o Authy. <strong>Mai via SMS</strong> se puoi evitarlo.</p></div>
        <div class="box box--danger"><span class="box-title">Attenzione</span>Verifica sempre l'URL: per Kraken è <strong>kraken.com</strong>. Il phishing è il metodo di truffa più comune.</div>
      `},
      { id: 'deposito-prelievo', title: 'Come depositare e prelevare', content: `
        <h3>Deposito con bonifico SEPA (consigliato)</h3>
        <ol>
          <li>Nell'exchange, vai su "Deposita" → "Euro" → "Bonifico SEPA"</li>
          <li>Copia IBAN e causale indicati</li>
          <li>Da Revolut, fai un bonifico con quei dati esatti</li>
          <li>Attendi 1-2 giorni lavorativi (a volte poche ore)</li>
        </ol>
        <h3>Deposito con carta</h3>
        <p>Più veloce ma con fee più alte (1,5-3%). Usa la carta virtuale Revolut se l'exchange la accetta.</p>
        <h3>Deposito crypto</h3>
        <p>Se hai già crypto altrove, puoi inviarle all'exchange. <strong>Controlla sempre la rete</strong> (BTC su Bitcoin, ETH su Ethereum, ecc.).</p>
        <h3>Reti diverse — errori da evitare</h3>
        <ul>
          <li>BTC → rete Bitcoin (BTC)</li>
          <li>ETH → rete Ethereum (ERC-20)</li>
          <li>USDT può essere ERC-20, TRC-20 o altro — devi scegliere la stessa rete su invio e ricezione</li>
        </ul>
        <div class="box box--warning"><span class="box-title">Errore comune</span>Inviare crypto sulla rete sbagliata può causare perdita permanente dei fondi. Controlla tre volte prima di confermare.</div>
      `},
      { id: 'affiliazione-kraken', title: 'Programma referral Kraken', content: `
        <p>Molti exchange, incluso Kraken, hanno un <strong>programma referral</strong>: se ti registri tramite il link di un utente esistente, entrambi potete ricevere vantaggi (bonus, sconti sulle fee) quando si verificano determinate condizioni.</p>
        <h3>Come funziona</h3>
        <ol>
          <li>Ti registri tramite il link referral</li>
          <li>Completi la verifica KYC</li>
          <li>Effettui il primo acquisto o raggiungi una soglia minima</li>
          <li>Eventuali bonus vengono accreditati secondo le promozioni attive</li>
        </ol>
        <p><strong>Link referral Kraken:</strong><br>
        <a href="https://invite.kraken.com/JDNW/pql7tac5" target="_blank" rel="noopener noreferrer">invite.kraken.com — registrazione Kraken</a></p>
        <p><strong>Codice affiliazione:</strong> <code>3h8q8cf5</code></p>
        <div class="box box--warning"><span class="box-title">Trasparenza</span>È un link referral. Potremmo ricevere una commissione se ti registri e operi, senza costi extra per te. Le promozioni bonus dipendono dalle campagne attive di Kraken e possono cambiare.</div>
      `},
      { id: 'primo-acquisto-kraken', title: 'Come fare il primo acquisto su Kraken', content: `
        <div class="step-block"><h3>1. Deposita euro</h3>
        <p>Bonifico SEPA da Revolut (consigliato) o carta. Attendi che i fondi appaiano nel saldo EUR.</p></div>
        <div class="step-block"><h3>2. Vai su "Compra crypto"</h3>
        <p>Seleziona Bitcoin (BTC) o un'altra crypto. Per iniziare, BTC o ETH sono le scelte più comuni.</p></div>
        <div class="step-block"><h3>3. Inserisci l'importo</h3>
        <p>Scrivi quanti euro vuoi spendere (es. 50€). Controlla il <strong>costo totale</strong> comprensivo di spread e fee.</p></div>
        <div class="step-block"><h3>4. Conferma l'ordine</h3>
        <p>Rivedi il riepilogo e conferma. Le crypto appariranno nel tuo saldo Kraken.</p></div>
        <div class="step-block"><h3>5. Preleva verso wallet personale (opzionale)</h3>
        <p>Per somme che vuoi conservare a lungo termine: vai su "Preleva", inserisci l'indirizzo del tuo wallet personale, seleziona la rete corretta e conferma. Fai un test con pochi euro prima.</p></div>
        <div class="box box--tip"><span class="box-title">Consiglio</span>Inizia con 20-50€ per fare pratica. Meglio sbagliare con poco che con molto.</div>
      `},
      { id: 'sicurezza-principianti', title: 'Consigli di sicurezza per principianti', content: `
        <ul>
          <li>❌ <strong>Non lasciare grandi somme sull'exchange</strong> — l'exchange è per tradare, non per conservare</li>
          <li>✅ <strong>Attiva sempre il 2FA</strong> — con app dedicata, non SMS</li>
          <li>❌ <strong>Non condividere mai la seed phrase</strong> — nemmeno con il "supporto"</li>
          <li>❌ <strong>Non cliccare link sospetti</strong> — vai sempre direttamente al sito digitando l'URL</li>
          <li>✅ <strong>Controlla la rete</strong> prima di ogni invio crypto</li>
          <li>✅ <strong>Usa email dedicata</strong> per exchange e crypto</li>
          <li>✅ <strong>Tieni traccia delle operazioni</strong> per la dichiarazione fiscale</li>
        </ul>
      `},
      { id: 'conclusione', title: 'Conclusione', content: `
        <p>Ricapitolando il percorso per iniziare:</p>
        <ol>
          <li><strong>Apri Revolut</strong> — per bonifici SEPA veloci verso gli exchange</li>
          <li><strong>Registrati su Kraken</strong> — exchange regolamentato e adatto ai principianti</li>
          <li><strong>Deposita euro</strong> — bonifico da Revolut (fee basse o gratuite)</li>
          <li><strong>Compra le prime crypto</strong> — inizia con poco</li>
          <li><strong>Trasferisci su wallet personale</strong> — quando sei pronto per conservare a lungo termine</li>
        </ol>
        <p>I link referral (Revolut e Kraken) possono offrirti vantaggi all'iscrizione senza costi aggiuntivi. In futuro, quando ti sentirai sicuro, potrai esplorare wallet personali, Lightning Network e DeFi.</p>
        <div class="box box--tip"><span class="box-title">Prossimi passi su The Little Satoshi News</span>
          <ul>
            <li><a href="articolo.html?slug=comprare-bitcoin-prima-volta">Come comprare Bitcoin per la prima volta</a></li>
            <li><a href="articolo.html?slug=creare-wallet-sicuro">Come creare un wallet sicuro</a></li>
            <li><a href="articolo.html?slug=proteggere-seed-phrase">Come proteggere la seed phrase</a></li>
          </ul>
        </div>
      `}
    ],
    faq: [
      { q: 'Revolut è obbligatorio per comprare crypto?', a: 'No. Puoi usare qualsiasi banca che accetti bonifici SEPA verso exchange crypto. Revolut è solo una delle opzioni più comode e veloci, specialmente se la tua banca tradizionale blocca questi bonifici.' },
      { q: 'Kraken è sicuro?', a: 'Kraken è uno degli exchange più longevi (dal 2011), regolamentato e con buona reputazione. Nessuna piattaforma è immune al rischio, ma Kraken è considerato affidabile nel settore.' },
      { q: 'I link referral costano qualcosa?', a: 'No, per te non cambia nulla in termini di costi. Il referral premia chi invita e a volte offre bonus al nuovo utente, secondo le promozioni attive.' },
      { q: 'Quanto devo investire la prima volta?', a: 'Anche 20-50€ bastano per imparare. L\'obiettivo del primo acquisto è capire il processo, non investire tanto.' },
      { q: 'Posso usare solo Revolut per le crypto?', a: 'Revolut offre anche acquisto crypto integrato, ma fee e controllo sono diversi da un exchange dedicato. Per imparare e avere più scelta, un exchange come Kraken è generalmente preferibile.' }
    ]
  },

  'lightning-network-guida': {
    intro: 'Bitcoin è fantastico, ma per un caffè da 2€ pagare 1€ di commissione on-chain non ha senso. Ecco entra in gioco il Lightning Network: pagamenti istantanei in satoshi (sats), con costi quasi zero. In questa guida ti spiego tutto in modo semplice — inclusi i wallet Lightning e come usare Satoshi Wallet con la sua mappa dei commercianti.',
    sections: [
      { id: 'cos-e-lightning', title: 'Cos\'è il Lightning Network', content: `
        <p>Il <strong>Lightning Network</strong> (LN) è una rete di pagamento costruita <em>sopra</em> Bitcoin. Non sostituisce Bitcoin: lo usa come base di sicurezza, ma permette di spostare piccole somme in modo velocissimo.</p>
        <p><strong>Perché esiste?</strong> La blockchain di Bitcoin può processare un numero limitato di transazioni al secondo. Ogni transazione on-chain (sulla blockchain principale) richiede una conferma dai miner e paga una fee. Per pagamenti piccoli e frequenti — un caffè, una mancia, un servizio online — questo è lento e costoso.</p>
        <h3>Bitcoin on-chain vs Lightning</h3>
        <ul>
          <li><strong>On-chain</strong> — transazione registrata sulla blockchain; sicura, ma lenta (minuti/ore) e con fee variabili</li>
          <li><strong>Lightning</strong> — pagamento fuori catena tramite canali; istantaneo e con fee di frazioni di centesimo</li>
        </ul>
        <p><strong>Vantaggi principali:</strong></p>
        <ul>
          <li>⚡ <strong>Velocità</strong> — pagamenti in meno di un secondo</li>
          <li>💸 <strong>Costi bassissimi</strong> — spesso meno di 0,01€</li>
          <li>🪙 <strong>Micro-pagamenti</strong> — puoi inviare anche solo 10 sats (frazioni di centesimo)</li>
        </ul>
        <div class="box box--tip"><span class="box-title">In parole semplici</span>Se Bitcoin on-chain è come un bonifico bancario, Lightning è come pagare con il telefono al bar: immediato e pratico.</div>
      `},
      { id: 'cosa-sono-sats', title: 'Cosa sono i SATS', content: `
        <p>Un <strong>satoshi</strong> (abbreviato <strong>sat</strong> o <strong>sats</strong>) è la più piccola unità di Bitcoin.</p>
        <ul>
          <li><strong>1 BTC = 100.000.000 satoshi</strong> (cento milioni)</li>
          <li>1 sat = 0,00000001 BTC</li>
        </ul>
        <p>Bitcoin è divisibile proprio per questo: non devi comprare un Bitcoin intero. Puoi possedere e spendere frazioni minuscole.</p>
        <h3>Perché i sats nei pagamenti Lightning?</h3>
        <p>Sui pagamenti Lightning si ragiona quasi sempre in <strong>sats</strong>, non in BTC interi. È più intuitivo: "questo caffè costa 3.500 sats" è più leggibile di "0,000035 BTC".</p>
        <h3>Esempi pratici</h3>
        <ul>
          <li><strong>100 sats</strong> — circa 0,01–0,03€ (varia con il prezzo di BTC)</li>
          <li><strong>3.500 sats</strong> — circa il costo di un caffè</li>
          <li><strong>10.000 sats</strong> — poche euro, utile per una mancia o micro-donazione</li>
        </ul>
        <div class="box box--warning"><span class="box-title">Nota</span>Il valore in euro dei sats cambia con il prezzo di Bitcoin. Controlla sempre il controvalore nell'app prima di pagare.</div>
      `},
      { id: 'come-scala', title: 'Come scala il Lightning Network', content: `
        <h3>I canali di pagamento</h3>
        <p>Due utenti possono aprire un <strong>canale di pagamento</strong>: bloccano una certa quantità di Bitcoin in un contratto speciale on-chain, e poi scambiano sats tra loro <em>illimitate volte</em> senza toccare la blockchain principale.</p>
        <p>Quando hanno finito, chiudono il canale e solo il risultato finale viene registrato on-chain.</p>
        <h3>Routing dei pagamenti</h3>
        <p>Non serve un canale diretto con chi riceve. La rete Lightning trova un <strong>percorso</strong> tra più nodi intermedi — come un GPS che sceglie la strada migliore. Ogni nodo inoltra il pagamento al successivo fino alla destinazione.</p>
        <h3>Perché è istantaneo?</h3>
        <p>Le transazioni Lightning avvengono <strong>off-chain</strong> (fuori dalla blockchain). Non aspetti i blocchi Bitcoin: il pagamento si propaga in rete in millisecondi.</p>
        <h3>Perché alleggerisce Bitcoin?</h3>
        <p>Milioni di micro-pagamenti Lightning non intasano la blockchain. Solo l'apertura e la chiusura dei canali richiedono una transazione on-chain. Tutto il resto avviene sulla rete Lightning.</p>
        <div class="box box--tip"><span class="box-title">Analogia</span>Il canale è come una tabaccheria prepagata: carichi 50€ una volta e poi compri sigarette, giornali e gratta e vinci senza pagare ogni volta con il bancomat.</div>
      `},
      { id: 'wallet-lightning', title: 'Wallet Lightning compatibili', content: `
        <p>Per usare Lightning ti serve un <strong>wallet compatibile</strong>. Ecco le categorie principali — senza preferenze commerciali, solo differenze utili.</p>
        <h3>Custodial vs non-custodial</h3>
        <ul>
          <li><strong>Custodial</strong> — un servizio tiene le chiavi per te. Più semplice per iniziare, ma devi fidarti del provider</li>
          <li><strong>Non-custodial</strong> — tu controlli le chiavi e i fondi. Più sicuro e sovrano, ma richiede più attenzione al backup</li>
        </ul>
        <h3>Wallet custodial (ideali per principianti)</h3>
        <p>App semplici: scarichi, crei account, ricevi sats. Spesso integrano mappe commercianti e acquisto sats con carta. Adatti a chi inizia e fa piccoli pagamenti.</p>
        <h3>Wallet non-custodial (più controllo)</h3>
        <p>Richiedono backup della seed phrase e a volte la gestione dei canali. Più adatti a utenti intermedi o avanzati che vogliono piena proprietà dei fondi.</p>
        <h3>Wallet con LNURL</h3>
        <p>Supportano lo standard <strong>LNURL</strong>: link e QR semplificati per ricevere pagamenti senza generare invoice manuali ogni volta. Molto comodi per mance e donazioni.</p>
        <h3>Wallet con NFC / Tap-to-Pay</h3>
        <p>Alcune app permettono di pagare avvicinando il telefono (NFC), come Apple Pay o Google Pay. Tecnologia ancora in crescita, ma promettente per i pagamenti fisici.</p>
        <div class="box box--tip"><span class="box-title">Consiglio</span>Se sei alle prime armi, inizia con un wallet custodial semplice. Quando ti senti sicuro, valuta un wallet non-custodial per somme più importanti.</div>
      `},
      { id: 'configurare-satoshi-wallet', title: 'Come configurare Satoshi Wallet', content: `
        <p><strong>Satoshi Wallet</strong> è un'app mobile che combina wallet Lightning, acquisto di sats e una mappa dei commercianti che accettano Bitcoin. Ecco la configurazione passo-passo.</p>
        <div class="step-block"><h3>Passo 1 — Download</h3>
        <p>Scarica l'app solo dagli store ufficiali (App Store o Google Play). Verifica che lo sviluppatore corrisponda all'app autentica.</p></div>
        <div class="step-block"><h3>Passo 2 — Creazione wallet</h3>
        <p>Apri l'app e segui la procedura guidata: crea un account o un nuovo wallet. Leggi ogni schermata con calma.</p></div>
        <div class="step-block"><h3>Passo 3 — Backup</h3>
        <p>Se l'app ti mostra una <strong>seed phrase</strong> o chiavi di recupero, scrivile su carta e conservale offline. Non fare screenshot. Senza backup, rischi di perdere i tuoi sats.</p></div>
        <div class="step-block"><h3>Passo 4 — Ricevere sats</h3>
        <p>Vai su "Ricevi" e genera un'<strong>invoice Lightning</strong> (richiesta di pagamento) con l'importo desiderato. Condividi il QR code o il codice testuale a chi deve pagarti.</p></div>
        <div class="step-block"><h3>Passo 5 — Inviare sats</h3>
        <p>Vai su "Invia", scansiona il QR code del destinatario oppure incolla l'invoice Lightning. Controlla importo e destinatario, poi conferma.</p></div>
        <div class="step-block"><h3>Passo 6 — Generare invoice</h3>
        <p>Per richiedere un pagamento specifico: imposta l'importo in sats, aggiungi una descrizione (opzionale) e genera il QR. Valido per un tempo limitato.</p></div>
        <div class="step-block"><h3>Passo 7 — Collegamento nodo (opzionale)</h3>
        <p>Alcune versioni avanzate permettono di collegarsi a un nodo Lightning personale. Per la maggior parte degli utenti non è necessario: l'app gestisce tutto in automatico.</p></div>
        <div class="box box--danger"><span class="box-title">Mai</span>Condividere seed phrase, screenshot di backup o credenziali con chiunque — nemmeno con il "supporto" dell'app.</div>
      `},
      { id: 'mappa-satoshi-wallet', title: 'Come usare la mappa di Satoshi Wallet', content: `
        <p>Una delle funzioni più utili di Satoshi Wallet è la <strong>mappa dei commercianti</strong> che accettano pagamenti Lightning.</p>
        <div class="step-block"><h3>Aprire la mappa</h3>
        <p>Nell'app, cerca la sezione <strong>Map</strong> o <strong>Mappa</strong> (icona del globo o pin sulla mappa). Consenti l'accesso alla posizione se vuoi trovare negozi vicini a te.</p></div>
        <div class="step-block"><h3>Filtrare i commercianti</h3>
        <p>Usa i filtri per categoria (bar, ristoranti, negozi, servizi) o per distanza. Puoi anche cercare per città o nome del locale.</p></div>
        <div class="step-block"><h3>Leggere le schede negozio</h3>
        <p>Ogni pin mostra: nome, indirizzo, tipo di attività e se accetta Lightning. Alcuni includono foto, orari e link al sito.</p></div>
        <div class="step-block"><h3>Pagare con QR code</h3>
        <p>Al momento del pagamento: apri "Invia" nell'app, scansiona il <strong>QR Lightning</strong> del commerciante, verifica l'importo in sats e conferma. Il pagamento è istantaneo.</p></div>
        <div class="step-block"><h3>Verificare la transazione</h3>
        <p>Dopo il pagamento vedrai una spunta verde e il dettaglio nella cronologia. Il commerciante riceve conferma in tempo reale — niente attese di blocchi.</p></div>
        <div class="box box--tip"><span class="box-title">Consiglio</span>Prima di andare in un negozio, controlla sulla mappa che sia ancora attivo e che accetti Lightning. I dati possono cambiare.</div>
      `},
      { id: 'esempi-pratici', title: 'Esempi pratici', content: `
        <h3>Comprare un caffè in sats</h3>
        <p>Entri nel bar, ordini un cappuccino (3.500 sats). Il barista mostra il QR Lightning sul tablet. Apri Satoshi Wallet → Invia → scansiona → conferma. Fatto in un secondo.</p>
        <h3>Inviare 100 sats a un amico</h3>
        <p>Il tuo amico genera un'invoice da 100 sats (o usa LNURL). Tu scansioni il suo QR e invii. Una mancia digitale immediata.</p>
        <h3>Pagare un servizio online</h3>
        <p>Un sito web mostra "Paga con Lightning" e un QR. Scansioni, paghi in sats, e il servizio si sblocca subito — senza carta di credito.</p>
        <h3>Micro-donazioni</h3>
        <p>Vuoi donare 500 sats a un creator o un progetto open source? Lightning è perfetto: fee quasi zero anche per importi piccolissimi.</p>
      `},
      { id: 'conclusione', title: 'Conclusione', content: `
        <p>Il <strong>Lightning Network</strong> risolve il problema dei pagamenti quotidiani con Bitcoin: velocità, costi minimi e micro-transazioni.</p>
        <p>I <strong>sats</strong> sono l'unità ideale per ragionare su questi pagamenti — più pratica del BTC intero.</p>
        <p>I <strong>wallet Lightning</strong> stanno diventando sempre più semplici: app come Satoshi Wallet abbassano la barriera d'ingresso per chi non è tecnico.</p>
        <p>La <strong>mappa dei commercianti</strong> collega la teoria alla pratica: trovi chi accetta Bitcoin nel mondo reale e paghi con un QR.</p>
        <div class="box box--tip"><span class="box-title">Prossimi passi</span>
          <ul>
            <li>Leggi la guida <a href="articolo.html?slug=comprare-bitcoin-prima-volta">Come comprare Bitcoin</a> se non hai ancora BTC</li>
            <li>Consulta <a href="articolo.html?slug=proteggere-seed-phrase">Come proteggere la seed phrase</a> prima di usare qualsiasi wallet</li>
            <li>Esplora il <a href="glossario/index.html">glossario</a> per i termini che non conosci</li>
          </ul>
        </div>
      `}
    ],
    faq: [
      { q: 'Lightning Network è sicuro?', a: 'Sì, è costruito sopra la sicurezza di Bitcoin. I canali usano contratti intelligenti che impediscono frodi. Usa però solo wallet affidabili e fai sempre backup della seed phrase.' },
      { q: 'Devo avere Bitcoin on-chain per usare Lightning?', a: 'Sì, in genere devi prima avere BTC (on-chain o acquistati nell\'app) e poi trasferirli sul wallet Lightning. Alcune app custodial semplificano questo passaggio.' },
      { q: 'Cosa succede se il mio telefono si rompe?', a: 'Se hai salvato la seed phrase, puoi ripristinare il wallet su un nuovo dispositivo. Senza backup, i fondi su wallet non-custodial potrebbero essere persi.' },
      { q: 'Satoshi Wallet è l\'unica app con mappa commercianti?', a: 'No, esistono altre mappe e directory (come BTCmap.org). Satoshi Wallet integra mappa e wallet in un\'unica app per comodità.' },
      { q: 'Posso pagare con Lightning in Italia?', a: 'Sì, ma l\'adozione è ancora in crescita. La mappa ti aiuta a trovare i locali che accettano Lightning. Nei grandi centri ci sono più opzioni che nei paesi piccoli.' }
    ]
  },

  'comprare-bitcoin-prima-volta': {
    intro: 'Vuoi comprare Bitcoin ma non sai da dove iniziare? In questa guida ti spiego tutto passo dopo passo: dalla scelta dell\'exchange alla sicurezza del tuo primo acquisto. Nessun hype, solo istruzioni pratiche.',
    sections: [
      { id: 'cosa-serve', title: 'Cosa ti serve prima di iniziare', content: `
        <p>Per comprare Bitcoin ti servono solo tre cose:</p>
        <ul>
          <li><strong>Documento d'identità</strong> — gli exchange regolamentati richiedono la verifica KYC</li>
          <li><strong>Conto bancario o carta</strong> — per depositare euro</li>
          <li><strong>Un po' di pazienza</strong> — la verifica può richiedere da pochi minuti a 24 ore</li>
        </ul>
        <div class="box box--tip"><span class="box-title">Consiglio pratico</span>Inizia con pochi euro (anche 20€) per familiarizzare con il processo prima di investire somme più importanti.</div>
      `},
      { id: 'scegliere-exchange', title: 'Passo 1: Scegliere un exchange sicuro', content: `
        <p>Un exchange è una piattaforma dove puoi comprare e vendere crypto con euro. Per l'Italia, ti consiglio exchange regolamentati come:</p>
        <ul>
          <li><strong>Kraken</strong> — regolamentato, buona reputazione, fee competitive</li>
          <li><strong>Coinbase</strong> — molto intuitivo per principianti</li>
          <li><strong>Young Platform</strong> — exchange italiano con supporto in italiano</li>
        </ul>
        <div class="box box--warning"><span class="box-title">Attenzione</span>Verifica sempre che l'URL sia corretto prima di inserire le tue credenziali. Il phishing è il metodo di truffa più comune.</div>
      `},
      { id: 'registrazione', title: 'Passo 2: Registrazione e verifica', content: `
        <div class="step-block"><h3>2.1 Crea il tuo account</h3>
        <p>Vai sul sito ufficiale dell'exchange, clicca "Registrati" e inserisci la tua email. Scegli una password forte e unica.</p></div>
        <div class="step-block"><h3>2.2 Attiva il 2FA</h3>
        <p>Subito dopo la registrazione, attiva l'autenticazione a due fattori con un'app come Google Authenticator o Authy. <strong>Mai via SMS.</strong></p></div>
        <div class="step-block"><h3>2.3 Completa il KYC</h3>
        <p>Carica foto del documento d'identità e un selfie. È un obbligo normativo, non un'opzione.</p></div>
      `},
      { id: 'deposito', title: 'Passo 3: Depositare euro', content: `
        <p>Una volta verificato, vai su "Deposita" e scegli il metodo:</p>
        <ul>
          <li><strong>Bonifico SEPA</strong> — fee basse o gratuite, 1-2 giorni lavorativi</li>
          <li><strong>Carta di credito/debito</strong> — istantaneo, ma fee più alte (1.5-3%)</li>
        </ul>
      `},
      { id: 'acquisto', title: 'Passo 4: Comprare Bitcoin', content: `
        <div class="step-block"><h3>4.1 Vai su "Compra" o "Trade"</h3>
        <p>Cerca BTC/EUR e seleziona "Acquisto immediato" se sei principiante.</p></div>
        <div class="step-block"><h3>4.2 Inserisci l'importo</h3>
        <p>Scrivi quanti euro vuoi spendere (es. 50€). Controlla il prezzo finale comprensivo di fee.</p></div>
        <div class="step-block"><h3>4.3 Conferma l'ordine</h3>
        <p>Rivedi il riepilogo e conferma. I Bitcoin appariranno nel tuo saldo exchange.</p></div>
      `},
      { id: 'dopo-acquisto', title: 'Passo 5: Cosa fare dopo l\'acquisto', content: `
        <p>I tuoi Bitcoin sono ora sull'exchange. Per piccole somme va bene, ma per somme importanti:</p>
        <ul>
          <li>Trasferiscili su un <strong>wallet personale</strong> che controlli tu</li>
          <li>Non lasciare grandi quantità sull'exchange a lungo termine</li>
          <li>Tieni traccia dell'operazione per la dichiarazione fiscale</li>
        </ul>
        <div class="box box--tip"><span class="box-title">Prossimo passo</span>Leggi la nostra guida su <a href="articolo.html?slug=creare-wallet-sicuro">come creare un wallet sicuro</a>.</div>
      `}
    ],
    faq: [
      { q: 'Quanto costa comprare Bitcoin?', a: 'Dipende dall\'exchange. Le fee vanno dallo 0.1% al 3% a seconda del metodo di pagamento. Controlla sempre il costo totale prima di confermare.' },
      { q: 'Posso comprare frazioni di Bitcoin?', a: 'Sì. Puoi comprare anche 0.0001 BTC (pochi euro). Non serve comprare un Bitcoin intero.' },
      { q: 'È legale comprare Bitcoin in Italia?', a: 'Sì, è perfettamente legale. Devi però dichiarare il possesso nel modello Redditi se superi determinate soglie.' }
    ]
  },

  'creare-wallet-sicuro': {
    intro: 'Un wallet è il posto dove conservi le tue crypto. Crearne uno sicuro richiede meno di 10 minuti, ma gli errori in questa fase possono costarti tutto. Segui questa guida con attenzione.',
    sections: [
      { id: 'tipi-wallet', title: 'Hot wallet vs Cold wallet', content: `
        <p>Ci sono due categorie principali:</p>
        <ul>
          <li><strong>Hot wallet</strong> — app o estensione browser, connessi a internet. Comodi per uso quotidiano.</li>
          <li><strong>Cold wallet</strong> — dispositivo hardware offline. Massima sicurezza per conservazione a lungo termine.</li>
        </ul>
        <p>Per iniziare, un hot wallet va benissimo. Per somme importanti, considera un hardware wallet.</p>
      `},
      { id: 'installazione', title: 'Passo 1: Installare il wallet', content: `
        <p>Per principianti consigliamo <strong>Trust Wallet</strong> (mobile) o <strong>MetaMask</strong> (browser + mobile).</p>
        <div class="step-block"><h3>Trust Wallet (smartphone)</h3>
        <ol>
          <li>Scarica solo dall'App Store o Google Play ufficiale</li>
          <li>Apri l'app e seleziona "Crea nuovo wallet"</li>
          <li>Imposta un PIN forte o attiva la biometria</li>
        </ol></div>
        <div class="box box--danger"><span class="box-title">Mai</span>Scaricare wallet da link ricevuti via email, Telegram o annunci. Solo store ufficiali.</div>
      `},
      { id: 'seed-phrase', title: 'Passo 2: Salvare la seed phrase', content: `
        <p>L'app ti mostrerà <strong>12 o 24 parole</strong> in un ordine preciso. Questa è la tua seed phrase (chiave di recupero).</p>
        <ol>
          <li>Scrivile su <strong>carta</strong>, nell'ordine esatto</li>
          <li>Verifica due volte ogni parola</li>
          <li>Conservale in un posto sicuro, lontano da occhi indiscreti</li>
          <li>Fai una seconda copia e conservala in un luogo diverso</li>
        </ol>
        <div class="box box--danger"><span class="box-title">Mai</span>Fotografare, fare screenshot, salvare su cloud, inviare via email o digitare su computer la seed phrase.</div>
      `},
      { id: 'verifica', title: 'Passo 3: Verificare il backup', content: `
        <p>Il wallet ti chiederà di reinserire alcune parole per confermare che le hai salvate correttamente. Fallo con calma.</p>
      `},
      { id: 'primo-uso', title: 'Passo 4: Primo utilizzo', content: `
        <p>Ora hai un indirizzo wallet per ogni crypto supportata. Prima di inviare somme importanti:</p>
        <ul>
          <li>Fai un <strong>test con pochi centesimi</strong></li>
          <li>Verifica di poter ricevere e inviare correttamente</li>
          <li>Controlla la transazione su un block explorer</li>
        </ul>
      `}
    ],
    faq: [
      { q: 'Cosa succede se perdo la seed phrase?', a: 'Perdi accesso permanente alle tue crypto. Nessuno può recuperarle per te. La seed phrase È il tuo wallet.' },
      { q: 'Posso usare lo stesso wallet su più dispositivi?', a: 'Sì, importando la stessa seed phrase. Ma ogni dispositivo in più è un rischio in più.' }
    ]
  },

  'proteggere-seed-phrase': {
    intro: 'La seed phrase è la chiave di tutto il tuo portafoglio crypto. Chi la possiede, possiede le tue crypto. Ecco come proteggerla correttamente.',
    sections: [
      { id: 'cosa-e', title: 'Cos\'è la seed phrase', content: `
        <p>È una sequenza di 12 o 24 parole in inglese (standard BIP39) generata dal tuo wallet. Serve a ricreare le chiavi private e recuperare l'accesso alle tue crypto su qualsiasi dispositivo compatibile.</p>
      `},
      { id: 'come-salvarla', title: 'Come salvarla correttamente', content: `
        <p>Segui la strategia <strong>3-2-1</strong>:</p>
        <ul>
          <li><strong>3 copie</strong> della seed phrase</li>
          <li><strong>2 supporti</strong> diversi (es. carta + metallo inciso)</li>
          <li><strong>1 copia</strong> in un luogo fisico diverso (es. cassetta di sicurezza)</li>
        </ul>
        <div class="box box--tip"><span class="box-title">Consiglio</span>Esistono piastre in acciaio per incidere la seed phrase: resistono a fuoco e acqua meglio della carta.</div>
      `},
      { id: 'errori', title: 'Errori da evitare assolutamente', content: `
        <ul>
          <li>❌ Screenshot o foto della seed phrase</li>
          <li>❌ Salvarla in note digitali, email o cloud</li>
          <li>❌ Condividerla con chiunque, incluso "supporto tecnico"</li>
          <li>❌ Digitare le parole su siti web</li>
          <li>❌ Conservare una sola copia</li>
        </ul>
      `},
      { id: 'emergenza', title: 'Cosa fare in caso di emergenza', content: `
        <p>Se sospetti che la tua seed phrase sia stata compromessa:</p>
        <ol>
          <li>Crea immediatamente un <strong>nuovo wallet</strong></li>
          <li>Trasferisci tutti i fondi al nuovo indirizzo</li>
          <li>Non usare più il vecchio wallet</li>
        </ol>
      `}
    ],
    faq: [
      { q: 'Posso cambiare la seed phrase?', a: 'No. È generata una volta alla creazione del wallet. Per avere una nuova seed, devi creare un nuovo wallet e trasferire i fondi.' }
    ]
  },

  'cardano-spiegato': {
    intro: 'Cardano è una blockchain fondata su ricerca accademica peer-reviewed. La sua crypto nativa si chiama ADA. Ecco tutto quello che devi sapere, spiegato senza tecnicismi.',
    sections: [
      { id: 'cosa-e', title: 'Cos\'è Cardano', content: `
        <p>Cardano è una piattaforma blockchain creata da Charles Hoskinson (co-fondatore di Ethereum). Si distingue per:</p>
        <ul>
          <li>Approccio basato su <strong>ricerca scientifica</strong></li>
          <li>Meccanismo <strong>Proof-of-Stake</strong> (Ouroboros)</li>
          <li>Focus su sostenibilità, scalabilità e interoperabilità</li>
        </ul>
      `},
      { id: 'ada', title: 'Cos\'è ADA', content: `
        <p>ADA è la criptovaluta nativa di Cardano. Si usa per:</p>
        <ul>
          <li>Pagare le fee di transazione</li>
          <li>Partecipare allo <strong>staking</strong> (delega ai pool)</li>
          <li>Governance (votare proposte con Project Catalyst)</li>
        </ul>
      `},
      { id: 'staking', title: 'Staking su Cardano', content: `
        <p>A differenza di Ethereum, lo staking su Cardano <strong>non blocca i tuoi ADA</strong>. Puoi delegare a un pool di staking e:</p>
        <ul>
          <li>Ricevere ricompense (~3-5% annuo)</li>
          <li>Spendere o trasferire i tuoi ADA in qualsiasi momento</li>
          <li>Cambiare pool quando vuoi</li>
        </ul>
        <div class="box box--tip"><span class="box-title">Consiglio</span>Leggi la guida completa: <a href="articolo.html?slug=staking-ada">Staking ADA passo-passo</a>.</div>
      `},
      { id: 'ecosistema', title: 'L\'ecosistema Cardano', content: `
        <p>Oltre a ADA, su Cardano trovi:</p>
        <ul>
          <li><strong>Native token</strong> — asset creati direttamente sulla blockchain</li>
          <li><strong>DeFi</strong> — Minswap, SundaeSwap e altri DEX</li>
          <li><strong>NFT</strong> — marketplace dedicati</li>
          <li><strong>Project Catalyst</strong> — sistema di funding comunitario</li>
        </ul>
      `}
    ],
    faq: [
      { q: 'Cardano è meglio di Ethereum?', a: 'Dipende dalle tue esigenze. Cardano ha fee più basse e staking più semplice. Ethereum ha un ecosistema DeFi più maturo. Non c\'è un "migliore" assoluto.' },
      { q: 'Quanto costa una transazione su Cardano?', a: 'Tipicamente meno di 0.20 ADA (pochi centesimi di euro). Molto più economico di Ethereum.' }
    ]
  },

  'blockchain-5-minuti': {
    intro: 'Senti parlare di blockchain ovunque ma non hai capito cos\'è? In 5 minuti ti spiego il concetto fondamentale, senza formule e senza hype.',
    sections: [
      { id: 'definizione', title: 'Blockchain in parole semplici', content: `
        <p>Immagina un <strong>registro contabile</strong> condiviso da migliaia di computer in tutto il mondo. Ogni volta che qualcuno fa una transazione, viene registrata in questo registro. E nessuno può cancellare o modificare le voci passate.</p>
        <p>Questo registro si chiama <strong>blockchain</strong> (catena di blocchi) perché le transazioni sono raggruppate in "blocchi" collegati tra loro come una catena.</p>
      `},
      { id: 'come-funziona', title: 'Come funziona', content: `
        <ol>
          <li>Alice invia 1 BTC a Bob</li>
          <li>La transazione viene proposta alla rete</li>
          <li>I "validatori" verificano che Alice abbia davvero 1 BTC</li>
          <li>La transazione viene aggiunta a un blocco</li>
          <li>Il blocco viene collegato alla catena — permanente e immutabile</li>
        </ol>
      `},
      { id: 'perche-importa', title: 'Perché è importante', content: `
        <ul>
          <li><strong>Decentralizzazione</strong> — nessuna banca o governo controlla tutto</li>
          <li><strong>Trasparenza</strong> — tutte le transazioni sono verificabili</li>
          <li><strong>Immutabilità</strong> — difficile alterare il passato</li>
        </ul>
      `}
    ],
    faq: [
      { q: 'Blockchain e Bitcoin sono la stessa cosa?', a: 'No. Bitcoin è una criptovaluta che usa la tecnologia blockchain. La blockchain è la tecnologia sottostante, usata anche da Ethereum, Cardano e molte altre.' }
    ]
  }
};

function generateGenericContent(article) {
  const categoryLabels = {
    guide: 'Guida passo-passo', tip: 'Crypto Tip', trend: 'Trend crypto',
    tutorial: 'Tutorial', cardano: 'Cardano', sicurezza: 'Sicurezza',
    bitcoin: 'Bitcoin', ethereum: 'Ethereum', 'smart-contract': 'Smart Contract'
  };
  return {
    intro: article.excerpt + ' Questo articolo fa parte della sezione ' + (categoryLabels[article.category] || article.category) + ' di The Little Satoshi News. Stiamo aggiornando il contenuto completo — nel frattempo, ecco una panoramica utile.',
    sections: [
      { id: 'panoramica', title: 'Panoramica', content: `<p>${article.excerpt}</p><p>In questa guida vedremo tutto ciò che serve per approfondire l'argomento in modo pratico e sicuro, senza hype e con esempi concreti.</p>` },
      { id: 'passi', title: 'Passi principali', content: `
        <div class="step-block"><h3>Passo 1 — Preparazione</h3><p>Raccogli le informazioni necessarie e assicurati di aver compreso i rischi base prima di procedere.</p></div>
        <div class="step-block"><h3>Passo 2 — Esecuzione</h3><p>Segui le istruzioni passo dopo passo, verificando ogni operazione prima di confermare.</p></div>
        <div class="step-block"><h3>Passo 3 — Verifica</h3><p>Controlla che tutto sia andato a buon fine e conserva traccia dell'operazione.</p></div>
        <div class="box box--warning"><span class="box-title">Attenzione</span>Questo contenuto ha scopo educativo. Non costituisce consulenza finanziaria. Investire in crypto comporta rischi.</div>
      `},
      { id: 'consigli', title: 'Consigli pratici', content: `
        <ul>
          <li>Inizia sempre con piccole somme per fare pratica</li>
          <li>Verifica le fonti ufficiali prima di ogni operazione</li>
          <li>Non condividere mai seed phrase o chiavi private</li>
          <li>Tieni traccia di ogni operazione per la dichiarazione fiscale</li>
        </ul>
      `}
    ],
    faq: [
      { q: 'Questo articolo è adatto ai principianti?', a: 'Sì, The Little Satoshi News è pensato per chi si avvicina al mondo crypto. Se un termine non ti è chiaro, consulta il nostro glossario.' },
      { q: 'Quando sarà aggiornato il contenuto completo?', a: 'Stiamo pubblicando le guide complete progressivamente. Iscriviti alla newsletter per ricevere gli aggiornamenti.' }
    ]
  };
}

async function initArticlePage() {
  if (document.body.dataset.page !== 'article') return;

  const params = new URLSearchParams(window.location.search);
  const slug = params.get('slug');
  if (!slug) { window.location.href = getBasePath() + 'index.html'; return; }

  await loadArticles();
  const article = articlesData.articles.find(a => a.slug === slug);
  if (!article) { window.location.href = getBasePath() + 'index.html'; return; }

  const base = getBasePath();
  const content = ARTICLE_CONTENT[slug] || generateGenericContent(article);

  document.title = `${article.title} — The Little Satoshi News`;
  const metaDesc = document.querySelector('meta[name="description"]');
  if (metaDesc) metaDesc.content = article.excerpt;

  const articleUrl = getArticleUrl(slug);
  [['og:title', article.title], ['og:description', article.excerpt], ['og:url', articleUrl], ['og:type', 'article']].forEach(([prop, content]) => {
    let el = document.querySelector(`meta[property="${prop}"]`);
    if (!el) {
      el = document.createElement('meta');
      el.setAttribute('property', prop);
      document.head.appendChild(el);
    }
    el.content = content;
  });

  const diffLabel = { beginner: 'Principiante', intermediate: 'Intermedio', advanced: 'Avanzato' }[article.difficulty] || 'Principiante';

  const breadcrumbMap = {
    guide: { label: 'Guide', href: 'guide/index.html' },
    tip: { label: 'Crypto Tips', href: 'crypto-tips/index.html' },
    trend: { label: 'Trend', href: 'trend/index.html' },
    tutorial: { label: 'Tutorial', href: 'guide/index.html' },
    cardano: { label: 'Cardano', href: 'cardano/index.html' },
    sicurezza: { label: 'Sicurezza', href: 'sicurezza/index.html' },
    bitcoin: { label: 'Bitcoin', href: 'bitcoin/index.html' },
    ethereum: { label: 'Ethereum', href: 'ethereum/index.html' },
    'smart-contract': { label: 'Smart Contract', href: 'smart-contract/index.html' }
  };
  const bc = breadcrumbMap[article.category] || { label: 'Guide', href: 'guide/index.html' };

  const breadcrumbEl = document.getElementById('article-breadcrumb');
  if (breadcrumbEl) {
    breadcrumbEl.innerHTML = renderBreadcrumb([
      bc,
      { label: article.title, href: '' }
    ]);
  }

  const headerEl = document.getElementById('article-header');
  if (headerEl) {
    headerEl.innerHTML = `
      <h1>${article.title}</h1>
      <div class="article-meta-bar">
        <span class="badge badge--${article.difficulty}">${diffLabel}</span>
        <span>📖 ${article.readTime} min di lettura</span>
        <span>📅 Aggiornato ${article.date}</span>
      </div>
      ${typeof renderFacebookShareBar === 'function' ? renderFacebookShareBar(article) : ''}`;
    initArticleFacebookShare(article);
  }

  const tocItems = content.sections.map(s => `<li><a href="#${s.id}" data-toc="${s.id}">${s.title}</a></li>`).join('');
  const tocEl = document.getElementById('article-toc');
  if (tocEl) tocEl.innerHTML = `<h4>Indice</h4><ul class="toc-list">${tocItems}</ul>`;

  const bodyEl = document.getElementById('article-body');
  if (bodyEl) {
    let html = `<p class="article-intro">${content.intro}</p>`;
    content.sections.forEach(s => {
      html += `<h2 id="${s.id}">${s.title}</h2>${s.content}`;
    });
    if (content.faq?.length) {
      html += '<h2 id="faq">Domande frequenti</h2>';
      content.faq.forEach(f => {
        html += `<details class="faq-item"><summary>${f.q}</summary><div class="faq-answer">${f.a}</div></details>`;
      });
    }
    bodyEl.innerHTML = html;
  }

  const related = articlesData.articles
    .filter(a => a.slug !== slug && (a.category === article.category || a.subcategory === article.subcategory))
    .slice(0, 3);

  const relatedEl = document.getElementById('related-articles');
  if (relatedEl) {
    relatedEl.innerHTML = related.map(a => renderArticleCard(a, base)).join('');
  }

  initProgressBar();
  initTocHighlight();
  injectArticleSchema(article, content);
}

function initProgressBar() {
  const bar = document.getElementById('progress-bar');
  if (!bar) return;
  window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    bar.style.width = docHeight > 0 ? (scrollTop / docHeight * 100) + '%' : '0%';
  });
}

function initTocHighlight() {
  const links = document.querySelectorAll('[data-toc]');
  if (!links.length) return;
  const observer = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        links.forEach(l => l.classList.remove('active'));
        const active = document.querySelector(`[data-toc="${e.target.id}"]`);
        if (active) active.classList.add('active');
      }
    });
  }, { rootMargin: '-20% 0px -60% 0px' });
  document.querySelectorAll('.article-content h2').forEach(h => observer.observe(h));
}

function injectArticleSchema(article, content) {
  const schema = {
    '@context': 'https://schema.org',
    '@type': 'Article',
    headline: article.title,
    description: article.excerpt,
    dateModified: '2026-06-01',
    author: { '@type': 'Organization', name: 'The Little Satoshi News' },
    publisher: { '@type': 'Organization', name: 'The Little Satoshi News', url: SITE_CONFIG.siteUrl }
  };
  if (content.sections.length > 2) {
    schema['@type'] = 'HowTo';
    schema.step = content.sections.map((s, i) => ({
      '@type': 'HowToStep', position: i + 1, name: s.title
    }));
  }
  const script = document.createElement('script');
  script.type = 'application/ld+json';
  script.textContent = JSON.stringify(schema);
  document.head.appendChild(script);
}

document.addEventListener('DOMContentLoaded', initArticlePage);