from datetime import datetime
from typing import Dict, Optional

from pydantic import BaseModel, Field

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
    amount: float = Field(..., gt=0)
    reference: str
    transaction_type: TransactionType
    payment_method: PaymentMethod
    transaction_status: TransactionStatus


class TransactionUpdate(TransactionCreate):
    user_id: Optional[int]
    date: Optional[datetime]
    amount: Optional[float] = Field(gt=0)
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
    highest_transaction: Dict[str, float | datetime]
