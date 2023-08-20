from tests.config import client


def test_create_transaction():
    url = "/api/v1/transactions/"

    transaction = {
        "user_id": 1,
        "date": "2023-08-20T13:16:27.541Z",
        "amount": 100.0,
        "fee": 0.0,
        "tax": 0.0,
        "reference": "test",
        "type": "deposit",
        "payment_method": "credit_card",
        "status": "completed",
    }

    response = client.post(url, json=transaction)

    assert response.status_code == 200

    created_transaction = response.json()
    assert created_transaction["user_id"] == transaction["user_id"]
    assert created_transaction["fee"] == transaction["fee"]
    assert created_transaction["tax"] == transaction["tax"]
    assert created_transaction["type"] == transaction["type"]
    assert created_transaction["amount"] == transaction["amount"]
    assert created_transaction["reference"] == transaction["reference"]
    assert created_transaction["payment_method"] == transaction["payment_method"]
    assert created_transaction["status"] == transaction["status"]
