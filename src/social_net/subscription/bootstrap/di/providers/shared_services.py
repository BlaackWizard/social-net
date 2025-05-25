from dishka import Provider, provide, Scope
from social_net.shared_services.adapters.gateway.user import SharedUserGatewayImpl
from social_net.shared_services.interfaces.gateway.user import SharedUserGateway

class SharedServicesProvider(Provider): # type: ignore[misc]
    component = "subscription"

    scope = Scope.REQUEST

    user_gateway = provide(SharedUserGatewayImpl, provides=SharedUserGateway)
