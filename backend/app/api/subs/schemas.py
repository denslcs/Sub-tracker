from pydantic import BaseModel, Field, field_validator
from datetime import date
from decimal import Decimal


class SubCreate(BaseModel):
    name: str = Field(min_length=1,max_length=100)
    price: Decimal = Field(gt=0, max_digits=10, decimal_places=2)
    auto_renew: bool
    next_payment_date: date
    @field_validator("next_payment_date")
    @classmethod
    def validate_payment_date(cls, payment_date: date) -> date:
        if payment_date <= date.today():
            raise ValueError("Дата следующего платежа должна быть позже сегодняшнего дня")

        return payment_date

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
    @field_validator("next_payment_date")
    @classmethod
    def validate_payment_date(cls, payment_date: date | None) -> date | None:
        if payment_date is None:
            return payment_date

        if payment_date <= date.today():
            raise ValueError("Дата следующего платежа должна быть позже сегодняшнего дня")

        return payment_date