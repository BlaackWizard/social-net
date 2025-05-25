
from dishka import provide, Scope, Provider, from_context

from social_net.subscription.adapters.db.provider import get_engine, get_sessionmaker, get_session
from social_net.subscription.adapters.id_provider import HTTPRequestIdProvider, AuthClient
from fastapi import Request

from social_net.subscription.adapters.uow import UoWS
from social_net.subscription.application.common.id_provider import IdProvider
from social_net.subscription.application.common.uow import UoW


def provide_auth_client(_) -> AuthClient: # type: ignore[no-untyped-def]

    return AuthClient(base_url="http://localhost:8000")


class SubscriptionAdapterProvider(Provider): # type: ignore[misc]
    component = "subscription"

    scope = Scope.REQUEST

    auth_client = provide(provide_auth_client, scope=Scope.APP)
    request = from_context(Request, scope=Scope.REQUEST)
    id_provider = provide(HTTPRequestIdProvider, provides=IdProvider)
    uow = provide(UoWS, provides=UoW)

def subscription_adapter_provider() -> SubscriptionAdapterProvider:
    provider = SubscriptionAdapterProvider()
    provider.provide(get_engine, scope=Scope.APP)
    provider.provide(get_sessionmaker, scope=Scope.APP)
    provider.provide(get_session, scope=Scope.REQUEST)

    return provider
