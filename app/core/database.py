from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings

DATABASE_URL = (
    f"mysql+pymysql://{settings.DB_USER}:{settings.DB_PASSWORD}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}?charset=utf8mb4"
)

engine = create_engine(
    DATABASE_URL,
    echo=True,   # выводит SQL-запросы в консоль
    future=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
