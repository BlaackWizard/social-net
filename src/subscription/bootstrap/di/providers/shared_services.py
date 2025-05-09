from dishka import Provider, provide, Scope
from src.shared_services.adapters.gateway.user import SharedUserGatewayImpl
from src.shared_services.interfaces.gateway.user import SharedUserGateway

class SharedServicesProvider(Provider):
    component = "subscription"

    scope = Scope.REQUEST

    user_gateway = provide(SharedUserGatewayImpl, provides=SharedUserGateway)
