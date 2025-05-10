from src.subscription.application.exceptions.base import SubscriptionException


class NotFoundUserError(SubscriptionException):
    ...


class SubscriptionAlreadyExists(SubscriptionException):
    ...


class AccessTokenOccurredError(SubscriptionException):
    ...


class FollowSelfForbidden(SubscriptionException):
    ...

class SubscriptionNotExistsError(SubscriptionException):
    ...
