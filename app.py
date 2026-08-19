from flask import Flask, render_template_string, jsonify
import threading
import time
import re
from modules.rss_fetcher import fetch_live_intel
from modules.markets_tracker import fetch_market_data
from modules.airspace_tracker import fetch_airspace_data
from modules.telegram_scraper import fetch_telegram_alerts

app = Flask(__name__)

# Global Cache for Instant Loading
CACHE = {
    'news': [],
    'markets': 'Loading market data...',
    'airspace': 'Loading airspace data...',
    'telegram': 'Loading Telegram feed...'
}

def clean_tags(text):
    """Strips Rich Terminal color tags like [bold white], [red], etc. for Web Clean Display"""
    if not isinstance(text, str):
        return text
    return re.sub(r'\[/*[a-zA-Z0-9 _]+\]', '', text)

def update_cache_background():
    """Background worker to fetch APIs continuously without freezing the UI"""
    global CACHE
    while True:
        try:
            CACHE['news'] = fetch_live_intel()
            CACHE['markets'] = fetch_market_data()
            CACHE['airspace'] = fetch_airspace_data()
            CACHE['telegram'] = fetch_telegram_alerts()
        except Exception as e:
            print(f"Error fetching background data: {e}")
        time.sleep(10)  # Refresh background data every 10 seconds

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>IRONSIGHT // OSINT COMMAND CENTER</title>
    <style>
        body { background-color: #0d1117; color: #00ff66; font-family: 'Courier New', monospace; margin: 20px; }
        h1 { text-align: center; color: #00e5ff; border-bottom: 2px solid #00ff66; padding-bottom: 10px; }
        .container { display: flex; gap: 20px; }
        .panel { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 15px; flex: 1; }
        .news-panel { flex: 2; }
        h2 { color: #ffab00; border-bottom: 1px dashed #444; padding-bottom: 5px; }
        table { width: 100%; border-collapse: collapse; }
        th, td { text-align: left; padding: 8px; border-bottom: 1px solid #21262d; }
        th { color: #00e5ff; }
        td { color: #c9d1d9; }
        .metric-title { color: #ff5555; font-weight: bold; margin-top: 15px; }
        .status { text-align: center; margin-top: 20px; color: #00ff66; font-weight: bold; }
    </style>
</head>
<body>
    <h1>IRONSIGHT // OSINT COMMAND CENTER</h1>
    <div class="container">
        <div class="panel news-panel">
            <h2>LIVE INTEL FEED</h2>
            <table id="news-table">
                <tr><th>Source</th><th>Headline</th></tr>
            </table>
        </div>
        <div class="panel">
            <h2>METRICS</h2>
            <div class="metric-title">GLOBAL MARKETS</div>
            <div id="markets">Fetching live data...</div>
            <div class="metric-title">AIRSPACE MONITORING</div>
            <div id="airspace">Fetching live data...</div>
            <div class="metric-title">TELEGRAM OSINT</div>
            <div id="telegram">Fetching live data...</div>
        </div>
    </div>
    <div class="status">STATUS: ONLINE | LOCALHOST SERVER ACTIVE</div>

    <script>
        function updateData() {
            fetch('/api/data')
                .then(res => res.json())
                .then(data => {
                    if (data.news && data.news.length > 0) {
                        let tableContent = '<tr><th>Source</th><th>Headline</th></tr>';
                        data.news.forEach(item => {
                            tableContent += `<tr><td style="color:#00e5ff;font-weight:bold;">${item.source}</td><td>${item.title}</td></tr>`;
                        });
                        document.getElementById('news-table').innerHTML = tableContent;
                    }

                    if(data.markets) document.getElementById('markets').innerHTML = data.markets.replace(/\\n/g, '<br>');
                    if(data.airspace) document.getElementById('airspace').innerHTML = data.airspace;
                    if(data.telegram) document.getElementById('telegram').innerHTML = data.telegram.replace(/\\n/g, '<br>');
                });
        }
        updateData();
        setInterval(updateData, 3000); // UI poll every 3s
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/data')
def get_data():
    return jsonify({
        'news': CACHE.get('news', []),
        'markets': clean_tags(CACHE.get('markets', '')),
        'airspace': clean_tags(CACHE.get('airspace', '')),
        'telegram': clean_tags(CACHE.get('telegram', ''))
    })

if __name__ == '__main__':
    # Background Thread for auto API Updates
    t = threading.Thread(target=update_cache_background)
    t.daemon = True
    t.start()
    
    print("\n[+] IRONSIGHT Localhost Web Server Starting...")
    print("[+] Open URL in Browser: http://127.0.0.1:5000\n")
    app.run(host='0.0.0.0', port=5000, debug=False)
