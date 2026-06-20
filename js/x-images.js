/**
 * Immagini clickbait per post X — @TheRiser100x
 */
const X_IMAGE_BASE = 'assets/img/x/posts/';

const X_SLOT_TYPES = ['bitcoin', 'regulation', 'elon', 'bitcoin_breaking', 'bitcoin_viral'];

const X_SLOT_TIMES = ['08:00', '11:15', '14:30', '17:45', '21:00'];

const X_SLOT_LABELS = {
  bitcoin: '₿ Bitcoin + foto clickbait',
  regulation: '⚖️ Regolamentazione crypto',
  elon: '🔄 Repost Elon Musk',
  bitcoin_breaking: '🚨 Breaking BTC',
  bitcoin_viral: '🔥 Top viral Bitcoin'
};

const X_SLOT_IMAGES = {
  bitcoin: 'bitcoin.jpg',
  regulation: 'regulation.jpg',
  elon: 'elon.jpg',
  bitcoin_breaking: 'breaking.jpg',
  bitcoin_viral: 'bitcoin.jpg'
};

function getXImageForSlot(slotIndex) {
  const type = X_SLOT_TYPES[slotIndex] || 'bitcoin';
  return `${X_IMAGE_BASE}${X_SLOT_IMAGES[type] || 'bitcoin.jpg'}`;
}

function getXImageForItem(item) {
  if (item?.xImage) return item.xImage.replace(/^https?:\/\/[^/]+\/[^/]+\//, '');
  const cat = item?.postCategory || 'bitcoin';
  const idx = X_SLOT_TYPES.indexOf(cat);
  return getXImageForSlot(idx >= 0 ? idx : 0);
}