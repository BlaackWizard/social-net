from dishka import Provider, Scope, WithParents, provide_all

from social_net.auth.adapters.gateway.user import UserGatewayImpl


class AuthGatewayProvider(Provider): # type: ignore[misc]
    component = "auth"
    scope = Scope.REQUEST

    provides = provide_all(
        WithParents[UserGatewayImpl],
    )
