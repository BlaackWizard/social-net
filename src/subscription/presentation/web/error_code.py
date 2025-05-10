from fastapi import status

from src.subscription.application.exceptions.subscription import (
    AccessTokenOccurredError, FollowSelfForbidden, NotFoundUserError,
    SubscriptionAlreadyExists, SubscriptionNotExistsError)


def exception_codes() -> dict:
    return {
        NotFoundUserError: status.HTTP_404_NOT_FOUND,
        AccessTokenOccurredError: status.HTTP_401_UNAUTHORIZED,
        SubscriptionAlreadyExists: status.HTTP_400_BAD_REQUEST,
        FollowSelfForbidden: status.HTTP_403_FORBIDDEN,
        SubscriptionNotExistsError: status.HTTP_400_BAD_REQUEST,
    }
