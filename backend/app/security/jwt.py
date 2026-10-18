from fastapi import HTTPException
import jwt
import os
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY не найден в .env")

ALGORITHM = "HS256"

def create_access_token(user_id: str) -> str:
    return jwt.encode(
        payload={
            "sub": user_id,
            "exp": datetime.now(timezone.utc) + timedelta(hours=2)
        },
        key=SECRET_KEY,
        algorithm=ALGORITHM
    )

def decode_access_token(token: str) -> dict:
    try:
        return jwt.decode(
            token,
            key=SECRET_KEY,
            algorithms=[ALGORITHM]
        )
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Недействительный токен")