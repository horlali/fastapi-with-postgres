import pytest

from fido_app.analytics.stats import user_average_transaction, user_max_transaction_day


def test_user_average_transaction_user_not_found(db_session):
    with pytest.raises(Exception):
        user_average_transaction(user_id=999)


def test_user_max_transaction_day_user_not_found(db_session):
    with pytest.raises(Exception):
        user_max_transaction_day(user_id=999)
