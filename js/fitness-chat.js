/**
 * Health & Fitness — Parla con Stefano (coach fitness)
 * Knowledge base locale: allenamento, nutrizione, integrazione
 */
(function () {
  'use strict';

  const LOGO = 'assets/img/fitness-bot-logo.jpg';
  const INSTAGRAM = 'https://www.instagram.com/krown.82/';
  const X_ACCOUNT = 'https://x.com/TheRiser100x';

  const knowledgeBase = [
    {
      keywords: ['chi sei', 'presentati', 'stefano', 'coach', 'personal trainer'],
      response: 'Sono l\'assistente fitness di Stefano Ciancimino — 15+ anni tra bodybuilding, corsa, bici e sport outdoor. Ti aiuto su allenamento, nutrizione e benessere con un approccio naturale, costante e evidence-based.'
    },
    {
      keywords: ['massa muscolare', 'ipertrofia', 'muscoli', 'crescita muscolare', 'hypertrophy'],
      response: 'Per aumentare la massa muscolare: sovraccarico progressivo (carico, ripetizioni o volume), 10–20 serie/settimana per gruppo muscolare, frequenza 2x/settimana. Surplus calorico moderato (+300–500 kcal), proteine 1,6–2,2 g/kg distribuite in 4–5 pasti. Sonno 7–9 ore — i muscoli crescono nel recupero.'
    },
    {
      keywords: ['proteine', 'proteina', 'whey', 'caseine', 'integrazione proteica', 'shake'],
      response: 'Proteine: 1,6–2,2 g/kg al giorno per ipertrofia, 1,8–2 g/kg per mantenimento. Whey post-workout (assorbimento rapido), caseina pre-nanna (rilascio lento), vegetali per chi evita latticini. Integratori non sostituiscono pasti — 20–40 g per serving se non raggiungi il fabbisogno con il cibo.'
    },
    {
      keywords: ['alimentazione', 'dieta', 'nutrizione', 'mangiare', 'calorie', 'macros', 'macronutrienti'],
      response: 'Equilibrio calorico tutto l\'anno: fasi di mantenimento (TDEE) evitano l\'effetto yo-yo. Proteine stabili, grassi buoni 0,8–1 g/kg, carboidrati variabili in base all\'attività. Pasti semplici e sostenibili — la dieta migliore è quella che segui per anni, non per settimane.'
    },
    {
      keywords: ['zucchero', 'zucchero raffinato', 'dolci', 'glicemia', 'insulina'],
      response: 'Lo zucchero raffinato apporta calorie vuote e picchi glicemici ripetuti possono favorire infiammazione e accumulo di grasso viscerale. Alternative: frutta fresca, miele con moderazione, dark chocolate 85%+. Leggi sempre le etichette — lo zucchero si nasconde ovunque.'
    },
    {
      keywords: ['deficit', 'dimagrire', 'perdere peso', 'grasso', 'cut', 'ricomposizione'],
      response: 'Ricomposizione corporea: deficit calorico intelligente (non estremo), proteine alte per preservare muscolo, allenamento con i pesi mantenuto. Perdere grasso mantenendo massa è l\'obiettivo — non solo la bilancia.'
    },
    {
      keywords: ['allenamento', 'workout', 'palestra', 'pesi', 'push pull legs', 'routine'],
      response: 'Routine tipo: Lun/Mer/Ven pesi (push/pull/legs), Mar/Gio corsa o bici 45–60 min, Sab outdoor o funzionale, Dom riposo attivo. Allenati 4–5 volte a settimana — la costanza batte l\'intensità sporadica.'
    },
    {
      keywords: ['corsa', 'running', 'cardio', 'bici', 'ciclismo', 'endurance'],
      response: 'Corsa e bici sviluppano cardio, resistenza e mentalità. Obiettivi esempio: 10 km sotto i 50 minuti, 100 km in bici senza fermate. Integra il cardio con i pesi — non sono nemici.'
    },
    {
      keywords: ['recupero', 'sonno', 'riposo', 'overtraining', 'deload'],
      response: 'Recupero = 50% del risultato. Dormi almeno 7 ore (non negoziabile), idratazione 2–3 litri/die, giorni di scarico quando serve. I muscoli crescono quando riposi, non solo quando ti alleni.'
    },
    {
      keywords: ['idratazione', 'acqua', 'bere'],
      response: 'Bevi 2–3 litri d\'acqua al giorno, di più con cardio intenso o caldo. L\'idratazione è spesso sottovalutata ma fondamentale per performance, recupero e composizione corporea. Acqua prima degli integratori.'
    },
    {
      keywords: ['bodybuilding', 'funzionale', 'outdoor', 'sport'],
      response: 'Stefano pratica bodybuilding (forza e massa), corsa e bici (cardio), allenamento funzionale (mobilità e prevenzione) e sport outdoor (natura ed equilibrio). Ogni disciplina aggiunge qualcosa al sistema completo.'
    },
    {
      keywords: ['integratori', 'creatina', 'pre workout', 'bcaa'],
      response: 'Approccio evidence-based: niente hype da integratore miracoloso. Proteine in polvere se utile per raggiungere il fabbisogno. Creatina è tra le più studiate — ma cibo, sonno e allenamento vengono prima di tutto.'
    },
    {
      keywords: ['filosofia', 'costanza', 'disciplina', 'motivazione'],
      response: 'Filosofia fitness: equilibrio, costanza, allenamento intelligente, alimentazione pulita. Il fitness non è una destinazione — è un sistema. Costanza batte intensità. Disciplina batte motivazione.'
    },
    {
      keywords: ['ciao', 'salve', 'buongiorno', 'hey', 'hello'],
      response: 'Ciao! Sono il coach fitness di Stefano. Chiedimi di massa muscolare, nutrizione, cardio, recupero o integrazione — risposte basate su esperienza reale e principi scientifici.'
    },
    {
      keywords: ['grazie', 'thanks', 'perfetto'],
      response: 'Prego! Resta costante e allenati in modo intelligente. Per altri contenuti esplora le guide nella pagina Health & Fitness.'
    }
  ];

  const defaultResponse =
    'Prova a chiedere su: massa muscolare, nutrizione, proteine, cardio, recupero, zucchero raffinato o routine settimanale.';

  const suggestions = [
    'Come aumentare massa?',
    'Proteine e integratori',
    'Alimentazione anno round',
    'Routine settimanale'
  ];

  function assetUrl(path) {
    return typeof getBasePath === 'function' ? `${getBasePath()}${path}` : path;
  }

  function normalize(text) {
    return text
      .toLowerCase()
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .trim();
  }

  function findResponse(query) {
    const normalized = normalize(query);
    let bestMatch = null;
    let bestScore = 0;
    knowledgeBase.forEach(entry => {
      let score = 0;
      entry.keywords.forEach(keyword => {
        if (normalized.includes(normalize(keyword))) score += keyword.split(' ').length;
      });
      if (score > bestScore) {
        bestScore = score;
        bestMatch = entry;
      }
    });
    return bestMatch ? bestMatch.response : defaultResponse;
  }

  function injectStyles() {
    if (document.getElementById('fitness-chat-css')) return;
    const link = document.createElement('link');
    link.id = 'fitness-chat-css';
    link.rel = 'stylesheet';
    const v = (typeof SITE_CONFIG !== 'undefined' && SITE_CONFIG.assetVersion) ? SITE_CONFIG.assetVersion : '1';
    link.href = assetUrl(`css/fitness-chat.css?v=${v}`);
    document.head.appendChild(link);
  }

  function createChatbot() {
    if (document.getElementById('fitness-chatbot')) return;
    const logo = assetUrl(LOGO);

    const chatbot = document.createElement('div');
    chatbot.id = 'fitness-chatbot';
    chatbot.className = 'fitness-chatbot';
    chatbot.innerHTML =
      '<div class="fitness-chatbot__launcher">' +
      '<span class="fitness-chatbot__launcher-label">Coach Fitness</span>' +
      '<button class="fitness-chatbot__toggle" aria-label="Parla con il coach fitness" title="Coach Fitness">' +
      `<img src="${logo}" alt="Coach Fitness" class="fitness-chatbot__toggle-logo" width="44" height="44" loading="eager" decoding="async">` +
      '</button></div>' +
      '<div class="fitness-chatbot__panel">' +
      '<div class="fitness-chatbot__header">' +
      `<div class="fitness-chatbot__avatar"><img src="${logo}" alt="Coach Fitness" class="fitness-chatbot__avatar-logo" width="36" height="36" loading="eager" decoding="async"></div>` +
      '<div class="fitness-chatbot__header-info"><strong>Coach Fitness</strong><span>Allenamento · Nutrizione · Benessere</span></div>' +
      '<button class="fitness-chatbot__close" aria-label="Chiudi"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6L6 18M6 6l12 12"/></svg></button>' +
      '</div>' +
      '<div class="fitness-chatbot__messages"></div>' +
      '<div class="fitness-chatbot__typing">Sto scrivendo...</div>' +
      '<div class="fitness-chatbot__suggestions"></div>' +
      '<div class="fitness-chatbot__input-area">' +
      '<input type="text" class="fitness-chatbot__input" placeholder="Chiedi su allenamento, nutrizione, proteine..." autocomplete="off">' +
      '<button class="fitness-chatbot__send" aria-label="Invia"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z"/></svg></button>' +
      '</div></div>';

    document.body.appendChild(chatbot);

    const toggle = chatbot.querySelector('.fitness-chatbot__toggle');
    const close = chatbot.querySelector('.fitness-chatbot__close');
    const messages = chatbot.querySelector('.fitness-chatbot__messages');
    const typing = chatbot.querySelector('.fitness-chatbot__typing');
    const input = chatbot.querySelector('.fitness-chatbot__input');
    const send = chatbot.querySelector('.fitness-chatbot__send');
    const suggestionsEl = chatbot.querySelector('.fitness-chatbot__suggestions');

    function addMessage(text, type) {
      const wrap = document.createElement('div');
      wrap.className = 'fitness-chatbot__message-row fitness-chatbot__message-row--' + type;

      if (type === 'bot') {
        const avatar = document.createElement('img');
        avatar.src = logo;
        avatar.alt = '';
        avatar.className = 'fitness-chatbot__msg-logo';
        avatar.width = 24;
        avatar.height = 24;
        wrap.appendChild(avatar);
      }

      const msg = document.createElement('div');
      msg.className = 'fitness-chatbot__message fitness-chatbot__message--' + type;
      msg.textContent = text;
      wrap.appendChild(msg);
      messages.appendChild(wrap);
      messages.scrollTop = messages.scrollHeight;
    }

    function respond(query) {
      typing.classList.add('fitness-chatbot__typing--visible');
      messages.scrollTop = messages.scrollHeight;
      setTimeout(() => {
        typing.classList.remove('fitness-chatbot__typing--visible');
        addMessage(findResponse(query), 'bot');
      }, 500 + Math.random() * 400);
    }

    function handleSend() {
      const text = input.value.trim();
      if (!text) return;
      addMessage(text, 'user');
      input.value = '';
      respond(text);
    }

    toggle.addEventListener('click', () => {
      chatbot.classList.toggle('fitness-chatbot--open');
      if (chatbot.classList.contains('fitness-chatbot--open') && messages.children.length === 0) {
        addMessage(
          'Ciao! Sono il coach fitness di Stefano — 15+ anni di esperienza. Chiedimi di massa muscolare, nutrizione, cardio o recupero.',
          'bot'
        );
      }
    });

    close.addEventListener('click', () => chatbot.classList.remove('fitness-chatbot--open'));
    send.addEventListener('click', handleSend);
    input.addEventListener('keydown', e => { if (e.key === 'Enter') handleSend(); });

    suggestions.forEach(text => {
      const btn = document.createElement('button');
      btn.className = 'fitness-chatbot__suggestion';
      btn.textContent = text;
      btn.addEventListener('click', () => {
        addMessage(text, 'user');
        respond(text);
      });
      suggestionsEl.appendChild(btn);
    });

    document.querySelectorAll('[data-fitness-chat-open]').forEach(el => {
      el.addEventListener('click', e => {
        e.preventDefault();
        chatbot.classList.add('fitness-chatbot--open');
        if (messages.children.length === 0) {
          addMessage(
            'Ciao! Sono il coach fitness di Stefano — 15+ anni di esperienza. Chiedimi di massa muscolare, nutrizione, cardio o recupero.',
            'bot'
          );
        }
        input.focus();
      });
    });
  }

  window.initFitnessChat = function () {
    injectStyles();
    createChatbot();
  };

})();