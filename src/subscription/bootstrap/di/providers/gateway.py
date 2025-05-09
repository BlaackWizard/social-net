from dishka import WithParents, Provider, Scope, provide_all
from src.subscription.adapters.gateway import SubscriptionGatewayImpl


class SubscriptionGatewayProvider(Provider):
    component = "subscription"
    scope = Scope.REQUEST

    provides = provide_all(
        WithParents[SubscriptionGatewayImpl]
    )
