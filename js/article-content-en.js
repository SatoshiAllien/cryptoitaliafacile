const ARTICLE_CONTENT_EN = {
  'iniziare-exchange-revolut-kraken': {
    intro: 'Want to buy your first crypto but don\'t know where to start? In this guide I explain what an exchange is, why Revolut makes life easier, how to choose a reliable platform, and how to make your first purchase on Kraken — step by step, without hype.',
    sections: [
      { id: 'cos-e-exchange', title: 'What is a crypto exchange', content: `
        <p>A <strong>crypto exchange</strong> is a platform where you can buy, sell, and trade cryptocurrencies using euros or other traditional currencies.</p>
        <h3>CEX vs DEX</h3>
        <ul>
          <li><strong>CEX (Centralized Exchange)</strong> — a centralized exchange like Kraken, Coinbase, or Binance. A company runs the platform, temporarily holds your funds, and offers support. Ideal for beginners.</li>
          <li><strong>DEX (Decentralized Exchange)</strong> — a decentralized exchange like Uniswap. You trade peer-to-peer via smart contracts, without an intermediary. More advanced.</li>
        </ul>
        <h3>Why beginners start with a CEX</h3>
        <ul>
          <li>Simple interface, often available in multiple languages</li>
          <li>Deposit euros via bank transfer or card</li>
          <li>Customer support if something goes wrong</li>
          <li>Identity verification (KYC), which offers a minimum of regulatory protection</li>
        </ul>
        <p><strong>Advantages:</strong> ease of use, liquidity, familiar payment methods.</p>
        <p><strong>Limitations:</strong> you don\'t directly control your private keys; you must trust the platform with deposited funds.</p>
        <div class="box box--tip"><span class="box-title">Golden rule</span>The exchange is for buying and selling. To hold crypto long term, move it to a personal wallet.</div>
      `},
      { id: 'perche-revolut', title: 'Why a Revolut account helps you get started', content: `
        <p>It\'s not mandatory, but <strong>Revolut</strong> is one of the most practical tools for getting started with crypto in Europe. Here\'s why.</p>
        <h3>Why it\'s useful</h3>
        <ul>
          <li><strong>Very fast SEPA transfers</strong> to exchanges like Kraken (usually 1 business day)</li>
          <li><strong>Multi-currency account</strong> — euros, dollars, and other currencies in one app</li>
          <li><strong>Virtual card</strong> — useful for card deposits on some exchanges</li>
          <li><strong>Intuitive mobile app</strong> — everything manageable from your phone</li>
        </ul>
        <h3>Why it\'s considered secure</h3>
        <ul>
          <li>Regulated with banking/e-money licenses in several EU countries</li>
          <li>Mandatory identity verification (KYC)</li>
          <li>Standard protections for European digital accounts</li>
          <li>Two-factor authentication available</li>
        </ul>
        <h3>The problem with traditional banks</h3>
        <p>Some traditional Italian banks block or slow down transfers to crypto exchanges. Revolut, being a digital-native fintech, usually doesn\'t have this problem — SEPA transfers to Kraken arrive without issues.</p>
        <h3>How to open a Revolut account</h3>
        <p>You can sign up for free via an invite link. The basic account is free and there are no mandatory costs to get started. Revolut periodically offers bonuses or cashback to new users — promotions vary over time.</p>
        <p><strong>Link to open Revolut:</strong><br>
        <a href="https://revolut.com/referral/?referral-code=stefan2ayd!JUN1-26-AR&geo-redirect" target="_blank" rel="noopener noreferrer">revolut.com/referral — free registration</a></p>
        <div class="box box--warning"><span class="box-title">Transparency</span>This is a referral link: if you sign up through this link, we may receive a small benefit at no extra cost to you. We include it because we actually use it and find it helpful for beginners.</div>
      `},
      { id: 'scegliere-exchange', title: 'How to choose a reliable exchange', content: `
        <p>Before depositing money, check these criteria:</p>
        <ul>
          <li><strong>Security</strong> — mandatory 2FA, no major hacks in its history, cold storage of funds</li>
          <li><strong>Licenses</strong> — regulated in the EU or USA (MiCA in Europe)</li>
          <li><strong>Reputation</strong> — years in operation, reviews, trading volume</li>
          <li><strong>Fees</strong> — spread, deposit/withdrawal fees, trading fees</li>
          <li><strong>Ease of use</strong> — clear interface for beginners</li>
          <li><strong>Deposit methods</strong> — SEPA transfer (ideal with Revolut), card, crypto</li>
        </ul>
        <p><strong>Kraken</strong> meets these criteria: it\'s regulated, active since 2011, with competitive fees and free SEPA deposits. That\'s why we use it as an example in this guide.</p>
      `},
      { id: 'registrazione-exchange', title: 'How to sign up on an exchange', content: `
        <div class="step-block"><h3>Step 1 — Create your account</h3>
        <p>Go to the exchange\'s official website (never from links in email or Telegram). Enter your email and create a <strong>unique, strong password</strong> — don\'t reuse passwords from other sites.</p></div>
        <div class="step-block"><h3>Step 2 — Verify your email</h3>
        <p>Click the confirmation link you receive by email. If it doesn\'t arrive, check your spam folder.</p></div>
        <div class="step-block"><h3>Step 3 — KYC (identity verification)</h3>
        <p>Upload photos of your ID and a selfie. It\'s required by law on regulated exchanges. Processing takes from a few minutes to 24 hours.</p></div>
        <div class="step-block"><h3>Step 4 — Enable 2FA</h3>
        <p>Right after registration, enable <strong>two-factor authentication</strong> with Google Authenticator or Authy. <strong>Never via SMS</strong> if you can avoid it.</p></div>
        <div class="box box--danger"><span class="box-title">Warning</span>Always verify the URL: for Kraken it\'s <strong>kraken.com</strong>. Phishing is the most common scam method.</div>
      `},
      { id: 'deposito-prelievo', title: 'How to deposit and withdraw', content: `
        <h3>Deposit via SEPA bank transfer (recommended)</h3>
        <ol>
          <li>On the exchange, go to "Deposit" → "Euro" → "SEPA transfer"</li>
          <li>Copy the IBAN and reference provided</li>
          <li>From Revolut, send a transfer with those exact details</li>
          <li>Wait 1-2 business days (sometimes just a few hours)</li>
        </ol>
        <h3>Deposit with card</h3>
        <p>Faster but with higher fees (1.5-3%). Use the Revolut virtual card if the exchange accepts it.</p>
        <h3>Crypto deposit</h3>
        <p>If you already have crypto elsewhere, you can send it to the exchange. <strong>Always check the network</strong> (BTC on Bitcoin, ETH on Ethereum, etc.).</p>
        <h3>Different networks — mistakes to avoid</h3>
        <ul>
          <li>BTC → Bitcoin network (BTC)</li>
          <li>ETH → Ethereum network (ERC-20)</li>
          <li>USDT can be ERC-20, TRC-20, or other — you must choose the same network on both send and receive</li>
        </ul>
        <div class="box box--warning"><span class="box-title">Common mistake</span>Sending crypto on the wrong network can cause permanent loss of funds. Check three times before confirming.</div>
      `},
      { id: 'affiliazione-kraken', title: 'Kraken referral program', content: `
        <p>Many exchanges, including Kraken, have a <strong>referral program</strong>: if you sign up through an existing user\'s link, both of you may receive benefits (bonuses, fee discounts) when certain conditions are met.</p>
        <h3>How it works</h3>
        <ol>
          <li>You sign up via the referral link</li>
          <li>You complete KYC verification</li>
          <li>You make your first purchase or reach a minimum threshold</li>
          <li>Any bonuses are credited according to active promotions</li>
        </ol>
        <p><strong>Kraken referral link:</strong><br>
        <a href="https://invite.kraken.com/JDNW/pql7tac5" target="_blank" rel="noopener noreferrer">invite.kraken.com — Kraken registration</a></p>
        <p><strong>Affiliate code:</strong> <code>3h8q8cf5</code></p>
        <div class="box box--warning"><span class="box-title">Transparency</span>This is a referral link. We may receive a commission if you sign up and trade, at no extra cost to you. Bonus promotions depend on Kraken\'s active campaigns and may change.</div>
      `},
      { id: 'primo-acquisto-kraken', title: 'How to make your first purchase on Kraken', content: `
        <div class="step-block"><h3>1. Deposit euros</h3>
        <p>SEPA transfer from Revolut (recommended) or card. Wait until the funds appear in your EUR balance.</p></div>
        <div class="step-block"><h3>2. Go to "Buy crypto"</h3>
        <p>Select Bitcoin (BTC) or another crypto. To start, BTC or ETH are the most common choices.</p></div>
        <div class="step-block"><h3>3. Enter the amount</h3>
        <p>Type how many euros you want to spend (e.g. €50). Check the <strong>total cost</strong> including spread and fees.</p></div>
        <div class="step-block"><h3>4. Confirm the order</h3>
        <p>Review the summary and confirm. The crypto will appear in your Kraken balance.</p></div>
        <div class="step-block"><h3>5. Withdraw to a personal wallet (optional)</h3>
        <p>For amounts you want to hold long term: go to "Withdraw", enter your personal wallet address, select the correct network, and confirm. Do a test with a small amount first.</p></div>
        <div class="box box--tip"><span class="box-title">Tip</span>Start with €20-50 to practice. Better to make mistakes with a little than with a lot.</div>
      `},
      { id: 'sicurezza-principianti', title: 'Security tips for beginners', content: `
        <ul>
          <li>❌ <strong>Don\'t leave large amounts on the exchange</strong> — the exchange is for trading, not storing</li>
          <li>✅ <strong>Always enable 2FA</strong> — with a dedicated app, not SMS</li>
          <li>❌ <strong>Never share your seed phrase</strong> — not even with "support"</li>
          <li>❌ <strong>Don\'t click suspicious links</strong> — always go directly to the site by typing the URL</li>
          <li>✅ <strong>Check the network</strong> before every crypto transfer</li>
          <li>✅ <strong>Use a dedicated email</strong> for exchanges and crypto</li>
          <li>✅ <strong>Keep track of transactions</strong> for tax reporting</li>
        </ul>
      `},
      { id: 'conclusione', title: 'Conclusion', content: `
        <p>Recapping the path to get started:</p>
        <ol>
          <li><strong>Open Revolut</strong> — for fast SEPA transfers to exchanges</li>
          <li><strong>Sign up on Kraken</strong> — a regulated exchange suitable for beginners</li>
          <li><strong>Deposit euros</strong> — transfer from Revolut (low or free fees)</li>
          <li><strong>Buy your first crypto</strong> — start small</li>
          <li><strong>Transfer to a personal wallet</strong> — when you\'re ready to hold long term</li>
        </ol>
        <p>Referral links (Revolut and Kraken) may offer signup benefits at no extra cost. Later, when you feel confident, you can explore personal wallets, the Lightning Network, and DeFi.</p>
        <div class="box box--tip"><span class="box-title">Next steps on The Little Satoshi News</span>
          <ul>
            <li><a href="articolo.html?slug=comprare-bitcoin-prima-volta">How to buy Bitcoin for the first time</a></li>
            <li><a href="articolo.html?slug=creare-wallet-sicuro">How to create a secure wallet</a></li>
            <li><a href="articolo.html?slug=proteggere-seed-phrase">How to protect your seed phrase</a></li>
          </ul>
        </div>
      `}
    ],
    faq: [
      { q: 'Is Revolut required to buy crypto?', a: 'No. You can use any bank that accepts SEPA transfers to crypto exchanges. Revolut is just one of the most convenient and fast options, especially if your traditional bank blocks these transfers.' },
      { q: 'Is Kraken safe?', a: 'Kraken is one of the longest-running exchanges (since 2011), regulated and with a good reputation. No platform is risk-free, but Kraken is considered reliable in the industry.' },
      { q: 'Do referral links cost anything?', a: 'No, nothing changes for you in terms of cost. Referrals reward the inviter and sometimes offer bonuses to the new user, depending on active promotions.' },
      { q: 'How much should I invest the first time?', a: 'Even €20-50 is enough to learn. The goal of the first purchase is to understand the process, not to invest a lot.' },
      { q: 'Can I use only Revolut for crypto?', a: 'Revolut also offers built-in crypto buying, but fees and control differ from a dedicated exchange. To learn and have more choice, an exchange like Kraken is generally preferable.' }
    ]
  },

  'lightning-network-guida': {
    intro: 'Bitcoin is great, but paying €1 in fees for a €2 coffee on-chain doesn\'t make sense. That\'s where the Lightning Network comes in: instant payments in satoshis (sats), with near-zero costs. In this guide I explain everything simply — including Lightning wallets and how to use Satoshi Wallet with its merchant map.',
    sections: [
      { id: 'cos-e-lightning', title: 'What is the Lightning Network', content: `
        <p>The <strong>Lightning Network</strong> (LN) is a payment network built <em>on top of</em> Bitcoin. It doesn\'t replace Bitcoin: it uses it as a security base, but allows you to move small amounts extremely fast.</p>
        <p><strong>Why does it exist?</strong> The Bitcoin blockchain can process a limited number of transactions per second. Every on-chain transaction (on the main blockchain) requires confirmation from miners and pays a fee. For small, frequent payments — a coffee, a tip, an online service — this is slow and expensive.</p>
        <h3>Bitcoin on-chain vs Lightning</h3>
        <ul>
          <li><strong>On-chain</strong> — transaction recorded on the blockchain; secure, but slow (minutes/hours) with variable fees</li>
          <li><strong>Lightning</strong> — off-chain payment via channels; instant with fees of fractions of a cent</li>
        </ul>
        <p><strong>Main advantages:</strong></p>
        <ul>
          <li>⚡ <strong>Speed</strong> — payments in less than a second</li>
          <li>💸 <strong>Very low costs</strong> — often less than €0.01</li>
          <li>🪙 <strong>Micro-payments</strong> — you can send as little as 10 sats (fractions of a cent)</li>
        </ul>
        <div class="box box--tip"><span class="box-title">In simple terms</span>If Bitcoin on-chain is like a bank transfer, Lightning is like paying with your phone at a bar: immediate and practical.</div>
      `},
      { id: 'cosa-sono-sats', title: 'What are SATS', content: `
        <p>A <strong>satoshi</strong> (abbreviated <strong>sat</strong> or <strong>sats</strong>) is the smallest unit of Bitcoin.</p>
        <ul>
          <li><strong>1 BTC = 100,000,000 satoshi</strong> (one hundred million)</li>
          <li>1 sat = 0.00000001 BTC</li>
        </ul>
        <p>Bitcoin is divisible for this reason: you don\'t have to buy a whole Bitcoin. You can own and spend tiny fractions.</p>
        <h3>Why sats for Lightning payments?</h3>
        <p>Lightning payments are almost always discussed in <strong>sats</strong>, not whole BTC. It\'s more intuitive: "this coffee costs 3,500 sats" is more readable than "0.000035 BTC".</p>
        <h3>Practical examples</h3>
        <ul>
          <li><strong>100 sats</strong> — roughly €0.01–0.03 (varies with BTC price)</li>
          <li><strong>3,500 sats</strong> — roughly the cost of a coffee</li>
          <li><strong>10,000 sats</strong> — a few euros, useful for a tip or micro-donation</li>
        </ul>
        <div class="box box--warning"><span class="box-title">Note</span>The euro value of sats changes with Bitcoin\'s price. Always check the equivalent in the app before paying.</div>
      `},
      { id: 'come-scala', title: 'How the Lightning Network scales', content: `
        <h3>Payment channels</h3>
        <p>Two users can open a <strong>payment channel</strong>: they lock a certain amount of Bitcoin in a special on-chain contract, then exchange sats between each other <em>unlimited times</em> without touching the main blockchain.</p>
        <p>When they\'re done, they close the channel and only the final result is recorded on-chain.</p>
        <h3>Payment routing</h3>
        <p>You don\'t need a direct channel with the recipient. The Lightning network finds a <strong>path</strong> through multiple intermediate nodes — like GPS choosing the best route. Each node forwards the payment to the next until it reaches the destination.</p>
        <h3>Why is it instant?</h3>
        <p>Lightning transactions happen <strong>off-chain</strong> (off the blockchain). You don\'t wait for Bitcoin blocks: the payment propagates across the network in milliseconds.</p>
        <h3>Why does it lighten Bitcoin?</h3>
        <p>Millions of Lightning micro-payments don\'t clog the blockchain. Only opening and closing channels require an on-chain transaction. Everything else happens on the Lightning network.</p>
        <div class="box box--tip"><span class="box-title">Analogy</span>The channel is like a prepaid tab at a shop: you load €50 once and then buy cigarettes, newspapers, and scratch cards without paying with your card every time.</div>
      `},
      { id: 'wallet-lightning', title: 'Compatible Lightning wallets', content: `
        <p>To use Lightning you need a <strong>compatible wallet</strong>. Here are the main categories — no commercial preferences, just useful differences.</p>
        <h3>Custodial vs non-custodial</h3>
        <ul>
          <li><strong>Custodial</strong> — a service holds the keys for you. Simpler to start, but you must trust the provider</li>
          <li><strong>Non-custodial</strong> — you control the keys and funds. More secure and sovereign, but requires more attention to backups</li>
        </ul>
        <h3>Custodial wallets (ideal for beginners)</h3>
        <p>Simple apps: download, create an account, receive sats. Often integrate merchant maps and sats purchases with a card. Suited for beginners making small payments.</p>
        <h3>Non-custodial wallets (more control)</h3>
        <p>Require seed phrase backup and sometimes channel management. Better suited for intermediate or advanced users who want full ownership of funds.</p>
        <h3>Wallets with LNURL</h3>
        <p>Support the <strong>LNURL</strong> standard: simplified links and QR codes to receive payments without generating invoices manually each time. Very handy for tips and donations.</p>
        <h3>Wallets with NFC / Tap-to-Pay</h3>
        <p>Some apps let you pay by tapping your phone (NFC), like Apple Pay or Google Pay. Technology still growing, but promising for in-person payments.</p>
        <div class="box box--tip"><span class="box-title">Tip</span>If you\'re just starting out, begin with a simple custodial wallet. When you feel confident, consider a non-custodial wallet for larger amounts.</div>
      `},
      { id: 'configurare-satoshi-wallet', title: 'How to set up Satoshi Wallet', content: `
        <p><strong>Satoshi Wallet</strong> is a mobile app that combines a Lightning wallet, sats purchasing, and a map of merchants that accept Bitcoin. Here\'s the step-by-step setup.</p>
        <div class="step-block"><h3>Step 1 — Download</h3>
        <p>Download the app only from official stores (App Store or Google Play). Verify the developer matches the authentic app.</p></div>
        <div class="step-block"><h3>Step 2 — Create wallet</h3>
        <p>Open the app and follow the guided process: create an account or a new wallet. Read each screen carefully.</p></div>
        <div class="step-block"><h3>Step 3 — Backup</h3>
        <p>If the app shows you a <strong>seed phrase</strong> or recovery keys, write them on paper and store them offline. Don\'t take screenshots. Without a backup, you risk losing your sats.</p></div>
        <div class="step-block"><h3>Step 4 — Receive sats</h3>
        <p>Go to "Receive" and generate a <strong>Lightning invoice</strong> (payment request) for the desired amount. Share the QR code or text code with whoever needs to pay you.</p></div>
        <div class="step-block"><h3>Step 5 — Send sats</h3>
        <p>Go to "Send", scan the recipient\'s QR code or paste the Lightning invoice. Check the amount and recipient, then confirm.</p></div>
        <div class="step-block"><h3>Step 6 — Generate an invoice</h3>
        <p>To request a specific payment: set the amount in sats, add a description (optional), and generate the QR. Valid for a limited time.</p></div>
        <div class="step-block"><h3>Step 7 — Node connection (optional)</h3>
        <p>Some advanced versions let you connect to a personal Lightning node. For most users this isn\'t necessary: the app handles everything automatically.</p></div>
        <div class="box box--danger"><span class="box-title">Never</span>Share your seed phrase, backup screenshots, or credentials with anyone — not even the app\'s "support".</div>
      `},
      { id: 'mappa-satoshi-wallet', title: 'How to use the Satoshi Wallet map', content: `
        <p>One of the most useful features of Satoshi Wallet is the <strong>merchant map</strong> of businesses that accept Lightning payments.</p>
        <div class="step-block"><h3>Open the map</h3>
        <p>In the app, find the <strong>Map</strong> section (globe icon or map pin). Allow location access if you want to find shops near you.</p></div>
        <div class="step-block"><h3>Filter merchants</h3>
        <p>Use filters by category (bars, restaurants, shops, services) or by distance. You can also search by city or business name.</p></div>
        <div class="step-block"><h3>Read shop listings</h3>
        <p>Each pin shows: name, address, type of business, and whether they accept Lightning. Some include photos, hours, and website links.</p></div>
        <div class="step-block"><h3>Pay with QR code</h3>
        <p>At checkout: open "Send" in the app, scan the merchant\'s <strong>Lightning QR</strong>, verify the amount in sats, and confirm. Payment is instant.</p></div>
        <div class="step-block"><h3>Verify the transaction</h3>
        <p>After payment you\'ll see a green checkmark and details in your history. The merchant gets confirmation in real time — no waiting for blocks.</p></div>
        <div class="box box--tip"><span class="box-title">Tip</span>Before visiting a shop, check on the map that it\'s still active and accepts Lightning. Data can change.</div>
      `},
      { id: 'esempi-pratici', title: 'Practical examples', content: `
        <h3>Buying a coffee in sats</h3>
        <p>You walk into a bar and order a cappuccino (3,500 sats). The barista shows the Lightning QR on a tablet. Open Satoshi Wallet → Send → scan → confirm. Done in a second.</p>
        <h3>Sending 100 sats to a friend</h3>
        <p>Your friend generates an invoice for 100 sats (or uses LNURL). You scan their QR and send. An instant digital tip.</p>
        <h3>Paying for an online service</h3>
        <p>A website shows "Pay with Lightning" and a QR. You scan, pay in sats, and the service unlocks immediately — no credit card needed.</p>
        <h3>Micro-donations</h3>
        <p>Want to donate 500 sats to a creator or open-source project? Lightning is perfect: near-zero fees even for tiny amounts.</p>
      `},
      { id: 'conclusione', title: 'Conclusion', content: `
        <p>The <strong>Lightning Network</strong> solves the problem of everyday Bitcoin payments: speed, minimal costs, and micro-transactions.</p>
        <p><strong>Sats</strong> are the ideal unit for thinking about these payments — more practical than whole BTC.</p>
        <p><strong>Lightning wallets</strong> are becoming simpler: apps like Satoshi Wallet lower the barrier for non-technical users.</p>
        <p>The <strong>merchant map</strong> connects theory to practice: find who accepts Bitcoin in the real world and pay with a QR.</p>
        <div class="box box--tip"><span class="box-title">Next steps</span>
          <ul>
            <li>Read the guide <a href="articolo.html?slug=comprare-bitcoin-prima-volta">How to buy Bitcoin</a> if you don\'t have BTC yet</li>
            <li>See <a href="articolo.html?slug=proteggere-seed-phrase">How to protect your seed phrase</a> before using any wallet</li>
            <li>Explore the <a href="glossario/index.html">glossary</a> for terms you don\'t know</li>
          </ul>
        </div>
      `}
    ],
    faq: [
      { q: 'Is the Lightning Network safe?', a: 'Yes, it\'s built on top of Bitcoin\'s security. Channels use smart contracts that prevent fraud. However, use only trusted wallets and always back up your seed phrase.' },
      { q: 'Do I need on-chain Bitcoin to use Lightning?', a: 'Yes, you usually need BTC first (on-chain or bought in the app) and then transfer it to your Lightning wallet. Some custodial apps simplify this step.' },
      { q: 'What happens if my phone breaks?', a: 'If you saved your seed phrase, you can restore the wallet on a new device. Without a backup, funds on non-custodial wallets may be lost.' },
      { q: 'Is Satoshi Wallet the only app with a merchant map?', a: 'No, other maps and directories exist (like BTCmap.org). Satoshi Wallet integrates map and wallet in one app for convenience.' },
      { q: 'Can I pay with Lightning in Italy?', a: 'Yes, but adoption is still growing. The map helps you find places that accept Lightning. Major cities have more options than small towns.' }
    ]
  },

  'comprare-bitcoin-prima-volta': {
    intro: 'Want to buy Bitcoin but don\'t know where to start? In this guide I explain everything step by step: from choosing an exchange to securing your first purchase. No hype, just practical instructions.',
    sections: [
      { id: 'cosa-serve', title: 'What you need before you start', content: `
        <p>To buy Bitcoin you only need three things:</p>
        <ul>
          <li><strong>ID document</strong> — regulated exchanges require KYC verification</li>
          <li><strong>Bank account or card</strong> — to deposit euros</li>
          <li><strong>A bit of patience</strong> — verification can take from a few minutes to 24 hours</li>
        </ul>
        <div class="box box--tip"><span class="box-title">Practical tip</span>Start with a small amount (even €20) to get familiar with the process before investing larger sums.</div>
      `},
      { id: 'scegliere-exchange', title: 'Step 1: Choose a secure exchange', content: `
        <p>An exchange is a platform where you can buy and sell crypto with euros. For Italy, I recommend regulated exchanges such as:</p>
        <ul>
          <li><strong>Kraken</strong> — regulated, good reputation, competitive fees</li>
          <li><strong>Coinbase</strong> — very intuitive for beginners</li>
          <li><strong>Young Platform</strong> — Italian exchange with Italian-language support</li>
        </ul>
        <div class="box box--warning"><span class="box-title">Warning</span>Always verify the URL is correct before entering your credentials. Phishing is the most common scam method.</div>
      `},
      { id: 'registrazione', title: 'Step 2: Registration and verification', content: `
        <div class="step-block"><h3>2.1 Create your account</h3>
        <p>Go to the exchange\'s official website, click "Sign up", and enter your email. Choose a strong, unique password.</p></div>
        <div class="step-block"><h3>2.2 Enable 2FA</h3>
        <p>Right after registration, enable two-factor authentication with an app like Google Authenticator or Authy. <strong>Never via SMS.</strong></p></div>
        <div class="step-block"><h3>2.3 Complete KYC</h3>
        <p>Upload photos of your ID and a selfie. It\'s a regulatory requirement, not optional.</p></div>
      `},
      { id: 'deposito', title: 'Step 3: Deposit euros', content: `
        <p>Once verified, go to "Deposit" and choose your method:</p>
        <ul>
          <li><strong>SEPA transfer</strong> — low or free fees, 1-2 business days</li>
          <li><strong>Credit/debit card</strong> — instant, but higher fees (1.5-3%)</li>
        </ul>
      `},
      { id: 'acquisto', title: 'Step 4: Buy Bitcoin', content: `
        <div class="step-block"><h3>4.1 Go to "Buy" or "Trade"</h3>
        <p>Find BTC/EUR and select "Instant buy" if you\'re a beginner.</p></div>
        <div class="step-block"><h3>4.2 Enter the amount</h3>
        <p>Type how many euros you want to spend (e.g. €50). Check the final price including fees.</p></div>
        <div class="step-block"><h3>4.3 Confirm the order</h3>
        <p>Review the summary and confirm. Bitcoin will appear in your exchange balance.</p></div>
      `},
      { id: 'dopo-acquisto', title: 'Step 5: What to do after buying', content: `
        <p>Your Bitcoin is now on the exchange. For small amounts that\'s fine, but for larger sums:</p>
        <ul>
          <li>Transfer it to a <strong>personal wallet</strong> you control</li>
          <li>Don\'t leave large amounts on the exchange long term</li>
          <li>Keep track of the transaction for tax reporting</li>
        </ul>
        <div class="box box--tip"><span class="box-title">Next step</span>Read our guide on <a href="articolo.html?slug=creare-wallet-sicuro">how to create a secure wallet</a>.</div>
      `}
    ],
    faq: [
      { q: 'How much does it cost to buy Bitcoin?', a: 'It depends on the exchange. Fees range from 0.1% to 3% depending on the payment method. Always check the total cost before confirming.' },
      { q: 'Can I buy fractions of Bitcoin?', a: 'Yes. You can buy as little as 0.0001 BTC (a few euros). You don\'t need to buy a whole Bitcoin.' },
      { q: 'Is it legal to buy Bitcoin in Italy?', a: 'Yes, it\'s perfectly legal. However, you must declare ownership on your tax return if you exceed certain thresholds.' }
    ]
  },

  'creare-wallet-sicuro': {
    intro: 'A wallet is where you store your crypto. Creating a secure one takes less than 10 minutes, but mistakes at this stage can cost you everything. Follow this guide carefully.',
    sections: [
      { id: 'tipi-wallet', title: 'Hot wallet vs cold wallet', content: `
        <p>There are two main categories:</p>
        <ul>
          <li><strong>Hot wallet</strong> — app or browser extension, connected to the internet. Convenient for daily use.</li>
          <li><strong>Cold wallet</strong> — offline hardware device. Maximum security for long-term storage.</li>
        </ul>
        <p>To start, a hot wallet is fine. For larger amounts, consider a hardware wallet.</p>
      `},
      { id: 'installazione', title: 'Step 1: Install the wallet', content: `
        <p>For beginners we recommend <strong>Trust Wallet</strong> (mobile) or <strong>MetaMask</strong> (browser + mobile).</p>
        <div class="step-block"><h3>Trust Wallet (smartphone)</h3>
        <ol>
          <li>Download only from the official App Store or Google Play</li>
          <li>Open the app and select "Create new wallet"</li>
          <li>Set a strong PIN or enable biometrics</li>
        </ol></div>
        <div class="box box--danger"><span class="box-title">Never</span>Download wallets from links received via email, Telegram, or ads. Official stores only.</div>
      `},
      { id: 'seed-phrase', title: 'Step 2: Save your seed phrase', content: `
        <p>The app will show you <strong>12 or 24 words</strong> in a specific order. This is your seed phrase (recovery key).</p>
        <ol>
          <li>Write them on <strong>paper</strong>, in the exact order</li>
          <li>Double-check every word</li>
          <li>Store them somewhere safe, away from prying eyes</li>
          <li>Make a second copy and keep it in a different location</li>
        </ol>
        <div class="box box--danger"><span class="box-title">Never</span>Photograph, screenshot, save to cloud, email, or type your seed phrase on a computer.</div>
      `},
      { id: 'verifica', title: 'Step 3: Verify your backup', content: `
        <p>The wallet will ask you to re-enter some words to confirm you saved them correctly. Take your time.</p>
      `},
      { id: 'primo-uso', title: 'Step 4: First use', content: `
        <p>You now have a wallet address for each supported crypto. Before sending large amounts:</p>
        <ul>
          <li>Do a <strong>test with a few cents</strong></li>
          <li>Verify you can receive and send correctly</li>
          <li>Check the transaction on a block explorer</li>
        </ul>
      `}
    ],
    faq: [
      { q: 'What happens if I lose my seed phrase?', a: 'You permanently lose access to your crypto. No one can recover them for you. The seed phrase IS your wallet.' },
      { q: 'Can I use the same wallet on multiple devices?', a: 'Yes, by importing the same seed phrase. But each additional device is an extra risk.' }
    ]
  },

  'proteggere-seed-phrase': {
    intro: 'The seed phrase is the key to your entire crypto portfolio. Whoever has it, has your crypto. Here\'s how to protect it properly.',
    sections: [
      { id: 'cosa-e', title: 'What is a seed phrase', content: `
        <p>It\'s a sequence of 12 or 24 English words (BIP39 standard) generated by your wallet. It\'s used to recreate private keys and recover access to your crypto on any compatible device.</p>
      `},
      { id: 'come-salvarla', title: 'How to save it correctly', content: `
        <p>Follow the <strong>3-2-1</strong> strategy:</p>
        <ul>
          <li><strong>3 copies</strong> of the seed phrase</li>
          <li><strong>2 different media</strong> (e.g. paper + engraved metal)</li>
          <li><strong>1 copy</strong> in a different physical location (e.g. a safe deposit box)</li>
        </ul>
        <div class="box box--tip"><span class="box-title">Tip</span>Steel plates exist for engraving your seed phrase: they resist fire and water better than paper.</div>
      `},
      { id: 'errori', title: 'Mistakes to absolutely avoid', content: `
        <ul>
          <li>❌ Screenshots or photos of your seed phrase</li>
          <li>❌ Saving it in digital notes, email, or cloud</li>
          <li>❌ Sharing it with anyone, including "technical support"</li>
          <li>❌ Typing the words on websites</li>
          <li>❌ Keeping only one copy</li>
        </ul>
      `},
      { id: 'emergenza', title: 'What to do in an emergency', content: `
        <p>If you suspect your seed phrase has been compromised:</p>
        <ol>
          <li>Immediately create a <strong>new wallet</strong></li>
          <li>Transfer all funds to the new address</li>
          <li>Stop using the old wallet</li>
        </ol>
      `}
    ],
    faq: [
      { q: 'Can I change my seed phrase?', a: 'No. It\'s generated once when the wallet is created. To get a new seed, you must create a new wallet and transfer your funds.' }
    ]
  },

  'cardano-spiegato': {
    intro: 'Cardano is a blockchain built on peer-reviewed academic research. Its native cryptocurrency is called ADA. Here\'s everything you need to know, explained without jargon.',
    sections: [
      { id: 'cosa-e', title: 'What is Cardano', content: `
        <p>Cardano is a blockchain platform created by Charles Hoskinson (co-founder of Ethereum). It stands out for:</p>
        <ul>
          <li>An approach based on <strong>scientific research</strong></li>
          <li><strong>Proof-of-Stake</strong> mechanism (Ouroboros)</li>
          <li>Focus on sustainability, scalability, and interoperability</li>
        </ul>
      `},
      { id: 'ada', title: 'What is ADA', content: `
        <p>ADA is Cardano\'s native cryptocurrency. It\'s used for:</p>
        <ul>
          <li>Paying transaction fees</li>
          <li>Participating in <strong>staking</strong> (delegating to pools)</li>
          <li>Governance (voting on proposals with Project Catalyst)</li>
        </ul>
      `},
      { id: 'staking', title: 'Staking on Cardano', content: `
        <p>Unlike Ethereum, staking on Cardano <strong>doesn\'t lock your ADA</strong>. You can delegate to a staking pool and:</p>
        <ul>
          <li>Receive rewards (~3-5% annually)</li>
          <li>Spend or transfer your ADA at any time</li>
          <li>Change pools whenever you want</li>
        </ul>
        <div class="box box--tip"><span class="box-title">Tip</span>Read the full guide: <a href="articolo.html?slug=staking-ada">Staking ADA step by step</a>.</div>
      `},
      { id: 'ecosistema', title: 'The Cardano ecosystem', content: `
        <p>Beyond ADA, on Cardano you\'ll find:</p>
        <ul>
          <li><strong>Native tokens</strong> — assets created directly on the blockchain</li>
          <li><strong>DeFi</strong> — Minswap, SundaeSwap, and other DEXs</li>
          <li><strong>NFTs</strong> — dedicated marketplaces</li>
          <li><strong>Project Catalyst</strong> — community funding system</li>
        </ul>
      `}
    ],
    faq: [
      { q: 'Is Cardano better than Ethereum?', a: 'It depends on your needs. Cardano has lower fees and simpler staking. Ethereum has a more mature DeFi ecosystem. There\'s no absolute "better".' },
      { q: 'How much does a transaction on Cardano cost?', a: 'Typically less than 0.20 ADA (a few cents in euros). Much cheaper than Ethereum.' }
    ]
  },

  'blockchain-5-minuti': {
    intro: 'You hear about blockchain everywhere but still don\'t get what it is? In 5 minutes I\'ll explain the core concept — no formulas, no hype.',
    sections: [
      { id: 'definizione', title: 'Blockchain in simple terms', content: `
        <p>Imagine a <strong>ledger</strong> shared by thousands of computers around the world. Every time someone makes a transaction, it\'s recorded in this ledger. And no one can delete or change past entries.</p>
        <p>This ledger is called a <strong>blockchain</strong> because transactions are grouped into "blocks" linked together like a chain.</p>
      `},
      { id: 'come-funziona', title: 'How it works', content: `
        <ol>
          <li>Alice sends 1 BTC to Bob</li>
          <li>The transaction is proposed to the network</li>
          <li>"Validators" verify that Alice really has 1 BTC</li>
          <li>The transaction is added to a block</li>
          <li>The block is linked to the chain — permanent and immutable</li>
        </ol>
      `},
      { id: 'perche-importa', title: 'Why it matters', content: `
        <ul>
          <li><strong>Decentralization</strong> — no single bank or government controls everything</li>
          <li><strong>Transparency</strong> — all transactions are verifiable</li>
          <li><strong>Immutability</strong> — hard to alter the past</li>
        </ul>
      `}
    ],
    faq: [
      { q: 'Are blockchain and Bitcoin the same thing?', a: 'No. Bitcoin is a cryptocurrency that uses blockchain technology. Blockchain is the underlying technology, also used by Ethereum, Cardano, and many others.' }
    ]
  },

  'cardano-science-first': {
    subtitle: 'eUTxO, staking, governance, Hydra, Mithril, and a layered scalability roadmap — explained for readers in Italy, Egypt, and beyond.',
    intro: 'Blockchain technology has moved well beyond early experimentation. Today it underpins digital identity, financial infrastructure, and decentralized applications for governments, enterprises, and developers worldwide — including growing communities in <strong>Italy</strong>, <strong>Egypt</strong>, and across Europe and the Middle East. Among the major platforms in this space, <strong>Cardano</strong> stands out for one defining choice: it was engineered from the ground up as a peer-reviewed, research-driven <strong>blockchain</strong>, not as a rapid prototype refined under live traffic.',
    sections: [
      { id: 'what-is-cardano', title: 'What Is Cardano?', content: `
        <p><strong>Cardano</strong> is a proof-of-stake <strong>blockchain</strong> platform built to host decentralized applications, digital assets, and governance systems without relying on a central authority. Launched in 2017 by Ethereum co-founder Charles Hoskinson, it introduced its native cryptocurrency <strong>ADA</strong> and a layered architecture designed to balance security, <strong>scalability</strong>, and <strong>decentralization</strong>.</p>
        <p>Unlike networks that prioritize speed of deployment, Cardano follows a deliberate philosophy: every major protocol change is grounded in academic research, formal verification, and community consensus.</p>
        <p>Think of Cardano less like a startup shipping features every quarter and more like civil engineering. Bridges and power grids are designed, stress-tested, and certified before they carry real traffic. Cardano applies that same discipline to distributed ledger technology.</p>
        <p>The network is organized around distinct developmental eras:</p>
        <ul>
          <li><strong>Byron</strong> — network launch and basic functionality</li>
          <li><strong>Shelley</strong> — <strong>decentralization</strong> through stake pool operation</li>
          <li><strong>Goguen</strong> — <strong>smart contract</strong> deployment via Plutus</li>
          <li><strong>Basho</strong> — <strong>scalability</strong> and performance optimization</li>
          <li><strong>Voltaire</strong> — on-chain governance and treasury management</li>
        </ul>
        <p>Today, Cardano operates as a fully functional <strong>Web3</strong> platform supporting smart contracts, on-chain governance, and a steadily expanding ecosystem.</p>
      `},
      { id: 'peer-reviewed', title: 'Peer-Reviewed Foundations: Why Science Matters', content: `
        <p>Most blockchains are built on whitepapers and production iteration. Cardano took a different path. Its core protocols, including the <strong>Ouroboros</strong> proof-of-stake consensus mechanism, were developed through university partnerships and published in peer-reviewed conferences.</p>
        <p>Ouroboros was among the first proof-of-stake protocols with mathematically proven security guarantees under clearly defined assumptions. Rather than asking users to trust marketing claims, Cardano invites scrutiny from cryptographers, academics, and independent auditors worldwide.</p>
        <p>This research-first model delivers practical benefits:</p>
        <ul>
          <li><strong>Formal methods</strong> reduce the risk of consensus bugs and economic exploits</li>
          <li><strong>Peer review</strong> surfaces vulnerabilities before they reach mainnet</li>
          <li><strong>Reproducibility</strong> allows other teams to verify and build upon Cardano's work</li>
          <li><strong>Long-term stability</strong> favors protocols designed for decades, not hype cycles</li>
        </ul>
        <p>For organizations evaluating <strong>blockchain</strong> infrastructure — whether a European public agency, a fintech in Cairo, or a global supply-chain operator — this matters. Critical systems cannot be anchored to unverified code.</p>
      `},
      { id: 'architecture', title: 'Architecture: UTxO, eUTxO, Staking, and Governance', content: `
        <h3>The UTxO model</h3>
        <p>Cardano uses a <strong>UTxO</strong> (Unspent Transaction Output) accounting model, the same foundational structure employed by Bitcoin. Transactions consume existing outputs and create new ones — like paying with cash and receiving change, rather than editing a central balance entry.</p>
        <p>UTxO models offer predictable parallelization, strong auditability, and cleaner security boundaries than account-based alternatives.</p>
        <h3>Extended UTxO (eUTxO)</h3>
        <p>Cardano extends UTxO into <strong>eUTxO</strong>, enabling <strong>smart contracts</strong> while preserving UTxO advantages. Transaction outputs can carry datum (arbitrary data) and be locked by validator scripts.</p>
        <ul>
          <li><strong>Deterministic execution</strong> — contract outcomes are knowable before submission</li>
          <li><strong>Composable security</strong> — each UTxO is an isolated state unit</li>
          <li><strong>Parallel processing potential</strong> — independent UTxOs can be processed concurrently</li>
        </ul>
        <h3>Staking and decentralization</h3>
        <p>Cardano achieves consensus through <strong>staking</strong>, not energy-intensive mining. <strong>ADA</strong> holders delegate stake to community-operated pools without locking their funds.</p>
        <ul>
          <li><strong>No lock-up requirement</strong> — ADA remains liquid while delegated</li>
          <li><strong>Incentivized honesty</strong> — pools earn rewards for valid block production</li>
          <li><strong>Broad participation</strong> — thousands of independent stake pools operate globally</li>
        </ul>
        <div class="box box--tip"><span class="box-title">Deep dive</span>Read the full guide: <a href="articolo.html?slug=staking-ada">Staking ADA step by step</a>.</div>
        <h3>On-chain governance</h3>
        <p>Cardano's <strong>Voltaire</strong> era introduces mature governance through Cardano Improvement Proposals (CIPs). A treasury system allocates resources to ecosystem development based on collective decisions — enabling adaptive evolution without centralized gatekeeping.</p>
      `},
      { id: 'unique-strengths', title: 'What Sets Cardano Apart?', content: `
        <table class="compare-table">
          <thead><tr><th>Dimension</th><th>Cardano's approach</th></tr></thead>
          <tbody>
            <tr><td>Development</td><td>Peer-reviewed research and formal verification</td></tr>
            <tr><td>Execution</td><td>eUTxO with deterministic smart contracts</td></tr>
            <tr><td>Consensus</td><td>Ouroboros proof-of-stake with proven security bounds</td></tr>
            <tr><td>Energy</td><td>Minimal consumption relative to proof-of-work</td></tr>
            <tr><td>Governance</td><td>On-chain voting and treasury via Voltaire</td></tr>
            <tr><td>Philosophy</td><td>Incremental, evidence-based deployment</td></tr>
          </tbody>
        </table>
        <p>Where some platforms optimize for maximum transactions per second at launch, Cardano optimizes for correctness first and scales second. That trade-off appeals to builders creating identity systems, supply chain tracking, educational credentials, and regulated financial instruments.</p>
      `},
      { id: 'scalability', title: 'The Scalability Roadmap', content: `
        <p><strong>Scalability</strong> is the defining challenge of modern <strong>blockchain</strong> design. Cardano addresses it through a multi-layered roadmap.</p>
        <h3>Hydra: Layer-2 state channels</h3>
        <p><strong>Hydra</strong> enables off-chain state channels where participants execute transactions rapidly, settling final state on the main chain only when needed — like a restaurant tab settled once at the end of the meal.</p>
        <div class="box box--tip"><span class="box-title">Learn more</span><a href="articolo.html?slug=hydra-cardano">Hydra on Cardano: full guide</a></div>
        <h3>Mithril: Lightweight chain verification</h3>
        <p><strong>Mithril</strong> lets users verify blockchain state without downloading the entire history. Using cryptographic multi-signatures and stake-based thresholds, lightweight clients — mobile wallets, browsers — can trustlessly verify the chain with minimal data. Crucial for regions with limited bandwidth, including parts of North Africa and rural Europe.</p>
        <h3>Leios and Input Endorsers: Layer-1 throughput</h3>
        <p><strong>Leios</strong> and <strong>Input Endorsers</strong> target base-layer performance. Input Endorsers separate transaction endorsement from block production, pipelining validation and increasing capacity without compromising Ouroboros security assumptions.</p>
        <p>Together, these form a coherent strategy:</p>
        <ul>
          <li><strong>Input Endorsers and Leios</strong> — increase layer-1 capacity</li>
          <li><strong>Hydra</strong> — offload high-frequency activity to layer-2</li>
          <li><strong>Mithril</strong> — keep verification accessible as the chain grows</li>
        </ul>
      `},
      { id: 'use-cases', title: 'Real-World Use Cases and Ecosystem Growth', content: `
        <p>Cardano's architecture translates into tangible applications:</p>
        <ul>
          <li><strong>Identity and credentials</strong> — verifiable digital identities and educational certificates in Africa and beyond</li>
          <li><strong>Supply chain traceability</strong> — product origin data for Mediterranean exports and cross-border trade corridors linking Europe, North Africa, and the Middle East</li>
          <li><strong>Financial inclusion</strong> — DeFi protocols providing lending and swapping in underserved regions</li>
          <li><strong>Government and enterprise pilots</strong> — tamper-resistant record-keeping, voting systems, and inter-agency data sharing</li>
          <li><strong>Developer ecosystem</strong> — Plutus, Aiken, and Marlowe for builders with varied backgrounds</li>
        </ul>
        <div class="box box--tip"><span class="box-title">DeFi on Cardano</span><a href="articolo.html?slug=cardano-defi">Cardano DeFi: Minswap, SundaeSwap and more</a></div>
        <p>Growth is measured in deployed applications and active users — consistent with Cardano's long-horizon ethos.</p>
      `},
      { id: 'explore-more', title: 'Going Deeper: Explore the Cardano Hub', content: `
        <p>Blockchain education remains fragmented. Newcomers benefit most from curated, sequential learning paths — from wallet setup and staking mechanics to smart contract concepts and ecosystem projects.</p>
        <p>For a structured walkthrough of the full Cardano ecosystem, explore <a href="cardano/index.html">Steven's Cardano guide hub</a> on Crypto Italia Facile. It bridges the gap between high-level overviews like this article and the hands-on knowledge required to participate meaningfully in the ecosystem.</p>
        <p>Whether you are a developer evaluating Plutus, a delegate choosing a stake pool, or curious about proof-of-stake governance in practice, a structured guide accelerates understanding far faster than scattered search results.</p>
        <p><strong>Start here:</strong> <a href="https://satoshiallien.github.io/cryptoitaliafacile/cardano/index.html" target="_blank" rel="noopener noreferrer">Cardano ecosystem hub — Crypto Italia Facile</a></p>
      `},
      { id: 'future', title: 'The Road Ahead: Cardano's Future in Web3', content: `
        <p>Cardano enters its next chapter with foundational elements in place: a live proof-of-stake network, functioning <strong>smart contracts</strong>, an active governance framework, and a pipeline of scaling technologies moving from research to implementation.</p>
        <p>The broader <strong>Web3</strong> movement demands infrastructure that is secure enough for institutions, scalable enough for global applications, and decentralized enough to resist capture. Cardano's bet is that these goals are achievable only through disciplined engineering, open research, and community-governed evolution.</p>
        <p>For developers, Cardano offers a deterministic, formally grounded environment. For community members, a voice in protocol direction. For organizations exploring <strong>blockchain</strong> adoption — in Rome, Milan, Cairo, Alexandria, or anywhere else — a platform whose design choices are documented, scrutinized, and intentionally conservative.</p>
        <p>The direction is clear: Cardano aims to be durable infrastructure — the kind of <strong>blockchain</strong> still operating, still decentralized, and still useful decades from now.</p>
        <p>Learn the architecture. Explore the <a href="cardano/index.html">ecosystem</a>. Engage with the community. And when you are ready to move from concept to practice, <a href="https://satoshiallien.github.io/cryptoitaliafacile/cardano/index.html" target="_blank" rel="noopener noreferrer">Steven's Cardano guide</a> can help you take the next step with confidence.</p>
        <div class="box box--warning"><span class="box-title">Disclaimer</span>This article is for educational purposes only and does not constitute financial advice.</div>
      `}
    ],
    faq: [
      { q: 'Is Cardano a proof-of-stake blockchain?', a: 'Yes. Cardano uses the Ouroboros proof-of-stake consensus mechanism, which is backed by peer-reviewed academic research and proven security guarantees.' },
      { q: 'What is the difference between UTxO and eUTxO?', a: 'UTxO is the basic transaction model where outputs are spent and new ones created. eUTxO extends this with datum and validator scripts, enabling smart contracts while keeping deterministic execution.' },
      { q: 'How does Cardano scale?', a: 'Through a layered approach: Input Endorsers and Leios improve layer-1 throughput, Hydra provides layer-2 state channels, and Mithril enables lightweight verification for mobile and low-bandwidth users.' },
      { q: 'Where can I learn more about Cardano step by step?', a: 'Visit the Cardano hub at satoshiallien.github.io/cryptoitaliafacile/cardano/ for structured guides on wallets, staking, DeFi, and more.' }
    ]
  },

};