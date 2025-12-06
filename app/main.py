# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db import models, crud
from app.core.database import get_db, engine
from app.schemas import FishProduct, Advertisement, PriceHistory

# Создаём все таблицы, если их нет
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Fishscope API")

# --- ROUTES ---

@app.get("/api/products", response_model=List[FishProduct])
def get_products(db: Session = Depends(get_db)):
    products = crud.get_products(db)
    return products

@app.get("/api/advertisements", response_model=List[Advertisement])
def get_advertisements(db: Session = Depends(get_db)):
    ads = crud.get_advertisements(db)
    return ads

@app.get("/api/prices", response_model=List[PriceHistory])
def get_price_history(product_id: int = None, db: Session = Depends(get_db)):
    prices = crud.get_price_history(db, product_id=product_id)
    return prices
