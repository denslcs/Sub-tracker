from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.api.subs.schemas import SubCreate, SubResponse, SubUpdate
from app.security.deps import get_current_user
from app.api.subs.models import SubModel
from app.api.auth.models import UserModel


router = APIRouter()

#Создание новой подписки
@router.post("/subsubs", response_model=SubResponse, status_code=201, summary="Создать новую подписку")
def Sub_Create(new_sub: SubCreate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    sub = SubModel(
        name=new_sub.name.strip(),
        price=new_sub.price,
        auto_renew=new_sub.auto_renew,
        next_payment_date=new_sub.next_payment_date,
        user_id=current_user.id
    )
   
    db.add(sub)
    db.commit()
    db.refresh(sub)

    return sub

#Получение всех подписок
@router.get("/subsubs", response_model=list[SubResponse], summary="Получить все подписки")
def Sub_Response_All(db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    return db.query(SubModel).filter(SubModel.user_id == current_user.id).all()

# Получение подписки
@router.get("/subsubs/{subscription_id}", response_model=SubResponse, summary="Получить конкретную подписку по ID")
def Sub_Response(subscription_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    sub = db.get(SubModel, subscription_id)
    if not sub:
        raise HTTPException(status_code=404, detail="Подписка не найдена")
    if sub.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Подписка не найдена")
    return sub

#Изменение подписки
@router.patch("/subsubs/{subscription_id}", response_model=SubResponse, summary="Изменить подписку")
def Sub_Update(subscription_id: int, updated_sub: SubUpdate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    sub = db.get(SubModel, subscription_id)
    if sub is None:
        raise HTTPException(status_code=404, detail="Подписка не найдена")
    if sub.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Подписка не найдена")

    changes = updated_sub.model_dump(exclude_unset=True)
    
    if "price" in changes:
        sub.price = changes["price"]

    if "name" in changes:
        sub.name = changes["name"]

    if "auto_renew" in changes:
        sub.auto_renew = changes["auto_renew"]

    if "next_payment_date" in changes:
        sub.next_payment_date = changes["next_payment_date"]

    db.commit()
    db.refresh(sub)

    return sub

#Удаление подписки
@router.delete("/subsubs/{subscription_id}", status_code=200, summary="Удалить подписку")
def Sub_Delete(subscription_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    sub = db.get(SubModel, subscription_id)
    if sub is None:
        raise HTTPException(status_code=404, detail="Подписка не найдена")
    if sub.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Подписка не найдена")

    
    db.delete(sub)
    db.commit()

    return {"message": f"Подписка {sub.name} успешно удалена"}