from dishka import Provider, provide, Scope

from src.subscription.adapters.id_provider import HTTPRequestIdProvider
from src.subscription.application.common.id_provider import IdProvider
from src.subscription.application.follow import Follow

class SubscriptionInteractorProvider(Provider):
    component = "subscription"

    scope = Scope.REQUEST
    follow = provide(Follow)

