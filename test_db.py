# test_db.py
from core.database import get_connection

def test_connection():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")  # узнаем, к какой базе подключились
        db_name = cursor.fetchone()[0]
        print(f"Подключение успешно! Текущая база: {db_name}")
    except Exception as e:
        print("Ошибка подключения:", e)
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    test_connection()
