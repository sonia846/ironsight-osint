# ⚡ IRONSIGHT // OSINT Command Center

> **High-Performance Real-Time Threat Intelligence & OSINT Aggregation Dashboard**

IRONSIGHT ek modular, lightweight, aur terminal-native Security Operations Center (SOC) dashboard hai jo global news feeds, financial market anomalies, live aviation tracking, aur threat alerts ko ek single interface par aggregate karta hai.

---

## 🛠️ Key Features

* **Live Intel Feed:** Global RSS news aggregation with automatic threat keyword parsing.
* **Global Markets Tracker:** Real-time monitoring of key indices & commodities (S&P 500, Crude Oil, Gold, Bitcoin) via yfinance.
* **Airspace Telemetry:** Real-time global aircraft count and flight telemetry using OpenSky Network API.
* **Telegram OSINT Monitor:** Live stream threat alerts from public geopolitical channels.
* **Dual Interface Support:**
  * **Cyberpunk Rich CLI:** Ultra-fast Terminal UI with zero GUI lag.
  * **Localhost Web Dashboard:** Integrated Flask web server rendering data at http://localhost:5000.

---

## 📂 Project Structure

ironsight-osint/
├── main.py                   # CLI Terminal Entry Point
├── app.py                    # Localhost Flask Web Dashboard
├── README.md                 # Project Documentation
├── requirements.txt          # Python Dependencies
│
├── modules/
│   ├── rss_fetcher.py        # Module 1: Live News Fetcher
│   ├── markets_tracker.py    # Module 2: Financial Commodities & Crypto
│   ├── airspace_tracker.py   # Module 3: OpenSky Flight Tracking
│   └── telegram_scraper.py   # Module 4: Geopolitical Threat Streamer
│
└── ui/
    └── dashboard.py          # Rich Terminal Grid Layout & Visualizer

---

## 🚀 Installation & Setup Guide

### 1. Repository Clone Karein
Terminal open karein aur repository clone karke folder mein enter hon:

git clone https://github.com/sonia846/ironsight-osint.git
cd ironsight-osint

### 2. Dependencies Install Karein
Required Python modules install karne ke liye execute karein:

pip install rich feedparser yfinance flask

---

## 💻 How to Run

### Option A: Terminal CLI Dashboard (Rich UI)
Cyberpunk Terminal UI launch karne ke liye:

python3 main.py

### Option B: Localhost Web Dashboard
Browser-based Web Dashboard start karne ke liye:

python3 app.py

1. Launch hone ke baad apna Web Browser open karein.
2. Address bar mein URL type karein: http://127.0.0.1:5000

---

## 🔑 Permanent Git Authentication Setup

Remote URL mein token set karne ke liye:

git remote set-url origin https://<YOUR_GITHUB_TOKEN>@github.com/sonia846/ironsight-osint.git

---

## 📜 License & Disclaimer
This project is built strictly for Educational, OSINT Research, and Defensive Cyber Intelligence purposes.
