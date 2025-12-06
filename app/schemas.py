# app/schemas.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# --- PRODUCTS ---

class FishProductBase(BaseModel):
    code: str
    name: str
    category: str

class FishProductCreate(FishProductBase):
    pass

class FishProduct(FishProductBase):
    id: int

    class Config:
        orm_mode = True

# --- ADVERTISEMENTS ---

class AdvertisementBase(BaseModel):
    product_id: int
    source_id: str
    source_url: str
    text: str

class AdvertisementCreate(AdvertisementBase):
    pass

class Advertisement(AdvertisementBase):
    id: int
    date_added: datetime

    class Config:
        orm_mode = True

# --- PRICE HISTORY ---

class PriceHistoryBase(BaseModel):
    product_id: int
    price: float
    source_id: str

class PriceHistoryCreate(PriceHistoryBase):
    pass

class PriceHistory(PriceHistoryBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True
