from dishka import make_async_container
from src.subscription.bootstrap.di.container import get_providers as subscription_providers
from src.auth.bootstrap.di.container import get_providers as auth_providers


def get_container():
    sub = subscription_providers()
    auth = auth_providers()

    return make_async_container(
        *sub, *auth
    )
