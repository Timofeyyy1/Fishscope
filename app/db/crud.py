# app/db/crud.py
from sqlalchemy.orm import Session
from app.db import models
from datetime import datetime
from typing import List, Optional

# --- PRODUCTS ---

def get_products(db: Session) -> List[models.FishProduct]:
    return db.query(models.FishProduct).all()

def get_product(db: Session, product_id: int) -> Optional[models.FishProduct]:
    return db.query(models.FishProduct).filter(models.FishProduct.id == product_id).first()

def create_product(db: Session, code: str, name: str, category: str) -> models.FishProduct:
    product = models.FishProduct(code=code, name=name, category=category)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

# --- ADVERTISEMENTS ---

def get_advertisements(db: Session) -> List[models.Advertisement]:
    return db.query(models.Advertisement).all()

def get_advertisement(db: Session, ad_id: int) -> Optional[models.Advertisement]:
    return db.query(models.Advertisement).filter(models.Advertisement.id == ad_id).first()

def create_advertisement(db: Session, product_id: int, source_id: str, source_url: str, text: str) -> models.Advertisement:
    ad = models.Advertisement(
        product_id=product_id,
        source_id=source_id,
        source_url=source_url,
        text=text,
        date_added=datetime.utcnow()
    )
    db.add(ad)
    db.commit()
    db.refresh(ad)
    return ad

# --- PRICE HISTORY ---

def get_price_history(db: Session, product_id: int = None) -> List[models.PriceHistory]:
    query = db.query(models.PriceHistory)
    if product_id is not None:
        query = query.filter(models.PriceHistory.product_id == product_id)
    return query.all()

def add_price(db: Session, product_id: int, price: float, source_id: str) -> models.PriceHistory:
    price_entry = models.PriceHistory(
        product_id=product_id,
        price=price,
        date=datetime.utcnow(),
        source_id=source_id
    )
    db.add(price_entry)
    db.commit()
    db.refresh(price_entry)
    return price_entry
