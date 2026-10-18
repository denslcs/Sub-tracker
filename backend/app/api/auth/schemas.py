from pydantic import BaseModel, Field, EmailStr

class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=100)

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=100)

class UserResponse(BaseModel):
    id: int
    email: EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str

class UserDelete(BaseModel):
    confirm: bool = Field(default=False, description="Флаг подтверждения удаления. Если false, пользователь не будет удален")
