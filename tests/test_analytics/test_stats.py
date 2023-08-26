import pytest

from fido_app.analytics.stats import user_average_transaction, user_highest_transaction
from fido_app.utils.extentions import UserNotFoundError


def test_user_average_transaction_user_not_found(session):
    with pytest.raises(UserNotFoundError):
        user_average_transaction(user_id=999, db=session)


def test_user_average_transaction_with_invalid_user(session):
    with pytest.raises(UserNotFoundError):
        user_average_transaction(user_id="1b3", db=session)


def test_user_max_transaction_user_not_found(session):
    with pytest.raises(UserNotFoundError):
        user_highest_transaction(user_id=999, db=session)


def test_user_max_transaction_with_invalid_user(session):
    with pytest.raises(UserNotFoundError):
        user_highest_transaction(user_id="1b3", db=session)
