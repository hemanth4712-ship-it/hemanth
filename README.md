# 🐄 Smart Dairy Farm Management System (గోకులం డైరీ మేనేజ్‌మెంట్)

An intelligent, practical, and full-stack AI-enabled platform specifically engineered for small and medium-scale Indian dairy farmers. The platform streamlines cattle registration, clinical triage monitoring, milk yield analytics, scientific feed formulation (ICAR/NDDB standards), water and heat stress tracking (THI), waste/biogas management, cold-chain logistics, and financial profit-and-loss accounting.

---

## 🌟 Key Highlights & Modules

### 1. 🐄 Animal Management
- Register cows and buffaloes with unique ear-tag / RFID IDs (e.g. `IND-AP-101`).
- Track breed (Gir, Sahiwal, Murrah Buffalo, HF Cross, Ongole, Jaffarabadi), body weight, parity/lactation count, and life stages (Milking, Dry, Pregnant, Heifer, Calf).
- Dedicated per-animal profile cards with lifetime milk production and individual medical history.

### 2. 🩺 AI-Assisted Clinical Health Triage & Vaccinations
- Multi-factor veterinary clinical decision matrix analyzing body temperature, rumination activity, feed refusal, and sudden milk drop.
- Generates categorized risk levels: **Low**, **Moderate**, and **High Risk (Urgent)** with veterinary contact recommendations.
- Automated immunization scheduling and reminders for **Foot-and-Mouth Disease (FMD)**, **Haemorrhagic Septicaemia (HS)**, **Black Quarter (BQ)**, and **Deworming**.
- *Legal & Medical Disclaimer:* Triage algorithm provides clinical decision-support and never claims to replace physical examination by a licensed veterinary doctor.

### 3. 🥛 Milk Production & Time-Series Forecasting
- Daily morning and evening milk quantity logs with Fat % and SNF % tracking.
- **7-Day Milk Forecast Engine:** Uses Holt's linear exponential smoothing model with $95\%$ confidence uncertainty intervals.
- **Milk Anomaly Detector:** Automatically flags sudden drops exceeding $15-20\%$ against an animal's 7-day rolling baseline to catch early mastitis.

### 4. 🌾 Smart Feed Management (ICAR / NDDB Rationing)
- Formulates daily dry matter intake ($2.5 - 3.0\%$ of body weight), green fodder (18-25 kg), dry straw (4-6 kg), and concentrate ($1.2\text{ kg} + 400\text{g/L}$ milk).
- Inventory stock management with automated reorder warnings.
- **Feed Cost Efficiency Analyzer:** Evaluates feed expenses as a percentage of milk revenue (optimal benchmark: $50-60\%$).

### 5. ☀️ Smart Water & Heat Stress Monitoring (THI)
- Computes the **Temperature-Humidity Index (THI)** for tropical dairy cattle:
  $$\text{THI} = (0.8 \times T) + \left(\frac{\text{RH}}{100} \times (T - 14.4)\right) + 46.4$$
- Classifies environmental stress into *Comfortable* ($<72$), *Mild Heat Stress* ($72-78$), *Moderate Heat Stress* ($79-88$), and *Severe Heat Stress* ($>88$).
- Alerts when farm water storage drops below the herd's daily hydration requirement ($75\text{L/animal}$).

### 6. ♻️ Dairy Waste, Biogas & Vermicompost Tracker
- Tracks daily dung collection, biogas digester feeding, and vermicompost fertilizer preparation.
- Converts biogas feedstock into estimated cubic meters of biogas and equivalent LPG cylinder fuel savings.
- Records organic manure sales and updates financial ledger automatically.

### 7. ❄️ Milk Quality, Storage & Cold-Chain Logistics
- Batch tracking with chilling temperature monitoring (strictly flags temperatures $>4.5^\circ\text{C}$ to prevent spoilage).
- Cooperative society collection center dispatch logs with vehicle tracking and rejection reason audits.

### 8. 💰 Complete Financial Accounting & Profit/Loss Ledger
- Categorizes all farm cashflows: Milk sales, Manure sales, Cattle Feed purchases, Veterinary care, Labor wages, Utilities, and Equipment maintenance.
- Computes:
  $$\text{Total Revenue} = \sum \text{Income}$$
  $$\text{Total Expenses} = \sum \text{Expenses}$$
  $$\text{Net Profit} = \text{Total Revenue} - \text{Total Expenses}$$
- 6-month historical cashflow bar charts and category expense distribution.

### 9. 🤖 AI Dairy Farm Assistant
- Queries actual recorded farm database telemetry to answer farm-specific questions:
  - *"How much did I spend on feed this month?"*
  - *"Why has my animal's milk production decreased?"*
  - *"Which animals need a scheduled vaccination?"*
  - *"What is my recorded profit this month?"*
- Supports English and Telugu (తెలుగు) natural queries.
- Built-in rule-based offline farm query engine + optional Google Gemini LLM API integration.

### 10. 🔔 In-App Notifications & Alerts
- Real-time notification center with severity badges (Info, Warning, Danger) for overdue vaccines, low feed inventory, sudden milk drops, and extreme heat stress.

### 11. 🌐 Bilingual Internationalization (English & తెలుగు)
- Instant, one-click language toggle across all navigation bars, cards, forms, tables, and AI assistant suggestions.

---

## 🛠️ Technology Stack

- **Backend:** Python 3.12+, FastAPI, SQLAlchemy 2.0 ORM, Pydantic v2, PyJWT, Bcrypt.
- **Database:** SQLite (default local zero-configuration) / PostgreSQL (production-ready).
- **Machine Learning & Analytics:** Holt's Linear Exponential Smoothing with uncertainty intervals, Z-score Anomaly Detection, ICAR Nutritional Engine, THI Heat Index formula.
- **Frontend:** Single Page Application (SPA), Tailwind CSS, Chart.js, FontAwesome Icons, Bilingual i18n Dictionary.
- **Testing:** Pytest, HTTPX TestClient.
- **Containerization:** Docker & Docker Compose.

---

## 🚀 Quick Start Guide (Local Setup)

### Prerequisites
- Python 3.12 or higher installed.

### 1. Clone & Enter the Directory
```bash
cd "c:\Users\gogula hemanth\OneDrive\Desktop\Dariy"
```

### 2. Activate Virtual Environment
On Windows (PowerShell):
```powershell
.\venv\Scripts\Activate.ps1
```
On Linux/macOS:
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python run.py
```

The system will start and be accessible at:
- **Web Application Portal:** [http://localhost:8000/](http://localhost:8000/)
- **Interactive Swagger API Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc API Specifications:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🔑 Pre-seeded Demo Credentials

A realistic Indian dairy farm dataset (*Sri Krishna Gokulam Dairy Farm, Guntur*) is automatically seeded on first launch:

| Field | Demo Value |
|---|---|
| **Email** | `farmer@dairy.in` |
| **Password** | `farmer123` |
| **Farmer Name** | Ramesh Reddy (రమేష్ రెడ్డి) |
| **Herd Size** | 8 Animals (Murrah Buffaloes, Gir, Sahiwal, HF Cross, Ongole) |
| **Language** | English & Telugu (Toggleable in top navbar) |

*(Note: The Web UI automatically logs into this demo account on first load so you can immediately explore and test all features without friction!)*

---

## 🧪 Running Automated Tests

Run the comprehensive unit and integration test suite:

```bash
$env:PYTHONPATH="backend"
pytest tests/ -v
```

All test suites verify:
- API health and authentication tokens
- Animal registration and profile generation
- Milk production logging and Holt's exponential forecasting
- Statistical anomaly detection on milk drops
- Veterinary clinical triage risk levels
- ICAR feed ration formulations and economics

---

## 🐳 Docker Deployment

To run the complete system with PostgreSQL using Docker Compose:

```bash
# 1. Copy environment template
cp .env.example .env

# 2. Build and run containers
docker-compose up --build -d

# 3. Check container logs
docker-compose logs -f
```

---

## 📁 Project Architecture & Directory Layout

```text
├── backend/
│   └── app/
│       ├── __init__.py
│       ├── config.py             # App settings and environment variables
│       ├── database.py           # SQLAlchemy engine & session maker
│       ├── models.py             # 12 Normalized relational database tables
│       ├── schemas.py            # Pydantic v2 schemas for request/response validation
│       ├── security.py           # Bcrypt hashing, JWT tokens, farm isolation
│       ├── seed_data.py          # Realistic Indian dairy farm dataset
│       ├── main.py               # FastAPI application & router mounting
│       ├── ml/
│       │   ├── milk_forecasting.py   # Holt's linear exponential smoothing & anomaly detection
│       │   ├── health_risk_model.py  # Veterinary triage risk scoring
│       │   └── nutrition_engine.py   # ICAR & NDDB feed ration formulations
│       └── routers/
│           ├── auth.py           # Registration, login, profile, language
│           ├── farms.py          # Multi-tenant farm records
│           ├── animals.py        # Animal profiles and herd registry
│           ├── health.py         # Clinical triage and vaccination schedules
│           ├── milk.py           # Production entries, forecasts, anomalies
│           ├── feed.py           # Inventory, consumption, ration calculator
│           ├── water_env.py      # THI index calculation & water shortage alerts
│           ├── waste.py          # Dung, biogas fuel estimation, compost sales
│           ├── logistics.py      # Chilling cold-chain (<=4C) & batch dispatch
│           ├── finance.py        # Ledger entries, P&L, expense distribution
│           ├── assistant.py      # Real telemetry AI assistant & Gemini API
│           ├── notifications.py  # Real-time alert center
│           └── reports.py        # Executive summary & dashboard KPIs
├── frontend/
│   ├── index.html                # Modern responsive UI with mobile bottom-nav
│   ├── app.js                    # SPA state machine, API client, Chart.js renderers
│   ├── translations.js           # Bilingual English & Telugu (తెలుగు) dictionary
│   └── styles.css                # Dairy theme styling, print formats, animations
├── tests/
│   ├── test_api.py               # End-to-end API integration tests
│   └── test_ml.py                # Machine learning and rule engine unit tests
├── .env.example                  # Environment variable configuration template
├── Dockerfile                    # Production container image definition
├── docker-compose.yml            # Multi-service container orchestration with PostgreSQL
├── requirements.txt              # Python library dependencies
├── run.py                        # Single-command application launcher
└── README.md                     # Comprehensive documentation
```

---

## 🔮 Roadmap & Future Enhancements

1. **IoT Sensor Gateway Integration:** Direct MQTT / HTTP ingestion for ESP32/LoRaWAN water level sensors and shed temperature/humidity probes.
2. **Automated Estrus & Rumination Neck Tags:** Real-time accelerometer collar data processing for automatic heat cycle and estrus detection.
3. **WhatsApp / SMS Gateway Integration:** Daily milk summary and critical mastitis alerts sent via Twilio or Gupshup WhatsApp APIs directly to the farmer's mobile phone.
