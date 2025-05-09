from dishka import provide, Scope, Provider, from_context, AnyOf
from sqlalchemy.ext.asyncio import AsyncSession

from src.subscription.adapters.db.provider import get_engine, get_sessionmaker, get_session
from src.subscription.adapters.id_provider import HTTPRequestIdProvider, AuthClient
from fastapi import Request
from typing import cast

from src.subscription.adapters.uow import UoWS
from src.subscription.application.common.id_provider import IdProvider
from src.subscription.application.common.uow import UoW

def provide_auth_client(_) -> AuthClient:
    return AuthClient(base_url="http://localhost:8000")


class SubscriptionAdapterProvider(Provider):
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
