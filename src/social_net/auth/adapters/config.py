import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

from social_net.auth.adapters.db.config_loader import AuthDBConfig
from social_net.auth.adapters.email_sender.config import (ConfirmationEmailConfig,
                                                   SMTPConfig)
from social_net.auth.application.common.jwt.config import ConfigJWT

env_path = Path(__file__).parent.parent.parent.parent / ".env.auth"
db_env_path = Path(__file__).parent.parent.parent.parent / ".env.db_config"


@dataclass(frozen=True)
class Config:
    db_config: AuthDBConfig
    confirmation_email_config: ConfirmationEmailConfig
    smtp_config: SMTPConfig
    jwt: ConfigJWT

    @classmethod
    def load_from_environment(cls: type["Config"]) -> "Config":
        load_dotenv(env_path)
        load_dotenv(db_env_path)

        db = AuthDBConfig(
            postgres_username=os.environ["AUTH_POSTGRES_USERNAME"],
            postgres_password=os.environ["AUTH_POSTGRES_PASSWORD"],
            postgres_host=os.environ["AUTH_POSTGRES_HOST"],
            postgres_port=int(os.environ["AUTH_POSTGRES_PORT"]),
            postgres_database=os.environ["AUTH_POSTGRES_DB"],
        )
        confirmation_email_config = ConfirmationEmailConfig(
            subject=os.environ.get('SUBJECT', 'no-reply'),
            confirmation_link=os.environ.get(
                'CONFIRMATION_LINK', 'localhost:8000/verify/'
            ),
            email_from=os.environ.get('no-reply@gmail.com'),
        )
        smtp_config = SMTPConfig(
            user=os.environ.get('SMTP_USER'),
            password=os.environ.get('SMTP_PASSWORD'),
            port=int(os.environ.get('SMTP_PORT', "587")),
            host=os.environ.get('SMTP_HOST'),
            use_tls=os.environ.get('SMTP_USE_TLS', 'False').lower() == 'true',
        )
        jwt = ConfigJWT(
            algorithm=os.environ.get('JWT_ALGORITHM', "HS256"),
            key=os.environ.get('JWT_SECRET_KEY'),
        )
        return cls(
            db_config=db,
            smtp_config=smtp_config,
            confirmation_email_config=confirmation_email_config,
            jwt=jwt,
        )
