import random

import pytest
from faker import Faker
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fido_app.core.database import Base, get_db
from fido_app.main import app

fake = Faker()

TestingDB = "sqlite:///./db_test.sqlite3"

engine = create_engine(TestingDB)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

payment_types = ["credit_card", "mobile_money", "bank_transfer"]
transaction_status = ["completed", "pending", "failed"]
transaction_types = ["credit", "debit"]


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
        "user_id": random.randint(1, 100),
        "full_name": fake.name(),
        "date": fake.iso8601(tzinfo=None),
        "amount": random.randint(1_000, 10_000_000),
        "reference": fake.text(max_nb_chars=20),
        "transaction_type": random.choice(transaction_types),
        "payment_method": random.choice(payment_types),
        "transaction_status": random.choice(transaction_status),
    }


@pytest.fixture
def transaction_multiple_data():
    return [
        {
            "user_id": random.randint(1, 100),
            "full_name": fake.name(),
            "date": fake.iso8601(tzinfo=None),
            "amount": random.randint(1_000, 10_000_000),
            "reference": fake.text(max_nb_chars=20),
            "transaction_type": random.choice(transaction_types),
            "payment_method": random.choice(payment_types),
            "transaction_status": random.choice(transaction_status),
        },
        {
            "user_id": random.randint(1, 100),
            "full_name": fake.name(),
            "date": fake.iso8601(tzinfo=None),
            "amount": random.randint(1_000, 10_000_000),
            "reference": fake.text(max_nb_chars=20),
            "transaction_type": random.choice(transaction_types),
            "payment_method": random.choice(payment_types),
            "transaction_status": random.choice(transaction_status),
        },
        {
            "user_id": random.randint(1, 100),
            "full_name": fake.name(),
            "date": fake.iso8601(tzinfo=None),
            "amount": random.randint(1_000, 10_000_000),
            "reference": fake.text(max_nb_chars=20),
            "transaction_type": random.choice(transaction_types),
            "payment_method": random.choice(payment_types),
            "transaction_status": random.choice(transaction_status),
        },
        {
            "user_id": random.randint(1, 100),
            "full_name": fake.name(),
            "date": fake.iso8601(tzinfo=None),
            "amount": random.randint(1_000, 10_000_000),
            "reference": fake.text(max_nb_chars=20),
            "transaction_type": random.choice(transaction_types),
            "payment_method": random.choice(payment_types),
            "transaction_status": random.choice(transaction_status),
        },
        {
            "user_id": random.randint(1, 100),
            "full_name": fake.name(),
            "date": fake.iso8601(tzinfo=None),
            "amount": random.randint(1_000, 10_000_000),
            "reference": fake.text(max_nb_chars=20),
            "transaction_type": random.choice(transaction_types),
            "payment_method": random.choice(payment_types),
            "transaction_status": random.choice(transaction_status),
        },
        {
            "user_id": random.randint(1, 100),
            "full_name": fake.name(),
            "date": fake.iso8601(tzinfo=None),
            "amount": random.randint(1_000, 10_000_000),
            "reference": fake.text(max_nb_chars=20),
            "transaction_type": random.choice(transaction_types),
            "payment_method": random.choice(payment_types),
            "transaction_status": random.choice(transaction_status),
        },
        {
            "user_id": random.randint(1, 100),
            "full_name": fake.name(),
            "date": fake.iso8601(tzinfo=None),
            "amount": random.randint(1_000, 10_000_000),
            "reference": fake.text(max_nb_chars=20),
            "transaction_type": random.choice(transaction_types),
            "payment_method": random.choice(payment_types),
            "transaction_status": random.choice(transaction_status),
        },
        {
            "user_id": random.randint(1, 100),
            "full_name": fake.name(),
            "date": fake.iso8601(tzinfo=None),
            "amount": random.randint(1_000, 10_000_000),
            "reference": fake.text(max_nb_chars=20),
            "transaction_type": random.choice(transaction_types),
            "payment_method": random.choice(payment_types),
            "transaction_status": random.choice(transaction_status),
        },
        {
            "user_id": random.randint(1, 100),
            "full_name": fake.name(),
            "date": fake.iso8601(tzinfo=None),
            "amount": random.randint(1_000, 10_000_000),
            "reference": fake.text(max_nb_chars=20),
            "transaction_type": random.choice(transaction_types),
            "payment_method": random.choice(payment_types),
            "transaction_status": random.choice(transaction_status),
        },
        {
            "user_id": random.randint(1, 100),
            "full_name": fake.name(),
            "date": fake.iso8601(tzinfo=None),
            "amount": random.randint(1_000, 10_000_000),
            "reference": fake.text(max_nb_chars=20),
            "transaction_type": random.choice(transaction_types),
            "payment_method": random.choice(payment_types),
            "transaction_status": random.choice(transaction_status),
        },
    ]
