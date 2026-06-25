let bitcoinNewsData = null;

const BTC_NEWS_LABELS = {
  guide: 'Guida',
  tip: 'Tip',
  trend: 'Trend',
  tutorial: 'Tutorial',
  cardano: 'Cardano',
  sicurezza: 'Sicurezza',
  bitcoin: 'Bitcoin',
  x: 'X'
};

async function loadBitcoinNews() {
  if (bitcoinNewsData) return bitcoinNewsData;
  const base = getBasePath();
  const v = (typeof SITE_CONFIG !== 'undefined' && SITE_CONFIG.assetVersion) ? `?v=${SITE_CONFIG.assetVersion}` : '';
  const res = await fetch(`${base}data/bitcoin-news.json${v}`);
  if (!res.ok) throw new Error(`bitcoin-news.json ${res.status}`);
  bitcoinNewsData = await res.json();
  return bitcoinNewsData;
}

function getBitcoinNewsArticleUrl(slug) {
  return `${getBasePath()}articolo.html?slug=${encodeURIComponent(slug)}`;
}

function getBitcoinNewsItemUrl(item) {
  if (item.external && item.url) return item.url;
  if (item.slug) return getBitcoinNewsArticleUrl(item.slug);
  return '#';
}

function getBitcoinNewsItemLabel(item) {
  if (item.sourceHandle) return item.sourceHandle;
  if (item.source && !item.external) return item.source;
  return t(`btcNews.categories.${item.category}`) || BTC_NEWS_LABELS[item.category] || item.category;
}

function renderBitcoinNewsCard(item, base, { compact = false } = {}) {
  const href = getBitcoinNewsItemUrl(item);
  const external = Boolean(item.external);
  const label = getBitcoinNewsItemLabel(item);
  const linkTarget = external ? ' target="_blank" rel="noopener noreferrer"' : '';
  const breaking = item.breaking
    ? `<span class="btc-news-badge">${t('btcNews.breaking')}</span>`
    : '';
  const readTime = item.readTime
    ? `<span class="btc-news-meta">${item.readTime} min</span>`
    : '';
  const cta = external ? t('btcNews.openOnX') : t('btcNews.readArticle');
  const ctaClass = external ? 'btn btn-ghost btn-sm' : 'btn btn-primary btn-sm';

  if (compact) {
    return `
      <article class="btc-news-card btc-news-card--compact fade-in" data-source="${item.sourceHandle || ''}">
        ${breaking}
        <div class="btc-news-card-head">
          <span class="btc-news-cat">${label}</span>
          <time class="btc-news-date">${item.date}</time>
        </div>
        <h3 class="btc-news-title"><a href="${href}"${linkTarget}>${item.title}</a></h3>
        <p class="btc-news-summary">${item.summary}</p>
        <a href="${href}" class="btc-news-link"${linkTarget}>${compact ? t('btcNews.readMore') : cta}</a>
      </article>`;
  }

  return `
    <article class="btc-news-card fade-in" data-news-id="${item.id}" data-source="${item.sourceHandle || ''}">
      ${breaking}
      <div class="btc-news-card-head">
        <span class="btc-news-cat">${label}</span>
        <div class="btc-news-meta-group">
          <time class="btc-news-date">${item.date}</time>
          ${readTime}
        </div>
      </div>
      <h3 class="btc-news-title"><a href="${href}"${linkTarget}>${item.title}</a></h3>
      <p class="btc-news-summary">${item.summary}</p>
      <div class="btc-news-actions">
        <a href="${href}" class="${ctaClass}"${linkTarget}>${cta}</a>
        <button type="button" class="btn btn-ghost btn-sm" data-copy-btc-news="${item.id}">${t('btcNews.repost')}</button>
        <a href="x-posts.html" class="btn btn-ghost btn-sm">Post X virale</a>
      </div>
    </article>`;
}

function buildBitcoinNewsExport(data) {
  const header = `${data.title}\n${t('btcNews.exported')}: ${data.exportedAt}\n${t('btcNews.source')}: ${data.source}\n${'—'.repeat(32)}\n\n`;
  const body = data.items.map((item, i) => {
    const url = getBitcoinNewsItemUrl(item);
    return `${i + 1}. [${item.sourceHandle || item.source}] ${item.title}\n${item.summary}\n${url}\n`;
  }).join('\n');
  return header + body;
}

function bindBitcoinNewsActions(root, data) {
  root.querySelectorAll('[data-copy-btc-news]').forEach(btn => {
    btn.addEventListener('click', async () => {
      const item = data.items.find(n => n.id === btn.dataset.copyBtcNews);
      if (!item) return;
      const text = item.postText;
      try {
        await navigator.clipboard.writeText(text);
        const prev = btn.textContent;
        btn.textContent = t('btcNews.copied');
        setTimeout(() => { btn.textContent = prev; }, 1600);
      } catch (_) {
        window.prompt(t('btcNews.copyPrompt'), text);
      }
    });
  });

  const exportAll = root.querySelector('[data-export-btc-news]');
  if (exportAll) {
    exportAll.addEventListener('click', async () => {
      const text = buildBitcoinNewsExport(data);
      try {
        await navigator.clipboard.writeText(text);
        const prev = exportAll.textContent;
        exportAll.textContent = t('btcNews.exportedAll');
        setTimeout(() => { exportAll.textContent = prev; }, 1800);
      } catch (_) {
        window.prompt(t('btcNews.copyPrompt'), text);
      }
    });
  }
}

function bindBitcoinNewsFilters(root, data, renderFn) {
  const filters = root.querySelector('.btc-news-filters');
  if (!filters) return;

  filters.addEventListener('click', e => {
    const btn = e.target.closest('[data-btc-filter]');
    if (!btn) return;
    const value = btn.dataset.btcFilter;
    filters.querySelectorAll('[data-btc-filter]').forEach(b => b.classList.toggle('active', b === btn));
    const items = value === 'all'
      ? data.items
      : data.items.filter(item => item.sourceHandle === value);
    renderFn(items);
  });
}

function renderBitcoinNewsList(root, items, base, compact) {
  const list = root.querySelector('#btc-news-list') || root.querySelector('#btc-news-feed');
  if (!list) return;
  list.innerHTML = items.length
    ? items.map(item => renderBitcoinNewsCard(item, base, { compact })).join('')
    : `<p class="btc-news-empty">${t('btcNews.noItems')}</p>`;
  initFadeIn();
}

async function initBitcoinNewsSession() {
  const session = document.getElementById('btc-news-session') || document.getElementById('news-session');
  const feed = document.getElementById('btc-news-feed');
  if (!session && !feed) return;

  try {
    const data = await loadBitcoinNews();
    const base = getBasePath();
    const compact = session?.dataset.compact === 'true' || feed?.dataset.compact === 'true';
    const limit = Number(session?.dataset.limit || feed?.dataset.limit || data.items.length);
    const initialItems = data.items.slice(0, limit);

    const renderItems = subset => {
      if (feed) {
        feed.innerHTML = subset.map(item => renderBitcoinNewsCard(item, base, { compact })).join('');
      }
      if (session) {
        const list = session.querySelector('#btc-news-list');
        if (list) {
          list.innerHTML = subset.map(item => renderBitcoinNewsCard(item, base, { compact: false })).join('');
        }
      }
      initFadeIn();
    };

    renderItems(initialItems);

    const actionRoot = session || feed?.closest('section');
    if (actionRoot) bindBitcoinNewsActions(actionRoot, data);
    if (session) bindBitcoinNewsFilters(session, data, renderItems);

    if (session) {
      const countEl = session.querySelector('[data-btc-news-count]');
      const updatedEl = session.querySelector('[data-btc-news-updated]');
      if (countEl) countEl.textContent = String(data.count);
      if (updatedEl) updatedEl.textContent = data.exportedAt;
    }

    initFadeIn();
  } catch (err) {
    const target = feed || session?.querySelector('#btc-news-list');
    if (target) {
      target.innerHTML = `<p class="btc-news-empty">${t('btcNews.error')}</p>`;
    }
  }
}