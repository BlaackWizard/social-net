from dishka import Provider, Scope, provide_all, from_context

from src.auth.adapters.db.config_loader import DBConfig
from src.auth.adapters.email_sender.config import SMTPConfig, ConfirmationEmailConfig
from src.auth.application.common.jwt.config import ConfigJWT


class ConfigProvider(Provider):
    scope = Scope.APP

    configs = provide_all(
        from_context(DBConfig),
        from_context(SMTPConfig),
        from_context(ConfirmationEmailConfig),
        from_context(ConfigJWT),
    )
