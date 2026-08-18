import feedparser

# RSS Feeds list (Aap aur bhi OSINT news links add kar sakti hain)
RSS_FEEDS = {
    "JPost": "https://www.jpost.com/rss/rssfeedsfrontpage.aspx",
    "BBC": "http://feeds.bbci.co.uk/news/world/rss.xml",
    "AlJazeera": "https://www.aljazeera.com/xml/rss/all.xml"
}

def fetch_live_intel():
    intel_items = []
    
    for source, url in RSS_FEEDS.items():
        try:
            # Parse RSS Feed
            feed = feedparser.parse(url)
            
            # Har feed se top 3 latest headlines nikalein
            for entry in feed.entries[:10]:
                intel_items.append({
                    "source": source,
                    "title": entry.title,
                    "link": entry.link,
                    "published": getattr(entry, 'published', 'N/A')
                })
        except Exception as e:
            intel_items.append({
                "source": source,
                "title": f"Error fetching feed: {str(e)}",
                "link": "#",
                "published": "N/A"
            })
            
    return intel_items

if __name__ == "__main__":
    # Test Run Module
    print("[+] Fetching Live Intel Feeds...\n")
    feeds = fetch_live_intel()
    for item in feeds:
        print(f"[{item['source']}] {item['title']}")
