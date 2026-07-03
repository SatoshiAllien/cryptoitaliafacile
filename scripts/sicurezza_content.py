"""IT + EN content for Sicurezza section articles."""

SECURITY_BOX_IT = """
<div class="box box--tip"><span class="box-title">Security first</span>La sicurezza non è un optional: proteggi seed phrase, dispositivi e abitudini prima di aumentare le somme.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>Contenuto 100% educativo. Nessuna promessa di guadagni. Solo pratiche concrete e verificabili.</div>
"""

SECURITY_BOX_EN = """
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>
"""

SLUGS = [
    "seed-phrase-guida", "hot-vs-cold-wallet", "confronto-hardware-wallet",
    "difendersi-phishing", "approvazioni-smart-contract", "backup-wallet-321",
    "sicurezza-mobile", "wallet-compromesso", "password-manager-crypto",
    "audit-sicurezza-portafoglio", "creare-wallet-sicuro", "proteggere-seed-phrase",
    "hardware-wallet-ledger", "cold-wallet-chiavi-offline",
]

CONTENT = {
    "seed-phrase-guida": {
        "it": {
            "intro": "La <strong>seed phrase</strong> (12 o 24 parole BIP39) è la chiave master del tuo wallet. Chi la possiede controlla i tuoi fondi. Questa guida spiega cos'è, come viene generata e come conservarla senza errori fatali.",
            "sections": [
                ("cos-e-seed", "Cos'è la seed phrase", """
<p>Quando crei un wallet self-custody, il software genera una sequenza di parole in un ordine preciso. Da quella sequenza derivano tutte le chiavi private del portafoglio.</p>
<h3>Perché è così importante</h3>
<ul><li>È l'<strong>unico modo</strong> per recuperare il wallet se perdi telefono o computer</li><li>Non esiste "reset password" — senza seed, i fondi sono irrecuperabili</li><li>Chiunque legga la seed può svuotare il wallet</li></ul>
"""),
                ("generazione", "Come viene generata", """
<p>La generazione avviene <strong>sul tuo dispositivo</strong>, in un ambiente sicuro del wallet (Trust Wallet, MetaMask, Ledger, ecc.).</p>
<ol><li>Scegli "Crea nuovo wallet"</li><li>Il software genera entropia casuale e la converte in parole BIP39</li><li>Ti mostra le parole una sola volta — annotale subito</li><li>Verifica con il test di conferma del wallet</li></ol>
<div class="box box--danger"><span class="box-title">Mai</span>Generare o inserire la seed su siti web, moduli Google, chat Telegram o "supporto tecnico".</div>
"""),
                ("conservazione", "Come conservarla correttamente", """
<p>Regola pratica: <strong>carta + metallo + luogo sicuro</strong>.</p>
<ul><li>Scrivi le parole su carta indelebile, senza abbreviazioni</li><li>Valuta una piastra in acciaio per resistere a fuoco e acqua</li><li>Crea almeno due copie in luoghi fisici diversi</li><li>Non numerare le copie in modo che sia ovvio che sono seed phrase</li></ul>
"""),
                ("errori", "Errori che costano caro", """
<ul><li>❌ Screenshot o foto della seed</li><li>❌ Salvataggio su cloud, email, Note, iCloud</li><li>❌ Digitare la seed su qualsiasi sito</li><li>❌ Condividere con familiari "per sicurezza" senza capire i rischi</li></ul>
"""),
            ],
            "faq": [
                ("Posso cambiare la seed phrase?", "No. Per averne una nuova devi creare un nuovo wallet e trasferire i fondi."),
                ("12 o 24 parole?", "Entrambe sono valide. 24 parole offrono più entropia; 12 è lo standard più comune su mobile."),
            ],
        },
        "en": {
            "intro": "The <strong>seed phrase</strong> (12 or 24 BIP39 words) is your wallet's master key. Whoever holds it controls your funds. This guide explains what it is, how it is generated, and how to store it without fatal mistakes.",
            "sections": [
                ("what-is-seed", "What is a seed phrase", """
<p>When you create a self-custody wallet, the software generates a precise sequence of words. All private keys in the wallet are derived from that sequence.</p>
<h3>Why it matters</h3>
<ul><li>It is the <strong>only way</strong> to recover your wallet if you lose your phone or computer</li><li>There is no password reset — without the seed, funds are gone</li><li>Anyone who reads the seed can drain the wallet</li></ul>
"""),
                ("generation", "How it is generated", """
<p>Generation happens <strong>on your device</strong>, inside the wallet's secure environment (Trust Wallet, MetaMask, Ledger, etc.).</p>
<ol><li>Choose "Create new wallet"</li><li>Software generates random entropy and converts it to BIP39 words</li><li>Words are shown once — write them down immediately</li><li>Complete the wallet's confirmation test</li></ol>
<div class="box box--danger"><span class="box-title">Never</span>Generate or enter a seed on websites, Google forms, Telegram chats, or with "technical support".</div>
"""),
                ("storage", "How to store it correctly", """
<p>Practical rule: <strong>paper + metal + safe location</strong>.</p>
<ul><li>Write words on permanent ink paper, no abbreviations</li><li>Consider a steel plate for fire and water resistance</li><li>Keep at least two copies in different physical locations</li><li>Do not label copies obviously as seed phrases</li></ul>
"""),
                ("mistakes", "Costly mistakes", """
<ul><li>❌ Screenshots or photos of the seed</li><li>❌ Saving to cloud, email, Notes, iCloud</li><li>❌ Typing the seed on any website</li><li>❌ Sharing with family "for safety" without understanding risks</li></ul>
"""),
            ],
            "faq": [
                ("Can I change my seed phrase?", "No. To get a new one you must create a new wallet and transfer funds."),
                ("12 or 24 words?", "Both are valid. 24 words offer more entropy; 12 is the most common mobile standard."),
            ],
        },
    },
}

# Additional articles — compact generator for remaining slugs
def _sec_article_it(slug, intro, blocks, faq):
    return {"intro": intro, "sections": blocks, "faq": faq}

def _pair(intro_it, intro_en, sections_it, sections_en, faq_it, faq_en):
    return {"it": {"intro": intro_it, "sections": sections_it, "faq": faq_it},
            "en": {"intro": intro_en, "sections": sections_en, "faq": faq_en}}

# Merge extended content
CONTENT.update({
    "hot-vs-cold-wallet": _pair(
        "Hot wallet e cold wallet non sono la stessa cosa. Capire la differenza ti aiuta a usare lo strumento giusto per ogni somma e ogni operazione.",
        "Hot and cold wallets are not the same. Understanding the difference helps you use the right tool for each amount and operation.",
        [
            ("differenza", "La differenza in 30 secondi", "<p><strong>Hot wallet</strong>: connesso a internet (app mobile, estensione browser). Comodo, veloce, più esposto.</p><p><strong>Cold wallet</strong>: chiavi offline (hardware wallet, paper wallet). Meno comodo, massima protezione per hodl.</p>"),
            ("quando-hot", "Quando usare un hot wallet", "<ul><li>Piccole somme per uso quotidiano</li><li>DeFi, NFT, operazioni frequenti</li><li>Test e apprendimento con importi minimi</li></ul>"),
            ("quando-cold", "Quando usare un cold wallet", "<ul><li>Conservazione a lungo termine (Bitcoin, ETH, ADA)</li><li>Somme che non ti servono ogni giorno</li><li>Dopo aver accumulato su exchange — preleva verso cold</li></ul><div class=\"box box--tip\"><span class=\"box-title\">Regola pratica</span>Exchange per comprare. Hot per operare. Cold per conservare.</div>"),
            ("rischi", "Rischi principali", "<p>Hot: malware, phishing, approvazioni malevole. Cold: perdita fisica del device, seed non backuppata, acquisto device tampered.</p>"),
        ],
        [
            ("difference", "The difference in 30 seconds", "<p><strong>Hot wallet</strong>: internet-connected (mobile app, browser extension). Convenient, fast, more exposed.</p><p><strong>Cold wallet</strong>: offline keys (hardware wallet, paper wallet). Less convenient, maximum protection for hodling.</p>"),
            ("when-hot", "When to use a hot wallet", "<ul><li>Small amounts for daily use</li><li>DeFi, NFTs, frequent operations</li><li>Learning with minimal amounts</li></ul>"),
            ("when-cold", "When to use a cold wallet", "<ul><li>Long-term storage (Bitcoin, ETH, ADA)</li><li>Funds you do not need daily</li><li>After accumulating on an exchange — withdraw to cold</li></ul><div class=\"box box--tip\"><span class=\"box-title\">Practical rule</span>Exchange to buy. Hot to operate. Cold to store.</div>"),
            ("risks", "Main risks", "<p>Hot: malware, phishing, malicious approvals. Cold: physical loss, no seed backup, tampered device purchase.</p>"),
        ],
        [("Posso usare solo hot wallet?", "Sì per iniziare, ma non per tutto il patrimonio. Diversifica quando le somme crescono."),
         ("Il cold wallet è difficile?", "Ledger e Trezor sono pensati per principianti. Setup in 20-30 minuti.")],
        [("Can I use only a hot wallet?", "Yes to start, but not for your entire portfolio. Diversify as amounts grow."),
         ("Is a cold wallet difficult?", "Ledger and Trezor are beginner-friendly. Setup takes 20-30 minutes.")],
    ),
    "confronto-hardware-wallet": _pair(
        "Ledger, Trezor e BitBox sono i tre hardware wallet più usati in Europa. Nessuno è \"perfetto\": la scelta dipende da budget, blockchain supportate e livello di privacy.",
        "Ledger, Trezor, and BitBox are the three most used hardware wallets in Europe. None is \"perfect\": the choice depends on budget, supported blockchains, and privacy level.",
        [
            ("panoramica", "Perché un hardware wallet", "<p>Un hardware wallet tiene le <strong>chiavi private offline</strong>. Anche se il PC è infetto, un attaccante non può firmare transazioni senza il dispositivo fisico e il PIN.</p><ul><li>Ideale per conservazione medio-lungo termine</li><li>Compatibile con MetaMask, Ledger Live, Trezor Suite</li><li>Acquista solo da sito ufficiale o rivenditore autorizzato</li></ul>"),
            ("ledger", "Ledger (Nano S Plus / Nano X)", "<h3>Punti di forza</h3><ul><li>Supporto ampissimo di chain e token</li><li>App Ledger Live intuitiva</li><li>Nano X con Bluetooth (attenzione: più superficie d'attacco)</li></ul><h3>Attenzioni</h3><p>Storico leak dati clienti (email, indirizzi). Usa email dedicata e non cliccare link sospetti.</p>"),
            ("trezor", "Trezor (Model One / Safe 3)", "<h3>Punti di forza</h3><ul><li>Firmware open source</li><li>Trezor Suite pulita e trasparente</li><li>Ottimo per Bitcoin ed Ethereum</li></ul><h3>Attenzioni</h3><p>Model One non supporta alcune chain moderne. Verifica compatibilità prima dell'acquisto.</p>"),
            ("bitbox", "BitBox (BitBox02)", "<h3>Punti di forza</h3><ul><li>Produzione svizzera, focus privacy</li><li>Backup su microSD oltre alla seed</li><li>Interfaccia minimalista</li></ul><h3>Attenzioni</h3><p>Meno chain rispetto a Ledger. Ottimo se il tuo stack è BTC/ETH-centric.</p>"),
            ("scelta", "Come scegliere", "<ol><li>Elenca le crypto che detieni oggi e quelle previste</li><li>Confronta prezzo, display, connettività (USB-C, Bluetooth)</li><li>Verifica che il firmware sia aggiornabile</li><li>Ordina dal sito ufficiale — mai da marketplace sconosciuti</li></ol><div class=\"box box--warning\"><span class=\"box-title\">Attenzione</span>Device \"già configurato\" o con seed precompilata = truffa garantita.</div>"),
        ],
        [
            ("overview", "Why a hardware wallet", "<p>A hardware wallet keeps <strong>private keys offline</strong>. Even if your PC is infected, an attacker cannot sign transactions without the physical device and PIN.</p><ul><li>Ideal for medium to long-term storage</li><li>Works with MetaMask, Ledger Live, Trezor Suite</li><li>Buy only from the official site or authorized reseller</li></ul>"),
            ("ledger", "Ledger (Nano S Plus / Nano X)", "<h3>Strengths</h3><ul><li>Broad chain and token support</li><li>Intuitive Ledger Live app</li><li>Nano X with Bluetooth (note: larger attack surface)</li></ul><h3>Caveats</h3><p>Past customer data leaks (emails, addresses). Use a dedicated email and avoid suspicious links.</p>"),
            ("trezor", "Trezor (Model One / Safe 3)", "<h3>Strengths</h3><ul><li>Open-source firmware</li><li>Clean, transparent Trezor Suite</li><li>Excellent for Bitcoin and Ethereum</li></ul><h3>Caveats</h3><p>Model One does not support some modern chains. Check compatibility before buying.</p>"),
            ("bitbox", "BitBox (BitBox02)", "<h3>Strengths</h3><ul><li>Swiss-made, privacy-focused</li><li>microSD backup in addition to seed</li><li>Minimalist interface</li></ul><h3>Caveats</h3><p>Fewer chains than Ledger. Great if your stack is BTC/ETH-centric.</p>"),
            ("choose", "How to choose", "<ol><li>List crypto you hold today and plan to hold</li><li>Compare price, display, connectivity (USB-C, Bluetooth)</li><li>Ensure firmware is updatable</li><li>Order from the official site — never unknown marketplaces</li></ol><div class=\"box box--warning\"><span class=\"box-title\">Warning</span>A device \"already set up\" or with a pre-filled seed = guaranteed scam.</div>"),
        ],
        [("Ledger o Trezor per principianti?", "Entrambi vanno bene. Ledger ha più tutorial in italiano; Trezor punta su trasparenza open source."),
         ("Serve il modello più costoso?", "No. Nano S Plus o Trezor Safe 3 bastano per la maggior parte degli utenti.")],
        [("Ledger or Trezor for beginners?", "Both work well. Ledger has more Italian tutorials; Trezor focuses on open-source transparency."),
         ("Do I need the most expensive model?", "No. Nano S Plus or Trezor Safe 3 are enough for most users.")],
    ),
    "difendersi-phishing": _pair(
        "Il phishing è l'attacco più comune nel mondo crypto. Non serve un hacker geniale: basta un link convincente e un momento di distrazione. Impara a riconoscerlo prima che sia tardi.",
        "Phishing is the most common attack in crypto. You do not need a genius hacker: a convincing link and a moment of distraction are enough. Learn to spot it before it is too late.",
        [
            ("cos-e", "Cos'è il phishing crypto", "<p>Messaggi che imitano exchange, wallet, airdrop o \"supporto tecnico\" per rubare seed phrase, password o far firmare transazioni malevole.</p><h3>Canali frequenti</h3><ul><li>Email e SMS con link urgenti</li><li>Annunci Google/Facebook con URL simili</li><li>DM su Telegram, Discord, X</li><li>Siti clone di MetaMask, Ledger, Uniswap</li></ul>"),
            ("segnali", "Segnali di allarme", "<ul><li>Urgenza: \"Il tuo account verrà bloccato in 24 ore\"</li><li>Richiesta di seed phrase o chiavi private</li><li>URL leggermente diversi (metamask.io vs metamask.com)</li><li>Promesse di raddoppio BTC o airdrop \"esclusivi\"</li><li>Assistenza non richiesta che ti contatta per primo</li></ul><div class=\"box box--danger\"><span class=\"box-title\">Regola d'oro</span>Nessuno legittimo ti chiederà mai la seed phrase. Nemmeno Ledger, MetaMask o Binance.</div>"),
            ("difesa", "Come difendersi", "<ol><li>Segna i siti ufficiali nei preferiti — non usare link da email</li><li>Verifica sempre l'URL carattere per carattere</li><li>Attiva 2FA con app authenticator (non SMS)</li><li>Usa un email dedicata per exchange e crypto</li><li>Controlla approvazioni token periodicamente</li></ol>"),
            ("cosa-fare", "Se hai cliccato un link sospetto", "<p><strong>Non inserire dati.</strong> Chiudi la pagina. Se hai digitato la seed: trasferisci subito i fondi su un nuovo wallet. Se hai collegato il wallet a un sito fake: revoca le approvazioni su revoke.cash o etherscan.io.</p>"),
        ],
        [
            ("what-is", "What is crypto phishing", "<p>Messages mimicking exchanges, wallets, airdrops, or \"technical support\" to steal seed phrases, passwords, or trick you into signing malicious transactions.</p><h3>Common channels</h3><ul><li>Emails and SMS with urgent links</li><li>Google/Facebook ads with similar URLs</li><li>DMs on Telegram, Discord, X</li><li>Clone sites of MetaMask, Ledger, Uniswap</li></ul>"),
            ("signals", "Warning signs", "<ul><li>Urgency: \"Your account will be locked in 24 hours\"</li><li>Requests for seed phrase or private keys</li><li>Slightly different URLs (metamask.io vs metamask.com)</li><li>Promises to double BTC or \"exclusive\" airdrops</li><li>Unsolicited support contacting you first</li></ul><div class=\"box box--danger\"><span class=\"box-title\">Golden rule</span>No legitimate service will ever ask for your seed phrase. Not Ledger, MetaMask, or Binance.</div>"),
            ("defense", "How to defend yourself", "<ol><li>Bookmark official sites — do not use email links</li><li>Always verify the URL character by character</li><li>Enable 2FA with an authenticator app (not SMS)</li><li>Use a dedicated email for exchanges and crypto</li><li>Review token approvals periodically</li></ol>"),
            ("clicked", "If you clicked a suspicious link", "<p><strong>Do not enter data.</strong> Close the page. If you typed your seed: immediately transfer funds to a new wallet. If you connected your wallet to a fake site: revoke approvals on revoke.cash or etherscan.io.</p>"),
        ],
        [("Come verifico se un sito è ufficiale?", "Controlla il dominio esatto, certificato HTTPS, e confronta con i link dal sito ufficiale dell'azienda su X o documentazione."),
         ("Il phishing colpisce solo i principianti?", "No. Anche utenti esperti cadono in truffe sofisticate. La routine di verifica protegge tutti.")],
        [("How do I verify if a site is official?", "Check the exact domain, HTTPS certificate, and compare with links from the company's official X account or documentation."),
         ("Does phishing only target beginners?", "No. Even experienced users fall for sophisticated scams. Verification habits protect everyone.")],
    ),
    "approvazioni-smart-contract": _pair(
        "Ogni volta che usi Uniswap, OpenSea o un protocollo DeFi, firmi <strong>approvazioni</strong> che permettono a uno smart contract di muovere i tuoi token. Capire cosa firmi è fondamentale per la sicurezza.",
        "Every time you use Uniswap, OpenSea, or a DeFi protocol, you sign <strong>approvals</strong> allowing a smart contract to move your tokens. Understanding what you sign is essential for security.",
        [
            ("cosa-sono", "Cosa sono le approvazioni", "<p>Un'approvazione (allowance) autorizza un contratto a prelevare un certo quantitativo di token dal tuo wallet senza chiedere ogni volta.</p><h3>Tipi</h3><ul><li><strong>Limitata</strong> — importo specifico (più sicura)</li><li><strong>Illimitata</strong> — accesso totale al token (rischiosa)</li></ul>"),
            ("rischi", "Rischi delle approvazioni aperte", "<p>Se un contratto viene compromesso o era malevolo fin dall'inizio, può svuotare i token approvati — anche mesi dopo.</p><div class=\"box box--danger\"><span class=\"box-title\">Mai</span>Approva importi illimitati su protocolli che non conosci o non usi regolarmente.</div>"),
            ("verifica", "Come verificare le approvazioni", "<ol><li>Visita <strong>revoke.cash</strong> o Etherscan Token Approvals</li><li>Collega il wallet (solo su siti affidabili)</li><li>Controlla ogni rete: Ethereum, Polygon, BSC, Arbitrum</li><li>Revoca approvazioni vecchie o sospette</li></ol>"),
            ("buone-pratiche", "Buone pratiche", "<ul><li>Approva solo l'importo necessario per la singola operazione</li><li>Usa un wallet separato per DeFi sperimentale</li><li>Rivedi le approvazioni ogni 1-3 mesi</li><li>Prima di revocare, verifica fee di rete</li></ul>"),
        ],
        [
            ("what-are", "What are approvals", "<p>An approval (allowance) authorizes a contract to withdraw a certain amount of tokens from your wallet without asking each time.</p><h3>Types</h3><ul><li><strong>Limited</strong> — specific amount (safer)</li><li><strong>Unlimited</strong> — full token access (risky)</li></ul>"),
            ("risks", "Risks of open approvals", "<p>If a contract is compromised or was malicious from the start, it can drain approved tokens — even months later.</p><div class=\"box box--danger\"><span class=\"box-title\">Never</span>Approve unlimited amounts on protocols you do not know or use regularly.</div>"),
            ("check", "How to check approvals", "<ol><li>Visit <strong>revoke.cash</strong> or Etherscan Token Approvals</li><li>Connect your wallet (only on trusted sites)</li><li>Check each network: Ethereum, Polygon, BSC, Arbitrum</li><li>Revoke old or suspicious approvals</li></ol>"),
            ("practices", "Best practices", "<ul><li>Approve only the amount needed for a single operation</li><li>Use a separate wallet for experimental DeFi</li><li>Review approvals every 1-3 months</li><li>Before revoking, check network fees</li></ul>"),
        ],
        [("Revocare un'approvazione è pericoloso?", "No, è una operazione standard. Costa solo la fee di rete della transazione di revoca."),
         ("Serve su tutte le chain?", "Sì. Ogni rete ha approvazioni separate. Controlla Ethereum, L2 e sidechain dove hai operato.")],
        [("Is revoking an approval dangerous?", "No, it is a standard operation. It only costs the network fee for the revoke transaction."),
         ("Do I need this on all chains?", "Yes. Each network has separate approvals. Check Ethereum, L2s, and sidechains where you have operated.")],
    ),
    "backup-wallet-321": _pair(
        "La strategia <strong>3-2-1</strong> nasce nel mondo IT ma si applica perfettamente alle crypto: tre copie, due supporti, una off-site. È il minimo sindacale per non perdere tutto.",
        "The <strong>3-2-1</strong> strategy comes from IT but applies perfectly to crypto: three copies, two media, one off-site. It is the bare minimum to avoid losing everything.",
        [
            ("strategia", "La regola 3-2-1 spiegata", "<ul><li><strong>3 copie</strong> della seed phrase o backup</li><li><strong>2 supporti diversi</strong> — es. carta + acciaio, o carta + microSD criptata</li><li><strong>1 copia off-site</strong> — luogo fisico diverso da casa (cassetta, parente fidato)</li></ul>"),
            ("supporti", "Supporti consigliati", "<h3>Carta</h3><p>Economica, immediata. Usa penna indelebile, evita post-it.</p><h3>Metallo</h3><p>Piastre Cryptosteel, Billfodl: resistono a fuoco e allagamento.</p><h3>MicroSD (hardware wallet)</h3><p>BitBox supporta backup su scheda. Conserva la scheda come tesoro.</p>"),
            ("cosa-no", "Cosa NON usare come backup", "<ul><li>❌ Screenshot, foto, file digitali non criptati</li><li>❌ Cloud (iCloud, Google Drive, Dropbox)</li><li>❌ Email a te stesso</li><li>❌ Password manager per la seed (solo per password exchange)</li></ul>"),
            ("test", "Testa il backup", "<p>Un backup non testato è un backup inutile. Una volta all'anno (o dopo ogni grande movimento):</p><ol><li>Recupera il wallet su un dispositivo pulito usando la seed</li><li>Verifica che gli indirizzi coincidano</li><li>Richiudi senza lasciare tracce sul device di test</li></ol>"),
        ],
        [
            ("strategy", "The 3-2-1 rule explained", "<ul><li><strong>3 copies</strong> of the seed phrase or backup</li><li><strong>2 different media</strong> — e.g. paper + steel, or paper + encrypted microSD</li><li><strong>1 off-site copy</strong> — physical location different from home (safe deposit box, trusted relative)</li></ul>"),
            ("media", "Recommended media", "<h3>Paper</h3><p>Cheap, immediate. Use permanent ink, avoid sticky notes.</p><h3>Metal</h3><p>Cryptosteel, Billfodl plates: resist fire and flooding.</p><h3>microSD (hardware wallet)</h3><p>BitBox supports card backup. Guard the card like treasure.</p>"),
            ("avoid", "What NOT to use as backup", "<ul><li>❌ Screenshots, photos, unencrypted digital files</li><li>❌ Cloud (iCloud, Google Drive, Dropbox)</li><li>❌ Email to yourself</li><li>❌ Password manager for the seed (only for exchange passwords)</li></ul>"),
            ("test", "Test your backup", "<p>An untested backup is useless. Once a year (or after major moves):</p><ol><li>Recover the wallet on a clean device using the seed</li><li>Verify addresses match</li><li>Close without leaving traces on the test device</li></ol>"),
        ],
        [("Tre copie non sono troppe?", "No. Una può bruciare, una può bagnarsi, una può perdersi. La ridondanza è il punto."),
         ("Posso dare una copia a un familiare?", "Solo se comprende che è come dare le chiavi di casa. Valuta passphrase aggiuntiva (BIP39 passphrase) per protezione extra.")],
        [("Are three copies too many?", "No. One can burn, one can get wet, one can get lost. Redundancy is the point."),
         ("Can I give a copy to a family member?", "Only if they understand it is like giving house keys. Consider an additional passphrase (BIP39 passphrase) for extra protection.")],
    ),
    "sicurezza-mobile": _pair(
        "Il telefono è il wallet più usato dai principianti — e il più rubato, perso o infettato. Pochi accorgimenti riducono drasticamente il rischio.",
        "The phone is the most used wallet for beginners — and the most stolen, lost, or infected. A few precautions drastically reduce risk.",
        [
            ("minaccia", "Perché il mobile è a rischio", "<ul><li>App malevole con permessi eccessivi</li><li>Telefono rubato o smarrito</li><li>Wi-Fi pubblico non sicuro</li><li>Backup cloud del telefono che include screenshot</li></ul>"),
            ("protezione", "Proteggi il dispositivo", "<ol><li>PIN forte (6+ cifre) o passphrase — non solo impronta</li><li>Aggiornamenti OS sempre installati</li><li>Scarica wallet solo da App Store / Play Store ufficiale</li><li>Disattiva backup cloud per app wallet se possibile</li><li>Non fare jailbreak/root se usi wallet con fondi reali</li></ol>"),
            ("wallet-app", "Configurazione wallet mobile", "<ul><li>Attiva biometria <strong>oltre</strong> al PIN del wallet</li><li>Disattiva anteprima notifiche con importi</li><li>Non fare screenshot della seed — mai</li><li>Usa wallet con open source verificabile quando possibile</li></ul>"),
            ("perso", "Se perdi o ti rubano il telefono", "<p>La seed phrase su carta ti salva. Installa il wallet su un nuovo device, importa la seed, verifica i fondi. Cambia password exchange e revoca sessioni attive.</p><div class=\"box box--warning\"><span class=\"box-title\">Senza seed</span>Se non hai backup della seed, i fondi sul telefono perso sono irrecuperabili.</div>"),
        ],
        [
            ("threat", "Why mobile is at risk", "<ul><li>Malicious apps with excessive permissions</li><li>Stolen or lost phone</li><li>Unsafe public Wi-Fi</li><li>Phone cloud backup including screenshots</li></ul>"),
            ("protect", "Protect the device", "<ol><li>Strong PIN (6+ digits) or passphrase — not fingerprint alone</li><li>Always install OS updates</li><li>Download wallets only from official App Store / Play Store</li><li>Disable cloud backup for wallet apps if possible</li><li>Do not jailbreak/root if using wallets with real funds</li></ol>"),
            ("wallet-app", "Mobile wallet setup", "<ul><li>Enable biometrics <strong>in addition to</strong> wallet PIN</li><li>Disable notification previews showing amounts</li><li>Never screenshot the seed</li><li>Use verifiable open-source wallets when possible</li></ul>"),
            ("lost", "If you lose or get robbed", "<p>Paper seed saves you. Install the wallet on a new device, import the seed, verify funds. Change exchange passwords and revoke active sessions.</p><div class=\"box box--warning\"><span class=\"box-title\">Without seed</span>If you have no seed backup, funds on the lost phone are unrecoverable.</div>"),
        ],
        [("Trust Wallet è sicuro?", "È widely usato ma resta un hot wallet. Sicuro per piccole somme se segui le best practice. Per grandi importi usa hardware wallet."),
         ("Devo usare VPN?", "Utile su Wi-Fi pubblico. A casa con rete affidabile è meno critico, ma non sostituisce buone abitudini.")],
        [("Is Trust Wallet safe?", "Widely used but still a hot wallet. Safe for small amounts if you follow best practices. For large holdings use a hardware wallet."),
         ("Should I use a VPN?", "Useful on public Wi-Fi. At home on a trusted network it is less critical, but does not replace good habits.")],
    ),
    "wallet-compromesso": _pair(
        "Sospetti che qualcuno abbia accesso al tuo wallet? Ogni minuto conta. Segui questo piano d'azione senza panico — ma senza perdere tempo.",
        "Suspect someone has access to your wallet? Every minute counts. Follow this action plan without panic — but without wasting time.",
        [
            ("segnali", "Segnali di compromissione", "<ul><li>Transazioni che non hai autorizzato</li><li>Approvazioni sconosciute su revoke.cash</li><li>Login exchange da IP o paese insolito</li><li>Hai inserito la seed su un sito sospetto</li><li>Hai installato un'app o estensione non ufficiale</li></ul>"),
            ("immediato", "Azioni immediate (primi 15 minuti)", "<ol><li><strong>Stop</strong> — non firmare altre transazioni</li><li>Se hai seed sicura altrove: crea <strong>nuovo wallet</strong> su device pulito</li><li>Trasferisci tutti i fondi al nuovo indirizzo con fee alte se serve velocità</li><li>Revoca tutte le approvazioni sul vecchio indirizzo</li></ol><div class=\"box box--danger\"><span class=\"box-title\">Priorità</span>Salvare i fondi prima di capire come è successo.</div>"),
            ("exchange", "Se i fondi sono su exchange", "<ol><li>Cambia password immediatamente</li><li>Revoca API key e sessioni attive</li><li>Attiva o verifica 2FA (authenticator, non SMS)</li><li>Contatta supporto ufficiale solo dal sito verificato</li><li>Preleva verso wallet self-custody se possibile</li></ol>"),
            ("dopo", "Dopo l'emergenza", "<ul><li>Analizza come è avvenuta la compromissione</li><li>Sostituisci device o reinstalla OS se malware</li><li>Nuova seed phrase — non riutilizzare quella compromessa</li><li>Documenta per eventuale denuncia (polizia postale)</li></ul>"),
        ],
        [
            ("signals", "Signs of compromise", "<ul><li>Transactions you did not authorize</li><li>Unknown approvals on revoke.cash</li><li>Exchange login from unusual IP or country</li><li>You entered your seed on a suspicious site</li><li>You installed an unofficial app or extension</li></ul>"),
            ("immediate", "Immediate actions (first 15 minutes)", "<ol><li><strong>Stop</strong> — do not sign more transactions</li><li>If you have a safe seed elsewhere: create a <strong>new wallet</strong> on a clean device</li><li>Transfer all funds to the new address with high fees if speed matters</li><li>Revoke all approvals on the old address</li></ol><div class=\"box box--danger\"><span class=\"box-title\">Priority</span>Save funds before figuring out how it happened.</div>"),
            ("exchange", "If funds are on an exchange", "<ol><li>Change password immediately</li><li>Revoke API keys and active sessions</li><li>Enable or verify 2FA (authenticator, not SMS)</li><li>Contact official support only from verified site</li><li>Withdraw to self-custody wallet if possible</li></ol>"),
            ("after", "After the emergency", "<ul><li>Analyze how the compromise happened</li><li>Replace device or reinstall OS if malware</li><li>New seed phrase — do not reuse the compromised one</li><li>Document for possible report (cyber police)</li></ul>"),
        ],
        [("Posso recuperare fondi rubati?", "Raramente. Le transazioni on-chain sono irreversibili. Agire in tempo è l'unica difesa reale."),
         ("Devo denunciare?", "Consigliato per truffe e phishing. Conserva hash transazioni, URL, screenshot.")],
        [("Can I recover stolen funds?", "Rarely. On-chain transactions are irreversible. Acting in time is the only real defense."),
         ("Should I file a report?", "Recommended for scams and phishing. Keep transaction hashes, URLs, screenshots.")],
    ),
    "password-manager-crypto": _pair(
        "Password manager e crypto vanno d'accordo — ma con regole precise. Gestiscono le password degli exchange, non la seed phrase.",
        "Password managers and crypto go together — but with clear rules. They manage exchange passwords, not the seed phrase.",
        [
            ("perche", "Perché usarne uno", "<ul><li>Password uniche e lunghe per ogni exchange</li><li>Niente riutilizzo tra piattaforme</li><li>2FA backup codes archiviati in modo sicuro</li><li>Condivisione controllata in contesti familiari (vault)</li></ul>"),
            ("scelta", "Quale scegliere", "<p>Opzioni affidabili: <strong>Bitwarden</strong> (open source), 1Password, KeePassXC (locale). Evita soluzioni sconosciute o \"gratis\" senza audit.</p><h3>Configurazione minima</h3><ol><li>Master password lunga (20+ caratteri) o passphrase</li><li>2FA sul vault stesso</li><li>Backup della chiave di recupero del PM in luogo fisico sicuro</li></ol>"),
            ("cosa-mettere", "Cosa mettere nel password manager", "<ul><li>✅ Login exchange, email crypto, API key label</li><li>✅ Backup codes 2FA</li><li>✅ Note su indirizzi wallet (pubblici) e PIN device</li><li>❌ Seed phrase — mai digitale</li><li>❌ Chiavi private raw</li></ul>"),
            ("abitudini", "Abitudini sicure", "<p>Aggiorna password dopo breach noti. Non autocompletare su siti crypto da link email. Usa il PM solo su device che controlli.</p>"),
        ],
        [
            ("why", "Why use one", "<ul><li>Unique, long passwords for each exchange</li><li>No reuse across platforms</li><li>2FA backup codes stored securely</li><li>Controlled sharing in family contexts (vault)</li></ul>"),
            ("choice", "Which to choose", "<p>Reliable options: <strong>Bitwarden</strong> (open source), 1Password, KeePassXC (local). Avoid unknown or \"free\" solutions without audits.</p><h3>Minimum setup</h3><ol><li>Long master password (20+ chars) or passphrase</li><li>2FA on the vault itself</li><li>Backup PM recovery key in a secure physical location</li></ol>"),
            ("what-store", "What to store in the password manager", "<ul><li>✅ Exchange logins, crypto email, API key labels</li><li>✅ 2FA backup codes</li><li>✅ Notes on wallet addresses (public) and device PINs</li><li>❌ Seed phrase — never digital</li><li>❌ Raw private keys</li></ul>"),
            ("habits", "Secure habits", "<p>Update passwords after known breaches. Do not autofill crypto sites from email links. Use the PM only on devices you control.</p>"),
        ],
        [("Bitwarden è abbastanza sicuro?", "Sì, con master password forte e 2FA. Il modello zero-knowledge protegge i dati anche se i server fossero compromessi."),
         ("Posso salvare la seed criptata nel PM?", "Sconsigliato. Un errore di sync, malware o subpoena espone comunque un rischio inaccettabile.")],
        [("Is Bitwarden secure enough?", "Yes, with a strong master password and 2FA. Zero-knowledge model protects data even if servers were compromised."),
         ("Can I store an encrypted seed in the PM?", "Not recommended. Sync errors, malware, or subpoena still pose unacceptable risk.")],
    ),
    "audit-sicurezza-portafoglio": _pair(
        "Un audit di sicurezza non richiede competenze da hacker: è una checklist che verifichi dove custodisci crypto, come proteggi le chiavi e quali abitudini ti espongono al rischio.",
        "A security audit does not require hacker skills: it is a checklist to verify where you store crypto, how you protect keys, and which habits expose you to risk.",
        [
            ("seed", "Seed phrase e backup", "<ul><li>□ Backup su carta/metallo, mai digitale</li><li>□ Almeno 2 copie in luoghi diversi</li><li>□ Test di recupero fatto negli ultimi 12 mesi</li><li>□ Nessuno oltre a te ha accesso non necessario</li></ul>"),
            ("wallet-device", "Wallet e dispositivi", "<ul><li>□ Hot wallet solo per somme operative</li><li>□ Hardware wallet per conservazione principale</li><li>□ Firmware wallet aggiornato</li><li>□ PIN/biometria attivi su telefono e app</li><li>□ Nessuna app wallet da fonti non ufficiali</li></ul>"),
            ("exchange", "Exchange e account", "<ul><li>□ 2FA authenticator (non SMS) su ogni exchange</li><li>□ Password uniche via password manager</li><li>□ Withdrawal whitelist attiva dove disponibile</li><li>□ Nessun fondo significativo lasciato su exchange a lungo</li></ul>"),
            ("defi", "DeFi e approvazioni", "<ul><li>□ Approvazioni token riviste negli ultimi 3 mesi</li><li>□ Nessuna approvazione illimitata su protocolli inattivi</li><li>□ Wallet DeFi separato da wallet principale</li></ul>"),
            ("abitudini", "Abitudini e phishing", "<ul><li>□ Siti ufficiali nei preferiti</li><li>□ Mai seed richiesta da \"supporto\"</li><li>□ Email dedicata per crypto</li><li>□ Sospetti segnalati e revoche fatte</li></ul><div class=\"box box--tip\"><span class=\"box-title\">Frequenza</span>Ripeti l'audit ogni 3-6 mesi o dopo ogni grande acquisto.</div>"),
        ],
        [
            ("seed", "Seed phrase and backup", "<ul><li>□ Backup on paper/metal, never digital</li><li>□ At least 2 copies in different locations</li><li>□ Recovery test done in the last 12 months</li><li>□ No one besides you has unnecessary access</li></ul>"),
            ("wallet-device", "Wallets and devices", "<ul><li>□ Hot wallet only for operational amounts</li><li>□ Hardware wallet for main storage</li><li>□ Wallet firmware updated</li><li>□ PIN/biometrics active on phone and apps</li><li>□ No wallet apps from unofficial sources</li></ul>"),
            ("exchange", "Exchanges and accounts", "<ul><li>□ Authenticator 2FA (not SMS) on every exchange</li><li>□ Unique passwords via password manager</li><li>□ Withdrawal whitelist enabled where available</li><li>□ No significant funds left on exchange long-term</li></ul>"),
            ("defi", "DeFi and approvals", "<ul><li>□ Token approvals reviewed in the last 3 months</li><li>□ No unlimited approvals on inactive protocols</li><li>□ Separate DeFi wallet from main wallet</li></ul>"),
            ("habits", "Habits and phishing", "<ul><li>□ Official sites bookmarked</li><li>□ Never seed requested by \"support\"</li><li>□ Dedicated email for crypto</li><li>□ Suspicious activity reported and revokes done</li></ul><div class=\"box box--tip\"><span class=\"box-title\">Frequency</span>Repeat the audit every 3-6 months or after every major purchase.</div>"),
        ],
        [("Quanto tempo richiede?", "30-45 minuti la prima volta, 15 minuti le volte successive."),
         ("Cosa fare se fallisco molti punti?", "Priorità: seed backup, 2FA, spostare fondi da exchange a self-custody. Un punto alla volta.")],
        [("How long does it take?", "30-45 minutes the first time, 15 minutes afterwards."),
         ("What if I fail many items?", "Priority: seed backup, 2FA, move funds from exchange to self-custody. One item at a time.")],
    ),
    "creare-wallet-sicuro": _pair(
        "Un wallet è il posto dove conservi le tue crypto. Crearne uno sicuro richiede meno di 10 minuti, ma gli errori in questa fase possono costarti tutto.",
        "A wallet is where you store your crypto. Creating a secure one takes less than 10 minutes, but mistakes at this stage can cost you everything.",
        [
            ("tipi-wallet", "Hot wallet vs Cold wallet", "<p>Ci sono due categorie principali:</p><ul><li><strong>Hot wallet</strong> — app o estensione browser, connessi a internet. Comodi per uso quotidiano.</li><li><strong>Cold wallet</strong> — dispositivo hardware offline. Massima sicurezza per conservazione a lungo termine.</li></ul><p>Per iniziare, un hot wallet va benissimo. Per somme importanti, considera un hardware wallet.</p>"),
            ("installazione", "Passo 1: Installare il wallet", "<p>Per principianti consigliamo <strong>Trust Wallet</strong> (mobile) o <strong>MetaMask</strong> (browser + mobile).</p><div class=\"step-block\"><h3>Trust Wallet (smartphone)</h3><ol><li>Scarica solo dall'App Store o Google Play ufficiale</li><li>Apri l'app e seleziona \"Crea nuovo wallet\"</li><li>Imposta un PIN forte o attiva la biometria</li></ol></div><div class=\"box box--danger\"><span class=\"box-title\">Mai</span>Scaricare wallet da link ricevuti via email, Telegram o annunci. Solo store ufficiali.</div>"),
            ("seed-phrase", "Passo 2: Salvare la seed phrase", "<p>L'app ti mostrerà <strong>12 o 24 parole</strong> in un ordine preciso.</p><ol><li>Scrivile su <strong>carta</strong>, nell'ordine esatto</li><li>Verifica due volte ogni parola</li><li>Conservale in un posto sicuro</li><li>Fai una seconda copia in luogo diverso</li></ol><div class=\"box box--danger\"><span class=\"box-title\">Mai</span>Fotografare, screenshot, cloud, email o digitare la seed phrase.</div>"),
            ("verifica", "Passo 3: Verificare il backup", "<p>Il wallet ti chiederà di reinserire alcune parole per confermare il backup. Fallo con calma.</p>"),
            ("primo-uso", "Passo 4: Primo utilizzo", "<ul><li>Fai un <strong>test con pochi centesimi</strong></li><li>Verifica ricezione e invio</li><li>Controlla la transazione su block explorer</li></ul>"),
        ],
        [
            ("wallet-types", "Hot wallet vs cold wallet", "<p>There are two main categories:</p><ul><li><strong>Hot wallet</strong> — app or browser extension, connected to the internet. Convenient for daily use.</li><li><strong>Cold wallet</strong> — offline hardware device. Maximum security for long-term storage.</li></ul><p>To start, a hot wallet is fine. For larger amounts, consider a hardware wallet.</p>"),
            ("install", "Step 1: Install the wallet", "<p>For beginners we recommend <strong>Trust Wallet</strong> (mobile) or <strong>MetaMask</strong> (browser + mobile).</p><div class=\"step-block\"><h3>Trust Wallet (smartphone)</h3><ol><li>Download only from official App Store or Google Play</li><li>Open the app and select \"Create new wallet\"</li><li>Set a strong PIN or enable biometrics</li></ol></div><div class=\"box box--danger\"><span class=\"box-title\">Never</span>Download wallets from links in email, Telegram, or ads. Official stores only.</div>"),
            ("seed-phrase", "Step 2: Save your seed phrase", "<p>The app will show <strong>12 or 24 words</strong> in a specific order.</p><ol><li>Write them on <strong>paper</strong>, in exact order</li><li>Double-check every word</li><li>Store them somewhere safe</li><li>Make a second copy in a different location</li></ol><div class=\"box box--danger\"><span class=\"box-title\">Never</span>Photograph, screenshot, cloud, email, or type your seed phrase.</div>"),
            ("verify", "Step 3: Verify your backup", "<p>The wallet will ask you to re-enter some words to confirm the backup. Take your time.</p>"),
            ("first-use", "Step 4: First use", "<ul><li>Do a <strong>test with a few cents</strong></li><li>Verify receive and send</li><li>Check the transaction on a block explorer</li></ul>"),
        ],
        [("Cosa succede se perdo la seed phrase?", "Perdi accesso permanente. Nessuno può recuperarle. La seed phrase È il tuo wallet."),
         ("Posso usare lo stesso wallet su più dispositivi?", "Sì, importando la stessa seed. Ogni dispositivo in più è un rischio in più.")],
        [("What happens if I lose my seed phrase?", "You permanently lose access. No one can recover it. The seed phrase IS your wallet."),
         ("Can I use the same wallet on multiple devices?", "Yes, by importing the same seed. Each extra device is extra risk.")],
    ),
    "proteggere-seed-phrase": _pair(
        "La seed phrase è la chiave di tutto il tuo portafoglio crypto. Chi la possiede, possiede le tue crypto. Ecco come proteggerla correttamente.",
        "The seed phrase is the key to your entire crypto portfolio. Whoever has it, has your crypto. Here's how to protect it properly.",
        [
            ("cosa-e", "Cos'è la seed phrase", "<p>Sequenza di 12 o 24 parole BIP39 generata dal wallet. Ricrea le chiavi private e recupera l'accesso su qualsiasi device compatibile.</p>"),
            ("come-salvarla", "Come salvarla correttamente", "<p>Strategia <strong>3-2-1</strong>:</p><ul><li><strong>3 copie</strong></li><li><strong>2 supporti</strong> (carta + metallo)</li><li><strong>1 copia</strong> off-site</li></ul><div class=\"box box--tip\"><span class=\"box-title\">Consiglio</span>Piastre in acciaio resistono a fuoco e acqua meglio della carta.</div>"),
            ("errori", "Errori da evitare", "<ul><li>❌ Screenshot o foto</li><li>❌ Note digitali, email, cloud</li><li>❌ Condividere con \"supporto tecnico\"</li><li>❌ Digitare su siti web</li><li>❌ Una sola copia</li></ul>"),
            ("emergenza", "Cosa fare in emergenza", "<p>Se sospetti compromissione:</p><ol><li>Crea <strong>nuovo wallet</strong></li><li>Trasferisci tutti i fondi</li><li>Non usare più il vecchio wallet</li></ol>"),
        ],
        [
            ("what-is", "What is a seed phrase", "<p>A sequence of 12 or 24 BIP39 words generated by your wallet. Recreates private keys and recovers access on any compatible device.</p>"),
            ("how-save", "How to save it correctly", "<p><strong>3-2-1</strong> strategy:</p><ul><li><strong>3 copies</strong></li><li><strong>2 media</strong> (paper + metal)</li><li><strong>1 copy</strong> off-site</li></ul><div class=\"box box--tip\"><span class=\"box-title\">Tip</span>Steel plates resist fire and water better than paper.</div>"),
            ("mistakes", "Mistakes to avoid", "<ul><li>❌ Screenshots or photos</li><li>❌ Digital notes, email, cloud</li><li>❌ Sharing with \"technical support\"</li><li>❌ Typing on websites</li><li>❌ Only one copy</li></ul>"),
            ("emergency", "What to do in an emergency", "<p>If you suspect compromise:</p><ol><li>Create a <strong>new wallet</strong></li><li>Transfer all funds</li><li>Stop using the old wallet</li></ol>"),
        ],
        [("Posso cambiare la seed phrase?", "No. Per una nuova seed crea un nuovo wallet e trasferisci i fondi.")],
        [("Can I change my seed phrase?", "No. For a new seed, create a new wallet and transfer funds.")],
    ),
    "hardware-wallet-ledger": _pair(
        "Un Ledger Nano protegge le chiavi offline. Configurarlo correttamente al primo utilizzo è il passo più importante: la seed viene generata una sola volta.",
        "A Ledger Nano keeps keys offline. Setting it up correctly the first time is the most important step: the seed is generated only once.",
        [
            ("prima", "Prima di iniziare", "<ul><li>Ledger acquistato da ledger.com o rivenditore ufficiale</li><li>Cavo USB funzionante</li><li>PC pulito, senza estensioni sospette</li><li>Carta e penna per la seed — mai digitale</li></ul>"),
            ("setup", "Configurazione iniziale", "<ol><li>Installa <strong>Ledger Live</strong> dal sito ufficiale</li><li>Collega il Nano e seleziona \"Configura come nuovo dispositivo\"</li><li>Scegli PIN (6-8 cifre, non data di nascita)</li><li>Annota le 24 parole nell'ordine mostrato sul device</li><li>Completa il test di verifica parole</li></ol><div class=\"box box--danger\"><span class=\"box-title\">Mai</span>Usare un Ledger con seed già fornita o \"pre-configurato\".</div>"),
            ("app", "Installare app crypto", "<p>In Ledger Live → Manager, installa le app per le chain che usi (Bitcoin, Ethereum, Cardano, ecc.). Ogni blockchain richiede la sua app sul device.</p>"),
            ("prima-tx", "Prima transazione", "<ol><li>Ricevi una piccola somma di test</li><li>Verifica indirizzo sul display del Ledger prima di condividere</li><li>Invia una piccola quantità per confermare invio</li><li>Collega a MetaMask se usi DeFi su Ethereum</li></ol>"),
            ("manutenzione", "Manutenzione", "<ul><li>Aggiorna firmware via Ledger Live regolarmente</li><li>Conserva seed su metallo oltre che carta</li><li>Non prestare il device</li></ul>"),
        ],
        [
            ("before", "Before you start", "<ul><li>Ledger bought from ledger.com or official reseller</li><li>Working USB cable</li><li>Clean PC, no suspicious extensions</li><li>Paper and pen for seed — never digital</li></ul>"),
            ("setup", "Initial setup", "<ol><li>Install <strong>Ledger Live</strong> from official site</li><li>Connect Nano and select \"Set up as new device\"</li><li>Choose PIN (6-8 digits, not birth date)</li><li>Write down 24 words in order shown on device</li><li>Complete word verification test</li></ol><div class=\"box box--danger\"><span class=\"box-title\">Never</span>Use a Ledger with a pre-supplied or \"pre-configured\" seed.</div>"),
            ("apps", "Install crypto apps", "<p>In Ledger Live → Manager, install apps for chains you use (Bitcoin, Ethereum, Cardano, etc.). Each blockchain needs its app on the device.</p>"),
            ("first-tx", "First transaction", "<ol><li>Receive a small test amount</li><li>Verify address on Ledger display before sharing</li><li>Send a small amount to confirm sending</li><li>Connect to MetaMask if using DeFi on Ethereum</li></ol>"),
            ("maintenance", "Maintenance", "<ul><li>Update firmware via Ledger Live regularly</li><li>Store seed on metal as well as paper</li><li>Do not lend the device</li></ul>"),
        ],
        [("Nano S Plus o Nano X?", "S Plus basta per USB desktop. Nano X se vuoi Bluetooth con mobile (valuta rischio extra)."),
         ("Ledger è ancora sicuro dopo i leak?", "Il device resta sicuro se seed non è compromessa. Usa email dedicata e diffida di phishing post-leak.")],
        [("Nano S Plus or Nano X?", "S Plus is enough for USB desktop. Nano X if you want Bluetooth with mobile (weigh extra risk)."),
         ("Is Ledger still safe after the leaks?", "The device remains secure if the seed is not compromised. Use a dedicated email and beware post-leak phishing.")],
    ),
    "cold-wallet-chiavi-offline": _pair(
        "Un cold wallet con chiavi generate offline elimina il rischio che malware sul PC legga la seed durante la creazione. È un approccio avanzato ma accessibile con metodo e pazienza.",
        "A cold wallet with offline-generated keys eliminates the risk of PC malware reading the seed during creation. It is an advanced but accessible approach with method and patience.",
        [
            ("perche-offline", "Perché generare offline", "<p>Su un PC connesso, malware può catturare schermo, clipboard o file durante la generazione. Un ambiente <strong>air-gapped</strong> (senza rete) riduce questa superficie a zero.</p>"),
            ("metodi", "Metodi principali", "<h3>Hardware wallet (consigliato)</h3><p>Ledger/Trezor generano seed nel chip sicuro. Il metodo più pratico per quasi tutti.</p><h3>Wallet su PC offline</h3><p>PC mai connesso + software come Electrum (BTC) o MyEtherWallet offline (ETH). Solo per utenti esperti.</p><h3>Paper wallet</h3><p>Chiave stampata su carta. Obsoleto per molti use case — sconsigliato ai principianti.</p>"),
            ("setup-offline", "Setup air-gapped (avanzato)", "<ol><li>Usa PC/live USB pulito mai connesso dopo download verificato</li><li>Verifica checksum del software (GPG, hash ufficiale)</li><li>Genera seed offline, scrivi su carta</li><li>Trasferisci solo indirizzi pubblici via QR su device secondo</li><li>Firma transazioni offline, broadcast da device online</li></ol>"),
            ("conservazione", "Conservazione chiavi", "<ul><li>Seed su carta + metallo, strategia 3-2-1</li><li>Mai fotografare chiavi private</li><li>Considera passphrase BIP39 aggiuntiva</li></ul><div class=\"box box--warning\"><span class=\"box-title\">Avanzato</span>Se non ti senti pronto, un hardware wallet standard è più che sufficiente.</div>"),
        ],
        [
            ("why-offline", "Why generate offline", "<p>On a connected PC, malware can capture screen, clipboard, or files during generation. An <strong>air-gapped</strong> environment (no network) reduces this surface to zero.</p>"),
            ("methods", "Main methods", "<h3>Hardware wallet (recommended)</h3><p>Ledger/Trezor generate seed in secure chip. Most practical method for almost everyone.</p><h3>Wallet on offline PC</h3><p>Never-connected PC + software like Electrum (BTC) or offline MyEtherWallet (ETH). Experts only.</p><h3>Paper wallet</h3><p>Key printed on paper. Obsolete for many use cases — not recommended for beginners.</p>"),
            ("airgap", "Air-gapped setup (advanced)", "<ol><li>Use clean PC/live USB never connected after verified download</li><li>Verify software checksum (GPG, official hash)</li><li>Generate seed offline, write on paper</li><li>Transfer only public addresses via QR to second device</li><li>Sign transactions offline, broadcast from online device</li></ol>"),
            ("storage", "Key storage", "<ul><li>Seed on paper + metal, 3-2-1 strategy</li><li>Never photograph private keys</li><li>Consider additional BIP39 passphrase</li></ul><div class=\"box box--warning\"><span class=\"box-title\">Advanced</span>If you are not ready, a standard hardware wallet is more than enough.</div>"),
        ],
        [("Serve davvero l'air-gap?", "Per la maggior parte degli utenti no. Hardware wallet moderno offre sicurezza comparabile con meno complessità."),
         ("Paper wallet nel 2026?", "Quasi sempre superato da hardware wallet. Evita salvo casi molto specifici.")],
        [("Do I really need air-gap?", "For most users no. Modern hardware wallets offer comparable security with less complexity."),
         ("Paper wallet in 2026?", "Almost always superseded by hardware wallets. Avoid except very specific cases.")],
    ),
})

SICUREZZA_CATEGORY_SLUGS = [
    "seed-phrase-guida", "hot-vs-cold-wallet", "confronto-hardware-wallet",
    "difendersi-phishing", "approvazioni-smart-contract", "backup-wallet-321",
    "sicurezza-mobile", "wallet-compromesso", "password-manager-crypto",
    "audit-sicurezza-portafoglio",
]