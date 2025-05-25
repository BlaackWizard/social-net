from dishka import Provider, Scope, provide

from social_net.auth.adapters.config import Config
from social_net.auth.adapters.db.config_loader import AuthDBConfig
from social_net.auth.adapters.email_sender.config import (ConfirmationEmailConfig,
                                                   SMTPConfig)
from social_net.auth.application.common.jwt.config import ConfigJWT

config_data = Config.load_from_environment()


class AuthConfigProvider(Provider): # type: ignore[misc]
    component = "auth"
    scope = Scope.APP

    @provide # type: ignore[misc]
    def auth_db(self) -> AuthDBConfig:
        return config_data.db_config

    @provide # type: ignore[misc]
    def smtp_config(self) -> SMTPConfig:
        return config_data.smtp_config

    @provide # type: ignore[misc]
    def confirmation_email_config(self) -> ConfirmationEmailConfig:
        return config_data.confirmation_email_config

    @provide # type: ignore[misc]
    def jwt_config(self) -> ConfigJWT:
        return config_data.jwt
