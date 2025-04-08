import os
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DBConfig:
    postgres_username: str
    postgres_password: str
    postgres_host: str
    postgres_port: int
    postgres_database: str


    @property
    def postgres_conn_url(self) -> str:
        user = self.postgres_username
        password = self.postgres_password
        host = self.postgres_host
        db_name = self.postgres_database

        return f"postgresql+asyncpg://{user}:{password}@{host}/{db_name}"


@dataclass(frozen=True)
class Config:
    db_config: DBConfig

    @classmethod
    def load_from_environment(cls: type["Config"]) -> "Config":
        db = DBConfig(
            postgres_username=os.environ["POSTGRES_USERNAME"],
            postgres_password=os.environ["POSTGRES_PASSWORD"],
            postgres_host=os.environ["POSTGRES_HOST"],
            postgres_port=int(os.environ["POSTGRES_PORT"]),
            postgres_database=os.environ["POSTGRES_DATABASE"],
        )
        return cls(
            db_config=db,
        )
