from datetime import datetime

from pydantic import BaseModel

from fido_app.utils.extentions import PaymentMethod, TransactionStatus, TransactionType


class TransactionBase(BaseModel):
    user_id: int
    full_name: str
    date: datetime
    amount: float
    fee: float
    reference: str
    type: TransactionType
    payment_method: PaymentMethod
    status: TransactionStatus


class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(TransactionBase):
    id: int


class Transaction(TransactionBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
