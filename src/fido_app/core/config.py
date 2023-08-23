import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseSettings

ROOT_DIR: Path = Path(__file__).resolve().parent.parent.parent.parent
load_dotenv(os.path.join(ROOT_DIR, ".env.dev"))

description = """
RESTful API using FastAPI, focusing on transactions
and user interactions integral to the system.
"""


class Settings(BaseSettings):
    TITLE: str = "FIDO SERVICE CHALLENGE"
    API_PREFIX: str = "/api/v1"
    VERSION: str = "0.1.0"
    RELEASE_ID: str = "0.0.1"
    DESCRIPTION = description
    LICENSE_INFO: dict = {
        "name": "MIT",
        "identifier": "MIT",
    }
    CONTACT: dict = {
        "name": "ele7en",
        "email": "ele7en@example.com",
        "linkedin": "https://www.linkedin.com/in/ele7en",
    }

    DOCS_URL: str = "/"
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    class Config:
        case_sensitive = True


settings = Settings()
