from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.api.auth.schemas import UserRegister, UserLogin, UserResponse, Token, UserDelete
from app.api.auth.models import UserModel
from app.api.subs.models import SubModel
from app.security.passwords import hash_password, verify_password
from app.security.jwt import create_access_token
from app.security.deps import get_current_user


router = APIRouter()

#Регистрация нового пользователя
@router.post("/users", response_model=UserResponse, status_code=201, summary="Регистрация нового пользователя")
def User_Register(new_user: UserRegister, db: Session = Depends(get_db)):
    email_check = db.query(UserModel).filter(UserModel.email == new_user.email).first()
    if email_check is not None:
        raise HTTPException(status_code=409, detail= "Пользователь с таким email уже существует")

    hashed_password = hash_password(new_user.password)
    user = UserModel(
        email = new_user.email,
        hashed_password = hashed_password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

#Логин пользователя
@router.post("/login", response_model=Token, status_code=200, summary="Логин пользователя")
def User_Login(user_log: UserLogin, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.email == user_log.email).first()
    if user is None:
        raise HTTPException(status_code=401, detail="Неверный email или пароль")

    password_check = verify_password(user_log.password, user.hashed_password)
    if password_check is False:
        raise HTTPException(status_code=401, detail="Неверный email или пароль")

    jwt_token = create_access_token(str(user.id))
    return {
        "access_token": jwt_token,
        "token_type": "bearer"
    }

@router.get("/users/me", response_model=UserResponse, status_code=200, summary="Профиль")
def User_Profile(current_user: UserModel = Depends(get_current_user)):
    return current_user

@router.delete("/users/me", status_code=200, summary="Удаление аккаунта")
def User_Delete(delete_data: UserDelete, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    if delete_data.confirm is False:
        raise HTTPException(status_code=400,detail="Удаление аккаунта не подтверждено")
    
    sub = db.query(SubModel).filter(SubModel.user_id == current_user.id).all()
   
    for subscription in sub:
        db.delete(subscription)

    db.delete(current_user)
    db.commit()

    return{"message": "Аккаунт успешно удалён"}
    