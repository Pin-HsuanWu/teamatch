import os
import sys

import loguru
from pydantic import BaseSettings


class Settings(BaseSettings):
    # database
    DATABASE_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_HOSTNAME: str

    class Config:
        env_file = "./.env"


settings = Settings()
