from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv()


class AppConfig(BaseSettings):
    postgres_dsn: str
    polling_delay_seconds: int = 10
    kafka_broker: str
    device_topic: str

config = AppConfig()
