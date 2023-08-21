# import pytest


def test_create_transaction(client, transaction_data):
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
