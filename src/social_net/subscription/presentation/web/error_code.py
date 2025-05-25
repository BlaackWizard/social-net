from typing import Type, Dict

from fastapi import status

from social_net.subscription.application.exceptions.base import SubscriptionException
from social_net.subscription.application.exceptions.subscription import (
    AccessTokenOccurredError, FollowSelfForbidden, NotFoundUserError,
    SubscriptionAlreadyExists, SubscriptionNotExistsError)


def exception_codes() -> Dict[Type[SubscriptionException], int]:
    return {
        NotFoundUserError: status.HTTP_404_NOT_FOUND,
        AccessTokenOccurredError: status.HTTP_401_UNAUTHORIZED,
        SubscriptionAlreadyExists: status.HTTP_400_BAD_REQUEST,
        FollowSelfForbidden: status.HTTP_403_FORBIDDEN,
        SubscriptionNotExistsError: status.HTTP_400_BAD_REQUEST,
    }
