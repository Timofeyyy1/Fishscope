from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class FishProduct(Base):
    __tablename__ = "fish_products"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    category = Column(String(50), nullable=True)

    advertisements = relationship("Advertisement", back_populates="product")
    price_history = relationship("PriceHistory", back_populates="product")


class Advertisement(Base):
    __tablename__ = "advertisements"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("fish_products.id"))
    source_id = Column(String(100), nullable=False, unique=True)
    source_url = Column(String(255), nullable=True)
    text = Column(String(1000), nullable=False)
    date_added = Column(DateTime, default=datetime.utcnow)

    product = relationship("FishProduct", back_populates="advertisements")


class PriceHistory(Base):
    __tablename__ = "price_history"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("fish_products.id"))
    price = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    source_id = Column(String(100), nullable=False)

    product = relationship("FishProduct", back_populates="price_history")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False)  # marketing / admin
