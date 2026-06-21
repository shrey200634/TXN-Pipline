from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database
    DATABASE_URL: str

    # Redis (Celery broker + result backend)
    REDIS_URL: str = "redis://redis:6379/0"

    # Kafka
    KAFKA_BOOTSTRAP_SERVERS: str = "kafka:9092"
    KAFKA_TOPIC: str = "txn-pipeline-events"

    # Gemini
    GEMINI_API_KEY: str

    # File upload
    UPLOAD_DIR: str = "/tmp/uploads"
    MAX_FILE_SIZE_MB: int = 10

    class Config:
        env_file = ".env"
        case_sensitive = True


# Single instance imported everywhere
settings = Settings()