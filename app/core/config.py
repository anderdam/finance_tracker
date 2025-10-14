from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    attachments_dir: str = "/data/attachments"

    class Config:
        env_file = ".env"


settings = Settings(database_url="database_url", attachments_dir="attachments_dir")
