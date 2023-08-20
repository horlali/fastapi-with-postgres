from datetime import datetime

import pytest


@pytest.fixture(scope="function")
def transaction():
    return {
        "user_id": 1,
        "date": datetime.now().isoformat(),
        "date": "2023-08-20T13:16:27.541000",
        "amount": 100.0,
        "fee": 0.0,
        "tax": 0.0,
        "reference": "test",
        "type": "deposit",
        "payment_method": "credit_card",
        "status": "completed",
    }
