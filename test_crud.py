from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.models import Base
from app.db import crud

# Настройка подключения к БД
DATABASE_URL = "mysql+pymysql://root:@localhost/fishscope"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

# Создаем таблицы (если еще не созданы)
Base.metadata.create_all(bind=engine)

def main():
    # 1️⃣ Создаем продукт
    product = crud.create_product(db, code="F001", name="Лосось", category="Рыба")
    print(f"Создан продукт: {product.id} {product.code} {product.name}")

    # 2️⃣ Создаем объявление
    ad = crud.create_advertisement(
        db,
        product_id=product.id,
        source_id="AD001",
        source_url="https://fishery.ru/ad/AD001",
        text="Лосось свежий, цена 500 руб/кг"
    )
    print(f"Создано объявление: {ad.id} {ad.source_id}")

    # 3️⃣ Добавляем цену
    price = crud.create_price(db, product_id=product.id, price=500, source_id=ad.source_id)
    print(f"Добавлена цена: {price.id} {price.price}")

    # 4️⃣ Создаем пользователя
    user = crud.create_user(db, email="admin@example.com", password="12345", role="admin")
    print(f"Создан пользователь: {user.id} {user.email}")

if __name__ == "__main__":
    main()
