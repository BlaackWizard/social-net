from dishka import WithParents, Provider, Scope, provide_all
from social_net.subscription.adapters.gateway import SubscriptionGatewayImpl


class SubscriptionGatewayProvider(Provider): # type: ignore[misc]
    component = "subscription"
    scope = Scope.REQUEST

    provides = provide_all(
        WithParents[SubscriptionGatewayImpl]
    )
