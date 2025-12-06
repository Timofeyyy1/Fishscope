from app.db.models import User, FishProduct, Advertisement, PriceHistory
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from datetime import datetime

# Используем argon2 вместо bcrypt
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# Пользователи
def create_user(db: Session, email: str, password: str, role: str):
    password_hash = pwd_context.hash(password[:72])
    user = User(email=email, password_hash=password_hash, role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Продукты
def create_product(db: Session, code: str, name: str, category: str):
    product = FishProduct(code=code, name=name, category=category)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

# Объявления
def create_advertisement(db: Session, product_id: int, source_id: str, source_url: str, text: str):
    ad = Advertisement(
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

# История цен
def create_price(db: Session, product_id: int, price: float, source_id: str):
    price_entry = PriceHistory(
        product_id=product_id,
        price=price,
        date=datetime.utcnow(),
        source_id=source_id
    )
    db.add(price_entry)
    db.commit()
    db.refresh(price_entry)
    return price_entry
