from pydantic import BaseModel
from datetime import datetime


class WatchlistItem(BaseModel):
    ticker: str
    date_added: datetime


class WatchlistCreate(BaseModel):
    ticker: str