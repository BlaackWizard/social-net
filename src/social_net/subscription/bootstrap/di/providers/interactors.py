from dishka import Provider, Scope, provide_all

from social_net.subscription.application.all_followers import AllFollowers
from social_net.subscription.application.follow import Follow
from social_net.subscription.application.unfollow import UnFollow


class SubscriptionInteractorProvider(Provider): # type: ignore[misc]
    component = "subscription"

    scope = Scope.REQUEST
    provides = provide_all(
        Follow,
        UnFollow,
        AllFollowers,
    )
