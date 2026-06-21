/**
 * Parla con Satoshi — Chat widget integrato nel sito web
 * Modalità locale su GitHub Pages · Steven AI quando API disponibile
 */
(function () {
  'use strict';

  const cfg = () => (typeof SITE_CONFIG !== 'undefined' && SITE_CONFIG.satoshiAi) || {};
  let sessionId = null;
  let isStreaming = false;
  let apiOnline = false;
  let onlineLlmReady = false;
  let useLocalMode = true;

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

  function satoshiApiUrl() {
    return chatApiUrl('/satoshi');
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
    const c = cfg();
    const fallback = c.useLocalFallback !== false;

    if (!base) {
      apiOnline = fallback;
      useLocalMode = fallback;
      return apiOnline;
    }

    try {
      const res = await fetch(`${base}/api/v1/health`, { signal: AbortSignal.timeout(4000) });
      const data = await res.json();
      apiOnline = data.status === 'ok';
      onlineLlmReady = !!(data.online_llm && data.online_llm.configured);
      useLocalMode = !apiOnline && fallback;
      return apiOnline || useLocalMode;
    } catch {
      apiOnline = false;
      useLocalMode = fallback;
      return useLocalMode;
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
        <span class="satoshi-launcher-pulse" aria-hidden="true"></span>
        <span class="satoshi-launcher-pulse satoshi-launcher-pulse--2" aria-hidden="true"></span>
        <img src="${avatar}" alt="Satoshi">
        <span class="satoshi-launcher-label">
          <span class="satoshi-launcher-title">${escapeHtml(title)}</span>
          <span class="satoshi-launcher-sub">Chiedi qualsiasi cosa su crypto</span>
        </span>
        <span class="satoshi-launcher-icon" aria-hidden="true">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2z"/></svg>
        </span>
      </button>
    `;
    document.body.appendChild(el);
    bindLauncherEvents();
    renderWelcome(document.body.dataset.page === 'chat' ? 'chat-page-messages' : 'satoshi-messages');
    checkApiHealth().then(updateStatus);
  }

  function updateStatus(online) {
    const dots = [
      document.getElementById('satoshi-status-dot'),
      document.getElementById('chat-page-status-dot')
    ].filter(Boolean);
    const texts = [
      document.getElementById('satoshi-status-text'),
      document.getElementById('chat-page-status-text')
    ].filter(Boolean);

    const label = online
      ? (onlineLlmReady ? 'Online — AI cloud' : apiOnline ? 'Online — motore locale' : 'Online')
      : 'Offline';

    dots.forEach(dot => {
      dot.className = online ? 'satoshi-status-dot satoshi-status-dot--online' : 'satoshi-status-dot';
    });
    texts.forEach(t => { t.textContent = label; });
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
        <div class="satoshi-welcome-icon" aria-hidden="true">₿</div>
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

  async function sendLocalMessage(containerId, text, botBubble) {
    if (!window.SatoshiBot) {
      botBubble.innerHTML = '<span class="satoshi-error">Bot non caricato. Ricarica la pagina.</span>';
      return;
    }
    const reply = SatoshiBot.findReply(text);
    let fullText = '';
    botBubble.innerHTML = '<span class="satoshi-cursor"></span>';
    await SatoshiBot.streamReply(reply, (token) => {
      fullText += token;
      botBubble.textContent = fullText;
      const container = document.getElementById(containerId);
      if (container) container.scrollTop = container.scrollHeight;
    }, 10);
  }

  async function sendApiMessage(containerId, text, botBubble) {
    const apiUrl = satoshiApiUrl();
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
            throw new Error(event.content || 'Errore API');
          }
        } catch (e) {
          if (e.message && e.message !== 'Errore API') throw e;
        }
      }
      const container = document.getElementById(containerId);
      if (container) container.scrollTop = container.scrollHeight;
    }
  }

  async function sendMessage(containerId) {
    const inputId = containerId === 'chat-page-messages' ? 'chat-page-input' : 'satoshi-input';
    const sendId = containerId === 'chat-page-messages' ? 'chat-page-send' : 'satoshi-send';
    const input = document.getElementById(inputId);
    const sendBtn = document.getElementById(sendId);
    if (!input) return;

    const text = input.value.trim();
    if (!text || isStreaming) return;

    isStreaming = true;
    if (sendBtn) sendBtn.disabled = true;
    input.value = '';
    input.style.height = 'auto';

    addMessage(containerId, 'user', text);
    const botBubble = addMessage(containerId, 'bot', '');
    botBubble.innerHTML = '<span class="satoshi-thinking">Satoshi sta pensando...</span>';

    const tryApi = getApiBase() && (apiOnline || getApiBase());

    try {
      if (tryApi) {
        await sendApiMessage(containerId, text, botBubble);
      } else if (useLocalMode && window.SatoshiBot) {
        await sendLocalMessage(containerId, text, botBubble);
      } else {
        throw new Error('offline');
      }
    } catch (err) {
      if (window.SatoshiBot && cfg().useLocalFallback !== false) {
        botBubble.innerHTML = '<span class="satoshi-thinking">Satoshi sta pensando...</span>';
        await sendLocalMessage(containerId, text, botBubble);
        useLocalMode = true;
        apiOnline = false;
        updateStatus(true);
      } else {
        const msg = err.name === 'TimeoutError'
          ? 'Timeout: il modello impiega troppo tempo. Riprova.'
          : 'Servizio temporaneamente non disponibile. Riprova tra poco.';
        botBubble.innerHTML = `<span class="satoshi-error">${escapeHtml(msg)}</span>`;
        updateStatus(false);
      }
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

    if (!openBtn) return;

    openBtn.addEventListener('click', () => {
      if (!panel) return;
      const opening = panel.hidden;
      panel.hidden = !opening;
      openBtn.classList.toggle('satoshi-launcher-btn--hidden', !panel.hidden);
      if (!panel.hidden) {
        input?.focus();
        checkApiHealth().then(updateStatus);
      }
    });
    closeBtn?.addEventListener('click', () => {
      if (panel) panel.hidden = true;
      openBtn?.classList.remove('satoshi-launcher-btn--hidden');
    });
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

    renderWelcome('chat-page-messages');
    checkApiHealth().then(updateStatus);

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

  function openSatoshiChat() {
    if (document.body.dataset.page === 'chat') {
      document.getElementById('chat-page-input')?.focus();
      return;
    }
    if (!document.getElementById('satoshi-launcher')) renderLauncher();
    const panel = document.getElementById('satoshi-panel');
    const openBtn = document.getElementById('satoshi-open');
    if (!panel) return;
    panel.hidden = false;
    openBtn?.classList.add('satoshi-launcher-btn--hidden');
    document.getElementById('satoshi-input')?.focus();
    checkApiHealth().then(updateStatus);
  }

  function bindOpenTriggers() {
    document.querySelectorAll('[data-satoshi-open]').forEach(el => {
      if (el.dataset.satoshiBound) return;
      el.dataset.satoshiBound = '1';
      const handler = e => {
        e.preventDefault();
        openSatoshiChat();
      };
      el.addEventListener('click', handler);
      if (el.tagName !== 'BUTTON') {
        el.addEventListener('keydown', e => {
          if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openSatoshiChat(); }
        });
      }
    });
  }

  window.openSatoshiChat = openSatoshiChat;

  window.initSatoshiChat = function () {
    injectStyles();
    renderLauncher();
    initChatPage();
    bindOpenTriggers();
    setInterval(() => {
      const panel = document.getElementById('satoshi-panel');
      if (panel && !panel.hidden) checkApiHealth().then(updateStatus);
    }, 30000);
  };
})();