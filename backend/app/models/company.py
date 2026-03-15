from pydantic import BaseModel
from typing import Optional


class Company(BaseModel):
    ticker: str
    name: Optional[str] = None
    sector: Optional[str] = None
    industry: Optional[str] = None