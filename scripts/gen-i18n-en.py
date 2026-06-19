#!/usr/bin/env python3
"""Generate English translations for articles.json"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_PATH = ROOT / "data" / "articles.json"

# slug -> (titleEn, excerptEn)
ARTICLE_EN = {
    "iniziare-exchange-revolut-kraken": (
        "Getting started with exchanges: Revolut + Kraken guide for beginners",
        "Crypto exchanges explained simply: why use Revolut, how to sign up on Kraken and make your first safe purchase.",
    ),
    "lightning-network-guida": (
        "Lightning Network explained simply: sats, wallets and Satoshi Wallet",
        "What Lightning is, how sats work, which wallets to use and how to pay with the Satoshi Wallet merchant map.",
    ),
    "comprare-bitcoin-prima-volta": (
        "How to buy Bitcoin for the first time (complete 2026 guide)",
        "Exchange, identity verification, first purchase and security: everything step by step.",
    ),
    "creare-wallet-sicuro": (
        "How to create a secure crypto wallet in 10 minutes",
        "Hot wallet, cold wallet and basic setup to protect your crypto.",
    ),
    "trasferire-crypto-exchange": (
        "How to transfer crypto from an exchange to a personal wallet",
        "Safe withdrawal: network, address, fees and transaction verification.",
    ),
    "staking-ethereum": (
        "How to stake Ethereum: step-by-step guide",
        "Direct staking, liquid staking and what to expect in terms of returns.",
    ),
    "usare-metamask": (
        "How to use MetaMask: installation and first transaction",
        "Install MetaMask, configure the network and send your first transaction.",
    ),
    "leggere-indirizzo-wallet": (
        "How to read a wallet address and verify a transaction",
        "Understanding addresses, transaction hashes and block explorers.",
    ),
    "dichiarare-crypto-italia": (
        "How to declare crypto in Italy (practical overview)",
        "RW form, RT section and tax obligations explained simply.",
    ),
    "scegliere-exchange-sicuro": (
        "How to choose a safe exchange: 7-point checklist",
        "Regulation, reputation, fees and security: what to check.",
    ),
    "proteggere-seed-phrase": (
        "How to protect your seed phrase: methods and mistakes to avoid",
        "The golden rule of crypto security: keeping your 12-24 recovery words safe.",
    ),
    "prima-swap-uniswap": (
        "How a DEX works: your first swap on Uniswap",
        "Decentralized exchange, liquidity and your first DeFi operation.",
    ),
    "hardware-wallet-ledger": (
        "How to set up a Ledger hardware wallet from scratch",
        "Setup, seed backup and first transaction with Ledger.",
    ),
    "capire-gas-fee": (
        "How to understand network fees (gas) and when to operate",
        "Gas on Ethereum and other networks: how to save on fees.",
    ),
    "dca-crypto": (
        "How to do DCA (Dollar Cost Averaging) with crypto",
        "Invest in installments without trying to time the market.",
    ),
    "verificare-smart-contract": (
        "How to verify a smart contract before investing",
        "Tools and red flags to avoid DeFi scams.",
    ),
    "usare-etherscan": (
        "How to use a block explorer (Etherscan explained simply)",
        "Read transactions, contracts and wallets on Etherscan.",
    ),
    "cold-wallet-chiavi-offline": (
        "How to create a cold wallet with offline keys",
        "Generate and store private keys without an internet connection.",
    ),
    "yield-farming-sicurezza": (
        "How to do yield farming safely (first steps)",
        "Provide liquidity without unnecessary risks: a cautious guide.",
    ),
    "convertire-crypto-euro": (
        "How to convert crypto to euros and withdraw",
        "Selling on an exchange, bank transfer and timelines.",
    ),
    "alert-prezzo-portafoglio": (
        "How to set price alerts and monitor your portfolio",
        "Apps and tools to keep track of your assets.",
    ),
    "recuperare-crypto-sbagliato": (
        "How to recover crypto sent to the wrong address",
        "What can and cannot be recovered: a realistic guide.",
    ),
    "tip-mai-seed-phrase": (
        "Never share your seed phrase — not even with \"support\"",
        "No legitimate service will ever ask for your 12 or 24 recovery words.",
    ),
    "tip-2fa-exchange": (
        "Always enable 2FA on your exchange (not via SMS)",
        "Two-factor authentication with a dedicated app, never SMS.",
    ),
    "tip-verifica-url": (
        "Verify the exchange URL: phishing starts there",
        "Always check the address bar before entering credentials.",
    ),
    "tip-non-tenere-exchange": (
        "Don't keep all your crypto on an exchange",
        "Exchanges are for buying/selling, not long-term storage.",
    ),
    "tip-inizia-poco": (
        "Start with a small amount: learn before investing big",
        "Better to make mistakes with €20 than with €2,000.",
    ),
    "tip-controlla-rete": (
        "Check the network before sending (ERC-20 ≠ BEP-20)",
        "Sending on the wrong network can be costly.",
    ),
    "tip-rubrica-wallet": (
        "Save frequent addresses in your wallet address book",
        "Avoid typos on addresses you use often.",
    ),
    "tip-no-screenshot-seed": (
        "Screenshot your seed? You've already lost",
        "Photos in the cloud are an easy target for hackers.",
    ),
    "tip-diffida-telegram": (
        "Beware of \"guaranteed returns\" on Telegram",
        "If they promise fixed returns, it's almost certainly a scam.",
    ),
    "tip-aggiorna-wallet": (
        "Always update wallets and apps",
        "Updates fix security vulnerabilities.",
    ),
    "tip-email-dedicata": (
        "Use a dedicated email for crypto only",
        "Separate crypto communications from the rest of your digital life.",
    ),
    "tip-leggi-transazione": (
        "Before signing a transaction, read what you're approving",
        "Every \"Confirm\" click can authorize a withdrawal.",
    ),
    "tip-diversifica": (
        "Diversify: don't put everything on one crypto",
        "A balanced portfolio reduces concentrated risk.",
    ),
    "tip-traccia-operazioni": (
        "Track every operation for tax reporting",
        "A spreadsheet or tracking app will save you at year-end.",
    ),
    "tip-spread-fee": (
        "The price you see isn't what you pay (spread + fees)",
        "Always calculate the total cost of the operation.",
    ),
    "tip-staking-unlock": (
        "Staking: understand the unlock period before locking funds",
        "Some staking locks funds for days or weeks.",
    ),
    "tip-test-transazione": (
        "New wallet? Test with a few cents first",
        "Verify everything works before sending large amounts.",
    ),
    "tip-no-link-email": (
        "Don't click crypto links from suspicious emails",
        "Always go directly to the site by typing the URL.",
    ),
    "tip-pin-wallet": (
        "Set a strong PIN on your mobile wallet",
        "Protect wallet access on your smartphone.",
    ),
    "tip-non-capisci-non-investi": (
        "If you don't understand the project, don't invest",
        "The simplest and most effective rule to avoid scams.",
    ),
    "trend-mica": (
        "What is MiCA regulation and what changes in Europe",
        "The new European framework for cryptocurrencies explained clearly.",
    ),
    "trend-etf-bitcoin": (
        "Bitcoin Spot ETF: what they are and why they matter",
        "Listed funds tracking Bitcoin: impact and what it means for you.",
    ),
    "trend-layer2": (
        "Layer 2: why Ethereum needs \"secondary roads\"",
        "Scalability solutions to reduce fees and confirmation times.",
    ),
    "trend-rwa": (
        "Real World Assets (RWA): crypto representing real assets",
        "Tokenization of real estate, bonds and commodities.",
    ),
    "trend-stablecoin": (
        "Stablecoins: how they work and what risks they hide",
        "USDT, USDC and DAI: apparent stability, real risks.",
    ),
    "trend-cbdc": (
        "CBDC: central bank digital currencies explained",
        "Digital euro and sovereign currencies: differences from decentralized crypto.",
    ),
    "trend-depin": (
        "DePIN: decentralized physical infrastructure",
        "Decentralized networks for storage, WiFi, energy and more.",
    ),
    "trend-ai-blockchain": (
        "AI + Blockchain: trend or real utility?",
        "Where artificial intelligence meets blockchain.",
    ),
    "trend-halving": (
        "The Bitcoin halving: what it is and why everyone talks about it",
        "Reduction of miner rewards: effects on the market.",
    ),
    "trend-modular-blockchain": (
        "Modular Blockchain: the new architecture of crypto networks",
        "Separating consensus, execution and data availability.",
    ),
    "blockchain-5-minuti": (
        "First steps: what is a blockchain in 5 minutes",
        "The fundamental concept explained without technical jargon.",
    ),
    "creare-account-exchange": (
        "Create an account on Coinbase/Kraken (with screenshots)",
        "Registration, KYC verification and first steps on the exchange.",
    ),
    "primi-20-euro-bitcoin": (
        "Buy your first €20 of Bitcoin",
        "Buy order, payment and confirmation step by step.",
    ),
    "installare-trust-wallet": (
        "Install and configure Trust Wallet",
        "Download, setup and first crypto receipt.",
    ),
    "prima-transazione-crypto": (
        "Send and receive your first crypto",
        "From copying the address to on-chain confirmation.",
    ),
    "leggere-grafico-candele": (
        "Read a price chart (basic candlesticks)",
        "Candlesticks, timeframes and volume for beginners.",
    ),
    "market-cap-volume": (
        "Understanding market cap, volume and supply",
        "The basic metrics to evaluate a cryptocurrency.",
    ),
    "esplorare-block-explorer": (
        "Explore your first transaction on a blockchain explorer",
        "Find and read your transaction on the blockchain.",
    ),
    "notifiche-prezzo-app": (
        "Set price notifications on mobile apps",
        "Custom alerts with CoinGecko and similar apps.",
    ),
    "creare-watchlist": (
        "Create your first personalized watchlist",
        "Monitor the crypto you're interested in.",
    ),
    "bridge-cross-chain": (
        "Cross-chain bridge: transfer assets between Ethereum and Arbitrum",
        "Bridges between blockchains: how they work and risks to consider.",
    ),
    "liquidita-uniswap-v3": (
        "Provide liquidity on Uniswap V3 (with impermanent loss calculation)",
        "Concentrated liquidity and impermanent loss risk.",
    ),
    "usare-aave": (
        "Use Aave for DeFi lending and deposits",
        "Decentralized lending and borrowing on Aave.",
    ),
    "analisi-on-chain-dune": (
        "On-chain analysis with Dune Analytics",
        "SQL queries and dashboards for blockchain analysis.",
    ),
    "nodo-validator": (
        "Configure a validator node (requirements overview)",
        "Hardware, software and costs to validate a network.",
    ),
    "leggere-solidity": (
        "Smart contracts: read basic Solidity code",
        "Functions, variables and common patterns for non-developers.",
    ),
    "mev-protezione": (
        "MEV and protection in DeFi transactions",
        "Maximal Extractable Value and how to defend against it.",
    ),
    "multisig-gnosis-safe": (
        "Multisig wallet with Gnosis Safe",
        "Multi-signature wallet for teams and DAOs.",
    ),
    "ottimizzazione-gas-batch": (
        "Gas optimization with batch transactions",
        "Group operations to save on fees.",
    ),
    "hedging-stablecoin": (
        "Hedging strategies with stablecoins and DeFi derivatives",
        "Protect your portfolio in volatile markets.",
    ),
    "cardano-spiegato": (
        "Cardano explained simply: what is ADA",
        "The proof-of-stake blockchain founded on academic research.",
    ),
    "comprare-ada": (
        "How to buy ADA on exchanges",
        "Where and how to buy Cardano.",
    ),
    "staking-ada": (
        "Staking ADA: complete guide (delegation vs pool)",
        "Delegate ADA to a staking pool: returns and pool selection.",
    ),
    "wallet-cardano-confronto": (
        "Eternl, Nami, Yoroi: which Cardano wallet to choose",
        "Comparison of the most used wallets in the Cardano ecosystem.",
    ),
    "project-catalyst": (
        "How to vote on Project Catalyst",
        "Participate in ecosystem governance and funding.",
    ),
    "cardano-defi": (
        "Cardano DeFi: Minswap, SundaeSwap and liquidity pools",
        "The main DEXs and DeFi protocols on Cardano.",
    ),
    "native-token-cardano": (
        "Native tokens on Cardano: create and manage assets",
        "Native tokens without complex smart contracts.",
    ),
    "hydra-cardano": (
        "Hydra: what it is and what it will change for scalability",
        "Cardano's Layer 2 for ultra-fast transactions.",
    ),
    "plutus-panoramica": (
        "Cardano smart contracts (Plutus): overview for users",
        "How smart contracts work on Cardano.",
    ),
    "cardano-vs-ethereum": (
        "Cardano vs Ethereum: practical differences for users",
        "A real comparison between the two ecosystems for beginners.",
    ),
    "seed-phrase-guida": (
        "Seed phrase: what it is, how to generate and store it",
        "Everything about wallet recovery words.",
    ),
    "hot-vs-cold-wallet": (
        "Hot wallet vs cold wallet: differences and when to use each",
        "Practical comparison between online and offline wallets.",
    ),
    "confronto-hardware-wallet": (
        "Hardware wallets: Ledger vs Trezor vs BitBox comparison",
        "Which device to choose for maximum security.",
    ),
    "difendersi-phishing": (
        "Recognize and defend against crypto phishing",
        "Warning signs and anti-scam best practices.",
    ),
    "approvazioni-smart-contract": (
        "Smart contract approvals: what you sign and how to revoke them",
        "Check and revoke permissions on your tokens.",
    ),
    "backup-wallet-321": (
        "Wallet backup: 3-2-1 strategy for crypto",
        "Three copies, two media, one off-site.",
    ),
    "sicurezza-mobile": (
        "Mobile security: protect wallets on your smartphone",
        "PIN, biometrics and precautions for mobile wallets.",
    ),
    "wallet-compromesso": (
        "What to do if you suspect your wallet is compromised",
        "Immediate action plan in case of emergency.",
    ),
    "password-manager-crypto": (
        "Password managers and crypto: best practices",
        "Manage passwords and secure notes for the crypto ecosystem.",
    ),
    "audit-sicurezza-portafoglio": (
        "Security audit of your portfolio (checklist)",
        "25 points to verify for a secure portfolio.",
    ),
}

GLOSSARY_EN = {
    "Blockchain": "Distributed digital ledger that records transactions immutably and transparently.",
    "Wallet": "Software or hardware tool to store and manage your cryptocurrencies.",
    "Seed Phrase": "Sequence of 12-24 words that allows you to recover a wallet. Must be kept offline.",
    "Exchange": "Platform where you buy, sell and trade cryptocurrencies.",
    "Staking": "Lock crypto to support a network and receive rewards.",
    "DeFi": "Decentralized finance: financial services without centralized intermediaries.",
    "Gas Fee": "Fee paid to execute transactions on a blockchain.",
    "Smart Contract": "Automatic program on the blockchain that executes agreements without intermediaries.",
    "DEX": "Decentralized exchange: peer-to-peer trading via smart contracts.",
    "KYC": "Know Your Customer: identity verification required by regulated exchanges.",
    "Cold Wallet": "Offline wallet, not connected to the internet, for maximum security.",
    "Hot Wallet": "Wallet connected to the internet, convenient but less secure than a cold wallet.",
    "MiCA": "Markets in Crypto-Assets: European regulation for cryptocurrencies.",
    "Layer 2": "Scalability solution built on top of a main blockchain.",
    "ADA": "Native cryptocurrency of the Cardano blockchain.",
    "Pool di Staking": "Group of validators to delegate your crypto for staking.",
    "Phishing": "Scam attempt to steal credentials or seed phrases via fake sites.",
    "2FA": "Two-factor authentication: second security layer beyond your password.",
    "Market Cap": "Total value of a crypto: price × number of coins in circulation.",
    "Stablecoin": "Cryptocurrency pegged to the value of a stable asset, like the dollar.",
    "Lightning Network": "Second-layer network on Bitcoin for instant, ultra-low-cost payments via payment channels.",
    "Satoshi (sat)": "Smallest unit of Bitcoin: 1 BTC = 100,000,000 satoshi. Sats are used in Lightning payments.",
    "Invoice Lightning": "Lightning payment request with amount and recipient, often shared as QR code or text string.",
}

DATE_EN = {
    "Giugno 2026": "June 2026",
    "Maggio 2026": "May 2026",
    "Aprile 2026": "April 2026",
    "Marzo 2026": "March 2026",
    "Febbraio 2026": "February 2026",
    "Gennaio 2026": "January 2026",
}

def main():
    with open(ARTICLES_PATH, encoding="utf-8") as f:
        data = json.load(f)

    missing = []
    for article in data["articles"]:
        slug = article["slug"]
        if slug in ARTICLE_EN:
            article["titleEn"] = ARTICLE_EN[slug][0]
            article["excerptEn"] = ARTICLE_EN[slug][1]
        else:
            missing.append(slug)
        if article.get("date") in DATE_EN:
            article["dateEn"] = DATE_EN[article["date"]]

    for term in data["glossary"]:
        if term["term"] in GLOSSARY_EN:
            term["definitionEn"] = GLOSSARY_EN[term["term"]]
        else:
            missing.append(f"glossary:{term['term']}")

    if missing:
        print("MISSING:", missing)
        raise SystemExit(1)

    with open(ARTICLES_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"Updated {len(data['articles'])} articles and {len(data['glossary'])} glossary terms")

if __name__ == "__main__":
    main()