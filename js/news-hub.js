const IT_MONTHS = {
  gennaio: 1, febbraio: 2, marzo: 3, aprile: 4, maggio: 5, giugno: 6,
  luglio: 7, agosto: 8, settembre: 9, ottobre: 10, novembre: 11, dicembre: 12
};

const EN_MONTHS = {
  january: 1, february: 2, march: 3, april: 4, may: 5, june: 6,
  july: 7, august: 8, september: 9, october: 10, november: 11, december: 12
};

function parseNewsSortKey(item) {
  if (item.dateSort) return new Date(item.dateSort).getTime();
  if (item.external && item.date) {
    const parsed = Date.parse(item.date.replace(/(\d{2}) (\w{3}) (\d{4})/, '$2 $1, $3'));
    if (!Number.isNaN(parsed)) return parsed;
  }
  const text = (item.date || '').toLowerCase();
  const months = { ...IT_MONTHS, ...EN_MONTHS };
  for (const [name, num] of Object.entries(months)) {
    if (text.includes(name)) {
      const yearMatch = text.match(/20\d{2}/);
      const year = yearMatch ? Number(yearMatch[0]) : 2026;
      return new Date(year, num - 1, 15).getTime();
    }
  }
  return 0;
}

function articleToNewsItem(article) {
  const loc = typeof localizeArticle === 'function' ? localizeArticle(article) : article;
  const base = typeof getBasePath === 'function' ? getBasePath() : '';
  const siteRoot = typeof SITE_CONFIG !== 'undefined' && SITE_CONFIG.siteUrl
    ? SITE_CONFIG.siteUrl
    : 'https://satoshiallien.github.io/cryptoitaliafacile/';
  const url = `${siteRoot}articolo.html?slug=${article.slug}`;
  return {
    id: `site-${article.slug}`,
    title: loc.title,
    summary: loc.excerpt,
    date: loc.date || article.date,
    category: article.category,
    feedType: article.category,
    source: 'The Little Satoshi News',
    sourceHandle: null,
    slug: article.slug,
    external: false,
    url: null,
    breaking: Boolean(article.popular || article.featured),
    readTime: article.readTime,
    postText: `📰 ${loc.title}\n\n${loc.excerpt}\n\n👉 ${url}\n\n#crypto #news`,
    sortKey: parseNewsSortKey({ date: loc.date || article.date })
  };
}

async function loadAggregatedNews() {
  const xData = await loadBitcoinNews();
  await loadArticles();

  const xItems = (xData.items || []).map(item => ({
    ...item,
    feedType: 'x',
    sortKey: parseNewsSortKey(item)
  }));

  const trendItems = getArticlesByFilter('trend').map(articleToNewsItem);
  const tipItems = getArticlesByFilter('tip').map(articleToNewsItem);

  return [...xItems, ...trendItems, ...tipItems]
    .sort((a, b) => (b.sortKey || 0) - (a.sortKey || 0));
}

function filterAggregatedNews(items, filter) {
  switch (filter) {
    case 'theriser':
      return items.filter(item => item.sourceHandle === '@TheRiser100x');
    case 'x':
      return items.filter(item => item.external || item.feedType === 'x');
    case 'trend':
      return items.filter(item => item.feedType === 'trend');
    case 'tip':
      return items.filter(item => item.feedType === 'tip');
    case 'site':
      return items.filter(item => !item.external);
    default:
      return items;
  }
}

function buildNewsHubExport(items) {
  const header = `${t('newsHub.exportTitle')}\n${t('btcNews.exported')}: ${new Date().toISOString().slice(0, 16).replace('T', ' ')}\n${'—'.repeat(32)}\n\n`;
  const body = items.map((item, i) => {
    const label = getBitcoinNewsItemLabel(item);
    const url = getBitcoinNewsItemUrl(item);
    return `${i + 1}. [${label}] ${item.title}\n${item.summary}\n${url}\n`;
  }).join('\n');
  return header + body;
}

async function initNewsHomePreview() {
  const feed = document.getElementById('btc-news-feed');
  if (!feed || document.body.dataset.page !== 'home') return;

  try {
    const allItems = await loadAggregatedNews();
    const limit = Number(feed.dataset.limit || 4);
    const items = allItems.slice(0, limit);
    const base = getBasePath();
    feed.innerHTML = items.map(item => renderBitcoinNewsCard(item, base, { compact: true })).join('');
    bindBitcoinNewsActions(feed.closest('section') || feed, { items: allItems });
    initFadeIn();
  } catch (_) { /* fallback: bitcoin-only feed from initBitcoinNewsSession */ }
}

async function initNewsHub() {
  if (document.body.dataset.hub !== 'news') return;

  const list = document.getElementById('news-hub-list');
  const countEl = document.getElementById('news-hub-count');
  const filters = document.getElementById('news-hub-filters');
  const exportBtn = document.getElementById('news-hub-export');
  if (!list) return;

  try {
    const allItems = await loadAggregatedNews();
    let currentFilter = 'all';

    const render = (items) => {
      const base = getBasePath();
      list.innerHTML = items.length
        ? items.map(item => renderBitcoinNewsCard(item, base, { compact: false })).join('')
        : `<p class="btc-news-empty">${t('newsHub.noItems')}</p>`;
      if (countEl) countEl.textContent = String(items.length);
      bindBitcoinNewsActions(list.closest('.news-hub-panel') || document.body, { items });
      initFadeIn();
    };

    render(filterAggregatedNews(allItems, currentFilter));

    filters?.addEventListener('click', e => {
      const btn = e.target.closest('[data-news-filter]');
      if (!btn) return;
      currentFilter = btn.dataset.newsFilter;
      filters.querySelectorAll('[data-news-filter]').forEach(b => b.classList.toggle('active', b === btn));
      render(filterAggregatedNews(allItems, currentFilter));
    });

    exportBtn?.addEventListener('click', async () => {
      const text = buildNewsHubExport(filterAggregatedNews(allItems, currentFilter));
      try {
        await navigator.clipboard.writeText(text);
        const prev = exportBtn.textContent;
        exportBtn.textContent = t('btcNews.exportedAll');
        setTimeout(() => { exportBtn.textContent = prev; }, 1800);
      } catch (_) {
        window.prompt(t('btcNews.copyPrompt'), text);
      }
    });
  } catch (_) {
    list.innerHTML = `<p class="btc-news-empty">${t('newsHub.error')}</p>`;
  }
}