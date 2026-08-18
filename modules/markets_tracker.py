import yfinance as yf

def fetch_market_data():
    # Key indices and commodities to track
    tickers = {
        "S&P 500": "^GSPC",
        "Crude Oil": "CL=F",
        "Gold": "GC=F",
        "Bitcoin": "BTC-USD"
    }
    
    market_summary = []
    
    for name, ticker in tickers.items():
        try:
            data = yf.Ticker(ticker).fast_info
            price = data.last_price
            prev_close = data.previous_close
            change = ((price - prev_close) / prev_close) * 100
            
            color = "green" if change >= 0 else "red"
            sign = "+" if change >= 0 else ""
            
            market_summary.append(f"[bold white]{name}:[/bold white] ${price:,.2f} [{color}]({sign}{change:.2f}%)[/{color}]")
        except Exception:
            market_summary.append(f"[bold white]{name}:[/bold white] [dim]N/A[/dim]")
            
    return "\n".join(market_summary)

if __name__ == "__main__":
    print(fetch_market_data())
