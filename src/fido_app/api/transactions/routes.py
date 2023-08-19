from fastapi import APIRouter, Request

transaction_router = APIRouter()


@transaction_router.get("/")
def read_root(request: Request):
    client_host = request.client.host
    return {"client_host": client_host}
