from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from modules.rss_fetcher import fetch_live_intel
from modules.markets_tracker import fetch_market_data
from modules.airspace_tracker import fetch_airspace_data
from modules.telegram_scraper import fetch_telegram_alerts
console = Console()

def create_layout():
    layout = Layout()
    
    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=3)
    )
    
    layout["main"].split_row(
        Layout(name="news_feed", ratio=2),
        Layout(name="stats_panel", ratio=1)
    )
    
    return layout

def render_dashboard():
    layout = create_layout()
    
    # Header
    layout["header"].update(
        Panel("", title="[bold cyan]IRONSIGHT // OSINT COMMAND CENTER[/bold cyan]", border_style="green")
    )
    
    # News Feed
    news_table = Table(title="[bold yellow]LIVE INTEL FEED[/bold yellow]", expand=True)
    news_table.add_column("Source", style="bold cyan", width=12)
    news_table.add_column("Headline", style="white")
    
    intel_data = fetch_live_intel()
    for item in intel_data:
        news_table.add_row(item['source'], item['title'])
        
    layout["news_feed"].update(Panel(news_table, border_style="bright_blue"))
    
    # Fetch Data for Side Panel
    market_info = fetch_market_data()
    airspace_info = fetch_airspace_data()
    telegram_info = fetch_telegram_alerts()

    layout["stats_panel"].update(
        Panel(
            f"[bold yellow]GLOBAL MARKETS[/bold yellow]\n{market_info}\n\n"
            f"[bold red]AIRSPACE MONITORING[/bold red]\n{airspace_info}\n\n"
            f"[bold yellow]TELEGRAM OSINT[/bold yellow]\n{telegram_info}",
            title="METRICS", 
            border_style="magenta"
        )
    )
    
    # Footer
    layout["footer"].update(
        Panel("[bold green]STATUS: ONLINE | SYSTEM HEALTH: OK[/bold green]", border_style="white")
    )
    
    return layout

if __name__ == "__main__":
    console.print(render_dashboard())
