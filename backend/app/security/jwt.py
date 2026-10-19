import jwt
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException

from app.config import (SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_HOURS)


def create_access_token(user_id: str) -> str:
    return jwt.encode(
        payload={
            "sub": user_id,
            "exp": datetime.now(timezone.utc) + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
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