
from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # database configurations
    DATABASE_URL: Optional[str] = None
    RABBITMQ_PORT: Optional[str] = None
    RABBITMQ_USER: Optional[str] = None
    RABBITMQ_PASS: Optional[str] = None
    RABBITMQ_HOST: Optional[str] = None
    RABBITMQ_VHOST: Optional[str] = None

    # JWT
    secret_key: str = "secret"
    algorithm: str = "HS256"

    class Config:
        env_file = ".env.docker-compose.fastapi"
        from_attributes = True