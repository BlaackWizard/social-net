from src.subscription.application.exceptions.subscription import (
    AccessTokenOccurredError, FollowSelfForbidden, NotFoundUserError,
    SubscriptionAlreadyExists, SubscriptionNotExistsError)


def exception_messages() -> dict:
    return {
        NotFoundUserError: "Пользователь не найден",
        AccessTokenOccurredError: "Токен поврежден",
        SubscriptionAlreadyExists: "Вы уже подписаны на этого пользователя",
        FollowSelfForbidden: "Запрещено подписываться на себя",
        SubscriptionNotExistsError: "Вы не подписаны на данный аккаунт!",
    }
