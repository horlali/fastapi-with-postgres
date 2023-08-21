from fastapi import HTTPException
from sqlalchemy import extract, func

from fido_app.api.transactions.models import TransactionDB
from fido_app.core.database import Session


def user_average_transaction(user_id: int):
    """
    Calculates the average transaction amount for a given user
    """

    with Session() as db:
        user_transactions = (
            db.query(TransactionDB).filter(user_id=TransactionDB.user_id).all()
        )

        if not user_transactions:
            raise HTTPException(status_code=404, detail="User not found")

        total_amount = sum(transaction.amount for transaction in user_transactions)
        average_amount = total_amount / len(user_transactions)

        return average_amount


def user_max_transaction_day(user_id: int):
    """
    Calculates the day with the highest number of transactions for a given user
    """

    with Session() as db:
        user_transactions = (
            db.query(TransactionDB).filter(user_id=TransactionDB.user_id).all()
        )

        if not user_transactions:
            raise HTTPException(status_code=404, detail="User not found")

        transaction_count_by_day = (
            db.query(
                func.count(TransactionDB.id), extract("day", TransactionDB.created_at)
            )
            .filter(TransactionDB.user_id == user_id)
            .group_by(extract("day", TransactionDB.created_at))
            .all()
        )
        transaction_count_by_day = dict(transaction_count_by_day)

        max_transaction_day = max(
            transaction_count_by_day, key=transaction_count_by_day.get
        )

        return max_transaction_day
