from dishka import WithParents, Provider, Scope, provide_all
from src.auth.adapters.gateway.user import UserGatewayImpl

class GatewayProvider(Provider):
    scope = Scope.REQUEST

    provides = provide_all(
        WithParents[UserGatewayImpl]
    )
