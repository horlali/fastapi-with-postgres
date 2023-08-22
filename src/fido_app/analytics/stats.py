from sqlalchemy import func
from sqlalchemy.orm import Session as DBSession

from fido_app.api.transactions.models import TransactionDB
from fido_app.core.database import Session
from fido_app.utils.extentions import UserNotFoundError


def user_average_transaction(user_id: int, db_session: DBSession = Session()):
    """
    Calculates the average transaction amount for a given user
    """

    average_amount = (
        db_session.query(func.avg(TransactionDB.amount))
        .filter_by(user_id=user_id)
        .scalar()
    )

    if not average_amount:
        raise UserNotFoundError("User not found")

    return average_amount


def user_highest_transaction(user_id: int, db_session: DBSession = Session()):
    """
    Calculates the day with the highest number of transactions for a given user
    """

    highest_transaction = (
        db_session.query(TransactionDB)
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
