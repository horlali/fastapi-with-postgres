from pathlib import Path

from pydantic import BaseSettings

description = """
RESTful API using FastAPI, focusing on transactions
and user interactions integral to the system.
"""


class Settings(BaseSettings):
    TITLE: str = "FIDO SERVICE CHALLENGE"
    VERSION: str = "0.1.0"
    RELEASE_ID: str = "0.0.1"
    DESCRIPTION = description
    LICENSE_INFO: dict = {
        "name": "MIT",
        "identifier": "MIT",
    }
    CONTACT: dict = {
        "name": "Gideon Ahiadzi",
        "email": "gideon.ahiadzi@gmail.com",
        "linkedin": "https://www.linkedin.com/in/ele7en",
    }

    DOCS_URL: str = "/"
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent

    class Config:
        case_sensitive = True


settings = Settings()
