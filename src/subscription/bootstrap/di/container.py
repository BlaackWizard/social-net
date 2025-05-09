from dishka import make_async_container, AsyncContainer, Provider
from dishka.integrations.fastapi import FastapiProvider

from src.subscription.adapters.db.config_loader import SubDBConfig
from src.subscription.bootstrap.di.providers.adapters import subscription_adapter_provider
from src.subscription.bootstrap.di.providers.config import SubscriptionConfigProvider
from src.subscription.bootstrap.di.providers.gateway import SubscriptionGatewayProvider

from src.subscription.bootstrap.di.providers.interactors import SubscriptionInteractorProvider
from src.subscription.bootstrap.di.providers.shared_services import SharedServicesProvider

config = SubDBConfig.from_env()

def get_providers() -> list[Provider]:
    return [
        subscription_adapter_provider(),
        SubscriptionInteractorProvider(),
        SubscriptionGatewayProvider(),
        SubscriptionConfigProvider(),
        SharedServicesProvider(),
    ]

