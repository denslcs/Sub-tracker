from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.security.jwt import decode_access_token
from app.database import get_db
from app.api.auth.models import UserModel

token_reader = HTTPBearer()


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(token_reader), db: Session = Depends(get_db)):
    payload = decode_access_token(credentials.credentials)
    user_id = payload.get("sub")
    try:
        user_id = int(user_id)
    except (ValueError, TypeError):
        raise HTTPException(status_code=401, detail="Недействительный токен")

    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=401, detail="Недействительный токен")

    return user