import os
from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TITLE: str = "Language Translator"
    API_V1_STR: str = "/api/v1"
    VERSION: str = "0.1.0"
    RELEASE_ID: str = "0.0.1"
    DESCRIPTION: str = "Text translation API base on Hugging Faces T5-Base Model"
    LICENSE_INFO: dict = {
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }
    CONTACT: dict = {
        "name": "Gideon Ahiadzi",
        "email": "gideon.ahiadzi@gmail.com",
        "linkedin": "https://www.linkedin.com/in/gideon-ahiadzi",
    }
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent

    class Config:
        case_sensitive = True


settings = Settings()
