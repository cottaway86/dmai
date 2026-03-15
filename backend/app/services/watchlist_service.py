from datetime import datetime
from app.models.watchlist import WatchlistItem

watchlist = []


def get_watchlist():
    return watchlist


def add_stock(ticker: str):
    item = WatchlistItem(
        ticker=ticker.upper(),
        date_added=datetime.utcnow()
    )
    watchlist.append(item)
    return item


def remove_stock(ticker: str):
    global watchlist
    watchlist = [w for w in watchlist if w.ticker != ticker.upper()]