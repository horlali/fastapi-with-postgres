from sqlalchemy import Column, DateTime, Enum, Float, Integer, String

from fido_app.core.database import Base
from fido_app.utils.extentions import PaymentMethod, TransactionStatus, TransactionType


class TransactionDB(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    date = Column(DateTime)
    amount = Column(Float)
    fee = Column(Float)
    tax = Column(Float)
    reference = Column(String)
    type = Column(Enum(TransactionType), nullable=False)
    payment_method = Column(Enum(PaymentMethod), nullable=False)
    status = Column(Enum(TransactionStatus), nullable=False)

    created_at = Column(DateTime)
    updated_at = Column(DateTime)
