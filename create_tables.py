from app.core.database import Base, engine
from app.db import models

Base.metadata.create_all(bind=engine)
print("Таблицы созданы!")
