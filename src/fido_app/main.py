from fastapi import FastAPI

from fido_app.api.transactions.routes import transaction_router
from fido_app.core.config import settings
from fido_app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.TITLE,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    contact=settings.CONTACT,
    license_info=settings.LICENSE_INFO,
    docs_url=settings.DOCS_URL,
)

app.include_router(transaction_router, prefix="/transactions")
