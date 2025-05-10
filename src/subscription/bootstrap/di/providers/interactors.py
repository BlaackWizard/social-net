from dishka import Provider, provide, Scope, provide_all

from src.subscription.adapters.id_provider import HTTPRequestIdProvider
from src.subscription.application.all_followers import AllFollowers
from src.subscription.application.common.id_provider import IdProvider
from src.subscription.application.follow import Follow
from src.subscription.application.unfollow import UnFollow


class SubscriptionInteractorProvider(Provider):
    component = "subscription"

    scope = Scope.REQUEST
    provides = provide_all(
        Follow,
        UnFollow,
        AllFollowers,
    )
