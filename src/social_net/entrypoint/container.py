from dishka import make_async_container, AsyncContainer
from social_net.subscription.bootstrap.di.container import get_providers as subscription_providers
from social_net.auth.bootstrap.di.container import get_providers as auth_providers


def get_container() -> AsyncContainer:
    sub = subscription_providers()
    auth = auth_providers()

    return make_async_container(
        *sub, *auth
    )
