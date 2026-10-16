from pydantic import BaseModel, Field
from datetime import date
from decimal import Decimal

class SubCreate(BaseModel):
    name: str = Field(min_length=1,max_length=100)
    price: Decimal = Field(gt=0, max_digits=10, decimal_places=2)
    auto_renew: bool
    next_payment_date: date

class SubResponse(BaseModel):
    id: int
    name: str = Field(max_length=100)
    price: Decimal = Field(gt=0, max_digits=10, decimal_places=2)
    auto_renew: bool
    next_payment_date: date
    is_active: bool

class SubUpdate(BaseModel):
    name: str = Field(default=None, min_length=1, max_length=100)
    price: Decimal = Field(default=None, gt=0, max_digits=10, decimal_places=2)
    auto_renew: bool | None = None
    next_payment_date: date | None = None
