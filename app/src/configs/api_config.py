from pydantic_settings import BaseSettings


class APIConfig(BaseSettings):
    ORIGINS: list = ["http://localhost"]
