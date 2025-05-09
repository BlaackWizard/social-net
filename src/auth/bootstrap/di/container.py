from dishka import Provider
from dishka.integrations.fastapi import FastapiProvider as AuthFastAPIProvider

from src.auth.bootstrap.di.providers.adapters import auth_adapter_provider
from src.auth.bootstrap.di.providers.config import AuthConfigProvider
from src.auth.bootstrap.di.providers.gateways import AuthGatewayProvider
from src.auth.bootstrap.di.providers.interactors import AuthInteractorProvider


def get_providers() -> list[Provider]:
    return [
        AuthFastAPIProvider(),
        auth_adapter_provider(),
        AuthGatewayProvider(),
        AuthInteractorProvider(),
        AuthConfigProvider(),
    ]
