from core.database import engine

try:
    with engine.connect() as conn:
        print("Подключение к базе данных успешно!")
except Exception as e:
    print("Ошибка подключения:", e)
