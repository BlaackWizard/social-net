from uuid import UUID

from dishka import Provider, provide, Scope, from_context
from fastapi import Request

from src.auth.adapters.email_sender.email_client import EmailClientImpl, EmailClient
from src.auth.adapters.id_provider import TokenProvider, TokenBearerIdProvider
from src.auth.adapters.password_hasher import Argon2PasswordHasher
from src.auth.adapters.token_encoder import TokenEncoder
from src.auth.application.common.id_provider import IdProvider
from src.auth.application.common.password_hasher import PasswordHasher
from src.auth.application.common.token_sender import TokenSender
from src.auth.application.common.uow import UoW


class AdapterProvider(Provider):
    idp = provide(TokenProvider, scope=Scope.REQUEST)
    uid = from_context(UUID, scope=Scope.REQUEST)
    encoder = provide(TokenEncoder, scope=Scope.APP)
    request = from_context(Request, scope=Scope.REQUEST)
    email_client = provide(EmailClientImpl, provides=EmailClient, scope=Scope.REQUEST)
