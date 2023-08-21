from typing import Dict, List

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from fido_app.api.transactions.models import TransactionDB
from fido_app.api.transactions.schemas import TransactionCreate


def test_create_transaction(
    client: TestClient, transaction_data: Dict, session: Session
):
    url = "/api/v1/transactions/"
    response = client.post(url, json=transaction_data)

    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["user_id"] == transaction_data["user_id"]
    assert response.json()["date"] == transaction_data["date"]
    assert response.json()["amount"] == transaction_data["amount"]
    assert response.json()["reference"] == transaction_data["reference"]
    assert response.json()["transaction_type"] == transaction_data["transaction_type"]
    assert response.json()["payment_method"] == transaction_data["payment_method"]
    assert (
        response.json()["transaction_status"] == transaction_data["transaction_status"]
    )

    assert "fee" in response.json()
    assert "tax" in response.json()

    # Check that the transaction was saved to the database
    transaction = session.query(TransactionDB).filter_by(id=1).first()
    assert transaction is not None
    assert transaction.user_id == transaction_data["user_id"]
    assert transaction.amount == transaction_data["amount"]
    assert transaction.reference == transaction_data["reference"]
    assert transaction.transaction_type == transaction_data["transaction_type"]
    assert transaction.payment_method == transaction_data["payment_method"]
    assert transaction.transaction_status == transaction_data["transaction_status"]
    assert transaction.fee == response.json()["fee"]
    assert transaction.tax == response.json()["tax"]


def test_cannot_create_transaction_without_data(client: TestClient):
    url = "/api/v1/transactions/"
    response = client.post(url)

    assert response.status_code == 422


def test_cannot_create_transaction_with_invalid_data(client: TestClient):
    url = "/api/v1/transactions/"
    response = client.post(url, json={"amount": "-24000"})

    assert response.status_code == 422


def test_read_transaction(client: TestClient, transaction_data: Dict, session: Session):
    data = TransactionCreate(**transaction_data)
    transaction = TransactionDB(**data.dict())
    session.add(transaction)
    session.commit()

    url = f"/api/v1/transactions/{transaction.id}"
    response = client.get(url)

    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["user_id"] == transaction_data["user_id"]
    assert response.json()["date"] == transaction_data["date"]
    assert response.json()["amount"] == transaction_data["amount"]
    assert response.json()["reference"] == transaction_data["reference"]
    assert response.json()["transaction_type"] == transaction_data["transaction_type"]
    assert response.json()["payment_method"] == transaction_data["payment_method"]
    assert (
        response.json()["transaction_status"] == transaction_data["transaction_status"]
    )

    assert "fee" in response.json()
    assert "tax" in response.json()


def test_read_transaction_not_found(client: TestClient):
    url = "/api/v1/transactions/9999"
    response = client.get(url)

    assert response.status_code == 404


def test_read_transaction_invalid_id(client: TestClient):
    url = "/api/v1/transactions/1b3"
    response = client.get(url)

    assert response.status_code == 422


def test_read_transactions(
    client: TestClient, transaction_multiple_data: List, session: Session
):
    data = [TransactionCreate(**item) for item in transaction_multiple_data]
    transactions = [TransactionDB(**item.dict()) for item in data]
    session.add_all(transactions)
    session.commit()

    url = "/api/v1/transactions/"
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.json()) == len(transaction_multiple_data)


def test_read_transactions_with_pagination(
    client: TestClient, transaction_multiple_data: List, session: Session
):
    data = [TransactionCreate(**item) for item in transaction_multiple_data]
    transactions = [TransactionDB(**item.dict()) for item in data]
    session.add_all(transactions)
    session.commit()

    skip, limit = (0, 5)
    url = f"/api/v1/transactions/?skip={skip}&limit={limit}"
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.json()) == 5


def test_read_transactions_with_invalid_pagination(client: TestClient):
    skip, limit = ("a", "b")
    url = f"/api/v1/transactions/?skip={skip}&limit={limit}"
    response = client.get(url)

    assert response.status_code == 422


def test_update_transaction(
    client: TestClient, transaction_data: Dict, session: Session
):
    data = TransactionCreate(**transaction_data)
    transaction = TransactionDB(**data.dict())
    session.add(transaction)
    session.commit()

    url = f"/api/v1/transactions/{transaction.id}"
    response = client.patch(url, json={"transaction_status": "pending", "amount": 100})

    assert response.status_code == 200
    assert response.json()["amount"] == 100
    assert response.json()["transaction_status"] == "pending"

    assert "fee" in response.json()
    assert "tax" in response.json()

    # Check that the transaction was updated in the database
    transaction = session.query(TransactionDB).filter_by(id=1).first()
    assert transaction is not None
    assert transaction.amount == 100
    assert transaction.transaction_status == "pending"
    assert transaction.fee == transaction.calculate_fee()
    assert transaction.tax == transaction.calculate_tax()


def test_cannot_update_transaction_with_invalid_data(
    client: TestClient, transaction_data: Dict, session: Session
):
    data = TransactionCreate(**transaction_data)
    transaction = TransactionDB(**data.dict())
    session.add(transaction)
    session.commit()

    url = f"/api/v1/transactions/{transaction.id}"
    response = client.patch(url, json={"amount": -100})

    assert response.status_code == 422


def test_cannot_update_transaction_not_found(client: TestClient):
    url = "/api/v1/transactions/9999"
    response = client.patch(url, json={"transaction_status": "pending"})

    assert response.status_code == 404


def test_cannot_update_transaction_invalid_id(client: TestClient):
    url = "/api/v1/transactions/1b3"
    response = client.patch(url, json={"transaction_status": "pending"})

    assert response.status_code == 422


def test_delete_transaction(
    client: TestClient, transaction_data: Dict, session: Session
):
    data = TransactionCreate(**transaction_data)
    transaction = TransactionDB(**data.dict())
    session.add(transaction)
    session.commit()

    url = f"/api/v1/transactions/{transaction.id}"
    response = client.delete(url)

    assert response.status_code == 200

    # Check that the transaction was deleted from the database
    transaction = session.query(TransactionDB).filter_by(id=1).first()
    assert transaction is None


def test_cannot_delete_transaction_not_found(client: TestClient):
    url = "/api/v1/transactions/9999"
    response = client.delete(url)

    assert response.status_code == 404


def test_cannot_delete_transaction_invalid_id(client: TestClient):
    url = "/api/v1/transactions/1b3"
    response = client.delete(url)

    assert response.status_code == 422
