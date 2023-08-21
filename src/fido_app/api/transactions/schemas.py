from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel

from fido_app.utils.extentions import PaymentMethod, TransactionStatus, TransactionType


class TransactionBase(BaseModel):
    user_id: int
    date: datetime
    amount: float
    fee: float
    tax: float
    reference: str
    transaction_type: TransactionType
    payment_method: PaymentMethod
    transaction_status: TransactionStatus


class TransactionCreate(BaseModel):
    user_id: int
    date: datetime
    amount: float
    reference: str
    transaction_type: TransactionType
    payment_method: PaymentMethod
    transaction_status: TransactionStatus


class TransactionUpdate(TransactionCreate):
    user_id: Optional[int]
    date: Optional[datetime]
    amount: Optional[float]
    reference: Optional[str]
    transaction_type: Optional[TransactionType]
    payment_method: Optional[PaymentMethod]
    transaction_status: Optional[TransactionStatus]


class TransactionSchema(TransactionBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserStats(BaseModel):
    average_transaction_value: float
    day_with_highest_transactions: date
