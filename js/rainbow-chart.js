/**
 * rainbow-chart.js
 * Fills #rainbow-data from the snapshot produced by
 * scripts/update-bitcoin-rainbow-chart.py (Grok Agent).
 * Educational UI only — not financial advice.
 */
(function () {
  'use strict';

  var DATA_URL = 'data/bitcoin-rainbow-live.json';

  function formatUsd(n) {
    if (typeof n !== 'number' || !isFinite(n)) return '—';
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      maximumFractionDigits: 0
    }).format(n);
  }

  function escapeHtml(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function render(data) {
    var el = document.getElementById('rainbow-data');
    if (!el || !data) return;

    var band = data.band || {};
    var bandOrig = data.band_original || {};
    var color = band.color || '#4472c4';
    var interpretation = data.interpretation || data.interpretation_it || '';

    el.innerHTML =
      '<div class="rainbow-data-grid">' +
        '<div class="rainbow-stat">' +
          '<span class="rainbow-stat-label">BTC price</span>' +
          '<span class="rainbow-stat-value">' + escapeHtml(formatUsd(data.price_usd)) + '</span>' +
        '</div>' +
        '<div class="rainbow-stat rainbow-stat--band" style="--band-color:' + escapeHtml(color) + '">' +
          '<span class="rainbow-stat-label">Dynamic band</span>' +
          '<span class="rainbow-stat-value">' +
            '<span class="rainbow-band-dot" aria-hidden="true"></span>' +
            escapeHtml(band.label || '—') +
          '</span>' +
        '</div>' +
        '<div class="rainbow-stat">' +
          '<span class="rainbow-stat-label">Original model</span>' +
          '<span class="rainbow-stat-value">' + escapeHtml(bandOrig.label || '—') + '</span>' +
        '</div>' +
        '<div class="rainbow-stat">' +
          '<span class="rainbow-stat-label">Power Law fit (R²)</span>' +
          '<span class="rainbow-stat-value">' + escapeHtml(String(data.r2_percent != null ? data.r2_percent + '%' : '—')) + '</span>' +
          '<span class="rainbow-stat-meta">' + escapeHtml(data.as_of || '') + '</span>' +
        '</div>' +
      '</div>' +
      '<p class="rainbow-interpretation">' + escapeHtml(interpretation) + '</p>' +
      '<p class="rainbow-updated">Updated: ' + escapeHtml(data.updated_at || '—') +
        ' · <a href="sections/bitcoin-rainbow-chart.md">Full analysis &amp; JSON dataset</a></p>';
  }

  function fail(msg) {
    var el = document.getElementById('rainbow-data');
    if (!el) return;
    el.innerHTML = '<p class="rainbow-data-error">' + escapeHtml(msg) + '</p>';
  }

  function init() {
    if (!document.getElementById('rainbow-data')) return;
    fetch(DATA_URL, { cache: 'no-cache' })
      .then(function (res) {
        if (!res.ok) throw new Error('HTTP ' + res.status);
        return res.json();
      })
      .then(render)
      .catch(function () {
        fail('Rainbow data unavailable. Re-run scripts/update-bitcoin-rainbow-chart.py');
      });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
