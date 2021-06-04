from pydantic import BaseSettings


class Settings(BaseSettings):
    db_driver: str = "postgresql"
    postgres_db: str = "zaim_test"
    postgres_host: str = "db"
    postgres_port: str = "5432"
    postgres_user: str = "your_name"
    postgres_password: str = "your_password"


settings = Settings()
