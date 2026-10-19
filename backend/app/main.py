from fastapi import FastAPI
from app.api.subs.router import router as subs_router
from app.api.auth.router import router as auth_router
from app.database import Base, engine
from app.api.auth import models as auth_models
from app.api.subs import models as subs_models

app = FastAPI()

app.include_router(subs_router, prefix="/api/v1", tags=["Подписки"])
app.include_router(auth_router, prefix="/api/v1", tags=["Авторизация"])

@app.get("/health")
def health_check():
    return {"status": "healthy"}

Base.metadata.create_all(bind=engine)