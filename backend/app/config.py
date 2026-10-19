import os
from dotenv import load_dotenv

load_dotenv()

# Настройки базы данных
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./sub.db")

# Настройки JWT
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 2

if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY не найден в .env")