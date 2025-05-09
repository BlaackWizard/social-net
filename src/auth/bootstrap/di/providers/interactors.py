from dishka import Provider, Scope, provide, provide_all

from src.auth.adapters.email_sender.confirmation_token_sender import \
    ConfirmationTokenSender
from src.auth.adapters.id_provider import TokenBearerIdProvider, TokenProvider
from src.auth.adapters.password_hasher import Argon2PasswordHasher
from src.auth.application.authorize_user import AuthorizeUser
from src.auth.application.common.id_provider import IdProvider
from src.auth.application.common.jwt.access_token_processor import \
    AccessTokenProcessor
from src.auth.application.common.jwt.confirmation_token_processor import \
    ConfirmationTokenProcessor
from src.auth.application.common.password_hasher import PasswordHasher
from src.auth.application.common.token_sender import TokenSender
from src.auth.application.delete_user import DeleteUser
from src.auth.application.me import Me
from src.auth.application.register_user import RegisterUser
from src.auth.application.verify_user import VerifyUser


class AuthInteractorProvider(Provider):
    component = "auth"

    scope = Scope.REQUEST

    id_provider = provide(TokenProvider, provides=IdProvider, scope=Scope.REQUEST)
    confirmation_token_processor = provide(
        ConfirmationTokenProcessor,
        scope=Scope.REQUEST,
    )
    password_hasher = provide(
        Argon2PasswordHasher,
        provides=PasswordHasher,
        scope=Scope.REQUEST,
    )
    token_bearer_parser = provide(TokenBearerIdProvider, scope=Scope.REQUEST)
    token_sender = provide(
        ConfirmationTokenSender,
        provides=TokenSender,
        scope=Scope.REQUEST,
    )
    access_token_processor = provide(AccessTokenProcessor, scope=Scope.APP)

    provides = provide_all(
        DeleteUser,
        RegisterUser,
        VerifyUser,
        AuthorizeUser,
        Me,
    )
