from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AuthDBConfig:
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
