import os
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Any, Self

from dotenv import load_dotenv

env_path = Path(__file__).resolve().parents[4] / ".env.db_config"
load_dotenv(dotenv_path=env_path)


@dataclass(frozen=True, slots=True)
class SubDBConfig:
    postgres_username: str
    postgres_password: str
    postgres_host: str
    postgres_port: int
    postgres_db: str

    @staticmethod
    def load_data() -> Dict[str, Any]:
        return dict(
            postgres_username=os.environ['SUBSCRIPTION_POSTGRES_USERNAME'],
            postgres_password=os.environ['SUBSCRIPTION_POSTGRES_PASSWORD'],
            postgres_host=os.environ['SUBSCRIPTION_POSTGRES_HOST'],
            postgres_port=int(os.environ['SUBSCRIPTION_POSTGRES_PORT']),
            postgres_db=os.environ['SUBSCRIPTION_POSTGRES_DB'],
        )

    @classmethod
    def from_env(cls) -> Self:
        data = cls.load_data()
        return cls(**data)

    def postgres_connection(self) -> str:
        return (
            f"postgresql+asyncpg://{self.postgres_username}:"
            f"{self.postgres_password}@{self.postgres_host}:"
            f"{self.postgres_port}/{self.postgres_db}"
        )
