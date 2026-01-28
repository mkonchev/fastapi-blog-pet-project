import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    ALGORITHM = os.environ.get("ALGORITHM")
    ACCESS_TOKEN_EXPIRES = os.environ.get("ACCESS_TOKEN_EXPIRES")
    REFRESH_TOKEN_EXPIRES = os.environ.get("REFRESH_TOKEN_EXPIRES")


settings = Settings()
