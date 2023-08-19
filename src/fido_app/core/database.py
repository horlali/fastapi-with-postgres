from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from fido_app.core.config import settings

sqlite_file_name = "db.sqlite3"
sqlite_url = f"sqlite:///{settings.BASE_DIR}/{sqlite_file_name}"

engine = create_engine(sqlite_url)


Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
 