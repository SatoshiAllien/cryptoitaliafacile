/**
 * Parla con Satoshi — Chat widget & API client
 * Connette al backend Steven AI (CryptoItaliaFacile)
 */
(function () {
  'use strict';

  const cfg = () => (typeof SITE_CONFIG !== 'undefined' && SITE_CONFIG.satoshiAi) || {};
  let sessionId = null;
  let isStreaming = false;
  let apiOnline = null;

  function getApiBase() {
    const c = cfg();
    if (c.apiUrl) return c.apiUrl.replace(/\/$/, '');
    const host = window.location.hostname;
    if (host === 'localhost' || host === '127.0.0.1') {
      return 'http://127.0.0.1:8765';
    }
    if (c.productionApiUrl) return c.productionApiUrl.replace(/\/$/, '');
    return '';
  }

  function chatApiUrl(path) {
    const base = getApiBase();
    if (!base) return '';
    return `${base}/api/v1/chat${path}`;
  }

  function assetUrl(path) {
    return typeof getBasePath === 'function' ? `${getBasePath()}${path}` : path;
  }

  function escapeHtml(text) {
    const d = document.createElement('div');
    d.textContent = text;
    return d.innerHTML;
  }

  async function checkApiHealth() {
    const base = getApiBase();
    if (!base) { apiOnline = false; return false; }
    try {
      const res = await fetch(`${base}/api/v1/health`, { signal: AbortSignal.timeout(4000) });
      const data = await res.json();
      apiOnline = data.status === 'ok';
      return apiOnline;
    } catch {
      apiOnline = false;
      return false;
    }
  }

  function injectStyles() {
    if (document.getElementById('satoshi-chat-css')) return;
    const link = document.createElement('link');
    link.id = 'satoshi-chat-css';
    link.rel = 'stylesheet';
    link.href = assetUrl(`css/satoshi-chat.css?v=${SITE_CONFIG?.assetVersion || '1'}`);
    document.head.appendChild(link);
  }

  function renderLauncher() {
    if (document.getElementById('satoshi-launcher')) return;
    if (document.body.dataset.page === 'chat') return;

    const c = cfg();
    const avatar = assetUrl(c.avatar || 'assets/img/welcome-bitcoin-boss.png');
    const title = c.title || 'Parla con Satoshi';

    const el = document.createElement('div');
    el.id = 'satoshi-launcher';
    el.className = 'satoshi-launcher';
    el.innerHTML = `
      <div class="satoshi-panel" id="satoshi-panel" hidden>
        <div class="satoshi-panel-header">
          <img src="${avatar}" alt="Satoshi" class="satoshi-panel-avatar">
          <div class="satoshi-panel-info">
            <h3>${escapeHtml(title)}</h3>
            <p class="satoshi-status"><span class="satoshi-status-dot" id="satoshi-status-dot"></span><span id="satoshi-status-text">Connessione...</span></p>
          </div>
          <div class="satoshi-panel-actions">
            <button class="satoshi-panel-btn" id="satoshi-new-chat" title="Nuova chat" aria-label="Nuova chat">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12h14"/></svg>
            </button>
            <button class="satoshi-panel-btn" id="satoshi-close" title="Chiudi" aria-label="Chiudi chat">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6L6 18M6 6l12 12"/></svg>
            </button>
          </div>
        </div>
        <div class="satoshi-messages" id="satoshi-messages"></div>
        <div class="satoshi-input-area">
          <div class="satoshi-input-wrap">
            <textarea class="satoshi-input" id="satoshi-input" rows="1" placeholder="Chiedi a Satoshi..."></textarea>
            <button class="satoshi-send" id="satoshi-send" aria-label="Invia">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z"/></svg>
            </button>
          </div>
          <a href="${assetUrl(c.chatPage || 'chat/index.html')}" class="satoshi-expand">Apri chat completa →</a>
        </div>
      </div>
      <button class="satoshi-launcher-btn" id="satoshi-open" aria-label="${escapeHtml(title)}">
        <img src="${avatar}" alt="">
        <span class="satoshi-launcher-label">${escapeHtml(title)}</span>
      </button>
    `;
    document.body.appendChild(el);
    bindLauncherEvents();
    renderWelcome('satoshi-messages');
    checkApiHealth().then(updateStatus);
  }

  function updateStatus(online) {
    const dot = document.getElementById('satoshi-status-dot');
    const text = document.getElementById('satoshi-status-text');
    if (!dot || !text) return;
    if (online) {
      dot.className = 'satoshi-status-dot satoshi-status-dot--online';
      text.textContent = 'Online';
    } else if (!getApiBase()) {
      dot.className = 'satoshi-status-dot';
      text.textContent = 'Configura API';
    } else {
      dot.className = 'satoshi-status-dot';
      text.textContent = 'Offline';
    }
  }

  function renderWelcome(containerId) {
    const el = document.getElementById(containerId);
    if (!el) return;
    const c = cfg();
    const suggestions = (c.suggestions || []).map(s =>
      `<button type="button" class="satoshi-suggestion" data-suggest="${escapeHtml(s)}">${escapeHtml(s)}</button>`
    ).join('');
    el.innerHTML = `
      <div class="satoshi-welcome">
        <p>${escapeHtml(c.tagline || 'Chiedi qualsiasi cosa su crypto, sicurezza e Web3')}</p>
        <div class="satoshi-suggestions">${suggestions}</div>
      </div>
    `;
    el.querySelectorAll('.satoshi-suggestion').forEach(btn => {
      btn.addEventListener('click', () => {
        const input = document.getElementById('satoshi-input') || document.getElementById('chat-page-input');
        if (input) input.value = btn.dataset.suggest;
        sendMessage(containerId);
      });
    });
  }

  function addMessage(containerId, role, content) {
    const container = document.getElementById(containerId);
    if (!container) return null;

    const welcome = container.querySelector('.satoshi-welcome');
    if (welcome) welcome.remove();

    const div = document.createElement('div');
    div.className = `satoshi-msg satoshi-msg--${role}`;
    div.innerHTML = `
      <div class="satoshi-msg-avatar">${role === 'user' ? 'Tu' : 'S'}</div>
      <div class="satoshi-msg-bubble">${escapeHtml(content)}</div>
    `;
    container.appendChild(div);
    container.scrollTop = container.scrollHeight;
    return div.querySelector('.satoshi-msg-bubble');
  }

  async function sendMessage(containerId) {
    const inputId = containerId === 'chat-page-messages' ? 'chat-page-input' : 'satoshi-input';
    const sendId = containerId === 'chat-page-messages' ? 'chat-page-send' : 'satoshi-send';
    const input = document.getElementById(inputId);
    const sendBtn = document.getElementById(sendId);
    if (!input) return;

    const text = input.value.trim();
    if (!text || isStreaming) return;

    const apiUrl = chatApiUrl('/message');
    if (!apiUrl) {
      addMessage(containerId, 'bot', 'Il servizio AI non è ancora configurato per il web. Contatta l\'amministratore o usa il sito in locale.');
      return;
    }

    isStreaming = true;
    if (sendBtn) sendBtn.disabled = true;
    input.value = '';
    input.style.height = 'auto';

    addMessage(containerId, 'user', text);
    const botBubble = addMessage(containerId, 'bot', '');
    botBubble.innerHTML = '<span class="satoshi-thinking">Satoshi sta pensando...</span>';

    try {
      const res = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text, session_id: sessionId }),
        signal: AbortSignal.timeout(300000),
      });

      if (!res.ok) throw new Error('Server errore ' + res.status);
      if (!res.body) throw new Error('Risposta vuota');

      const reader = res.body.getReader();
      const decoder = new TextDecoder();
      let buffer = '';
      let fullText = '';

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split('\n');
        buffer = lines.pop();

        for (const line of lines) {
          if (!line.startsWith('data: ')) continue;
          const data = line.slice(6);
          if (data === '[DONE]') continue;
          try {
            const event = JSON.parse(data);
            if (event.type === 'session') sessionId = event.session_id;
            else if (event.type === 'thinking') botBubble.innerHTML = `<span class="satoshi-thinking">${escapeHtml(event.content)}</span>`;
            else if (event.type === 'tool_start') botBubble.innerHTML = `<span class="satoshi-thinking">Eseguo: ${escapeHtml(event.tool)}...</span>`;
            else if (event.type === 'token') {
              fullText += event.content;
              botBubble.innerHTML = escapeHtml(fullText) + '<span class="satoshi-cursor"></span>';
            }
            else if (event.type === 'done') {
              if (!fullText) fullText = event.content || '';
              botBubble.textContent = fullText;
            }
            else if (event.type === 'error') {
              fullText = event.content || 'Errore';
              botBubble.innerHTML = `<span class="satoshi-error">${escapeHtml(fullText)}</span>`;
            }
          } catch (_) { /* skip malformed */ }
        }
        const container = document.getElementById(containerId);
        if (container) container.scrollTop = container.scrollHeight;
      }
    } catch (err) {
      const msg = err.name === 'TimeoutError'
        ? 'Timeout: il modello impiega troppo tempo. Riprova.'
        : 'Non riesco a connettermi al server AI. Verifica che il servizio sia attivo.';
      botBubble.innerHTML = `<span class="satoshi-error">${escapeHtml(msg)}</span>`;
      apiOnline = false;
      updateStatus(false);
    }

    isStreaming = false;
    if (sendBtn) sendBtn.disabled = false;
  }

  function bindLauncherEvents() {
    const panel = document.getElementById('satoshi-panel');
    const openBtn = document.getElementById('satoshi-open');
    const closeBtn = document.getElementById('satoshi-close');
    const newBtn = document.getElementById('satoshi-new-chat');
    const input = document.getElementById('satoshi-input');
    const sendBtn = document.getElementById('satoshi-send');

    openBtn?.addEventListener('click', () => {
      panel.hidden = !panel.hidden;
      if (!panel.hidden) {
        input?.focus();
        checkApiHealth().then(updateStatus);
      }
    });
    closeBtn?.addEventListener('click', () => { panel.hidden = true; });
    newBtn?.addEventListener('click', () => {
      sessionId = null;
      renderWelcome('satoshi-messages');
    });
    sendBtn?.addEventListener('click', () => sendMessage('satoshi-messages'));
    input?.addEventListener('keydown', e => {
      if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage('satoshi-messages'); }
    });
    input?.addEventListener('input', () => {
      input.style.height = 'auto';
      input.style.height = Math.min(input.scrollHeight, 100) + 'px';
    });
  }

  function initChatPage() {
    if (document.body.dataset.page !== 'chat') return;

    const container = document.getElementById('chat-page-messages');
    if (!container) return;

    renderWelcome('chat-page-messages');
    checkApiHealth().then(online => {
      const dot = document.getElementById('chat-page-status-dot');
      const text = document.getElementById('chat-page-status-text');
      if (dot && text) {
        if (online) {
          dot.className = 'satoshi-status-dot satoshi-status-dot--online';
          text.textContent = 'Online — Steven AI';
        } else {
          text.textContent = getApiBase() ? 'Offline — avvia il servizio AI' : 'API non configurata';
        }
      }
    });

    const input = document.getElementById('chat-page-input');
    const sendBtn = document.getElementById('chat-page-send');
    const newBtn = document.getElementById('chat-page-new');

    sendBtn?.addEventListener('click', () => sendMessage('chat-page-messages'));
    newBtn?.addEventListener('click', () => {
      sessionId = null;
      renderWelcome('chat-page-messages');
    });
    input?.addEventListener('keydown', e => {
      if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage('chat-page-messages'); }
    });
    input?.addEventListener('input', () => {
      input.style.height = 'auto';
      input.style.height = Math.min(input.scrollHeight, 150) + 'px';
    });
  }

  window.initSatoshiChat = function () {
    injectStyles();
    renderLauncher();
    initChatPage();
    setInterval(() => {
      if (document.getElementById('satoshi-panel') && !document.getElementById('satoshi-panel').hidden) {
        checkApiHealth().then(updateStatus);
      }
    }, 30000);
  };
})();