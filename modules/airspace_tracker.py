import urllib.request
import json

def fetch_airspace_data():
    # Fetch live state vectors from OpenSky Network
    url = "https://opensky-network.org/api/states/all"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            total_flights = len(data.get('states', []))
            return f"[bold white]Tracked Aircraft:[/bold white] [cyan]{total_flights:,}[/cyan]"
    except Exception:
        return "[bold white]Tracked Aircraft:[/bold white] [dim]API Busy (Retrying)[/dim]"

if __name__ == "__main__":
    print(fetch_airspace_data())
