const CRYPTO_LOGOS = {
  eth: `<svg viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="16" fill="#627EEA"/><path d="M16 4v8.8l7.4 3.3L16 4z" fill="#fff" fill-opacity=".6"/><path d="M16 4L8.6 16.1 16 12.8V4z" fill="#fff"/><path d="M16 21.9v6.1l7.4-10.3L16 21.9z" fill="#fff" fill-opacity=".6"/><path d="M16 28v-6.1l-7.4-4.2L16 28z" fill="#fff"/><path d="M16 20.5l7.4-4.4L16 13.9v6.6z" fill="#fff" fill-opacity=".2"/><path d="M8.6 16.1l7.4 4.4v-6.6l-7.4 2.2z" fill="#fff" fill-opacity=".6"/></svg>`,

  xrp: `<svg viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="16" fill="#23292F"/><path d="M8 10h3.5l4.5 5.5L20.5 10H24l-6.5 8L24 26h-3.5l-4.5-5.5L11.5 26H8l6.5-8L8 10z" fill="#fff"/></svg>`,

  sol: `<svg viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="16" fill="#9945FF"/><path d="M10 20.5c.2-.2.5-.3.8-.3h12.2c.5 0 .7.6.4.9l-2.2 2.2c-.2.2-.5.3-.8.3H8.2c-.5 0-.7-.6-.4-.9l2.2-2.2zM10 13.5c.2-.2.5-.3.8-.3h12.2c.5 0 .7.6.4.9l-2.2 2.2c-.2.2-.5.3-.8.3H8.2c-.5 0-.7-.6-.4-.9l2.2-2.2zM18.8 6.5c.2-.2.5-.3.8-.3h2.2c.5 0 .7.6.4.9l-2.2 2.2c-.2.2-.5.3-.8.3h-2.2c-.5 0-.7-.6-.4-.9l2.2-2.2z" fill="#fff"/></svg>`,

  uni: `<svg viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="16" fill="#FF007A"/><path d="M16 8c-1.5 0-2.8.5-3.8 1.5-1 1-1.5 2.3-1.5 3.8 0 1 .3 1.9.8 2.7-.8.3-1.5.8-2 1.5-.8 1-1.2 2.2-1.2 3.5 0 2.8 2.2 5 5 5h4c2.8 0 5-2.2 5-5 0-1.3-.4-2.5-1.2-3.5-.5-.7-1.2-1.2-2-1.5.5-.8.8-1.7.8-2.7 0-1.5-.5-2.8-1.5-3.8C18.8 8.5 17.5 8 16 8z" fill="#fff" fill-opacity=".9"/></svg>`,

  aave: `<svg viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="16" fill="#B6509E"/><path d="M8 22l4-12h2.5l2 6.5 2-6.5H21l4 12h-2.5l-2.5-7.5L18 22h-2l-2.5-7.5L11.5 22H8z" fill="#fff"/></svg>`,

  link: `<svg viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="16" fill="#2A5ADA"/><path d="M14 10h-2.5c-2 0-3.5 1.5-3.5 3.5v5c0 2 1.5 3.5 3.5 3.5H14V10zm4 0v12h2.5c2 0 3.5-1.5 3.5-3.5v-5c0-2-1.5-3.5-3.5-3.5H18z" fill="#fff"/></svg>`,

  doge: `<svg viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="16" fill="#C2A633"/><ellipse cx="16" cy="15" rx="7" ry="6" fill="#F5E6A3"/><circle cx="13" cy="14" r="1.2" fill="#333"/><circle cx="19" cy="14" r="1.2" fill="#333"/><ellipse cx="16" cy="17" rx="2" ry="1.2" fill="#333"/><path d="M10 12c-2 0-3 1.5-3 3.5" stroke="#8B6914" stroke-width="1.5" fill="none"/></svg>`,

  pepe: `<svg viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="16" fill="#3D9E4F"/><ellipse cx="16" cy="17" rx="8" ry="7" fill="#5CB85C"/><circle cx="12" cy="14" r="3.5" fill="#fff"/><circle cx="20" cy="14" r="3.5" fill="#fff"/><circle cx="12" cy="14" r="1.8" fill="#333"/><circle cx="20" cy="14" r="1.8" fill="#333"/><path d="M13 20q3 3 6 0" stroke="#2D6B35" stroke-width="1.5" fill="none" stroke-linecap="round"/></svg>`,

  shib: `<svg viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="16" fill="#FFA409"/><ellipse cx="16" cy="16" rx="7" ry="8" fill="#F5D5A0"/><circle cx="13" cy="14" r="1" fill="#333"/><circle cx="19" cy="14" r="1" fill="#333"/><ellipse cx="16" cy="18" rx="2.5" ry="1.5" fill="#E8873D"/><path d="M11 11l2 1M21 11l-2 1" stroke="#8B4513" stroke-width="1" stroke-linecap="round"/></svg>`,

  matic: `<svg viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="16" fill="#8247E5"/><path d="M20 8.5l-4-2.3-4 2.3v4.6l4 2.3 4-2.3v-4.6zm-8 9.2l-4 2.3v4.6l4 2.3 4-2.3v-4.6l-4-2.3z" fill="#fff" fill-opacity=".85"/></svg>`
};

const FLOATING_COINS = [
  { id: 'btc',   label: 'Bitcoin',   x: 8,  delay: 0,   duration: 28, size: 52, depth: 1 },
  { id: 'eth',   label: 'Ethereum',  x: 22, delay: 4,   duration: 32, size: 48, depth: 2 },
  { id: 'ada',   label: 'Cardano',   x: 78, delay: 2,   duration: 26, size: 44, depth: 1 },
  { id: 'xrp',   label: 'XRP',       x: 65, delay: 7,   duration: 30, size: 40, depth: 3 },
  { id: 'sol',   label: 'Solana',    x: 42, delay: 1,   duration: 24, size: 38, depth: 2 },
  { id: 'uni',   label: 'Uniswap',   x: 88, delay: 9,   duration: 34, size: 36, depth: 2 },
  { id: 'aave',  label: 'Aave',      x: 15, delay: 12,  duration: 29, size: 34, depth: 3 },
  { id: 'link',  label: 'Chainlink', x: 55, delay: 5,   duration: 31, size: 36, depth: 1 },
  { id: 'doge',  label: 'Dogecoin',  x: 32, delay: 8,   duration: 22, size: 42, depth: 2, cute: true },
  { id: 'pepe',  label: 'Pepe',      x: 72, delay: 3,   duration: 20, size: 40, depth: 2, cute: true },
  { id: 'shib',  label: 'Shiba Inu', x: 48, delay: 11,  duration: 23, size: 38, depth: 3, cute: true },
  { id: 'matic', label: 'Polygon',   x: 92, delay: 6,   duration: 27, size: 32, depth: 3 },
  { id: 'btc',   label: 'Bitcoin',   x: 58, delay: 15,  duration: 35, size: 30, depth: 3 },
  { id: 'eth',   label: 'Ethereum',  x: 5,  delay: 18,  duration: 33, size: 28, depth: 3 },
  { id: 'ada',   label: 'Cardano',   x: 38, delay: 20,  duration: 25, size: 32, depth: 2 },
  { id: 'doge',  label: 'Dogecoin',  x: 82, delay: 14,  duration: 21, size: 34, depth: 1, cute: true },
  { id: 'snek',  label: 'Snek',      x: 25, delay: 6,   duration: 19, size: 46, depth: 1, cute: true, meme: true },
  { id: 'snek',  label: 'Snek',      x: 68, delay: 16,  duration: 22, size: 36, depth: 2, cute: true, meme: true }
];

const CRYPTO_IMAGES = {
  btc: 'assets/img/bitcoin-btc.png',
  ada: 'assets/img/cardano-ada.png',
  snek: 'assets/img/meme-snek.png'
};

function getCryptoLogo(id) {
  if (CRYPTO_IMAGES[id]) {
    const base = typeof getBasePath === 'function' ? getBasePath() : '';
    const extraClass = id === 'snek' ? ' crypto-coin-img--snek' : id === 'btc' ? ' crypto-coin-img--btc' : '';
    return `<img src="${base}${CRYPTO_IMAGES[id]}" alt="" class="crypto-coin-img${extraClass}" loading="lazy" draggable="false" />`;
  }
  return CRYPTO_LOGOS[id] || '';
}

function renderCryptoBackground() {
  const coins = FLOATING_COINS.map(c => `
    <div class="crypto-coin crypto-coin--depth-${c.depth}${c.cute ? ' crypto-coin--cute' : ''}${c.id === 'btc' ? ' crypto-coin--btc' : ''}${c.id === 'ada' ? ' crypto-coin--ada' : ''}${c.meme ? ' crypto-coin--meme' : ''}"
         style="--x:${c.x}%;--delay:${c.delay}s;--duration:${c.duration}s;--size:${c.size}px"
         aria-hidden="true"
         title="${c.label}">
      <div class="crypto-coin-glow"></div>
      <div class="crypto-coin-icon">${getCryptoLogo(c.id)}</div>
    </div>`).join('');

  const base = typeof getBasePath === 'function' ? getBasePath() : '';
  const photoUrl = `${base}assets/img/crypto-hero-bg.png`;

  return `
    <div class="crypto-bg" id="crypto-bg" aria-hidden="true">
      <div class="crypto-bg-photo" style="background-image:url('${photoUrl}')"></div>
      <div class="crypto-bg-overlay"></div>
      <div class="crypto-bg-mesh"></div>
      <div class="crypto-bg-grid"></div>
      <div class="crypto-bg-orb crypto-bg-orb--1"></div>
      <div class="crypto-bg-orb crypto-bg-orb--2"></div>
      <div class="crypto-bg-orb crypto-bg-orb--3"></div>
      <div class="crypto-coins-layer">${coins}</div>
    </div>`;
}

function initCryptoBackground() {
  if (document.getElementById('crypto-bg')) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.body.classList.add('crypto-bg-static');
  }
  const bg = document.createElement('div');
  bg.innerHTML = renderCryptoBackground();
  document.body.insertBefore(bg.firstElementChild, document.body.firstChild);
}