from dotenv import load_dotenv
import os
from dataclasses import dataclass

from src.auth.adapters.db.config_loader import DBConfig
from src.auth.adapters.email_sender.config import ConfirmationEmailConfig, SMTPConfig
from src.auth.application.common.jwt.config import ConfigJWT


@dataclass(frozen=True)
class Config:
    db_config: DBConfig
    confirmation_email_config: ConfirmationEmailConfig
    smtp_config: SMTPConfig
    jwt: ConfigJWT

    @classmethod
    def load_from_environment(cls: type["Config"]) -> "Config":
        load_dotenv()

        db = DBConfig(
            postgres_username=os.environ["POSTGRES_USERNAME"],
            postgres_password=os.environ["POSTGRES_PASSWORD"],
            postgres_host=os.environ["POSTGRES_HOST"],
            postgres_port=int(os.environ["POSTGRES_PORT"]),
            postgres_database=os.environ["POSTGRES_DATABASE"],
        )
        confirmation_email_config = ConfirmationEmailConfig(
            subject=os.environ.get('SUBJECT'),
            confirmation_link=os.environ.get('CONFIRMATION_LINK'),
            email_from=os.environ.get('EMAIL_FROM')
        )
        smtp_config = SMTPConfig(
            user=os.environ.get('SMTP_USER'),
            password=os.environ.get('SMTP_PASSWORD'),
            port=int(os.environ.get('SMTP_PORT')),
            host=os.environ.get('SMTP_HOST'),
            use_tls=os.environ.get('SMTP_USE_TLS', 'False').lower() == 'true'
        )
        jwt = ConfigJWT(
            algorithm=os.environ.get('JWT_ALGORITHM'),
            key=os.environ.get('JWT_SECRET_KEY')
        )
        return cls(
            db_config=db,
            smtp_config=smtp_config,
            confirmation_email_config=confirmation_email_config,
            jwt=jwt
        )
