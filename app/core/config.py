from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://nevermind:nevermind@db:5432/nevermind"
    REDIS_URL: str = "redis://redis:6379/0"
    APP_NAME: str = "NeverMind"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()