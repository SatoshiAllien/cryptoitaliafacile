# Bitcoin Rainbow Chart – Dynamic Analysis

> Aggiornato automaticamente da **Grok Agent** · 2026-07-18T06:27:19Z  
> Fonte: [https://www.blockchaincenter.net/bitcoin-rainbow-chart/](https://www.blockchaincenter.net/bitcoin-rainbow-chart/)

## Cos’è il Bitcoin Rainbow Chart?

Il **Bitcoin Rainbow Chart** è un grafico logaritmico della storia del prezzo di Bitcoin,
sovrapposto a fasce colorate (il “arcobaleno”) che rappresentano zone di valutazione relativa
rispetto a una curva di lungo periodo.

Nato come meme su Reddit (2014, utente *azop*) e reso interattivo da
[BlockchainCenter](https://www.blockchaincenter.net/bitcoin-rainbow-chart/), **non è un modello scientifico di previsione** né consulenza
finanziaria. Serve a “zoomare fuori” dalla volatilità quotidiana e a collocare il prezzo
corrente nel contesto dei cicli pluriennali.

La versione **Dynamic** ricalcola in tempo reale una regressione **Power Law** sulla storia
dei prezzi (fit sui minimi locali a 180 giorni), con forza di adattamento dichiarata dal sito
fonte intorno al **94%+ R²**.

---

## Dati live (da BlockchainCenter)

| Campo | Valore |
|-------|--------|
| Prezzo BTC (USD) | **$63,945.00** |
| Prezzo BTC (EUR) | €55,907.00 |
| Variazione 24h | +1.72% |
| Variazione 7g | -0.28% |
| Market cap (USD) | $1,282,588,746,509 |
| ATH | $126,080 (2025-10-06) |
| Data riferimento | 2026-07-18 |

### Posizione sulle fasce

| Modello | Fascia corrente | Label IT |
|---------|-----------------|----------|
| **Dynamic Power Law** | **Basically a Fire Sale** | Quasi saldi da liquidazione |
| Originale (log regression) | Bitcoin is dead | Bitcoin è morto |

- Formula dinamica: `Price = 10^(5.7695 * log10(days) + -17.0916)`
- R² fit: **99.6%**
- Deviazione vs centro modello: **-65.6%**

---

## Grafico generato

![Bitcoin Rainbow Chart](../assets/rainbow-chart.png)

*Immagine rigenerata a ogni esecuzione di `scripts/update-bitcoin-rainbow-chart.py`.*

---

## Legenda fasce e colori

| Colore | Label (EN) | Label (IT) |
|--------|------------|------------|
| `#c00000` | **Maximum Bubble Territory** | Massimo territorio bolla |
| `#d64018` | **Sell. Seriously, SELL!** | Vendi. Seriamente, VENDI! |
| `#ed7d31` | **FOMO intensifies** | FOMO in aumento |
| `#f6b45a` | **Is this a bubble?** | È una bolla? |
| `#ffeb84` | **HODL!** | HODL! |
| `#b1d580` | **Still cheap** | Ancora economico |
| `#63be7b` | **Accumulate** | Accumula |
| `#54989f` | **BUY!** | COMPRA! |
| `#4472c4` | **Basically a Fire Sale** | Quasi saldi da liquidazione |
| `#9568db` | **Bitcoin is dead** | Bitcoin è morto |

Fasce dall’alto (euforia / sopravvalutazione relativa) verso il basso
(panico / sottovalutazione relativa rispetto al trend di lungo periodo del modello).

---

## Interpretazione della fascia corrente

### Modello dinamico — Basically a Fire Sale (Quasi saldi da liquidazione)

[Modello dinamico] Tra le fasce più basse: storicamente legata a panico o fine di bear market. Il nome è un meme; non costituisce consulenza finanziaria.

### Modello originale — Bitcoin is dead

[Modello originale] Fascia viola aggiunta nelle versioni successive quando il prezzo scende sotto il rainbow classico. Indica estrema distanza verso il basso rispetto al modello originale.

### Nota di lettura (senza consulenza finanziaria)

- Il chart descrive **storia e sentiment di lungo periodo**, non timing di ingresso/uscita.
- Le etichette (BUY, SELL, FOMO, HODL…) sono **meme educativi**, non ordini di trading.
- Un prezzo in fascia bassa non garantisce rialzi; uno in fascia alta non garantisce ribassi.
- Usa il rainbow come **contesto**, affiancato a gestione del rischio, orizzonte temporale e
  comprensione del protocollo Bitcoin.

---

## Dataset JSON (dinamico)

Il blocco seguente è un estratto del payload generato. Il dataset storico completo
(settimanale) è in [`/data/bitcoin-rainbow-chart.json`](../data/bitcoin-rainbow-chart.json).

```json
{
  "meta": {
    "title": "Bitcoin Rainbow Chart – Dynamic Analysis",
    "source": "https://www.blockchaincenter.net/bitcoin-rainbow-chart/",
    "source_apis": {
      "chartdata": "https://www.blockchaincenter.net/api/coin/chartdata/?crypto=BTC",
      "rates": "https://www.blockchaincenter.net/api/coin/rates/?crypto=BTC"
    },
    "generated_at": "2026-07-18T06:27:19Z",
    "as_of": "2026-07-18",
    "disclaimer": "Il Rainbow Chart non è consulenza finanziaria. Le performance passate non indicano risultati futuri. È un modo divertente e visuale di osservare i movimenti di lungo periodo.",
    "agent": "Grok Agent · CryptoItaliaFacile",
    "feed": {
      "feed_unit_detected": "eur_converted_to_usd",
      "fx_used": 1.143774,
      "raw_last_close": 55893.0,
      "points": 5301
    }
  },
  "live": {
    "price_usd": 63945.0,
    "price_eur": 55907,
    "market_cap_usd": 1282588746509,
    "percent_change_24h": 1.7246865670696678,
    "percent_change_7d": -0.2825978213422718,
    "ath": 126080,
    "ath_date": "2025-10-06T18:57:42.558Z",
    "symbol": "BTC",
    "name": "Bitcoin"
  },
  "legend": [
    {
      "id": 0,
      "label": "Maximum Bubble Territory",
      "label_it": "Massimo territorio bolla",
      "color": "#c00000"
    },
    {
      "id": 1,
      "label": "Sell. Seriously, SELL!",
      "label_it": "Vendi. Seriamente, VENDI!",
      "color": "#d64018"
    },
    {
      "id": 2,
      "label": "FOMO intensifies",
      "label_it": "FOMO in aumento",
      "color": "#ed7d31"
    },
    {
      "id": 3,
      "label": "Is this a bubble?",
      "label_it": "È una bolla?",
      "color": "#f6b45a"
    },
    {
      "id": 4,
      "label": "HODL!",
      "label_it": "HODL!",
      "color": "#ffeb84"
    },
    {
      "id": 5,
      "label": "Still cheap",
      "label_it": "Ancora economico",
      "color": "#b1d580"
    },
    {
      "id": 6,
      "label": "Accumulate",
      "label_it": "Accumula",
      "color": "#63be7b"
    },
    {
      "id": 7,
      "label": "BUY!",
      "label_it": "COMPRA!",
      "color": "#54989f"
    },
    {
      "id": 8,
      "label": "Basically a Fire Sale",
      "label_it": "Quasi saldi da liquidazione",
      "color": "#4472c4"
    },
    {
      "id": 9,
      "label": "Bitcoin is dead",
      "label_it": "Bitcoin è morto",
      "color": "#9568db"
    }
  ],
  "original_model": {
    "type": "static_log_regression",
    "day_index_since_2012": 5312,
    "band_index": 9,
    "band": {
      "id": 9,
      "label": "Bitcoin is dead",
      "label_it": "Bitcoin è morto",
      "color": "#9568db"
    },
    "interpretation_it": "[Modello originale] Fascia viola aggiunta nelle versioni successive quando il prezzo scende sotto il rainbow classico. Indica estrema distanza verso il basso rispetto al modello originale.",
    "bounds_usd_sample": [
      1232513.03,
      905021.54,
      664646.4,
      495715.83,
      363438.9,
      260842.52,
      189748.24,
      139456.7,
      104604.05,
      78472.3
    ]
  },
  "dynamic_model": {
    "type": "power_law_bottoms_180d",
    "formula": "Price = 10^(5.7695 * log10(days) + -17.0916)",
    "slope": 5.769481827395767,
    "intercept": -17.09162650659551,
    "r2": 0.9964,
    "r2_percent": 99.6,
    "fit_price_usd": 74133.83,
    "band_index": 8,
    "band": {
      "id": 8,
      "label": "Basically a Fire Sale",
      "label_it": "Quasi saldi da liquidazione",
      "color": "#4472c4"
    },
    "deviation_percent_vs_center": -65.57,
    "bottoms_used": 8,
    "tops_used": 8,
    "interpretation_it": "[Modello dinamico] Tra le fasce più basse: storicamente legata a panico o fine di bear market. Il nome è un meme; non costituisce consulenza finanziaria.",
    "band_edges_usd": [
      604732.46,
      465178.82,
      357829.86,
      275253.74,
      211733.64,
      162872.03,
      125286.18,
      96373.98,
      74133.83,
      57026.03
    ]
  },
  "historical_summary": {
    "points": 759,
    "from": "2012-01-01",
    "to": "2026-07-18",
    "note": "Dataset completo in /data/bitcoin-rainbow-chart.json"
  }
}
```

---

## Come aggiornare

```bash
python3 scripts/update-bitcoin-rainbow-chart.py
```

Lo script:

1. Scarica prezzi storici e live da BlockchainCenter  
2. Ricalcola fasce Original + Dynamic  
3. Rigenera PNG, JSON e questo markdown  

---

## Disclaimer

Il Rainbow Chart non è consulenza finanziaria. Le performance passate non indicano risultati futuri. È un modo divertente e visuale di osservare i movimenti di lungo periodo.

Progetto: **CryptoItaliaFacile / The Little Satoshi News** · Agente: Grok
