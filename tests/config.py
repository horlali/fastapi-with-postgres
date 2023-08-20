from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import drop_database

from fido_app.core.database import Base, get_db
from fido_app.main import app


def get_test_db_url():
    return "sqlite:///./test.db"


def override_get_db():
    db_url = get_test_db_url()
    engine = create_engine(db_url)
    Base.metadata.create_all(bind=engine)
    session = Session(bind=engine)
    try:
        yield session
    finally:
        session.close()
        drop_database(get_test_db_url())


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)
