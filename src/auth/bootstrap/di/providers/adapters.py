from uuid import UUID

from dishka import AnyOf, Provider, Scope, from_context, provide
from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.adapters.db.provider import (get_engine, get_session,
                                           get_sessionmaker)
from src.auth.adapters.email_sender.email_client import (EmailClient,
                                                         EmailClientImpl)
from src.auth.adapters.id_provider import TokenProvider
from src.auth.adapters.token_encoder import TokenEncoder
from src.auth.application.common.uow import UoW


class AuthAdapterProvider(Provider):
    component = "auth"

    idp = provide(TokenProvider, scope=Scope.REQUEST)
    uid = from_context(UUID, scope=Scope.REQUEST)
    encoder = provide(TokenEncoder, scope=Scope.APP)
    request = from_context(Request, scope=Scope.REQUEST)
    email_client = provide(EmailClientImpl, provides=EmailClient, scope=Scope.REQUEST)


def auth_adapter_provider() -> AuthAdapterProvider:
    provider = AuthAdapterProvider()
    provider.provide(get_engine, scope=Scope.APP)
    provider.provide(get_sessionmaker, scope=Scope.APP)
    provider.provide(
        get_session,
        provides=AnyOf[AsyncSession, UoW],
        scope=Scope.REQUEST,
    )

    return provider
