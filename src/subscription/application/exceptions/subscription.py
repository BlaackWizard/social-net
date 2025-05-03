from src.subscription.application.exceptions.base import SubscriptionException


class NotFoundUserError(SubscriptionException):
    message = "Пользователь не найден"

class SubscriptionAlreadyExists(SubscriptionException):
    message = "Вы уже подписаны на данного пользователя"
