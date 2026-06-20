/**
 * Testi virali X per @TheRiser100x — preview lato client
 */
const X_ACCOUNT_URL = 'https://x.com/TheRiser100x';

const X_VIRAL_HOOKS = {
  breaking: '🚨 BREAKING',
  whitehouse: '🇺🇸 WHITE HOUSE · CRYPTO',
  bitcoin: '₿ BITCOIN ALERT',
  ethereum: '⟠ ETH UPDATE',
  regulation: '⚖️ REGOLAMENTAZIONE CRYPTO',
  market: '📈 MERCATO CRYPTO',
  default: '🔥 CRYPTO NEWS'
};

const X_HASHTAGS = {
  whitehouse: '#WhiteHouse #Crypto #Bitcoin #USA #TheRiser100x',
  bitcoin: '#Bitcoin #BTC #Crypto #CryptoNews #TheRiser100x',
  ethereum: '#Ethereum #ETH #Crypto #DeFi #TheRiser100x',
  regulation: '#Crypto #Regulation #SEC #Bitcoin #TheRiser100x',
  market: '#Crypto #Bitcoin #Altcoins #CryptoNews #TheRiser100x',
  default: '#Crypto #Bitcoin #CryptoNews #BTC #TheRiser100x'
};

function detectXTopics(text, handle) {
  const low = (text || '').toLowerCase();
  const h = (handle || '').toLowerCase().replace('@', '');
  const topics = [];
  if (h === 'whitehouse' || /white house|whitehouse|biden|trump|congress/.test(low)) topics.push('whitehouse');
  if (/bitcoin|btc|satoshi/.test(low)) topics.push('bitcoin');
  if (/ethereum|\beth\b|\$eth/.test(low)) topics.push('ethereum');
  if (/sec|regulation|mica|law|ban|legal|fed|treasury/.test(low)) topics.push('regulation');
  if (/breaking|just in|alert|🚨/.test(low)) topics.push('breaking');
  if (/market|price|rally|dump|etf|surge/.test(low)) topics.push('market');
  return topics.length ? topics : ['default'];
}

function buildXViralPost(item) {
  if (item.viralPostText) return item.viralPostText;
  const raw = item.summary || item.title || '';
  const topics = detectXTopics(raw, item.sourceHandle);
  const hook = X_VIRAL_HOOKS[topics.find(t => X_VIRAL_HOOKS[t])] || X_VIRAL_HOOKS.default;
  const tags = X_HASHTAGS[topics.find(t => X_HASHTAGS[t])] || X_HASHTAGS.default;
  let body = raw.replace(/https?:\/\/\S+/g, '').replace(/@\w+/g, '').replace(/\s+/g, ' ').trim();
  if (!/[\u{1F300}-\u{1FAFF}]/u.test(body)) {
    body = (topics.includes('breaking') ? '🚨 ' : topics.includes('whitehouse') ? '🇺🇸 ' : '👀 ') + body;
  }
  if (body.length > 150) body = body.slice(0, 149) + '…';
  const via = item.sourceHandle ? `via ${item.sourceHandle}` : '';
  let post = `${hook}\n\n${body}`;
  if (via) post += `\n\n${via}`;
  post += `\n\n${tags}`;
  return post.length > 280 ? post.slice(0, 277) + '…' : post;
}

function getXShareUrl(text) {
  return `https://twitter.com/intent/tweet?text=${encodeURIComponent(text)}`;
}

function xViralScore(item) {
  const text = (item.title || '') + ' ' + (item.summary || '');
  const topics = detectXTopics(text, item.sourceHandle);
  let s = item.viralScore || item.priority || 0;
  if (topics.includes('breaking')) s += 8;
  if (topics.includes('whitehouse')) s += 10;
  if (topics.includes('regulation')) s += 6;
  if (topics.includes('bitcoin')) s += 5;
  if (item.breaking) s += 4;
  return s;
}