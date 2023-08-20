from fastapi import APIRouter, Depends, HTTPException

from fido_app.analytics.maths import user_average_transaction, user_max_transaction_day
from fido_app.api.transactions.models import TransactionDB
from fido_app.api.transactions.schemas import (
    TransactionCreate,
    TransactionSchema,
    TransactionUpdate,
    UserStats,
)
from fido_app.core.database import Session, get_db

transaction_router = APIRouter()


@transaction_router.post("/transactions/", response_model=TransactionSchema)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    db_transaction = TransactionDB(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


@transaction_router.get(
    "/transactions/{transaction_id}", response_model=TransactionSchema
)
def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    db_transaction = (
        db.query(TransactionDB).filter(TransactionDB.id == transaction_id).first()
    )
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return db_transaction


@transaction_router.get("/transactions/", response_model=list[TransactionSchema])
def read_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    transactions = db.query(TransactionDB).offset(skip).limit(limit).all()
    return transactions


@transaction_router.put(
    "/transactions/{transaction_id}", response_model=TransactionSchema
)
def update_transaction(
    transaction_id: int,
    transaction: TransactionUpdate,
    db: Session = Depends(get_db),
):
    db_transaction = (
        db.query(TransactionDB).filter(TransactionDB.id == transaction_id).first()
    )
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    for field, value in transaction:
        setattr(db_transaction, field, value)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


@transaction_router.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    db_transaction = (
        db.query(TransactionDB).filter(TransactionDB.id == transaction_id).first()
    )
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    db.delete(db_transaction)
    db.commit()
    return {"message": "Transaction deleted successfully"}


@transaction_router.get("/users/{user_id}/stats", response_model=UserStats)
def get_user_stats(user_id: int, db: Session = Depends(get_db)):
    return UserStats(
        average_transaction_value=user_average_transaction(user_id),
        day_with_highest_transactions=user_max_transaction_day(user_id),
    )
