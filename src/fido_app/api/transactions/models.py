from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, Float, Integer, String, event
from sqlalchemy.orm import validates

from fido_app.core.database import Base
from fido_app.utils.extentions import PaymentMethod, TransactionStatus, TransactionType


class TransactionDB(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    date = Column(DateTime)
    amount = Column(Float, nullable=False)
    fee = Column(Float)
    tax = Column(Float)
    reference = Column(String)
    transaction_type = Column(Enum(TransactionType), nullable=False)
    payment_method = Column(Enum(PaymentMethod), nullable=False)
    transaction_status = Column(Enum(TransactionStatus), nullable=False)

    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)

    @validates("amount")
    def validate_amount(self, key, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        return amount

    def calculate_fee(self):
        return self.amount * 0.02

    def calculate_tax(self):
        return self.amount * 0.1


@event.listens_for(TransactionDB, "before_insert")
def calculate_fee_tax_on_insert(mapper, connection, target):
    target.fee = target.calculate_fee()
    target.tax = target.calculate_tax()


@event.listens_for(TransactionDB, "before_update")
def calculate_fee_tax_on_update(mapper, connection, target):
    target.fee = target.calculate_fee()
    target.tax = target.calculate_tax()
