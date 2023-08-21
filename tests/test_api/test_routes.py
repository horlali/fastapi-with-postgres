from typing import Dict

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from fido_app.api.transactions.models import TransactionDB


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
