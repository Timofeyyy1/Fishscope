from core.database import get_connection

conn = get_connection()
cursor = conn.cursor()
# работа с базой
