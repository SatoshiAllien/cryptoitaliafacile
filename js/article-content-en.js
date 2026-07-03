const ARTICLE_CONTENT_EN = {
  'iniziare-exchange-revolut-kraken': {
    intro: 'Want to buy your first crypto but don\'t know where to start? In this guide I explain what an exchange is, why Revolut makes life easier, how to choose a reliable platform, and how to make your first purchase on Kraken — step by step, without hype.',
    sections: [
      { id: 'cos-e-exchange', title: 'What Is a Crypto Exchange?', content: `
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
        <p>Here\'s a recap of the path to get started:</p>
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
      { id: 'cos-e-lightning', title: 'What Is the Lightning Network?', content: `
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
      { id: 'cosa-sono-sats', title: 'What Are Satoshis (Sats)?', content: `
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
          <li><strong>Young Platform</strong> — Italy-based exchange with local-language support</li>
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
      { q: 'What happens if I lose my seed phrase?', a: 'You permanently lose access to your funds. No one can recover them for you. The seed phrase is your wallet.' },
      { q: 'Can I use the same wallet on multiple devices?', a: 'Yes, by importing the same seed phrase. But each additional device is an extra risk.' }
    ]
  },
  'trasferire-crypto-exchange': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this step-by-step guide covers <strong>How to transfer crypto from an exchange to a personal wallet</strong>. Safe withdrawal: network, address, fees and transaction verification.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Safe withdrawal: network, address, fees and transaction verification.</p><p>In this step-by-step guide, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Safe withdrawal: network, address, fees and transaction verification.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Always verify the platform is regulated, enable two-factor authentication, and double-check deposit and withdrawal networks before moving funds. Your seed phrase is the master key to your funds. Write it on paper, never store it digitally, and test with a small amount before transferring larger balances.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Always verify the platform is regulated, enable two-factor authentication, and double-check deposit and withdrawal networks before moving funds. Your seed phrase is the master key to your funds. Write it on paper, never store it digitally, and test with a small amount before transferring larger balances.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Always verify the platform is regulated, enable two-factor authentication, and double-check deposit and withdrawal networks before moving funds. Your seed phrase is the master key to your funds. Write it on paper, never store it digitally, and test with a small amount before transferring larger balances.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this step-by-step guide take?', a: 'Most readers complete it in about 8 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'staking-ethereum': {
    intro: 'If you already understand wallets and exchanges, this step-by-step guide covers <strong>How to stake Ethereum: step-by-step guide</strong>. Direct staking, liquid staking and what to expect in terms of returns.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Direct staking, liquid staking and what to expect in terms of returns.</p><p>In this step-by-step guide, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Direct staking, liquid staking and what to expect in terms of returns.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Ethereum powers most of DeFi and NFT activity. Confirm you are on the correct network (mainnet or an approved layer 2) before signing any transaction. Staking rewards depend on network conditions and pool performance. Never share private keys — legitimate staking only requires delegation, not custody transfer.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Ethereum powers most of DeFi and NFT activity. Confirm you are on the correct network (mainnet or an approved layer 2) before signing any transaction. Staking rewards depend on network conditions and pool performance. Never share private keys — legitimate staking only requires delegation, not custody transfer.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Ethereum powers most of DeFi and NFT activity. Confirm you are on the correct network (mainnet or an approved layer 2) before signing any transaction. Staking rewards depend on network conditions and pool performance. Never share private keys — legitimate staking only requires delegation, not custody transfer.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>Ethereum powers most of DeFi and NFT activity. Confirm you are on the correct network (mainnet or an approved layer 2) before signing any transaction. Staking rewards depend on network conditions and pool performance. Never share private keys — legitimate staking only requires delegation, not custody transfer.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this step-by-step guide take?', a: 'Most readers complete it in about 12 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'usare-metamask': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this step-by-step guide covers <strong>How to use MetaMask: installation and first transaction</strong>. Install MetaMask, configure the network and send your first transaction.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Install MetaMask, configure the network and send your first transaction.</p><p>In this step-by-step guide, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Install MetaMask, configure the network and send your first transaction.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Your seed phrase is the master key to your funds. Write it on paper, never store it digitally, and test with a small amount before transferring larger balances.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Your seed phrase is the master key to your funds. Write it on paper, never store it digitally, and test with a small amount before transferring larger balances.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Your seed phrase is the master key to your funds. Write it on paper, never store it digitally, and test with a small amount before transferring larger balances.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>Your seed phrase is the master key to your funds. Write it on paper, never store it digitally, and test with a small amount before transferring larger balances.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this step-by-step guide take?', a: 'Most readers complete it in about 10 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'leggere-indirizzo-wallet': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this step-by-step guide covers <strong>How to read a wallet address and verify a transaction</strong>. Understanding addresses, transaction hashes and block explorers.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Understanding addresses, transaction hashes and block explorers.</p><p>In this step-by-step guide, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Understanding addresses, transaction hashes and block explorers.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this step-by-step guide take?', a: 'Most readers complete it in about 7 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'dichiarare-crypto-italia': {
    intro: 'If you already understand wallets and exchanges, this step-by-step guide covers <strong>How to declare crypto in Italy (practical overview)</strong>. RW form, RT section and tax obligations explained simply.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>RW form, RT section and tax obligations explained simply.</p><p>In this step-by-step guide, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>RW form, RT section and tax obligations explained simply.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this step-by-step guide take?', a: 'Most readers complete it in about 14 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'scegliere-exchange-sicuro': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this step-by-step guide covers <strong>How to choose a safe exchange: 7-point checklist</strong>. Regulation, reputation, fees and security: what to check.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Regulation, reputation, fees and security: what to check.</p><p>In this step-by-step guide, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Regulation, reputation, fees and security: what to check.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Always verify the platform is regulated, enable two-factor authentication, and double-check deposit and withdrawal networks before moving funds. Security in crypto is cumulative: strong passwords, hardware wallets for large holdings, and skepticism toward unsolicited messages.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Always verify the platform is regulated, enable two-factor authentication, and double-check deposit and withdrawal networks before moving funds. Security in crypto is cumulative: strong passwords, hardware wallets for large holdings, and skepticism toward unsolicited messages.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Always verify the platform is regulated, enable two-factor authentication, and double-check deposit and withdrawal networks before moving funds. Security in crypto is cumulative: strong passwords, hardware wallets for large holdings, and skepticism toward unsolicited messages.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>Always verify the platform is regulated, enable two-factor authentication, and double-check deposit and withdrawal networks before moving funds. Security in crypto is cumulative: strong passwords, hardware wallets for large holdings, and skepticism toward unsolicited messages.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this step-by-step guide take?', a: 'Most readers complete it in about 9 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
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
  'prima-swap-uniswap': {
    intro: 'If you already understand wallets and exchanges, this step-by-step guide covers <strong>How a DEX works: your first swap on Uniswap</strong>. Decentralized exchange, liquidity and your first DeFi operation.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Decentralized exchange, liquidity and your first DeFi operation.</p><p>In this step-by-step guide, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Decentralized exchange, liquidity and your first DeFi operation.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this step-by-step guide take?', a: 'Most readers complete it in about 13 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'hardware-wallet-ledger': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this step-by-step guide covers <strong>How to set up a Ledger hardware wallet from scratch</strong>. Setup, seed backup and first transaction with Ledger.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Setup, seed backup and first transaction with Ledger.</p><p>In this step-by-step guide, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Setup, seed backup and first transaction with Ledger.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this step-by-step guide take?', a: 'Most readers complete it in about 12 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'capire-gas-fee': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this step-by-step guide covers <strong>How to understand network fees (gas) and when to operate</strong>. Gas on Ethereum and other networks: how to save on fees.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Gas on Ethereum and other networks: how to save on fees.</p><p>In this step-by-step guide, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Gas on Ethereum and other networks: how to save on fees.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Gas fees spike during network congestion. Use block explorers and gas trackers to time transactions when costs are lower.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Gas fees spike during network congestion. Use block explorers and gas trackers to time transactions when costs are lower.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Gas fees spike during network congestion. Use block explorers and gas trackers to time transactions when costs are lower.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this step-by-step guide take?', a: 'Most readers complete it in about 8 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'dca-crypto': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this step-by-step guide covers <strong>How to do DCA (Dollar Cost Averaging) with crypto</strong>. Invest in installments without trying to time the market.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Invest in installments without trying to time the market.</p><p>In this step-by-step guide, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Invest in installments without trying to time the market.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this step-by-step guide take?', a: 'Most readers complete it in about 7 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'verificare-smart-contract': {
    intro: 'For experienced users who want a precise, no-nonsense walkthrough, this step-by-step guide covers <strong>How to verify a smart contract before investing</strong>. Tools and red flags to avoid DeFi scams.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Tools and red flags to avoid DeFi scams.</p><p>In this step-by-step guide, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Tools and red flags to avoid DeFi scams.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Security in crypto is cumulative: strong passwords, hardware wallets for large holdings, and skepticism toward unsolicited messages.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Security in crypto is cumulative: strong passwords, hardware wallets for large holdings, and skepticism toward unsolicited messages.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Security in crypto is cumulative: strong passwords, hardware wallets for large holdings, and skepticism toward unsolicited messages.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>Security in crypto is cumulative: strong passwords, hardware wallets for large holdings, and skepticism toward unsolicited messages.</p>
      `},
      { id: 'step-5-document-for-compliance', title: 'Step 5: Document for compliance', content: `
<p>Log dates, amounts, and platforms used. You will need this for tax reporting and audit trails.</p><p>Security in crypto is cumulative: strong passwords, hardware wallets for large holdings, and skepticism toward unsolicited messages.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this step-by-step guide take?', a: 'Most readers complete it in about 15 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'usare-etherscan': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this step-by-step guide covers <strong>How to use a block explorer (Etherscan explained simply)</strong>. Read transactions, contracts and wallets on Etherscan.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Read transactions, contracts and wallets on Etherscan.</p><p>In this step-by-step guide, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Read transactions, contracts and wallets on Etherscan.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this step-by-step guide take?', a: 'Most readers complete it in about 9 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'cold-wallet-chiavi-offline': {
    intro: 'For experienced users who want a precise, no-nonsense walkthrough, this step-by-step guide covers <strong>How to create a cold wallet with offline keys</strong>. Generate and store private keys without an internet connection.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Generate and store private keys without an internet connection.</p><p>In this step-by-step guide, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Generate and store private keys without an internet connection.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Security in crypto is cumulative: strong passwords, hardware wallets for large holdings, and skepticism toward unsolicited messages.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Security in crypto is cumulative: strong passwords, hardware wallets for large holdings, and skepticism toward unsolicited messages.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Security in crypto is cumulative: strong passwords, hardware wallets for large holdings, and skepticism toward unsolicited messages.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>Security in crypto is cumulative: strong passwords, hardware wallets for large holdings, and skepticism toward unsolicited messages.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this step-by-step guide take?', a: 'Most readers complete it in about 14 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'yield-farming-sicurezza': {
    intro: 'If you already understand wallets and exchanges, this step-by-step guide covers <strong>How to do yield farming safely (first steps)</strong>. Provide liquidity without unnecessary risks: a cautious guide.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Provide liquidity without unnecessary risks: a cautious guide.</p><p>In this step-by-step guide, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Provide liquidity without unnecessary risks: a cautious guide.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this step-by-step guide take?', a: 'Most readers complete it in about 12 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'convertire-crypto-euro': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this step-by-step guide covers <strong>How to convert crypto to euros and withdraw</strong>. Selling on an exchange, bank transfer and timelines.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Selling on an exchange, bank transfer and timelines.</p><p>In this step-by-step guide, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Selling on an exchange, bank transfer and timelines.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Always verify the platform is regulated, enable two-factor authentication, and double-check deposit and withdrawal networks before moving funds.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Always verify the platform is regulated, enable two-factor authentication, and double-check deposit and withdrawal networks before moving funds.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Always verify the platform is regulated, enable two-factor authentication, and double-check deposit and withdrawal networks before moving funds.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this step-by-step guide take?', a: 'Most readers complete it in about 8 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'alert-prezzo-portafoglio': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this step-by-step guide covers <strong>How to set price alerts and monitor your portfolio</strong>. Apps and tools to keep track of your assets.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Apps and tools to keep track of your assets.</p><p>In this step-by-step guide, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Apps and tools to keep track of your assets.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this step-by-step guide take?', a: 'Most readers complete it in about 6 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'recuperare-crypto-sbagliato': {
    intro: 'If you already understand wallets and exchanges, this step-by-step guide covers <strong>How to recover crypto sent to the wrong address</strong>. What can and cannot be recovered: a realistic guide.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>What can and cannot be recovered: a realistic guide.</p><p>In this step-by-step guide, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>What can and cannot be recovered: a realistic guide.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this step-by-step guide take?', a: 'Most readers complete it in about 10 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'tip-mai-seed-phrase': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this Crypto Tip covers <strong>Never share your seed phrase — not even with "support"</strong>. No legitimate service will ever ask for your 12 or 24 recovery words.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>No legitimate service will ever ask for your 12 or 24 recovery words.</p><p>Apply this advice before your next crypto operation — it takes minutes and can prevent irreversible losses.</p>
      `},
      { id: 'the-rule', title: 'The rule', content: `
<p><strong>Never share your seed phrase — not even with "support"</strong> — No legitimate service will ever ask for your 12 or 24 recovery words.</p><p>This is one of the simplest, highest-impact habits in cryptocurrency security and operations.</p>
      `},
      { id: 'how-to-apply-it-today', title: 'How to apply it today', content: `
<ul><li>Review your current setup against this rule before your next transaction</li><li>Adjust wallet, exchange, or browser settings if needed</li><li>Share the practice with anyone who has access to shared devices or accounts</li></ul>
      `},
      { id: 'mistakes-to-avoid', title: 'Mistakes to avoid', content: `
<p>Most losses in crypto come from ignored basics, not sophisticated hacks. Security in crypto is cumulative: strong passwords, hardware wallets for large holdings, and skepticism toward unsolicited messages.</p><div class="box box--warning"><span class="box-title">Warning</span>This content is educational only and does not constitute financial advice.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this Crypto Tip take?', a: 'Most readers complete it in about 2 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'tip-2fa-exchange': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this Crypto Tip covers <strong>Always enable 2FA on your exchange (not via SMS)</strong>. Two-factor authentication with a dedicated app, never SMS.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Two-factor authentication with a dedicated app, never SMS.</p><p>Apply this advice before your next crypto operation — it takes minutes and can prevent irreversible losses.</p>
      `},
      { id: 'the-rule', title: 'The rule', content: `
<p><strong>Always enable 2FA on your exchange (not via SMS)</strong> — Two-factor authentication with a dedicated app, never SMS.</p><p>This is one of the simplest, highest-impact habits in cryptocurrency security and operations.</p>
      `},
      { id: 'how-to-apply-it-today', title: 'How to apply it today', content: `
<ul><li>Review your current setup against this rule before your next transaction</li><li>Adjust wallet, exchange, or browser settings if needed</li><li>Share the practice with anyone who has access to shared devices or accounts</li></ul>
      `},
      { id: 'mistakes-to-avoid', title: 'Mistakes to avoid', content: `
<p>Most losses in crypto come from ignored basics, not sophisticated hacks. Security in crypto is cumulative: strong passwords, hardware wallets for large holdings, and skepticism toward unsolicited messages. Always verify the platform is regulated, enable two-factor authentication, and double-check deposit and withdrawal networks before moving funds.</p><div class="box box--warning"><span class="box-title">Warning</span>This content is educational only and does not constitute financial advice.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this Crypto Tip take?', a: 'Most readers complete it in about 2 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'tip-verifica-url': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this Crypto Tip covers <strong>Verify the exchange URL: phishing starts there</strong>. Always check the address bar before entering credentials.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Always check the address bar before entering credentials.</p><p>Apply this advice before your next crypto operation — it takes minutes and can prevent irreversible losses.</p>
      `},
      { id: 'the-rule', title: 'The rule', content: `
<p><strong>Verify the exchange URL: phishing starts there</strong> — Always check the address bar before entering credentials.</p><p>This is one of the simplest, highest-impact habits in cryptocurrency security and operations.</p>
      `},
      { id: 'how-to-apply-it-today', title: 'How to apply it today', content: `
<ul><li>Review your current setup against this rule before your next transaction</li><li>Adjust wallet, exchange, or browser settings if needed</li><li>Share the practice with anyone who has access to shared devices or accounts</li></ul>
      `},
      { id: 'mistakes-to-avoid', title: 'Mistakes to avoid', content: `
<p>Most losses in crypto come from ignored basics, not sophisticated hacks. Phishing is the most common attack vector in crypto. Type URLs manually, bookmark official sites, and never share recovery phrases.</p><div class="box box--warning"><span class="box-title">Warning</span>This content is educational only and does not constitute financial advice.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this Crypto Tip take?', a: 'Most readers complete it in about 2 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'tip-non-tenere-exchange': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this Crypto Tip covers <strong>Don\'t keep all your crypto on an exchange</strong>. Exchanges are for buying/selling, not long-term storage.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Exchanges are for buying/selling, not long-term storage.</p><p>Apply this advice before your next crypto operation — it takes minutes and can prevent irreversible losses.</p>
      `},
      { id: 'the-rule', title: 'The rule', content: `
<p><strong>Don't keep all your crypto on an exchange</strong> — Exchanges are for buying/selling, not long-term storage.</p><p>This is one of the simplest, highest-impact habits in cryptocurrency security and operations.</p>
      `},
      { id: 'how-to-apply-it-today', title: 'How to apply it today', content: `
<ul><li>Review your current setup against this rule before your next transaction</li><li>Adjust wallet, exchange, or browser settings if needed</li><li>Share the practice with anyone who has access to shared devices or accounts</li></ul>
      `},
      { id: 'mistakes-to-avoid', title: 'Mistakes to avoid', content: `
<p>Most losses in crypto come from ignored basics, not sophisticated hacks. Your seed phrase is the master key to your funds. Write it on paper, never store it digitally, and test with a small amount before transferring larger balances. Always verify the platform is regulated, enable two-factor authentication, and double-check deposit and withdrawal networks before moving funds.</p><div class="box box--warning"><span class="box-title">Warning</span>This content is educational only and does not constitute financial advice.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this Crypto Tip take?', a: 'Most readers complete it in about 2 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'tip-inizia-poco': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this Crypto Tip covers <strong>Start with a small amount: learn before investing big</strong>. Better to make mistakes with €20 than with €2,000.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Better to make mistakes with €20 than with €2,000.</p><p>Apply this advice before your next crypto operation — it takes minutes and can prevent irreversible losses.</p>
      `},
      { id: 'the-rule', title: 'The rule', content: `
<p><strong>Start with a small amount: learn before investing big</strong> — Better to make mistakes with €20 than with €2,000.</p><p>This is one of the simplest, highest-impact habits in cryptocurrency security and operations.</p>
      `},
      { id: 'how-to-apply-it-today', title: 'How to apply it today', content: `
<ul><li>Review your current setup against this rule before your next transaction</li><li>Adjust wallet, exchange, or browser settings if needed</li><li>Share the practice with anyone who has access to shared devices or accounts</li></ul>
      `},
      { id: 'mistakes-to-avoid', title: 'Mistakes to avoid', content: `
<p>Most losses in crypto come from ignored basics, not sophisticated hacks. Start with a small amount to learn the process. The goal of your first operation is understanding the workflow, not maximizing returns.</p><div class="box box--warning"><span class="box-title">Warning</span>This content is educational only and does not constitute financial advice.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this Crypto Tip take?', a: 'Most readers complete it in about 2 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'tip-controlla-rete': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this Crypto Tip covers <strong>Check the network before sending (ERC-20 ≠ BEP-20)</strong>. Sending on the wrong network can be costly.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Sending on the wrong network can be costly.</p><p>Apply this advice before your next crypto operation — it takes minutes and can prevent irreversible losses.</p>
      `},
      { id: 'the-rule', title: 'The rule', content: `
<p><strong>Check the network before sending (ERC-20 ≠ BEP-20)</strong> — Sending on the wrong network can be costly.</p><p>This is one of the simplest, highest-impact habits in cryptocurrency security and operations.</p>
      `},
      { id: 'how-to-apply-it-today', title: 'How to apply it today', content: `
<ul><li>Review your current setup against this rule before your next transaction</li><li>Adjust wallet, exchange, or browser settings if needed</li><li>Share the practice with anyone who has access to shared devices or accounts</li></ul>
      `},
      { id: 'mistakes-to-avoid', title: 'Mistakes to avoid', content: `
<p>Most losses in crypto come from ignored basics, not sophisticated hacks. Move slowly, verify every address and network, and keep records for tax reporting.</p><div class="box box--warning"><span class="box-title">Warning</span>This content is educational only and does not constitute financial advice.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this Crypto Tip take?', a: 'Most readers complete it in about 2 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'tip-rubrica-wallet': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this Crypto Tip covers <strong>Save frequent addresses in your wallet address book</strong>. Avoid typos on addresses you use often.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Avoid typos on addresses you use often.</p><p>Apply this advice before your next crypto operation — it takes minutes and can prevent irreversible losses.</p>
      `},
      { id: 'the-rule', title: 'The rule', content: `
<p><strong>Save frequent addresses in your wallet address book</strong> — Avoid typos on addresses you use often.</p><p>This is one of the simplest, highest-impact habits in cryptocurrency security and operations.</p>
      `},
      { id: 'how-to-apply-it-today', title: 'How to apply it today', content: `
<ul><li>Review your current setup against this rule before your next transaction</li><li>Adjust wallet, exchange, or browser settings if needed</li><li>Share the practice with anyone who has access to shared devices or accounts</li></ul>
      `},
      { id: 'mistakes-to-avoid', title: 'Mistakes to avoid', content: `
<p>Most losses in crypto come from ignored basics, not sophisticated hacks. Your seed phrase is the master key to your funds. Write it on paper, never store it digitally, and test with a small amount before transferring larger balances.</p><div class="box box--warning"><span class="box-title">Warning</span>This content is educational only and does not constitute financial advice.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this Crypto Tip take?', a: 'Most readers complete it in about 2 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'tip-no-screenshot-seed': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this Crypto Tip covers <strong>Screenshot your seed? You\'ve already lost</strong>. Photos in the cloud are an easy target for hackers.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Photos in the cloud are an easy target for hackers.</p><p>Apply this advice before your next crypto operation — it takes minutes and can prevent irreversible losses.</p>
      `},
      { id: 'the-rule', title: 'The rule', content: `
<p><strong>Screenshot your seed? You've already lost</strong> — Photos in the cloud are an easy target for hackers.</p><p>This is one of the simplest, highest-impact habits in cryptocurrency security and operations.</p>
      `},
      { id: 'how-to-apply-it-today', title: 'How to apply it today', content: `
<ul><li>Review your current setup against this rule before your next transaction</li><li>Adjust wallet, exchange, or browser settings if needed</li><li>Share the practice with anyone who has access to shared devices or accounts</li></ul>
      `},
      { id: 'mistakes-to-avoid', title: 'Mistakes to avoid', content: `
<p>Most losses in crypto come from ignored basics, not sophisticated hacks. Move slowly, verify every address and network, and keep records for tax reporting.</p><div class="box box--warning"><span class="box-title">Warning</span>This content is educational only and does not constitute financial advice.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this Crypto Tip take?', a: 'Most readers complete it in about 2 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'tip-diffida-telegram': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this Crypto Tip covers <strong>Beware of "guaranteed returns" on Telegram</strong>. If they promise fixed returns, it\'s almost certainly a scam.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>If they promise fixed returns, it's almost certainly a scam.</p><p>Apply this advice before your next crypto operation — it takes minutes and can prevent irreversible losses.</p>
      `},
      { id: 'the-rule', title: 'The rule', content: `
<p><strong>Beware of "guaranteed returns" on Telegram</strong> — If they promise fixed returns, it's almost certainly a scam.</p><p>This is one of the simplest, highest-impact habits in cryptocurrency security and operations.</p>
      `},
      { id: 'how-to-apply-it-today', title: 'How to apply it today', content: `
<ul><li>Review your current setup against this rule before your next transaction</li><li>Adjust wallet, exchange, or browser settings if needed</li><li>Share the practice with anyone who has access to shared devices or accounts</li></ul>
      `},
      { id: 'mistakes-to-avoid', title: 'Mistakes to avoid', content: `
<p>Most losses in crypto come from ignored basics, not sophisticated hacks. Move slowly, verify every address and network, and keep records for tax reporting.</p><div class="box box--warning"><span class="box-title">Warning</span>This content is educational only and does not constitute financial advice.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this Crypto Tip take?', a: 'Most readers complete it in about 2 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'tip-aggiorna-wallet': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this Crypto Tip covers <strong>Always update wallets and apps</strong>. Updates fix security vulnerabilities.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Updates fix security vulnerabilities.</p><p>Apply this advice before your next crypto operation — it takes minutes and can prevent irreversible losses.</p>
      `},
      { id: 'the-rule', title: 'The rule', content: `
<p><strong>Always update wallets and apps</strong> — Updates fix security vulnerabilities.</p><p>This is one of the simplest, highest-impact habits in cryptocurrency security and operations.</p>
      `},
      { id: 'how-to-apply-it-today', title: 'How to apply it today', content: `
<ul><li>Review your current setup against this rule before your next transaction</li><li>Adjust wallet, exchange, or browser settings if needed</li><li>Share the practice with anyone who has access to shared devices or accounts</li></ul>
      `},
      { id: 'mistakes-to-avoid', title: 'Mistakes to avoid', content: `
<p>Most losses in crypto come from ignored basics, not sophisticated hacks. Security in crypto is cumulative: strong passwords, hardware wallets for large holdings, and skepticism toward unsolicited messages.</p><div class="box box--warning"><span class="box-title">Warning</span>This content is educational only and does not constitute financial advice.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this Crypto Tip take?', a: 'Most readers complete it in about 2 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'tip-email-dedicata': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this Crypto Tip covers <strong>Use a dedicated email for crypto only</strong>. Separate crypto communications from the rest of your digital life.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Separate crypto communications from the rest of your digital life.</p><p>Apply this advice before your next crypto operation — it takes minutes and can prevent irreversible losses.</p>
      `},
      { id: 'the-rule', title: 'The rule', content: `
<p><strong>Use a dedicated email for crypto only</strong> — Separate crypto communications from the rest of your digital life.</p><p>This is one of the simplest, highest-impact habits in cryptocurrency security and operations.</p>
      `},
      { id: 'how-to-apply-it-today', title: 'How to apply it today', content: `
<ul><li>Review your current setup against this rule before your next transaction</li><li>Adjust wallet, exchange, or browser settings if needed</li><li>Share the practice with anyone who has access to shared devices or accounts</li></ul>
      `},
      { id: 'mistakes-to-avoid', title: 'Mistakes to avoid', content: `
<p>Most losses in crypto come from ignored basics, not sophisticated hacks. Security in crypto is cumulative: strong passwords, hardware wallets for large holdings, and skepticism toward unsolicited messages.</p><div class="box box--warning"><span class="box-title">Warning</span>This content is educational only and does not constitute financial advice.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this Crypto Tip take?', a: 'Most readers complete it in about 2 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'tip-leggi-transazione': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this Crypto Tip covers <strong>Before signing a transaction, read what you\'re approving</strong>. Every "Confirm" click can authorize a withdrawal.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Every "Confirm" click can authorize a withdrawal.</p><p>Apply this advice before your next crypto operation — it takes minutes and can prevent irreversible losses.</p>
      `},
      { id: 'the-rule', title: 'The rule', content: `
<p><strong>Before signing a transaction, read what you're approving</strong> — Every "Confirm" click can authorize a withdrawal.</p><p>This is one of the simplest, highest-impact habits in cryptocurrency security and operations.</p>
      `},
      { id: 'how-to-apply-it-today', title: 'How to apply it today', content: `
<ul><li>Review your current setup against this rule before your next transaction</li><li>Adjust wallet, exchange, or browser settings if needed</li><li>Share the practice with anyone who has access to shared devices or accounts</li></ul>
      `},
      { id: 'mistakes-to-avoid', title: 'Mistakes to avoid', content: `
<p>Most losses in crypto come from ignored basics, not sophisticated hacks. Security in crypto is cumulative: strong passwords, hardware wallets for large holdings, and skepticism toward unsolicited messages.</p><div class="box box--warning"><span class="box-title">Warning</span>This content is educational only and does not constitute financial advice.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this Crypto Tip take?', a: 'Most readers complete it in about 2 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'tip-diversifica': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this Crypto Tip covers <strong>Diversify: don\'t put everything on one crypto</strong>. A balanced portfolio reduces concentrated risk.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>A balanced portfolio reduces concentrated risk.</p><p>Apply this advice before your next crypto operation — it takes minutes and can prevent irreversible losses.</p>
      `},
      { id: 'the-rule', title: 'The rule', content: `
<p><strong>Diversify: don't put everything on one crypto</strong> — A balanced portfolio reduces concentrated risk.</p><p>This is one of the simplest, highest-impact habits in cryptocurrency security and operations.</p>
      `},
      { id: 'how-to-apply-it-today', title: 'How to apply it today', content: `
<ul><li>Review your current setup against this rule before your next transaction</li><li>Adjust wallet, exchange, or browser settings if needed</li><li>Share the practice with anyone who has access to shared devices or accounts</li></ul>
      `},
      { id: 'mistakes-to-avoid', title: 'Mistakes to avoid', content: `
<p>Most losses in crypto come from ignored basics, not sophisticated hacks. Move slowly, verify every address and network, and keep records for tax reporting.</p><div class="box box--warning"><span class="box-title">Warning</span>This content is educational only and does not constitute financial advice.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this Crypto Tip take?', a: 'Most readers complete it in about 2 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'tip-traccia-operazioni': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this Crypto Tip covers <strong>Track every operation for tax reporting</strong>. A spreadsheet or tracking app will save you at year-end.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>A spreadsheet or tracking app will save you at year-end.</p><p>Apply this advice before your next crypto operation — it takes minutes and can prevent irreversible losses.</p>
      `},
      { id: 'the-rule', title: 'The rule', content: `
<p><strong>Track every operation for tax reporting</strong> — A spreadsheet or tracking app will save you at year-end.</p><p>This is one of the simplest, highest-impact habits in cryptocurrency security and operations.</p>
      `},
      { id: 'how-to-apply-it-today', title: 'How to apply it today', content: `
<ul><li>Review your current setup against this rule before your next transaction</li><li>Adjust wallet, exchange, or browser settings if needed</li><li>Share the practice with anyone who has access to shared devices or accounts</li></ul>
      `},
      { id: 'mistakes-to-avoid', title: 'Mistakes to avoid', content: `
<p>Most losses in crypto come from ignored basics, not sophisticated hacks. Move slowly, verify every address and network, and keep records for tax reporting.</p><div class="box box--warning"><span class="box-title">Warning</span>This content is educational only and does not constitute financial advice.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this Crypto Tip take?', a: 'Most readers complete it in about 2 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'tip-spread-fee': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this Crypto Tip covers <strong>The price you see isn\'t what you pay (spread + fees)</strong>. Always calculate the total cost of the operation.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Always calculate the total cost of the operation.</p><p>Apply this advice before your next crypto operation — it takes minutes and can prevent irreversible losses.</p>
      `},
      { id: 'the-rule', title: 'The rule', content: `
<p><strong>The price you see isn't what you pay (spread + fees)</strong> — Always calculate the total cost of the operation.</p><p>This is one of the simplest, highest-impact habits in cryptocurrency security and operations.</p>
      `},
      { id: 'how-to-apply-it-today', title: 'How to apply it today', content: `
<ul><li>Review your current setup against this rule before your next transaction</li><li>Adjust wallet, exchange, or browser settings if needed</li><li>Share the practice with anyone who has access to shared devices or accounts</li></ul>
      `},
      { id: 'mistakes-to-avoid', title: 'Mistakes to avoid', content: `
<p>Most losses in crypto come from ignored basics, not sophisticated hacks. Always verify the platform is regulated, enable two-factor authentication, and double-check deposit and withdrawal networks before moving funds.</p><div class="box box--warning"><span class="box-title">Warning</span>This content is educational only and does not constitute financial advice.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this Crypto Tip take?', a: 'Most readers complete it in about 2 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'tip-staking-unlock': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this Crypto Tip covers <strong>Staking: understand the unlock period before locking funds</strong>. Some staking locks funds for days or weeks.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Some staking locks funds for days or weeks.</p><p>Apply this advice before your next crypto operation — it takes minutes and can prevent irreversible losses.</p>
      `},
      { id: 'the-rule', title: 'The rule', content: `
<p><strong>Staking: understand the unlock period before locking funds</strong> — Some staking locks funds for days or weeks.</p><p>This is one of the simplest, highest-impact habits in cryptocurrency security and operations.</p>
      `},
      { id: 'how-to-apply-it-today', title: 'How to apply it today', content: `
<ul><li>Review your current setup against this rule before your next transaction</li><li>Adjust wallet, exchange, or browser settings if needed</li><li>Share the practice with anyone who has access to shared devices or accounts</li></ul>
      `},
      { id: 'mistakes-to-avoid', title: 'Mistakes to avoid', content: `
<p>Most losses in crypto come from ignored basics, not sophisticated hacks. Staking rewards depend on network conditions and pool performance. Never share private keys — legitimate staking only requires delegation, not custody transfer.</p><div class="box box--warning"><span class="box-title">Warning</span>This content is educational only and does not constitute financial advice.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this Crypto Tip take?', a: 'Most readers complete it in about 2 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'tip-test-transazione': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this Crypto Tip covers <strong>New wallet? Test with a few cents first</strong>. Verify everything works before sending large amounts.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Verify everything works before sending large amounts.</p><p>Apply this advice before your next crypto operation — it takes minutes and can prevent irreversible losses.</p>
      `},
      { id: 'the-rule', title: 'The rule', content: `
<p><strong>New wallet? Test with a few cents first</strong> — Verify everything works before sending large amounts.</p><p>This is one of the simplest, highest-impact habits in cryptocurrency security and operations.</p>
      `},
      { id: 'how-to-apply-it-today', title: 'How to apply it today', content: `
<ul><li>Review your current setup against this rule before your next transaction</li><li>Adjust wallet, exchange, or browser settings if needed</li><li>Share the practice with anyone who has access to shared devices or accounts</li></ul>
      `},
      { id: 'mistakes-to-avoid', title: 'Mistakes to avoid', content: `
<p>Most losses in crypto come from ignored basics, not sophisticated hacks. Your seed phrase is the master key to your funds. Write it on paper, never store it digitally, and test with a small amount before transferring larger balances.</p><div class="box box--warning"><span class="box-title">Warning</span>This content is educational only and does not constitute financial advice.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this Crypto Tip take?', a: 'Most readers complete it in about 2 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'tip-no-link-email': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this Crypto Tip covers <strong>Don\'t click crypto links from suspicious emails</strong>. Always go directly to the site by typing the URL.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Always go directly to the site by typing the URL.</p><p>Apply this advice before your next crypto operation — it takes minutes and can prevent irreversible losses.</p>
      `},
      { id: 'the-rule', title: 'The rule', content: `
<p><strong>Don't click crypto links from suspicious emails</strong> — Always go directly to the site by typing the URL.</p><p>This is one of the simplest, highest-impact habits in cryptocurrency security and operations.</p>
      `},
      { id: 'how-to-apply-it-today', title: 'How to apply it today', content: `
<ul><li>Review your current setup against this rule before your next transaction</li><li>Adjust wallet, exchange, or browser settings if needed</li><li>Share the practice with anyone who has access to shared devices or accounts</li></ul>
      `},
      { id: 'mistakes-to-avoid', title: 'Mistakes to avoid', content: `
<p>Most losses in crypto come from ignored basics, not sophisticated hacks. Phishing is the most common attack vector in crypto. Type URLs manually, bookmark official sites, and never share recovery phrases.</p><div class="box box--warning"><span class="box-title">Warning</span>This content is educational only and does not constitute financial advice.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this Crypto Tip take?', a: 'Most readers complete it in about 2 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'tip-pin-wallet': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this Crypto Tip covers <strong>Set a strong PIN on your mobile wallet</strong>. Protect wallet access on your smartphone.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Protect wallet access on your smartphone.</p><p>Apply this advice before your next crypto operation — it takes minutes and can prevent irreversible losses.</p>
      `},
      { id: 'the-rule', title: 'The rule', content: `
<p><strong>Set a strong PIN on your mobile wallet</strong> — Protect wallet access on your smartphone.</p><p>This is one of the simplest, highest-impact habits in cryptocurrency security and operations.</p>
      `},
      { id: 'how-to-apply-it-today', title: 'How to apply it today', content: `
<ul><li>Review your current setup against this rule before your next transaction</li><li>Adjust wallet, exchange, or browser settings if needed</li><li>Share the practice with anyone who has access to shared devices or accounts</li></ul>
      `},
      { id: 'mistakes-to-avoid', title: 'Mistakes to avoid', content: `
<p>Most losses in crypto come from ignored basics, not sophisticated hacks. Security in crypto is cumulative: strong passwords, hardware wallets for large holdings, and skepticism toward unsolicited messages.</p><div class="box box--warning"><span class="box-title">Warning</span>This content is educational only and does not constitute financial advice.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this Crypto Tip take?', a: 'Most readers complete it in about 2 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'tip-non-capisci-non-investi': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this Crypto Tip covers <strong>If you don\'t understand the project, don\'t invest</strong>. The simplest and most effective rule to avoid scams.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>The simplest and most effective rule to avoid scams.</p><p>Apply this advice before your next crypto operation — it takes minutes and can prevent irreversible losses.</p>
      `},
      { id: 'the-rule', title: 'The rule', content: `
<p><strong>If you don't understand the project, don't invest</strong> — The simplest and most effective rule to avoid scams.</p><p>This is one of the simplest, highest-impact habits in cryptocurrency security and operations.</p>
      `},
      { id: 'how-to-apply-it-today', title: 'How to apply it today', content: `
<ul><li>Review your current setup against this rule before your next transaction</li><li>Adjust wallet, exchange, or browser settings if needed</li><li>Share the practice with anyone who has access to shared devices or accounts</li></ul>
      `},
      { id: 'mistakes-to-avoid', title: 'Mistakes to avoid', content: `
<p>Most losses in crypto come from ignored basics, not sophisticated hacks. Move slowly, verify every address and network, and keep records for tax reporting.</p><div class="box box--warning"><span class="box-title">Warning</span>This content is educational only and does not constitute financial advice.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this Crypto Tip take?', a: 'Most readers complete it in about 2 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'trend-mica': {
    subtitle: 'The European regulation reshaping exchanges, stablecoins, and investor rights — explained without legal jargon.',
    intro: '<strong>MiCA</strong> (Markets in Crypto-Assets) is the European Union\'s first comprehensive regulatory framework for cryptocurrencies. It took effect in late 2024, and by <strong>2026</strong> the practical impact is clear: licensed exchanges, stablecoins under oversight, stronger investor protections, and a Europe positioning itself to compete with the US and Asia. Here\'s what you need to know — in plain language.',
    sections: [
      { id: 'trasparenza-exchange', title: 'Mandatory Transparency for Exchanges', content: `
        <p>Under MiCA, operating in Europe is no longer a matter of "launch a website and start trading." <strong>Crypto-Asset Service Providers</strong> (CASPs) — exchanges, custody platforms, crypto brokers — must obtain <strong>authorization</strong> from a national competent authority (in Italy, typically the Bank of Italy or Consob, depending on the service).</p>
        <p>What this means for you in practice:</p>
        <ul>
          <li><strong>Mandatory white paper</strong> for public offerings of tokens not already regulated</li>
          <li><strong>Clear disclosure</strong> of risks, fees, and conflicts of interest</li>
          <li><strong>Segregation of client funds</strong> from the operator\'s own assets</li>
          <li><strong>Transaction traceability</strong> and strengthened anti-money laundering procedures</li>
        </ul>
        <p>Non-compliant exchanges must exit the EU market or adapt. In 2026, the list of authorized operators becomes the first filter to check before depositing euros or cryptocurrency.</p>
        <div class="box box--tip"><span class="box-title">How to verify</span>Always check whether a platform declares a MiCA license or VASP registration in your country. Be wary of operators that do not clearly state their regulator and authorization number.</div>
      `},
      { id: 'protezione-investitori', title: 'Investor Protection', content: `
        <p>MiCA introduces rules that bring crypto closer to traditional finance standards — without eliminating market risk, but reducing exposure to <strong>opacity and bad faith</strong>.</p>
        <p>The main pillars:</p>
        <ul>
          <li><strong>Asset classification</strong> — e-money tokens, asset-referenced tokens, and other crypto-assets: each category carries different obligations</li>
          <li><strong>Market manipulation and insider trading bans</strong>, with significant penalties</li>
          <li><strong>Marketing communications</strong> — must be clear, not misleading, and identifiable as advertising</li>
          <li><strong>Complaints and dispute resolution</strong> — mandatory procedures for authorized providers</li>
        </ul>
        <p>For retail investors, the advantage is greater <strong>predictability</strong>: you know whom to contact if something goes wrong and what minimum rights to expect. The risk of losing capital to volatility remains — MiCA is not a price guarantee.</p>
        <div class="box box--warning"><span class="box-title">Important</span>MiCA protects you from non-compliant operators and unfair practices, not from Bitcoin or altcoin price swings. Only invest amounts you can afford to lose.</div>
      `},
      { id: 'stablecoin-regole', title: 'Stablecoins and the New Rules', content: `
        <p>Stablecoins sit at the center of MiCA. The regulation distinguishes primarily between:</p>
        <ul>
          <li><strong>E-Money Tokens (EMT)</strong> — pegged to a fiat currency (e.g. the euro). Issuers must be authorized as electronic money institutions or banks</li>
          <li><strong>Asset-Referenced Tokens (ART)</strong> — pegged to a basket of assets (currencies, commodities, crypto). Stricter capital and governance requirements apply</li>
        </ul>
        <p>The most visible trends in 2026:</p>
        <ul>
          <li>Non-compliant stablecoins <strong>restricted or withdrawn</strong> from the European market</li>
          <li>More room for <strong>regulated euro stablecoins</strong> (fiat-backed with verifiable reserves)</li>
          <li>Greater transparency on <strong>reserves, audits, and redemption</strong> — the peg is no longer just a promise on a website</li>
        </ul>
        <p>If you use stablecoins for trading, DeFi, or simply to park value, verify whether the issuer is authorized in the EU. A stablecoin without MiCA compliance may become difficult to use on European exchanges.</p>
      `},
      { id: 'competitivita-europea', title: 'European Competitiveness', content: `
        <p>Europe has chosen the path of <strong>explicit regulation</strong> while other countries — such as the United States — pursue more fragmented or post-hoc enforcement approaches. 2026 is the test case.</p>
        <p><strong>Strengths</strong> for the EU ecosystem:</p>
        <ul>
          <li><strong>European passport</strong> — one MiCA authorization valid across all member states (with notifications)</li>
          <li><strong>Regulatory certainty</strong> — attracts institutions that avoid gray zones</li>
          <li><strong>Integration with PSD2/AML</strong> — a framework aligned with banks and fintech</li>
        </ul>
        <p><strong>Risks</strong> to watch:</p>
        <ul>
          <li>High compliance costs for startups — possible consolidation around a few large players</li>
          <li>Volume shifting to unregulated offshore markets</li>
          <li>Slower DeFi innovation pace compared to less regulated markets</li>
        </ul>
        <p>Competition is not only legal but technological: layer 2, CBDCs, and real-world asset (RWA) tokenization. MiCA is the foundation, not the finish line.</p>
      `},
      { id: 'adozione-istituzionale', title: 'Institutional Adoption', content: `
        <p>2026 marks a turning point: banks, asset managers, and large corporations can no longer ignore MiCA if they want to operate with crypto in Europe.</p>
        <p>Trends underway:</p>
        <ul>
          <li><strong>ETFs and listed products</strong> — already governed by traditional financial regulation, now in clearer dialogue with MiCA for ancillary services</li>
          <li><strong>Institutional custody</strong> — banks offering crypto custody under MiCA standards</li>
          <li><strong>Tokenization</strong> — bonds, funds, and securities on blockchain with a defined legal framework</li>
          <li><strong>CBDCs and stablecoins</strong> — the digital euro (in pilot phase) coexists with regulated private stablecoins</li>
        </ul>
        <p>For retail users, the most tangible effect is <strong>normalization</strong>: crypto increasingly integrated into banking apps, investment platforms, and pension services — with KYC, tax reporting, and consumer protection aligned with the rest of finance.</p>
        <div class="box box--tip"><span class="box-title">Perspective</span>Understanding MiCA today means understanding where the European market is headed over the next 3–5 years. You don\'t need a law degree — just know who is authorized, which assets are compliant, and which risks remain yours.</div>
      `},
      { id: 'conclusione', title: 'Conclusion: Summary and Future Outlook', content: `
        <p><strong>MiCA in 2026</strong> is not a technical detail for lawyers — it is the new playing field for Europe\'s crypto market. In summary:</p>
        <ul>
          <li>Exchanges and platforms must be <strong>authorized and transparent</strong></li>
          <li>Investors have <strong>stronger protections</strong> against bad operators</li>
          <li>Stablecoins enter a <strong>strict, verifiable</strong> regime</li>
          <li>Europe bets on <strong>clear rules</strong> to compete globally</li>
          <li>Institutional adoption accelerates across <strong>custody, ETFs, and tokenization</strong></li>
        </ul>
        <p>In the coming years we will likely see <strong>sector consolidation</strong> (fewer operators, more solid ones), deeper <strong>bank-crypto integration</strong>, and new challenges around DeFi and privacy — areas still partially outside MiCA\'s scope.</p>
        <p>Your smart move: use only compliant platforms, diversify, document transactions for tax purposes, and stay informed. The regulation protects those who operate consciously — not those who leave everything to chance.</p>
      `}
    ],
    faq: [
      { q: 'Does MiCA apply in Italy too?', a: 'Yes. MiCA is an EU regulation directly applicable in all member states, including Italy. National authorities oversee implementation.' },
      { q: 'Do I need to declare crypto differently under MiCA?', a: 'MiCA regulates operators and markets — it does not replace tax obligations. In Italy, cryptocurrency must still be declared under current tax rules (RW form, RT section, capital gains).' },
      { q: 'Is Bitcoin regulated by MiCA?', a: 'Bitcoin, as a decentralized asset without an issuer, does not fall under the category of publicly offered tokens. Services on Bitcoin (exchanges, custody) do — they must comply with MiCA.' },
      { q: 'Can I still use non-European exchanges?', a: 'It depends on licenses, geographic restrictions, and compliance. An exchange without EU authorization may be inaccessible or riskier for European residents.' }
    ]
  },
  'trend-etf-bitcoin': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this crypto trend analysis covers <strong>Bitcoin Spot ETF: what they are and why they matter</strong>. Listed funds tracking Bitcoin: impact and what it means for you.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Listed funds tracking Bitcoin: impact and what it means for you.</p><p>In this crypto trend analysis, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'why-this-trend-matters-in-2026', title: 'Why this trend matters in 2026', content: `
<p>Listed funds tracking Bitcoin: impact and what it means for you.</p><p>Macro trends shape regulation, liquidity, institutional adoption, and which infrastructure layers gain traction over the next cycle.</p>
      `},
      { id: 'key-developments-to-understand', title: 'Key developments to understand', content: `
<ul><li><strong>Regulation</strong> — MiCA in Europe, evolving US enforcement, and global licensing standards</li><li><strong>Infrastructure</strong> — layer-2 scaling, real-world asset tokenization, and institutional custody</li><li><strong>Market structure</strong> — ETFs, stablecoin policy, and exchange consolidation</li></ul>
      `},
      { id: 'what-it-means-for-retail-investors', title: 'What it means for retail investors', content: `
<p>You do not need to chase every narrative. Focus on authorized platforms, transparent disclosures, and assets you understand. Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'outlook', title: 'Outlook', content: `
<p>Crypto markets remain volatile and fast-moving. Use trends to inform your education and risk management — not as buy signals.</p><div class="box box--tip"><span class="box-title">Stay informed</span>Subscribe to The Little Satoshi News newsletter for weekly security tips and new guides.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this crypto trend analysis take?', a: 'Most readers complete it in about 7 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'trend-layer2': {
    intro: 'If you already understand wallets and exchanges, this crypto trend analysis covers <strong>Layer 2: why Ethereum needs "secondary roads"</strong>. Scalability solutions to reduce fees and confirmation times.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Scalability solutions to reduce fees and confirmation times.</p><p>In this crypto trend analysis, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'why-this-trend-matters-in-2026', title: 'Why this trend matters in 2026', content: `
<p>Scalability solutions to reduce fees and confirmation times.</p><p>Macro trends shape regulation, liquidity, institutional adoption, and which infrastructure layers gain traction over the next cycle.</p>
      `},
      { id: 'key-developments-to-understand', title: 'Key developments to understand', content: `
<ul><li><strong>Regulation</strong> — MiCA in Europe, evolving US enforcement, and global licensing standards</li><li><strong>Infrastructure</strong> — layer-2 scaling, real-world asset tokenization, and institutional custody</li><li><strong>Market structure</strong> — ETFs, stablecoin policy, and exchange consolidation</li></ul>
      `},
      { id: 'what-it-means-for-retail-investors', title: 'What it means for retail investors', content: `
<p>You do not need to chase every narrative. Focus on authorized platforms, transparent disclosures, and assets you understand. Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'outlook', title: 'Outlook', content: `
<p>Crypto markets remain volatile and fast-moving. Use trends to inform your education and risk management — not as buy signals.</p><div class="box box--tip"><span class="box-title">Stay informed</span>Subscribe to The Little Satoshi News newsletter for weekly security tips and new guides.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this crypto trend analysis take?', a: 'Most readers complete it in about 9 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'trend-rwa': {
    intro: 'If you already understand wallets and exchanges, this crypto trend analysis covers <strong>Real World Assets (RWA): crypto representing real assets</strong>. Tokenization of real estate, bonds and commodities.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Tokenization of real estate, bonds and commodities.</p><p>In this crypto trend analysis, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'why-this-trend-matters-in-2026', title: 'Why this trend matters in 2026', content: `
<p>Tokenization of real estate, bonds and commodities.</p><p>Macro trends shape regulation, liquidity, institutional adoption, and which infrastructure layers gain traction over the next cycle.</p>
      `},
      { id: 'key-developments-to-understand', title: 'Key developments to understand', content: `
<ul><li><strong>Regulation</strong> — MiCA in Europe, evolving US enforcement, and global licensing standards</li><li><strong>Infrastructure</strong> — layer-2 scaling, real-world asset tokenization, and institutional custody</li><li><strong>Market structure</strong> — ETFs, stablecoin policy, and exchange consolidation</li></ul>
      `},
      { id: 'what-it-means-for-retail-investors', title: 'What it means for retail investors', content: `
<p>You do not need to chase every narrative. Focus on authorized platforms, transparent disclosures, and assets you understand. Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'outlook', title: 'Outlook', content: `
<p>Crypto markets remain volatile and fast-moving. Use trends to inform your education and risk management — not as buy signals.</p><div class="box box--tip"><span class="box-title">Stay informed</span>Subscribe to The Little Satoshi News newsletter for weekly security tips and new guides.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this crypto trend analysis take?', a: 'Most readers complete it in about 8 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'trend-stablecoin': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this crypto trend analysis covers <strong>Stablecoins: how they work and what risks they hide</strong>. USDT, USDC and DAI: apparent stability, real risks.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>USDT, USDC and DAI: apparent stability, real risks.</p><p>In this crypto trend analysis, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'why-this-trend-matters-in-2026', title: 'Why this trend matters in 2026', content: `
<p>USDT, USDC and DAI: apparent stability, real risks.</p><p>Macro trends shape regulation, liquidity, institutional adoption, and which infrastructure layers gain traction over the next cycle.</p>
      `},
      { id: 'key-developments-to-understand', title: 'Key developments to understand', content: `
<ul><li><strong>Regulation</strong> — MiCA in Europe, evolving US enforcement, and global licensing standards</li><li><strong>Infrastructure</strong> — layer-2 scaling, real-world asset tokenization, and institutional custody</li><li><strong>Market structure</strong> — ETFs, stablecoin policy, and exchange consolidation</li></ul>
      `},
      { id: 'what-it-means-for-retail-investors', title: 'What it means for retail investors', content: `
<p>You do not need to chase every narrative. Focus on authorized platforms, transparent disclosures, and assets you understand. Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'outlook', title: 'Outlook', content: `
<p>Crypto markets remain volatile and fast-moving. Use trends to inform your education and risk management — not as buy signals.</p><div class="box box--tip"><span class="box-title">Stay informed</span>Subscribe to The Little Satoshi News newsletter for weekly security tips and new guides.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this crypto trend analysis take?', a: 'Most readers complete it in about 8 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'trend-cbdc': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this crypto trend analysis covers <strong>CBDC: central bank digital currencies explained</strong>. Digital euro and sovereign currencies: differences from decentralized crypto.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Digital euro and sovereign currencies: differences from decentralized crypto.</p><p>In this crypto trend analysis, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'why-this-trend-matters-in-2026', title: 'Why this trend matters in 2026', content: `
<p>Digital euro and sovereign currencies: differences from decentralized crypto.</p><p>Macro trends shape regulation, liquidity, institutional adoption, and which infrastructure layers gain traction over the next cycle.</p>
      `},
      { id: 'key-developments-to-understand', title: 'Key developments to understand', content: `
<ul><li><strong>Regulation</strong> — MiCA in Europe, evolving US enforcement, and global licensing standards</li><li><strong>Infrastructure</strong> — layer-2 scaling, real-world asset tokenization, and institutional custody</li><li><strong>Market structure</strong> — ETFs, stablecoin policy, and exchange consolidation</li></ul>
      `},
      { id: 'what-it-means-for-retail-investors', title: 'What it means for retail investors', content: `
<p>You do not need to chase every narrative. Focus on authorized platforms, transparent disclosures, and assets you understand. Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'outlook', title: 'Outlook', content: `
<p>Crypto markets remain volatile and fast-moving. Use trends to inform your education and risk management — not as buy signals.</p><div class="box box--tip"><span class="box-title">Stay informed</span>Subscribe to The Little Satoshi News newsletter for weekly security tips and new guides.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this crypto trend analysis take?', a: 'Most readers complete it in about 7 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'trend-depin': {
    intro: 'If you already understand wallets and exchanges, this crypto trend analysis covers <strong>DePIN: decentralized physical infrastructure</strong>. Decentralized networks for storage, WiFi, energy and more.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Decentralized networks for storage, WiFi, energy and more.</p><p>In this crypto trend analysis, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'why-this-trend-matters-in-2026', title: 'Why this trend matters in 2026', content: `
<p>Decentralized networks for storage, WiFi, energy and more.</p><p>Macro trends shape regulation, liquidity, institutional adoption, and which infrastructure layers gain traction over the next cycle.</p>
      `},
      { id: 'key-developments-to-understand', title: 'Key developments to understand', content: `
<ul><li><strong>Regulation</strong> — MiCA in Europe, evolving US enforcement, and global licensing standards</li><li><strong>Infrastructure</strong> — layer-2 scaling, real-world asset tokenization, and institutional custody</li><li><strong>Market structure</strong> — ETFs, stablecoin policy, and exchange consolidation</li></ul>
      `},
      { id: 'what-it-means-for-retail-investors', title: 'What it means for retail investors', content: `
<p>You do not need to chase every narrative. Focus on authorized platforms, transparent disclosures, and assets you understand. Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'outlook', title: 'Outlook', content: `
<p>Crypto markets remain volatile and fast-moving. Use trends to inform your education and risk management — not as buy signals.</p><div class="box box--tip"><span class="box-title">Stay informed</span>Subscribe to The Little Satoshi News newsletter for weekly security tips and new guides.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this crypto trend analysis take?', a: 'Most readers complete it in about 8 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'trend-ai-blockchain': {
    intro: 'If you already understand wallets and exchanges, this crypto trend analysis covers <strong>AI + Blockchain: trend or real utility?</strong>. Where artificial intelligence meets blockchain.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Where artificial intelligence meets blockchain.</p><p>In this crypto trend analysis, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'why-this-trend-matters-in-2026', title: 'Why this trend matters in 2026', content: `
<p>Where artificial intelligence meets blockchain.</p><p>Macro trends shape regulation, liquidity, institutional adoption, and which infrastructure layers gain traction over the next cycle.</p>
      `},
      { id: 'key-developments-to-understand', title: 'Key developments to understand', content: `
<ul><li><strong>Regulation</strong> — MiCA in Europe, evolving US enforcement, and global licensing standards</li><li><strong>Infrastructure</strong> — layer-2 scaling, real-world asset tokenization, and institutional custody</li><li><strong>Market structure</strong> — ETFs, stablecoin policy, and exchange consolidation</li></ul>
      `},
      { id: 'what-it-means-for-retail-investors', title: 'What it means for retail investors', content: `
<p>You do not need to chase every narrative. Focus on authorized platforms, transparent disclosures, and assets you understand. Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'outlook', title: 'Outlook', content: `
<p>Crypto markets remain volatile and fast-moving. Use trends to inform your education and risk management — not as buy signals.</p><div class="box box--tip"><span class="box-title">Stay informed</span>Subscribe to The Little Satoshi News newsletter for weekly security tips and new guides.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this crypto trend analysis take?', a: 'Most readers complete it in about 9 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'trend-halving': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this crypto trend analysis covers <strong>The Bitcoin halving: what it is and why everyone talks about it</strong>. Reduction of miner rewards: effects on the market.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Reduction of miner rewards: effects on the market.</p><p>In this crypto trend analysis, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'why-this-trend-matters-in-2026', title: 'Why this trend matters in 2026', content: `
<p>Reduction of miner rewards: effects on the market.</p><p>Macro trends shape regulation, liquidity, institutional adoption, and which infrastructure layers gain traction over the next cycle.</p>
      `},
      { id: 'key-developments-to-understand', title: 'Key developments to understand', content: `
<ul><li><strong>Regulation</strong> — MiCA in Europe, evolving US enforcement, and global licensing standards</li><li><strong>Infrastructure</strong> — layer-2 scaling, real-world asset tokenization, and institutional custody</li><li><strong>Market structure</strong> — ETFs, stablecoin policy, and exchange consolidation</li></ul>
      `},
      { id: 'what-it-means-for-retail-investors', title: 'What it means for retail investors', content: `
<p>You do not need to chase every narrative. Focus on authorized platforms, transparent disclosures, and assets you understand. Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'outlook', title: 'Outlook', content: `
<p>Crypto markets remain volatile and fast-moving. Use trends to inform your education and risk management — not as buy signals.</p><div class="box box--tip"><span class="box-title">Stay informed</span>Subscribe to The Little Satoshi News newsletter for weekly security tips and new guides.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this crypto trend analysis take?', a: 'Most readers complete it in about 7 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'trend-modular-blockchain': {
    intro: 'For experienced users who want a precise, no-nonsense walkthrough, this crypto trend analysis covers <strong>Modular Blockchain: the new architecture of crypto networks</strong>. Separating consensus, execution and data availability.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Separating consensus, execution and data availability.</p><p>In this crypto trend analysis, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'why-this-trend-matters-in-2026', title: 'Why this trend matters in 2026', content: `
<p>Separating consensus, execution and data availability.</p><p>Macro trends shape regulation, liquidity, institutional adoption, and which infrastructure layers gain traction over the next cycle.</p>
      `},
      { id: 'key-developments-to-understand', title: 'Key developments to understand', content: `
<ul><li><strong>Regulation</strong> — MiCA in Europe, evolving US enforcement, and global licensing standards</li><li><strong>Infrastructure</strong> — layer-2 scaling, real-world asset tokenization, and institutional custody</li><li><strong>Market structure</strong> — ETFs, stablecoin policy, and exchange consolidation</li></ul>
      `},
      { id: 'what-it-means-for-retail-investors', title: 'What it means for retail investors', content: `
<p>You do not need to chase every narrative. Focus on authorized platforms, transparent disclosures, and assets you understand. Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'outlook', title: 'Outlook', content: `
<p>Crypto markets remain volatile and fast-moving. Use trends to inform your education and risk management — not as buy signals.</p><div class="box box--tip"><span class="box-title">Stay informed</span>Subscribe to The Little Satoshi News newsletter for weekly security tips and new guides.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this crypto trend analysis take?', a: 'Most readers complete it in about 10 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
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
  'creare-account-exchange': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this tutorial covers <strong>Create an account on Coinbase/Kraken (with screenshots)</strong>. Registration, KYC verification and first steps on the exchange.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Registration, KYC verification and first steps on the exchange.</p><p>In this tutorial, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Registration, KYC verification and first steps on the exchange.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Always verify the platform is regulated, enable two-factor authentication, and double-check deposit and withdrawal networks before moving funds.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Always verify the platform is regulated, enable two-factor authentication, and double-check deposit and withdrawal networks before moving funds.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Always verify the platform is regulated, enable two-factor authentication, and double-check deposit and withdrawal networks before moving funds.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this tutorial take?', a: 'Most readers complete it in about 8 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'primi-20-euro-bitcoin': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this tutorial covers <strong>Buy your first €20 of Bitcoin</strong>. Buy order, payment and confirmation step by step.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Buy order, payment and confirmation step by step.</p><p>In this tutorial, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Buy order, payment and confirmation step by step.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Bitcoin remains the most liquid and widely recognized cryptocurrency. On-chain fees vary with network congestion — check mempool conditions before sending.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Bitcoin remains the most liquid and widely recognized cryptocurrency. On-chain fees vary with network congestion — check mempool conditions before sending.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Bitcoin remains the most liquid and widely recognized cryptocurrency. On-chain fees vary with network congestion — check mempool conditions before sending.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this tutorial take?', a: 'Most readers complete it in about 6 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'installare-trust-wallet': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this tutorial covers <strong>Install and configure Trust Wallet</strong>. Download, setup and first crypto receipt.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Download, setup and first crypto receipt.</p><p>In this tutorial, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Download, setup and first crypto receipt.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Your seed phrase is the master key to your funds. Write it on paper, never store it digitally, and test with a small amount before transferring larger balances.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Your seed phrase is the master key to your funds. Write it on paper, never store it digitally, and test with a small amount before transferring larger balances.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Your seed phrase is the master key to your funds. Write it on paper, never store it digitally, and test with a small amount before transferring larger balances.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this tutorial take?', a: 'Most readers complete it in about 7 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'prima-transazione-crypto': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this tutorial covers <strong>Send and receive your first crypto</strong>. From copying the address to on-chain confirmation.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>From copying the address to on-chain confirmation.</p><p>In this tutorial, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>From copying the address to on-chain confirmation.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this tutorial take?', a: 'Most readers complete it in about 6 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'leggere-grafico-candele': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this tutorial covers <strong>Read a price chart (basic candlesticks)</strong>. Candlesticks, timeframes and volume for beginners.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Candlesticks, timeframes and volume for beginners.</p><p>In this tutorial, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Candlesticks, timeframes and volume for beginners.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this tutorial take?', a: 'Most readers complete it in about 8 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'market-cap-volume': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this tutorial covers <strong>Understanding market cap, volume and supply</strong>. The basic metrics to evaluate a cryptocurrency.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>The basic metrics to evaluate a cryptocurrency.</p><p>In this tutorial, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>The basic metrics to evaluate a cryptocurrency.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this tutorial take?', a: 'Most readers complete it in about 7 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'esplorare-block-explorer': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this tutorial covers <strong>Explore your first transaction on a blockchain explorer</strong>. Find and read your transaction on the blockchain.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Find and read your transaction on the blockchain.</p><p>In this tutorial, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Find and read your transaction on the blockchain.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this tutorial take?', a: 'Most readers complete it in about 6 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'notifiche-prezzo-app': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this tutorial covers <strong>Set price notifications on mobile apps</strong>. Custom alerts with CoinGecko and similar apps.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Custom alerts with CoinGecko and similar apps.</p><p>In this tutorial, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Custom alerts with CoinGecko and similar apps.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this tutorial take?', a: 'Most readers complete it in about 5 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'creare-watchlist': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this tutorial covers <strong>Create your first personalized watchlist</strong>. Monitor the crypto you\'re interested in.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Monitor the crypto you're interested in.</p><p>In this tutorial, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Monitor the crypto you're interested in.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this tutorial take?', a: 'Most readers complete it in about 4 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'bridge-cross-chain': {
    intro: 'For experienced users who want a precise, no-nonsense walkthrough, this tutorial covers <strong>Cross-chain bridge: transfer assets between Ethereum and Arbitrum</strong>. Bridges between blockchains: how they work and risks to consider.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Bridges between blockchains: how they work and risks to consider.</p><p>In this tutorial, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Bridges between blockchains: how they work and risks to consider.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this tutorial take?', a: 'Most readers complete it in about 14 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'liquidita-uniswap-v3': {
    intro: 'For experienced users who want a precise, no-nonsense walkthrough, this tutorial covers <strong>Provide liquidity on Uniswap V3 (with impermanent loss calculation)</strong>. Concentrated liquidity and impermanent loss risk.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Concentrated liquidity and impermanent loss risk.</p><p>In this tutorial, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Concentrated liquidity and impermanent loss risk.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending.</p>
      `},
      { id: 'step-5-document-for-compliance', title: 'Step 5: Document for compliance', content: `
<p>Log dates, amounts, and platforms used. You will need this for tax reporting and audit trails.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this tutorial take?', a: 'Most readers complete it in about 16 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'usare-aave': {
    intro: 'For experienced users who want a precise, no-nonsense walkthrough, this tutorial covers <strong>Use Aave for DeFi lending and deposits</strong>. Decentralized lending and borrowing on Aave.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Decentralized lending and borrowing on Aave.</p><p>In this tutorial, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Decentralized lending and borrowing on Aave.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this tutorial take?', a: 'Most readers complete it in about 14 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'analisi-on-chain-dune': {
    intro: 'For experienced users who want a precise, no-nonsense walkthrough, this tutorial covers <strong>On-chain analysis with Dune Analytics</strong>. SQL queries and dashboards for blockchain analysis.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>SQL queries and dashboards for blockchain analysis.</p><p>In this tutorial, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>SQL queries and dashboards for blockchain analysis.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-5-document-for-compliance', title: 'Step 5: Document for compliance', content: `
<p>Log dates, amounts, and platforms used. You will need this for tax reporting and audit trails.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this tutorial take?', a: 'Most readers complete it in about 15 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'nodo-validator': {
    intro: 'For experienced users who want a precise, no-nonsense walkthrough, this tutorial covers <strong>Configure a validator node (requirements overview)</strong>. Hardware, software and costs to validate a network.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Hardware, software and costs to validate a network.</p><p>In this tutorial, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Hardware, software and costs to validate a network.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Staking rewards depend on network conditions and pool performance. Never share private keys — legitimate staking only requires delegation, not custody transfer.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Staking rewards depend on network conditions and pool performance. Never share private keys — legitimate staking only requires delegation, not custody transfer.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Staking rewards depend on network conditions and pool performance. Never share private keys — legitimate staking only requires delegation, not custody transfer.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>Staking rewards depend on network conditions and pool performance. Never share private keys — legitimate staking only requires delegation, not custody transfer.</p>
      `},
      { id: 'step-5-document-for-compliance', title: 'Step 5: Document for compliance', content: `
<p>Log dates, amounts, and platforms used. You will need this for tax reporting and audit trails.</p><p>Staking rewards depend on network conditions and pool performance. Never share private keys — legitimate staking only requires delegation, not custody transfer.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this tutorial take?', a: 'Most readers complete it in about 18 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'leggere-solidity': {
    intro: 'For experienced users who want a precise, no-nonsense walkthrough, this tutorial covers <strong>Smart contracts: read basic Solidity code</strong>. Functions, variables and common patterns for non-developers.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Functions, variables and common patterns for non-developers.</p><p>In this tutorial, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Functions, variables and common patterns for non-developers.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-5-document-for-compliance', title: 'Step 5: Document for compliance', content: `
<p>Log dates, amounts, and platforms used. You will need this for tax reporting and audit trails.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this tutorial take?', a: 'Most readers complete it in about 16 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'mev-protezione': {
    intro: 'For experienced users who want a precise, no-nonsense walkthrough, this tutorial covers <strong>MEV and protection in DeFi transactions</strong>. Maximal Extractable Value and how to defend against it.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Maximal Extractable Value and how to defend against it.</p><p>In this tutorial, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Maximal Extractable Value and how to defend against it.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this tutorial take?', a: 'Most readers complete it in about 12 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'multisig-gnosis-safe': {
    intro: 'For experienced users who want a precise, no-nonsense walkthrough, this tutorial covers <strong>Multisig wallet with Gnosis Safe</strong>. Multi-signature wallet for teams and DAOs.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Multi-signature wallet for teams and DAOs.</p><p>In this tutorial, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Multi-signature wallet for teams and DAOs.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Your seed phrase is the master key to your funds. Write it on paper, never store it digitally, and test with a small amount before transferring larger balances.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Your seed phrase is the master key to your funds. Write it on paper, never store it digitally, and test with a small amount before transferring larger balances.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Your seed phrase is the master key to your funds. Write it on paper, never store it digitally, and test with a small amount before transferring larger balances.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>Your seed phrase is the master key to your funds. Write it on paper, never store it digitally, and test with a small amount before transferring larger balances.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this tutorial take?', a: 'Most readers complete it in about 13 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'ottimizzazione-gas-batch': {
    intro: 'For experienced users who want a precise, no-nonsense walkthrough, this tutorial covers <strong>Gas optimization with batch transactions</strong>. Group operations to save on fees.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Group operations to save on fees.</p><p>In this tutorial, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Group operations to save on fees.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Gas fees spike during network congestion. Use block explorers and gas trackers to time transactions when costs are lower. Ethereum powers most of DeFi and NFT activity. Confirm you are on the correct network (mainnet or an approved layer 2) before signing any transaction.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Gas fees spike during network congestion. Use block explorers and gas trackers to time transactions when costs are lower. Ethereum powers most of DeFi and NFT activity. Confirm you are on the correct network (mainnet or an approved layer 2) before signing any transaction.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Gas fees spike during network congestion. Use block explorers and gas trackers to time transactions when costs are lower. Ethereum powers most of DeFi and NFT activity. Confirm you are on the correct network (mainnet or an approved layer 2) before signing any transaction.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>Gas fees spike during network congestion. Use block explorers and gas trackers to time transactions when costs are lower. Ethereum powers most of DeFi and NFT activity. Confirm you are on the correct network (mainnet or an approved layer 2) before signing any transaction.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this tutorial take?', a: 'Most readers complete it in about 11 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'hedging-stablecoin': {
    intro: 'For experienced users who want a precise, no-nonsense walkthrough, this tutorial covers <strong>Hedging strategies with stablecoins and DeFi derivatives</strong>. Protect your portfolio in volatile markets.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Protect your portfolio in volatile markets.</p><p>In this tutorial, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Protect your portfolio in volatile markets.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this tutorial take?', a: 'Most readers complete it in about 14 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
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
        <h3>Hydra: layer-2 state channels</h3>
        <p><strong>Hydra</strong> enables off-chain state channels where participants execute transactions rapidly, settling final state on the main chain only when needed — like a restaurant tab settled once at the end of the meal.</p>
        <div class="box box--tip"><span class="box-title">Learn more</span><a href="articolo.html?slug=hydra-cardano">Hydra on Cardano: full guide</a></div>
        <h3>Mithril: Lightweight chain verification</h3>
        <p><strong>Mithril</strong> lets users verify blockchain state without downloading the entire history. Using cryptographic multi-signatures and stake-based thresholds, lightweight clients — mobile wallets, browsers — can trustlessly verify the chain with minimal data. Crucial for regions with limited bandwidth, including parts of North Africa and rural Europe.</p>
        <h3>Leios and Input Endorsers: layer-1 throughput</h3>
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
        <p>For a structured walkthrough of the full Cardano ecosystem, explore <a href="cardano/index.html">Steven\'s Cardano guide hub</a> on CryptoItaliaFacile. It bridges the gap between high-level overviews like this article and the hands-on knowledge required to participate meaningfully in the ecosystem.</p>
        <p>Whether you are a developer evaluating Plutus, a delegate choosing a stake pool, or curious about proof-of-stake governance in practice, a structured guide accelerates understanding far faster than scattered search results.</p>
        <p><strong>Start here:</strong> <a href="https://satoshiallien.github.io/cryptoitaliafacile/cardano/index.html" target="_blank" rel="noopener noreferrer">Cardano ecosystem hub — CryptoItaliaFacile</a></p>
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
  'comprare-ada': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this Cardano guide covers <strong>How to buy ADA on exchanges</strong>. Where and how to buy Cardano.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Where and how to buy Cardano.</p><p>In this Cardano guide, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Where and how to buy Cardano.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Always verify the platform is regulated, enable two-factor authentication, and double-check deposit and withdrawal networks before moving funds.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Always verify the platform is regulated, enable two-factor authentication, and double-check deposit and withdrawal networks before moving funds.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Always verify the platform is regulated, enable two-factor authentication, and double-check deposit and withdrawal networks before moving funds.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this Cardano guide take?', a: 'Most readers complete it in about 8 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'staking-ada': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this Cardano guide covers <strong>Staking ADA: complete guide (delegation vs pool)</strong>. Delegate ADA to a staking pool: returns and pool selection.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Delegate ADA to a staking pool: returns and pool selection.</p><p>In this Cardano guide, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Delegate ADA to a staking pool: returns and pool selection.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Staking rewards depend on network conditions and pool performance. Never share private keys — legitimate staking only requires delegation, not custody transfer.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Staking rewards depend on network conditions and pool performance. Never share private keys — legitimate staking only requires delegation, not custody transfer.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Staking rewards depend on network conditions and pool performance. Never share private keys — legitimate staking only requires delegation, not custody transfer.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>Staking rewards depend on network conditions and pool performance. Never share private keys — legitimate staking only requires delegation, not custody transfer.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this Cardano guide take?', a: 'Most readers complete it in about 12 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'wallet-cardano-confronto': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this Cardano guide covers <strong>Eternl, Nami, Yoroi: which Cardano wallet to choose</strong>. Comparison of the most used wallets in the Cardano ecosystem.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Comparison of the most used wallets in the Cardano ecosystem.</p><p>In this Cardano guide, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Comparison of the most used wallets in the Cardano ecosystem.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Your seed phrase is the master key to your funds. Write it on paper, never store it digitally, and test with a small amount before transferring larger balances. Cardano uses a proof-of-stake model with low transaction fees. Choose reputable wallets and stake pools with consistent performance and transparent fees.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Your seed phrase is the master key to your funds. Write it on paper, never store it digitally, and test with a small amount before transferring larger balances. Cardano uses a proof-of-stake model with low transaction fees. Choose reputable wallets and stake pools with consistent performance and transparent fees.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Your seed phrase is the master key to your funds. Write it on paper, never store it digitally, and test with a small amount before transferring larger balances. Cardano uses a proof-of-stake model with low transaction fees. Choose reputable wallets and stake pools with consistent performance and transparent fees.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>Your seed phrase is the master key to your funds. Write it on paper, never store it digitally, and test with a small amount before transferring larger balances. Cardano uses a proof-of-stake model with low transaction fees. Choose reputable wallets and stake pools with consistent performance and transparent fees.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this Cardano guide take?', a: 'Most readers complete it in about 10 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'project-catalyst': {
    intro: 'If you already understand wallets and exchanges, this Cardano guide covers <strong>How to vote on Project Catalyst</strong>. Participate in ecosystem governance and funding.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Participate in ecosystem governance and funding.</p><p>In this Cardano guide, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Participate in ecosystem governance and funding.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this Cardano guide take?', a: 'Most readers complete it in about 9 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'cardano-defi': {
    intro: 'If you already understand wallets and exchanges, this Cardano guide covers <strong>Cardano DeFi: Minswap, SundaeSwap and liquidity pools</strong>. The main DEXs and DeFi protocols on Cardano.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>The main DEXs and DeFi protocols on Cardano.</p><p>In this Cardano guide, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>The main DEXs and DeFi protocols on Cardano.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending. Cardano uses a proof-of-stake model with low transaction fees. Choose reputable wallets and stake pools with consistent performance and transparent fees.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending. Cardano uses a proof-of-stake model with low transaction fees. Choose reputable wallets and stake pools with consistent performance and transparent fees.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending. Cardano uses a proof-of-stake model with low transaction fees. Choose reputable wallets and stake pools with consistent performance and transparent fees.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>DeFi removes intermediaries but not risk. Verify contract addresses, understand impermanent loss, and never approve unlimited token spending. Cardano uses a proof-of-stake model with low transaction fees. Choose reputable wallets and stake pools with consistent performance and transparent fees.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this Cardano guide take?', a: 'Most readers complete it in about 13 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'native-token-cardano': {
    intro: 'If you already understand wallets and exchanges, this Cardano guide covers <strong>Native tokens on Cardano: create and manage assets</strong>. Native tokens without complex smart contracts.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Native tokens without complex smart contracts.</p><p>In this Cardano guide, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Native tokens without complex smart contracts.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Cardano uses a proof-of-stake model with low transaction fees. Choose reputable wallets and stake pools with consistent performance and transparent fees.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Cardano uses a proof-of-stake model with low transaction fees. Choose reputable wallets and stake pools with consistent performance and transparent fees.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Cardano uses a proof-of-stake model with low transaction fees. Choose reputable wallets and stake pools with consistent performance and transparent fees.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>Cardano uses a proof-of-stake model with low transaction fees. Choose reputable wallets and stake pools with consistent performance and transparent fees.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this Cardano guide take?', a: 'Most readers complete it in about 11 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'hydra-cardano': {
    intro: 'If you already understand wallets and exchanges, this Cardano guide covers <strong>Hydra: what it is and what it will change for scalability</strong>. Cardano\'s Layer 2 for ultra-fast transactions.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>Cardano's Layer 2 for ultra-fast transactions.</p><p>In this Cardano guide, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>Cardano's Layer 2 for ultra-fast transactions.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this Cardano guide take?', a: 'Most readers complete it in about 9 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'plutus-panoramica': {
    intro: 'If you already understand wallets and exchanges, this Cardano guide covers <strong>Cardano smart contracts (Plutus): overview for users</strong>. How smart contracts work on Cardano.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>How smart contracts work on Cardano.</p><p>In this Cardano guide, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>How smart contracts work on Cardano.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>Move slowly, verify every address and network, and keep records for tax reporting.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'This is written for users with some prior crypto experience. Beginners may want to start with our beginner path on the homepage.' },
      { q: 'How long does this Cardano guide take?', a: 'Most readers complete it in about 10 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'cardano-vs-ethereum': {
    intro: 'Whether you are new to cryptocurrency or refreshing the basics, this Cardano guide covers <strong>Cardano vs Ethereum: practical differences for users</strong>. A real comparison between the two ecosystems for beginners.',
    sections: [
      { id: 'overview', title: 'Overview', content: `
<p>A real comparison between the two ecosystems for beginners.</p><p>In this Cardano guide, we walk through the process practically and safely, without hype and with concrete checkpoints.</p>
      `},
      { id: 'what-you-need-before-you-start', title: 'What you need before you start', content: `
<p>A real comparison between the two ecosystems for beginners.</p><ul><li>A verified exchange or wallet account with two-factor authentication enabled</li><li>A secure backup of your recovery phrase (if using a self-custody wallet)</li><li>Time to read each confirmation screen before approving</li></ul>
      `},
      { id: 'step-1-prepare-your-accounts', title: 'Step 1: Prepare your accounts', content: `
<p>Confirm KYC is complete, 2FA is active, and you are on the official app or website — not a link from email or social media.</p><p>Cardano uses a proof-of-stake model with low transaction fees. Choose reputable wallets and stake pools with consistent performance and transparent fees. Ethereum powers most of DeFi and NFT activity. Confirm you are on the correct network (mainnet or an approved layer 2) before signing any transaction.</p>
      `},
      { id: 'step-2-configure-the-settings', title: 'Step 2: Configure the settings', content: `
<p>Select the correct network, fee level, and destination address. For first-time operations, use a small test amount.</p><p>Cardano uses a proof-of-stake model with low transaction fees. Choose reputable wallets and stake pools with consistent performance and transparent fees. Ethereum powers most of DeFi and NFT activity. Confirm you are on the correct network (mainnet or an approved layer 2) before signing any transaction.</p>
      `},
      { id: 'step-3-execute-and-verify', title: 'Step 3: Execute and verify', content: `
<p>Submit the transaction and verify it on a block explorer. Save the transaction ID for your records.</p><p>Cardano uses a proof-of-stake model with low transaction fees. Choose reputable wallets and stake pools with consistent performance and transparent fees. Ethereum powers most of DeFi and NFT activity. Confirm you are on the correct network (mainnet or an approved layer 2) before signing any transaction.</p>
      `},
      { id: 'step-4-secure-your-funds', title: 'Step 4: Secure your funds', content: `
<p>Move long-term holdings to a personal wallet you control. Never leave large balances on an exchange indefinitely.</p><p>Cardano uses a proof-of-stake model with low transaction fees. Choose reputable wallets and stake pools with consistent performance and transparent fees. Ethereum powers most of DeFi and NFT activity. Confirm you are on the correct network (mainnet or an approved layer 2) before signing any transaction.</p>
      `},
      { id: 'security-checklist', title: 'Security checklist', content: `
<ul><li>Enable 2FA with an authenticator app — not SMS</li><li>Verify URLs and contract addresses character by character</li><li>Never share seed phrases or private keys</li><li>Use hardware wallets for significant long-term holdings</li></ul><div class="box box--danger"><span class="box-title">Never</span>Approve transactions you do not fully understand, especially unlimited token allowances.</div>
      `},
    ],
    faq: [
      { q: 'Is this article suitable for beginners?', a: 'Yes. The Little Satoshi News is designed for readers new to crypto. If a term is unclear, check our glossary.' },
      { q: 'How long does this Cardano guide take?', a: 'Most readers complete it in about 11 minutes, plus time to execute the steps carefully.' },
      { q: 'Does this constitute financial advice?', a: 'No. This content is for education only. Cryptocurrency involves significant risk — only invest what you can afford to lose.' },
    ]
  },
  'seed-phrase-guida': {
    intro: 'The <strong>seed phrase</strong> (12 or 24 BIP39 words) is your wallet\'s master key. Whoever holds it controls your funds. This guide explains what it is, how it is generated, and how to store it without fatal mistakes.',
    sections: [
      { id: 'what-is-seed', title: 'What is a seed phrase', content: `
<p>When you create a self-custody wallet, the software generates a precise sequence of words. All private keys in the wallet are derived from that sequence.</p>
<h3>Why it matters</h3>
<ul><li>It is the <strong>only way</strong> to recover your wallet if you lose your phone or computer</li><li>There is no password reset — without the seed, funds are gone</li><li>Anyone who reads the seed can drain the wallet</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'generation', title: 'How it is generated', content: `
<p>Generation happens <strong>on your device</strong>, inside the wallet's secure environment (Trust Wallet, MetaMask, Ledger, etc.).</p>
<ol><li>Choose "Create new wallet"</li><li>Software generates random entropy and converts it to BIP39 words</li><li>Words are shown once — write them down immediately</li><li>Complete the wallet's confirmation test</li></ol>
<div class="box box--danger"><span class="box-title">Never</span>Generate or enter a seed on websites, Google forms, Telegram chats, or with "technical support".</div>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'storage', title: 'How to store it correctly', content: `
<p>Practical rule: <strong>paper + metal + safe location</strong>.</p>
<ul><li>Write words on permanent ink paper, no abbreviations</li><li>Consider a steel plate for fire and water resistance</li><li>Keep at least two copies in different physical locations</li><li>Do not label copies obviously as seed phrases</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'mistakes', title: 'Costly mistakes', content: `
<ul><li>❌ Screenshots or photos of the seed</li><li>❌ Saving to cloud, email, Notes, iCloud</li><li>❌ Typing the seed on any website</li><li>❌ Sharing with family "for safety" without understanding risks</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
    ],
    faq: [
      { q: 'Can I change my seed phrase?', a: 'No. To get a new one you must create a new wallet and transfer funds.' },
      { q: '12 or 24 words?', a: 'Both are valid. 24 words offer more entropy; 12 is the most common mobile standard.' },
    ]
  }
  'hot-vs-cold-wallet': {
    intro: 'Hot and cold wallets are not the same. Understanding the difference helps you use the right tool for each amount and operation.',
    sections: [
      { id: 'difference', title: 'The difference in 30 seconds', content: `
<p><strong>Hot wallet</strong>: internet-connected (mobile app, browser extension). Convenient, fast, more exposed.</p><p><strong>Cold wallet</strong>: offline keys (hardware wallet, paper wallet). Less convenient, maximum protection for hodling.</p>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'when-hot', title: 'When to use a hot wallet', content: `
<ul><li>Small amounts for daily use</li><li>DeFi, NFTs, frequent operations</li><li>Learning with minimal amounts</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'when-cold', title: 'When to use a cold wallet', content: `
<ul><li>Long-term storage (Bitcoin, ETH, ADA)</li><li>Funds you do not need daily</li><li>After accumulating on an exchange — withdraw to cold</li></ul><div class="box box--tip"><span class="box-title">Practical rule</span>Exchange to buy. Hot to operate. Cold to store.</div>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'risks', title: 'Main risks', content: `
<p>Hot: malware, phishing, malicious approvals. Cold: physical loss, no seed backup, tampered device purchase.</p>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
    ],
    faq: [
      { q: 'Can I use only a hot wallet?', a: 'Yes to start, but not for your entire portfolio. Diversify as amounts grow.' },
      { q: 'Is a cold wallet difficult?', a: 'Ledger and Trezor are beginner-friendly. Setup takes 20-30 minutes.' },
    ]
  }
  'confronto-hardware-wallet': {
    intro: 'Ledger, Trezor, and BitBox are the three most used hardware wallets in Europe. None is "perfect": the choice depends on budget, supported blockchains, and privacy level.',
    sections: [
      { id: 'overview', title: 'Why a hardware wallet', content: `
<p>A hardware wallet keeps <strong>private keys offline</strong>. Even if your PC is infected, an attacker cannot sign transactions without the physical device and PIN.</p><ul><li>Ideal for medium to long-term storage</li><li>Works with MetaMask, Ledger Live, Trezor Suite</li><li>Buy only from the official site or authorized reseller</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'ledger', title: 'Ledger (Nano S Plus / Nano X)', content: `
<h3>Strengths</h3><ul><li>Broad chain and token support</li><li>Intuitive Ledger Live app</li><li>Nano X with Bluetooth (note: larger attack surface)</li></ul><h3>Caveats</h3><p>Past customer data leaks (emails, addresses). Use a dedicated email and avoid suspicious links.</p>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'trezor', title: 'Trezor (Model One / Safe 3)', content: `
<h3>Strengths</h3><ul><li>Open-source firmware</li><li>Clean, transparent Trezor Suite</li><li>Excellent for Bitcoin and Ethereum</li></ul><h3>Caveats</h3><p>Model One does not support some modern chains. Check compatibility before buying.</p>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'bitbox', title: 'BitBox (BitBox02)', content: `
<h3>Strengths</h3><ul><li>Swiss-made, privacy-focused</li><li>microSD backup in addition to seed</li><li>Minimalist interface</li></ul><h3>Caveats</h3><p>Fewer chains than Ledger. Great if your stack is BTC/ETH-centric.</p>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'choose', title: 'How to choose', content: `
<ol><li>List crypto you hold today and plan to hold</li><li>Compare price, display, connectivity (USB-C, Bluetooth)</li><li>Ensure firmware is updatable</li><li>Order from the official site — never unknown marketplaces</li></ol><div class="box box--warning"><span class="box-title">Warning</span>A device "already set up" or with a pre-filled seed = guaranteed scam.</div>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
    ],
    faq: [
      { q: 'Ledger or Trezor for beginners?', a: 'Both work well. Ledger has more Italian tutorials; Trezor focuses on open-source transparency.' },
      { q: 'Do I need the most expensive model?', a: 'No. Nano S Plus or Trezor Safe 3 are enough for most users.' },
    ]
  }
  'difendersi-phishing': {
    intro: 'Phishing is the most common attack in crypto. You do not need a genius hacker: a convincing link and a moment of distraction are enough. Learn to spot it before it is too late.',
    sections: [
      { id: 'what-is', title: 'What is crypto phishing', content: `
<p>Messages mimicking exchanges, wallets, airdrops, or "technical support" to steal seed phrases, passwords, or trick you into signing malicious transactions.</p><h3>Common channels</h3><ul><li>Emails and SMS with urgent links</li><li>Google/Facebook ads with similar URLs</li><li>DMs on Telegram, Discord, X</li><li>Clone sites of MetaMask, Ledger, Uniswap</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'signals', title: 'Warning signs', content: `
<ul><li>Urgency: "Your account will be locked in 24 hours"</li><li>Requests for seed phrase or private keys</li><li>Slightly different URLs (metamask.io vs metamask.com)</li><li>Promises to double BTC or "exclusive" airdrops</li><li>Unsolicited support contacting you first</li></ul><div class="box box--danger"><span class="box-title">Golden rule</span>No legitimate service will ever ask for your seed phrase. Not Ledger, MetaMask, or Binance.</div>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'defense', title: 'How to defend yourself', content: `
<ol><li>Bookmark official sites — do not use email links</li><li>Always verify the URL character by character</li><li>Enable 2FA with an authenticator app (not SMS)</li><li>Use a dedicated email for exchanges and crypto</li><li>Review token approvals periodically</li></ol>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'clicked', title: 'If you clicked a suspicious link', content: `
<p><strong>Do not enter data.</strong> Close the page. If you typed your seed: immediately transfer funds to a new wallet. If you connected your wallet to a fake site: revoke approvals on revoke.cash or etherscan.io.</p>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
    ],
    faq: [
      { q: 'How do I verify if a site is official?', a: 'Check the exact domain, HTTPS certificate, and compare with links from the company\'s official X account or documentation.' },
      { q: 'Does phishing only target beginners?', a: 'No. Even experienced users fall for sophisticated scams. Verification habits protect everyone.' },
    ]
  }
  'approvazioni-smart-contract': {
    intro: 'Every time you use Uniswap, OpenSea, or a DeFi protocol, you sign <strong>approvals</strong> allowing a smart contract to move your tokens. Understanding what you sign is essential for security.',
    sections: [
      { id: 'what-are', title: 'What are approvals', content: `
<p>An approval (allowance) authorizes a contract to withdraw a certain amount of tokens from your wallet without asking each time.</p><h3>Types</h3><ul><li><strong>Limited</strong> — specific amount (safer)</li><li><strong>Unlimited</strong> — full token access (risky)</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'risks', title: 'Risks of open approvals', content: `
<p>If a contract is compromised or was malicious from the start, it can drain approved tokens — even months later.</p><div class="box box--danger"><span class="box-title">Never</span>Approve unlimited amounts on protocols you do not know or use regularly.</div>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'check', title: 'How to check approvals', content: `
<ol><li>Visit <strong>revoke.cash</strong> or Etherscan Token Approvals</li><li>Connect your wallet (only on trusted sites)</li><li>Check each network: Ethereum, Polygon, BSC, Arbitrum</li><li>Revoke old or suspicious approvals</li></ol>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'practices', title: 'Best practices', content: `
<ul><li>Approve only the amount needed for a single operation</li><li>Use a separate wallet for experimental DeFi</li><li>Review approvals every 1-3 months</li><li>Before revoking, check network fees</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
    ],
    faq: [
      { q: 'Is revoking an approval dangerous?', a: 'No, it is a standard operation. It only costs the network fee for the revoke transaction.' },
      { q: 'Do I need this on all chains?', a: 'Yes. Each network has separate approvals. Check Ethereum, L2s, and sidechains where you have operated.' },
    ]
  }
  'backup-wallet-321': {
    intro: 'The <strong>3-2-1</strong> strategy comes from IT but applies perfectly to crypto: three copies, two media, one off-site. It is the bare minimum to avoid losing everything.',
    sections: [
      { id: 'strategy', title: 'The 3-2-1 rule explained', content: `
<ul><li><strong>3 copies</strong> of the seed phrase or backup</li><li><strong>2 different media</strong> — e.g. paper + steel, or paper + encrypted microSD</li><li><strong>1 off-site copy</strong> — physical location different from home (safe deposit box, trusted relative)</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'media', title: 'Recommended media', content: `
<h3>Paper</h3><p>Cheap, immediate. Use permanent ink, avoid sticky notes.</p><h3>Metal</h3><p>Cryptosteel, Billfodl plates: resist fire and flooding.</p><h3>microSD (hardware wallet)</h3><p>BitBox supports card backup. Guard the card like treasure.</p>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'avoid', title: 'What NOT to use as backup', content: `
<ul><li>❌ Screenshots, photos, unencrypted digital files</li><li>❌ Cloud (iCloud, Google Drive, Dropbox)</li><li>❌ Email to yourself</li><li>❌ Password manager for the seed (only for exchange passwords)</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'test', title: 'Test your backup', content: `
<p>An untested backup is useless. Once a year (or after major moves):</p><ol><li>Recover the wallet on a clean device using the seed</li><li>Verify addresses match</li><li>Close without leaving traces on the test device</li></ol>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
    ],
    faq: [
      { q: 'Are three copies too many?', a: 'No. One can burn, one can get wet, one can get lost. Redundancy is the point.' },
      { q: 'Can I give a copy to a family member?', a: 'Only if they understand it is like giving house keys. Consider an additional passphrase (BIP39 passphrase) for extra protection.' },
    ]
  }
  'sicurezza-mobile': {
    intro: 'The phone is the most used wallet for beginners — and the most stolen, lost, or infected. A few precautions drastically reduce risk.',
    sections: [
      { id: 'threat', title: 'Why mobile is at risk', content: `
<ul><li>Malicious apps with excessive permissions</li><li>Stolen or lost phone</li><li>Unsafe public Wi-Fi</li><li>Phone cloud backup including screenshots</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'protect', title: 'Protect the device', content: `
<ol><li>Strong PIN (6+ digits) or passphrase — not fingerprint alone</li><li>Always install OS updates</li><li>Download wallets only from official App Store / Play Store</li><li>Disable cloud backup for wallet apps if possible</li><li>Do not jailbreak/root if using wallets with real funds</li></ol>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'wallet-app', title: 'Mobile wallet setup', content: `
<ul><li>Enable biometrics <strong>in addition to</strong> wallet PIN</li><li>Disable notification previews showing amounts</li><li>Never screenshot the seed</li><li>Use verifiable open-source wallets when possible</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'lost', title: 'If you lose or get robbed', content: `
<p>Paper seed saves you. Install the wallet on a new device, import the seed, verify funds. Change exchange passwords and revoke active sessions.</p><div class="box box--warning"><span class="box-title">Without seed</span>If you have no seed backup, funds on the lost phone are unrecoverable.</div>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
    ],
    faq: [
      { q: 'Is Trust Wallet safe?', a: 'Widely used but still a hot wallet. Safe for small amounts if you follow best practices. For large holdings use a hardware wallet.' },
      { q: 'Should I use a VPN?', a: 'Useful on public Wi-Fi. At home on a trusted network it is less critical, but does not replace good habits.' },
    ]
  }
  'wallet-compromesso': {
    intro: 'Suspect someone has access to your wallet? Every minute counts. Follow this action plan without panic — but without wasting time.',
    sections: [
      { id: 'signals', title: 'Signs of compromise', content: `
<ul><li>Transactions you did not authorize</li><li>Unknown approvals on revoke.cash</li><li>Exchange login from unusual IP or country</li><li>You entered your seed on a suspicious site</li><li>You installed an unofficial app or extension</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'immediate', title: 'Immediate actions (first 15 minutes)', content: `
<ol><li><strong>Stop</strong> — do not sign more transactions</li><li>If you have a safe seed elsewhere: create a <strong>new wallet</strong> on a clean device</li><li>Transfer all funds to the new address with high fees if speed matters</li><li>Revoke all approvals on the old address</li></ol><div class="box box--danger"><span class="box-title">Priority</span>Save funds before figuring out how it happened.</div>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'exchange', title: 'If funds are on an exchange', content: `
<ol><li>Change password immediately</li><li>Revoke API keys and active sessions</li><li>Enable or verify 2FA (authenticator, not SMS)</li><li>Contact official support only from verified site</li><li>Withdraw to self-custody wallet if possible</li></ol>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'after', title: 'After the emergency', content: `
<ul><li>Analyze how the compromise happened</li><li>Replace device or reinstall OS if malware</li><li>New seed phrase — do not reuse the compromised one</li><li>Document for possible report (cyber police)</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
    ],
    faq: [
      { q: 'Can I recover stolen funds?', a: 'Rarely. On-chain transactions are irreversible. Acting in time is the only real defense.' },
      { q: 'Should I file a report?', a: 'Recommended for scams and phishing. Keep transaction hashes, URLs, screenshots.' },
    ]
  }
  'password-manager-crypto': {
    intro: 'Password managers and crypto go together — but with clear rules. They manage exchange passwords, not the seed phrase.',
    sections: [
      { id: 'why', title: 'Why use one', content: `
<ul><li>Unique, long passwords for each exchange</li><li>No reuse across platforms</li><li>2FA backup codes stored securely</li><li>Controlled sharing in family contexts (vault)</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'choice', title: 'Which to choose', content: `
<p>Reliable options: <strong>Bitwarden</strong> (open source), 1Password, KeePassXC (local). Avoid unknown or "free" solutions without audits.</p><h3>Minimum setup</h3><ol><li>Long master password (20+ chars) or passphrase</li><li>2FA on the vault itself</li><li>Backup PM recovery key in a secure physical location</li></ol>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'what-store', title: 'What to store in the password manager', content: `
<ul><li>✅ Exchange logins, crypto email, API key labels</li><li>✅ 2FA backup codes</li><li>✅ Notes on wallet addresses (public) and device PINs</li><li>❌ Seed phrase — never digital</li><li>❌ Raw private keys</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'habits', title: 'Secure habits', content: `
<p>Update passwords after known breaches. Do not autofill crypto sites from email links. Use the PM only on devices you control.</p>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
    ],
    faq: [
      { q: 'Is Bitwarden secure enough?', a: 'Yes, with a strong master password and 2FA. Zero-knowledge model protects data even if servers were compromised.' },
      { q: 'Can I store an encrypted seed in the PM?', a: 'Not recommended. Sync errors, malware, or subpoena still pose unacceptable risk.' },
    ]
  }
  'audit-sicurezza-portafoglio': {
    intro: 'A security audit does not require hacker skills: it is a checklist to verify where you store crypto, how you protect keys, and which habits expose you to risk.',
    sections: [
      { id: 'seed', title: 'Seed phrase and backup', content: `
<ul><li>□ Backup on paper/metal, never digital</li><li>□ At least 2 copies in different locations</li><li>□ Recovery test done in the last 12 months</li><li>□ No one besides you has unnecessary access</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'wallet-device', title: 'Wallets and devices', content: `
<ul><li>□ Hot wallet only for operational amounts</li><li>□ Hardware wallet for main storage</li><li>□ Wallet firmware updated</li><li>□ PIN/biometrics active on phone and apps</li><li>□ No wallet apps from unofficial sources</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'exchange', title: 'Exchanges and accounts', content: `
<ul><li>□ Authenticator 2FA (not SMS) on every exchange</li><li>□ Unique passwords via password manager</li><li>□ Withdrawal whitelist enabled where available</li><li>□ No significant funds left on exchange long-term</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'defi', title: 'DeFi and approvals', content: `
<ul><li>□ Token approvals reviewed in the last 3 months</li><li>□ No unlimited approvals on inactive protocols</li><li>□ Separate DeFi wallet from main wallet</li></ul>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
      { id: 'habits', title: 'Habits and phishing', content: `
<ul><li>□ Official sites bookmarked</li><li>□ Never seed requested by "support"</li><li>□ Dedicated email for crypto</li><li>□ Suspicious activity reported and revokes done</li></ul><div class="box box--tip"><span class="box-title">Frequency</span>Repeat the audit every 3-6 months or after every major purchase.</div>
<div class="box box--tip"><span class="box-title">Security first</span>Security is not optional: protect your seed phrase, devices, and habits before increasing your holdings.</div>
<div class="box box--info"><span class="box-title">Zero hype</span>100% educational content. No profit promises. Only concrete, verifiable practices.</div>

      `},
    ],
    faq: [
      { q: 'How long does it take?', a: '30-45 minutes the first time, 15 minutes afterwards.' },
      { q: 'What if I fail many items?', a: 'Priority: seed backup, 2FA, move funds from exchange to self-custody. One item at a time.' },
    ]
  }

};
