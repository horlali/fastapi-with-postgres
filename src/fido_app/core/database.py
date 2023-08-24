from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from fido_app.core.config import settings

engine = create_engine(settings.DATABASE_URL, max_overflow=0, pool_size=20)
Session = sessionmaker(bind=engine)

Base = declarative_base()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
