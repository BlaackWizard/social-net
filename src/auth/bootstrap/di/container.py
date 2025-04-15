from dishka import make_async_container, AsyncContainer
from dishka.integrations.fastapi import FastapiProvider

from src.auth.adapters.config import Config
from src.auth.adapters.db.config_loader import DBConfig
from src.auth.adapters.email_sender.config import SMTPConfig, ConfirmationEmailConfig
from src.auth.application.common.jwt.config import ConfigJWT
from src.auth.bootstrap.di.providers.adapters import AdapterProvider
from src.auth.bootstrap.di.providers.connection import ConnectionProvider
from src.auth.bootstrap.di.providers.gateways import GatewayProvider
from src.auth.bootstrap.di.providers.interactors import InteractorProvider
from src.auth.bootstrap.di.providers.config import ConfigProvider

def get_async_container(
    config: Config
) -> AsyncContainer:
    container = make_async_container(
        FastapiProvider(),
        AdapterProvider(),
        GatewayProvider(),
        InteractorProvider(),
        ConfigProvider(),
        ConnectionProvider(),
        context={
            DBConfig: config.db_config,
            SMTPConfig: config.smtp_config,
            ConfirmationEmailConfig: config.confirmation_email_config,
            ConfigJWT: config.jwt
        }
    )
    return container
