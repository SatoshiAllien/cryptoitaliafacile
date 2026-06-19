let bitcoinNewsData = null;

const BTC_NEWS_LABELS = {
  guide: 'Guida',
  tip: 'Tip',
  trend: 'Trend',
  tutorial: 'Tutorial',
  cardano: 'Cardano',
  sicurezza: 'Sicurezza',
  bitcoin: 'Bitcoin'
};

async function loadBitcoinNews() {
  if (bitcoinNewsData) return bitcoinNewsData;
  const base = getBasePath();
  const res = await fetch(`${base}data/bitcoin-news.json`);
  bitcoinNewsData = await res.json();
  return bitcoinNewsData;
}

function getBitcoinNewsArticleUrl(slug) {
  return `${getBasePath()}articolo.html?slug=${encodeURIComponent(slug)}`;
}

function renderBitcoinNewsCard(item, base, { compact = false } = {}) {
  const href = getBitcoinNewsArticleUrl(item.slug);
  const label = t(`btcNews.categories.${item.category}`) || BTC_NEWS_LABELS[item.category] || item.category;
  const breaking = item.breaking
    ? `<span class="btc-news-badge">${t('btcNews.breaking')}</span>`
    : '';
  const readTime = item.readTime
    ? `<span class="btc-news-meta">${item.readTime} min</span>`
    : '';

  if (compact) {
    return `
      <article class="btc-news-card btc-news-card--compact fade-in">
        ${breaking}
        <div class="btc-news-card-head">
          <span class="btc-news-cat">${label}</span>
          <time class="btc-news-date">${item.date}</time>
        </div>
        <h3 class="btc-news-title"><a href="${href}">${item.title}</a></h3>
        <p class="btc-news-summary">${item.summary}</p>
        <a href="${href}" class="btc-news-link">${t('btcNews.readMore')}</a>
      </article>`;
  }

  return `
    <article class="btc-news-card fade-in" data-news-id="${item.id}">
      ${breaking}
      <div class="btc-news-card-head">
        <span class="btc-news-cat">${label}</span>
        <div class="btc-news-meta-group">
          <time class="btc-news-date">${item.date}</time>
          ${readTime}
        </div>
      </div>
      <h3 class="btc-news-title"><a href="${href}">${item.title}</a></h3>
      <p class="btc-news-summary">${item.summary}</p>
      <div class="btc-news-actions">
        <a href="${href}" class="btn btn-primary btn-sm">${t('btcNews.readArticle')}</a>
        <button type="button" class="btn btn-ghost btn-sm" data-copy-btc-news="${item.id}">${t('btcNews.repost')}</button>
      </div>
    </article>`;
}

function buildBitcoinNewsExport(data) {
  const header = `${data.title}\n${t('btcNews.exported')}: ${data.exportedAt}\n${t('btcNews.source')}: ${data.source}\n${'—'.repeat(32)}\n\n`;
  const body = data.items.map((item, i) => {
    return `${i + 1}. ${item.title}\n${item.summary}\n${getBitcoinNewsArticleUrl(item.slug)}\n`;
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

async function initBitcoinNewsSession() {
  const session = document.getElementById('btc-news-session') || document.getElementById('news-session');
  const feed = document.getElementById('btc-news-feed');
  if (!session && !feed) return;

  try {
    const data = await loadBitcoinNews();
    const base = getBasePath();
    const compact = session?.dataset.compact === 'true' || feed?.dataset.compact === 'true';
    const limit = Number(session?.dataset.limit || feed?.dataset.limit || data.items.length);
    const items = data.items.slice(0, limit);

    if (feed) {
      feed.innerHTML = items.map(item => renderBitcoinNewsCard(item, base, { compact })).join('');
      bindBitcoinNewsActions(feed.closest('section') || feed, data);
    }

    if (session) {
      const list = session.querySelector('#btc-news-list');
      const countEl = session.querySelector('[data-btc-news-count]');
      const updatedEl = session.querySelector('[data-btc-news-updated]');
      if (list) {
        list.innerHTML = items.map(item => renderBitcoinNewsCard(item, base, { compact: false })).join('');
        bindBitcoinNewsActions(session, data);
      }
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