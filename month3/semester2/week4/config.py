from pydantic import BaseSettings, HttpUrl


class Settings(BaseSettings):
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    SENTRY_DSN: HttpUrl
    MONGO_DB_CONNECTION_URI: str
    JWT_ALGORITHM: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
