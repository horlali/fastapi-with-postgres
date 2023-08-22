from datetime import datetime

import pytest

from fido_app.api.transactions.models import (
    PaymentMethod,
    TransactionDB,
    TransactionStatus,
    TransactionType,
)


def test_transactiondb_model():
    # Create a new transaction
    transaction = TransactionDB(
        user_id=1,
        date=datetime.now(),
        amount=100.0,
        fee=None,
        tax=None,
        reference="123456",
        transaction_type=TransactionType.DEPOSIT,
        payment_method=PaymentMethod.BANK_TRANSFER,
        transaction_status=TransactionStatus.COMPLETED,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )

    # Test that the transaction was created correctly
    assert transaction.user_id == 1
    assert transaction.amount == 100.0
    assert transaction.reference == "123456"
    assert transaction.transaction_type == TransactionType.DEPOSIT
    assert transaction.payment_method == PaymentMethod.BANK_TRANSFER
    assert transaction.transaction_status == TransactionStatus.COMPLETED

    # Test that the amount validation works
    with pytest.raises(ValueError):
        data = {"key": "amount", "value": -100}
        transaction.validate_amount(**data)

    # Test that the fee and tax calculations work
    assert transaction.calculate_fee() == 2.0
    assert transaction.calculate_tax() == 10.0
