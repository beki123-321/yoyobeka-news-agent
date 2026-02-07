import feedparser

BBC_RSS = "http://feeds.bbci.co.uk/news/rss.xml"

def fetch_top_headlines(limit=4):
    feed = feedparser.parse(BBC_RSS)
    headlines = []

    for entry in feed.entries[:limit]:
        headlines.append(entry.title)

    return headlines
