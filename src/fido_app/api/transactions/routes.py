from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from fido_app.analytics.stats import user_average_transaction, user_highest_transaction
from fido_app.api.transactions.models import TransactionDB
from fido_app.api.transactions.schemas import (
    TransactionCreate,
    TransactionSchema,
    TransactionUpdate,
    UserStats,
)
from fido_app.core.database import get_db
from fido_app.utils.extentions import UserNotFoundError

transaction_router = APIRouter()


@transaction_router.post("/transactions/", response_model=TransactionSchema)
async def create_transaction(
    transaction: TransactionCreate, db: Session = Depends(get_db)
):
    db_transaction = TransactionDB(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)

    return db_transaction


@transaction_router.get(
    "/transactions/{transaction_id}", response_model=TransactionSchema
)
async def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    db_transaction = db.query(TransactionDB).filter_by(id=transaction_id).first()

    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return db_transaction


@transaction_router.get("/transactions/", response_model=list[TransactionSchema])
async def read_transactions(
    offset: int = 0, limit: int = 10, db: Session = Depends(get_db)
):
    return db.query(TransactionDB).offset(offset).limit(limit).all()


@transaction_router.patch(
    "/transactions/{transaction_id}", response_model=TransactionSchema
)
async def update_transaction(
    transaction_id: int,
    transaction: TransactionUpdate,
    db: Session = Depends(get_db),
):
    db_transaction = db.query(TransactionDB).filter_by(id=transaction_id).first()

    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")

    for field, value in transaction:
        if value is not None:
            setattr(db_transaction, field, value)

    db.commit()
    db.refresh(db_transaction)

    return db_transaction


@transaction_router.delete("/transactions/{transaction_id}")
async def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    db_transaction = db.query(TransactionDB).filter_by(id=transaction_id).first()

    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")

    db.delete(db_transaction)
    db.commit()

    return {"message": "Transaction deleted successfully"}


@transaction_router.get("/analytics/{user_id}", response_model=UserStats)
async def get_user_stats(user_id: int, db: Session = Depends(get_db)):
    try:
        return UserStats(
            average_transaction_value=user_average_transaction(user_id, db),
            highest_transaction=user_highest_transaction(user_id, db),
        )

    except UserNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
