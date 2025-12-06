from app.core.database import SessionLocal
from app.db import crud

def main():
    db = SessionLocal()

    # 1. Создаём продукт
    product = crud.create_product(db, code="F001", name="Лосось", category="Рыба")
    print("Создан продукт:", product.id, product.code, product.name)

    # 2. Создаём объявление для продукта
    ad = crud.create_advertisement(
        db,
        product_id=product.id,
        source_id="AD001",
        source_url="https://fishery.ru/ad/AD001",
        text="Лосось свежий, цена 500 руб/кг"
    )
    print("Создано объявление:", ad.id, ad.source_id)

    # 3. Добавляем цену в историю
    price = crud.add_price(db, product_id=product.id, price=500, source_id=ad.source_id)
    print("Добавлена цена:", price.id, price.price)

    # 4. Создаём пользователя
    user = crud.create_user(db, email="admin@example.com", password="12345", role="admin")
    print("Создан пользователь:", user.id, user.email, user.role)

    # 5. Получаем все продукты
    products = crud.list_products(db)
    print("Список продуктов:", [(p.id, p.name) for p in products])

    # 6. Получаем объявления по продукту
    ads = crud.get_ads_by_product(db, product_id=product.id)
    print("Объявления продукта:", [(a.id, a.source_id) for a in ads])

    # 7. Получаем историю цен
    prices = crud.get_price_history(db, product_id=product.id)
    print("История цен продукта:", [(p.id, p.price) for p in prices])

    db.close()

if __name__ == "__main__":
    main()
