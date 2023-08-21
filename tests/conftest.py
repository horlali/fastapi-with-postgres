import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fido_app.core.database import Base

engine = create_engine("sqlite:///./test.db")
Base.metadata.create_all(bind=engine)


@pytest.fixture(scope="function")
def transaction():
    return {
        "user_id": 1,
        "date": "2023-08-20T13:16:27.541000",
        "amount": 100.0,
        "fee": 0.0,
        "tax": 0.0,
        "reference": "test",
        "transaction_type": "deposit",
        "payment_method": "credit_card",
        "transaction_status": "completed",
    }


@pytest.fixture
def db_session():
    connection = engine.connect()
    transaction = connection.begin()

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()
