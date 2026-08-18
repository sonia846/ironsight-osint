import time
from rich.live import Live
from ui.dashboard import render_dashboard

if __name__ == "__main__":
    # Live updating dashboard UI
    with Live(render_dashboard(), refresh_per_second=1) as live:
        while True:
            time.sleep(10)
            live.update(render_dashboard())
