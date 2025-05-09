from dishka import Provider, Scope, provide

from src.auth.adapters.config import Config
from src.auth.adapters.db.config_loader import AuthDBConfig
from src.auth.adapters.email_sender.config import (ConfirmationEmailConfig,
                                                   SMTPConfig)
from src.auth.application.common.jwt.config import ConfigJWT

config_data = Config.load_from_environment()


class AuthConfigProvider(Provider):
    component = "auth"
    scope = Scope.APP

    @provide
    def auth_db(self) -> AuthDBConfig:
        return config_data.db_config

    @provide
    def smtp_config(self) -> SMTPConfig:
        return config_data.smtp_config

    @provide
    def confirmation_email_config(self) -> ConfirmationEmailConfig:
        return config_data.confirmation_email_config

    @provide
    def jwt_config(self) -> ConfigJWT:
        return config_data.jwt
