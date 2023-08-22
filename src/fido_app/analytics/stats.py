from fido_app.api.transactions.models import TransactionDB
from fido_app.core.database import Session
from fido_app.utils.extentions import UserNotFoundError


def user_average_transaction(user_id: int):
    """
    Calculates the average transaction amount for a given user
    """

    with Session() as db:
        user_transactions = db.query(TransactionDB).filter_by(user_id=user_id).all()

        if not user_transactions:
            raise UserNotFoundError("User not found")

        average_amount = sum(
            transaction.amount for transaction in user_transactions
        ) / len(user_transactions)

        return average_amount


def user_highest_transaction(user_id: int):
    """
    Calculates the day with the highest number of transactions for a given user
    """

    with Session() as db:
        highest_transaction = (
            db.query(TransactionDB)
            .filter_by(user_id=user_id)
            .order_by(
                TransactionDB.amount.desc(),
                TransactionDB.date.desc(),
            )
            .first()
        )

        if not highest_transaction:
            raise UserNotFoundError("User not found")

        return {"amount": highest_transaction.amount, "date": highest_transaction.date}
