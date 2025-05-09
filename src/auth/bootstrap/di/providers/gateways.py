from dishka import Provider, Scope, WithParents, provide_all

from src.auth.adapters.gateway.user import UserGatewayImpl


class AuthGatewayProvider(Provider):
    component = "auth"
    scope = Scope.REQUEST

    provides = provide_all(
        WithParents[UserGatewayImpl],
    )
