from social_net.subscription.application.exceptions.base import SubscriptionException


class NotFoundUserError(SubscriptionException): # type: ignore[misc]
    ...


class SubscriptionAlreadyExists(SubscriptionException): # type: ignore[misc]
    ...


class AccessTokenOccurredError(SubscriptionException): # type: ignore[misc]
    ...


class FollowSelfForbidden(SubscriptionException): # type: ignore[misc]
    ...

class SubscriptionNotExistsError(SubscriptionException): # type: ignore[misc]
    ...
