from dishka import Provider

from social_net.subscription.adapters.db.config_loader import SubDBConfig
from social_net.subscription.bootstrap.di.providers.adapters import subscription_adapter_provider
from social_net.subscription.bootstrap.di.providers.config import SubscriptionConfigProvider
from social_net.subscription.bootstrap.di.providers.gateway import SubscriptionGatewayProvider

from social_net.subscription.bootstrap.di.providers.interactors import SubscriptionInteractorProvider
from social_net.subscription.bootstrap.di.providers.shared_services import SharedServicesProvider

config = SubDBConfig.from_env()

def get_providers() -> list[Provider]:
    return [
        subscription_adapter_provider(),
        SubscriptionInteractorProvider(),
        SubscriptionGatewayProvider(),
        SubscriptionConfigProvider(),
        SharedServicesProvider(),
    ]

