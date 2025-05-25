from typing import Dict, Type

from social_net.subscription.application.exceptions.base import SubscriptionException
from social_net.subscription.application.exceptions.subscription import (
    AccessTokenOccurredError, FollowSelfForbidden, NotFoundUserError,
    SubscriptionAlreadyExists, SubscriptionNotExistsError)


def exception_messages() -> Dict[Type[SubscriptionException], str]:
    return {
        NotFoundUserError: "Пользователь не найден",
        AccessTokenOccurredError: "Токен поврежден",
        SubscriptionAlreadyExists: "Вы уже подписаны на этого пользователя",
        FollowSelfForbidden: "Запрещено подписываться на себя",
        SubscriptionNotExistsError: "Вы не подписаны на данный аккаунт!",
    }
