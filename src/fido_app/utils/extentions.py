from enum import Enum


class PaymentMethod(str, Enum):
    CREDIT_CARD = "credit_card"
    MOBILE_MONEY = "mobile_money"
    BANK_TRANSFER = "bank_transfer"


class TransactionType(str, Enum):
    CREDIT = "credit"
    DEBIT = "debit"


class TransactionStatus(str, Enum):
    COMPLETED = "completed"
    PENDING = "pending"
    FAILED = "failed"


class UserNotFoundError(Exception):
    pass
