import pytest

from fido_app.analytics.stats import user_average_transaction


def test_user_average_transaction_user_not_found(db_session):
    with pytest.raises(Exception):
        user_average_transaction(user_id=999)


# from datetime import datetime
# from fido_app.api.transactions.models import TransactionDB
# from fido_app.utils.extentions import PaymentMethod, TransactionStatus, TransactionType


# def test_user_average_transaction_no_transactions(db_session):
#     average_amount = user_average_transaction(user_id=1, db_session=db_session)

#     assert average_amount == 0.0


# def test_user_average_transaction_single_transaction(db_session):
#     example_data = [
#         TransactionDB(
#             user_id=1,
#             date=datetime.now(),
#             amount=50.0,
#             fee=2.0,
#             tax=1.0,
#             reference="ref123",
#             type=TransactionType.DEPOSIT,
#             payment_method=PaymentMethod.CREDIT_CARD,
#             status=TransactionStatus.COMPLETED,
#         )
#     ]

#     db_session.add_all(example_data)
#     db_session.commit()

#     average_amount = user_average_transaction(user_id=1, db=db_session)

#     assert average_amount == pytest.approx(50.0, rel=1e-2)


# def test_user_average_transaction_multiple_transactions(db_session):
#     example_data = [
#         TransactionDB(
#             user_id=1,
#             date=datetime.now(),
#             amount=100.0,
#             fee=5.0,
#             tax=2.0,
#             reference="ref123",
#             type=TransactionType.purchase,
#             payment_method=PaymentMethod.credit_card,
#             status=TransactionStatus.completed,
#         ),
#         TransactionDB(
#             user_id=1,
#             date=datetime.now(),
#             amount=200.0,
#             fee=10.0,
#             tax=4.0,
#             reference="ref456",
#             type=TransactionType.purchase,
#             payment_method=PaymentMethod.bank_transfer,
#             status=TransactionStatus.completed,
#         ),
#     ]

#     db_session.add_all(example_data)
#     db_session.commit()

#     average_amount = user_average_transaction(user_id=1, db=db_session)

#     assert average_amount == pytest.approx(150.0, rel=1e-2)
