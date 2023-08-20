from tests.config import client


def test_create_transaction(transaction):
    url = "/api/v1/transactions/"
    response = client.post(url, json=transaction)

    assert response.status_code == 200

    created_transaction = response.json()
    assert created_transaction["user_id"] == transaction["user_id"]
    assert created_transaction["date"] == transaction["date"]
    assert created_transaction["fee"] == transaction["fee"]
    assert created_transaction["tax"] == transaction["tax"]
    assert created_transaction["type"] == transaction["type"]
    assert created_transaction["amount"] == transaction["amount"]
    assert created_transaction["reference"] == transaction["reference"]
    assert created_transaction["payment_method"] == transaction["payment_method"]
    assert created_transaction["status"] == transaction["status"]
