const FB_POST_EMOJI = {
  guide: '📖',
  tip: '💡',
  trend: '📈',
  tutorial: '🎓',
  cardano: '🔷',
  sicurezza: '🔒'
};

const FB_POST_LABELS = {
  guide: 'Guida',
  tip: 'Crypto Tip',
  trend: 'Trend',
  tutorial: 'Tutorial',
  cardano: 'Cardano',
  sicurezza: 'Sicurezza'
};

function getArticleUrl(slug) {
  const base = SITE_CONFIG.siteUrl || 'https://satoshiallien.github.io/cryptoitaliafacile/';
  return `${base.replace(/\/?$/, '/')}articolo.html?slug=${encodeURIComponent(slug)}`;
}

function buildFacebookHashtags(article) {
  const base = ['#crypto', '#The Little Satoshi News', '#educazione'];
  const fromTags = (article.tags || [])
    .slice(0, 4)
    .map(tag => tag.replace(/^#+/, '').replace(/[^a-zA-Z0-9àèéìòù]/g, ''))
    .filter(Boolean)
    .map(tag => `#${tag}`);
  return [...new Set([...fromTags, ...base])].join(' ');
}

function buildFacebookPost(article) {
  const emoji = FB_POST_EMOJI[article.category] || '📖';
  const label = FB_POST_LABELS[article.category] || 'Guida';
  const url = getArticleUrl(article.slug);
  return `${emoji} ${label}: ${article.title}\n\n${article.excerpt}\n\n👉 Leggi la guida completa:\n${url}\n\n${buildFacebookHashtags(article)}`;
}

function getFacebookShareUrl(articleUrl) {
  return `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(articleUrl)}`;
}

function getFacebookPageUrl() {
  return getSocial('facebook')?.url || 'https://www.facebook.com/profile.php?id=61591151756348';
}

function renderFacebookShareBar(article) {
  const url = getArticleUrl(article.slug);
  const post = buildFacebookPost(article);
  const shareUrl = getFacebookShareUrl(url);
  const pageUrl = getFacebookPageUrl();
  return `
    <div class="article-share" data-article-slug="${article.slug}">
      <span class="article-share-label">Condividi questa guida</span>
      <div class="article-share-actions">
        <a href="${shareUrl}" class="btn btn-facebook btn-sm" target="_blank" rel="noopener noreferrer">
          ${SOCIAL_ICONS.facebook} Condividi su Facebook
        </a>
        <button type="button" class="btn btn-ghost btn-sm" data-copy-fb-post>Copia testo post</button>
        <a href="${pageUrl}" class="btn btn-ghost btn-sm" target="_blank" rel="noopener noreferrer">Vai alla pagina FB</a>
      </div>
      <textarea class="article-share-draft" hidden readonly></textarea>
    </div>`;
}

const FB_SCHEDULE_SLOTS = {
  2: [
    { label: 'Mattina', time: '10:00', hint: 'Guida o articolo principale' },
    { label: 'Sera', time: '19:00', hint: 'Tip, trend o Cardano' }
  ],
  3: [
    { label: 'Mattina', time: '09:00', hint: 'Guida in evidenza' },
    { label: 'Pranzo', time: '13:00', hint: 'Crypto Tip breve' },
    { label: 'Sera', time: '19:00', hint: 'Trend, Cardano o Sicurezza' }
  ]
};

function articlePriority(article) {
  return (article.featured ? 4 : 0) + (article.popular ? 2 : 0);
}

function sortArticlesForSchedule(articles) {
  return [...articles].sort((a, b) =>
    articlePriority(b) - articlePriority(a) || a.title.localeCompare(b.title, 'it')
  );
}

function buildBalancedQueue(articles) {
  const buckets = {
    guide: sortArticlesForSchedule(articles.filter(a => a.category === 'guide' || a.category === 'tutorial')),
    tip: sortArticlesForSchedule(articles.filter(a => a.category === 'tip')),
    trend: sortArticlesForSchedule(articles.filter(a => a.category === 'trend')),
    other: sortArticlesForSchedule(articles.filter(a => ['cardano', 'sicurezza'].includes(a.category)))
  };
  const queue = [];
  const maxLen = Math.max(buckets.guide.length, buckets.tip.length, buckets.trend.length, buckets.other.length, 1);
  for (let i = 0; i < maxLen; i++) {
    if (buckets.guide[i]) queue.push(buckets.guide[i]);
    if (buckets.tip[i]) queue.push(buckets.tip[i]);
    if (buckets.trend[i]) queue.push(buckets.trend[i]);
    if (buckets.other[i]) queue.push(buckets.other[i]);
  }
  const seen = new Set();
  return queue.filter(a => {
    if (seen.has(a.slug)) return false;
    seen.add(a.slug);
    return true;
  });
}

function buildDailyPlan(articles, postsPerDay = 3) {
  const slots = FB_SCHEDULE_SLOTS[postsPerDay] || FB_SCHEDULE_SLOTS[3];
  const queue = buildBalancedQueue(articles);
  const days = [];
  for (let i = 0; i < queue.length; i += postsPerDay) {
    const chunk = queue.slice(i, i + postsPerDay);
    days.push({
      day: days.length + 1,
      posts: chunk.map((article, idx) => ({
        article,
        slot: slots[idx] || slots[slots.length - 1]
      }))
    });
  }
  return days;
}

function formatScheduleDate(startDate, dayIndex) {
  const d = new Date(startDate);
  d.setDate(d.getDate() + dayIndex);
  return d.toLocaleDateString('it-IT', { weekday: 'short', day: 'numeric', month: 'short' });
}

function getTodayPlanDay(plan, startDate) {
  const start = new Date(startDate);
  start.setHours(0, 0, 0, 0);
  const today = new Date();
  today.setHours(0, 0, 0, 0);
  const diff = Math.floor((today - start) / 86400000);
  if (diff < 0 || diff >= plan.length) return null;
  return plan[diff];
}

function initArticleFacebookShare(article) {
  const bar = document.querySelector('.article-share[data-article-slug]');
  if (!bar) return;
  const draft = bar.querySelector('.article-share-draft');
  const btn = bar.querySelector('[data-copy-fb-post]');
  if (!btn || !draft) return;
  draft.value = buildFacebookPost(article);
  btn.addEventListener('click', async () => {
    const text = buildFacebookPost(article);
    try {
      await navigator.clipboard.writeText(text);
      btn.textContent = 'Copiato!';
      setTimeout(() => { btn.textContent = 'Copia testo post'; }, 1800);
    } catch (_) {
      draft.hidden = false;
      draft.select();
    }
  });
}