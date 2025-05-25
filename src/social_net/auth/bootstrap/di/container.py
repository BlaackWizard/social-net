from dishka import Provider
from dishka.integrations.fastapi import FastapiProvider as AuthFastAPIProvider

from social_net.auth.bootstrap.di.providers.adapters import auth_adapter_provider
from social_net.auth.bootstrap.di.providers.config import AuthConfigProvider
from social_net.auth.bootstrap.di.providers.gateways import AuthGatewayProvider
from social_net.auth.bootstrap.di.providers.interactors import AuthInteractorProvider


def get_providers() -> list[Provider]:
    return [
        AuthFastAPIProvider(),
        auth_adapter_provider(),
        AuthGatewayProvider(),
        AuthInteractorProvider(),
        AuthConfigProvider(),
    ]
