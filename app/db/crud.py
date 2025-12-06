from sqlalchemy.orm import Session
from datetime import datetime
from app.db import models
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ---------------- FishProduct ----------------
def create_product(db: Session, code: str, name: str, category: str = None):
    product = models.FishProduct(code=code, name=name, category=category)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_product_by_code(db: Session, code: str):
    return db.query(models.FishProduct).filter(models.FishProduct.code == code).first()

def list_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.FishProduct).offset(skip).limit(limit).all()


# ---------------- Advertisement ----------------
def create_advertisement(db: Session, product_id: int, source_id: str, source_url: str, text: str):
    ad = models.Advertisement(
        product_id=product_id,
        source_id=source_id,
        source_url=source_url,
        text=text
    )
    db.add(ad)
    db.commit()
    db.refresh(ad)
    return ad

def get_ads_by_product(db: Session, product_id: int):
    return db.query(models.Advertisement).filter(models.Advertisement.product_id == product_id).all()


# ---------------- PriceHistory ----------------
def add_price(db: Session, product_id: int, price: float, source_id: str, date: datetime = None):
    if date is None:
        date = datetime.utcnow()
    price_record = models.PriceHistory(
        product_id=product_id,
        price=price,
        source_id=source_id,
        date=date
    )
    db.add(price_record)
    db.commit()
    db.refresh(price_record)
    return price_record

def get_price_history(db: Session, product_id: int):
    return db.query(models.PriceHistory).filter(models.PriceHistory.product_id == product_id).all()


# ---------------- User ----------------
def create_user(db: Session, email: str, password: str, role: str):
    password_hash = pwd_context.hash(password)
    user = models.User(email=email, password_hash=password_hash, role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()
