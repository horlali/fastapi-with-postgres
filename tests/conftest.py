import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fido_app.core.database import Base, get_db
from fido_app.main import app

TestingDB = "sqlite:///./db_test.sqlite3"

engine = create_engine(TestingDB)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def session():
    Base.metadata.create_all(engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(engine)


@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture
def transaction_data():
    return {
        "user_id": 1,
        "date": "2023-08-21T11:37:21.630000",
        "amount": 45000,
        "reference": "123456789",
        "transaction_type": "deposit",
        "payment_method": "credit_card",
        "transaction_status": "completed",
    }


@pytest.fixture
def transaction_multiple_data():
    return [
        {
            "user_id": 1,
            "date": "2023-01-21T11:37:21.630000",
            "amount": 245000,
            "reference": "Payment for lunch",
            "transaction_type": "deposit",
            "payment_method": "credit_card",
            "transaction_status": "completed",
        },
        {
            "user_id": 1,
            "date": "2023-02-21T11:37:21.630000",
            "amount": 105000,
            "reference": "Payment for lunch",
            "transaction_type": "deposit",
            "payment_method": "credit_card",
            "transaction_status": "completed",
        },
        {
            "user_id": 1,
            "date": "2023-03-21T11:37:21.630000",
            "amount": 125000,
            "reference": "Payment for lunch",
            "transaction_type": "deposit",
            "payment_method": "credit_card",
            "transaction_status": "completed",
        },
        {
            "user_id": 1,
            "date": "2023-04-21T11:37:21.630000",
            "amount": 145000,
            "reference": "Payment for lunch",
            "transaction_type": "deposit",
            "payment_method": "credit_card",
            "transaction_status": "completed",
        },
        {
            "user_id": 1,
            "date": "2023-05-21T11:37:21.630000",
            "amount": 160000,
            "reference": "Payment for lunch",
            "transaction_type": "deposit",
            "payment_method": "credit_card",
            "transaction_status": "completed",
        },
        {
            "user_id": 1,
            "date": "2023-06-21T11:37:21.630000",
            "amount": 185000,
            "reference": "Payment for lunch",
            "transaction_type": "deposit",
            "payment_method": "credit_card",
            "transaction_status": "completed",
        },
        {
            "user_id": 1,
            "date": "2023-07-21T11:37:21.630000",
            "amount": 225000,
            "reference": "Payment for lunch",
            "transaction_type": "deposit",
            "payment_method": "credit_card",
            "transaction_status": "completed",
        },
        {
            "user_id": 1,
            "date": "2023-10-21T11:37:21.630000",
            "amount": 85000,
            "reference": "Payment for lunch",
            "transaction_type": "deposit",
            "payment_method": "credit_card",
            "transaction_status": "completed",
        },
        {
            "user_id": 1,
            "date": "2023-11-21T11:37:21.630000",
            "amount": 65000,
            "reference": "123456789",
            "transaction_type": "deposit",
            "payment_method": "credit_card",
            "transaction_status": "completed",
        },
        {
            "user_id": 1,
            "date": "2023-12-21T11:37:21.630000",
            "amount": 45000,
            "reference": "Sweet Momma",
            "transaction_type": "deposit",
            "payment_method": "credit_card",
            "transaction_status": "completed",
        },
    ]
