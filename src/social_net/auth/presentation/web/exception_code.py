from typing import Type, Dict

from fastapi import status

from social_net.auth.application.common.exceptions.base import ApplicationError
from social_net.auth.application.errors.jwt_errors import \
    ConfirmationTokenСorruptedError, ConfirmationTokenExpiredError
from social_net.auth.application.errors.user_errors import UserNotFoundError
from social_net.auth.application.errors.user_request import (
    IncorrectEmailData, InvalidPasswordError, PasswordsNotMatchError,
    UnauthorizedError, UserAlreadyExistsWithThisEmailError,
    UserNameIsOccupiedError)


def get_error_codes() -> Dict[Type[ApplicationError], int]:
    return {
        UserNotFoundError: status.HTTP_400_BAD_REQUEST,
        UserNameIsOccupiedError: status.HTTP_400_BAD_REQUEST,
        ConfirmationTokenСorruptedError: status.HTTP_400_BAD_REQUEST,
        IncorrectEmailData: status.HTTP_400_BAD_REQUEST,
        InvalidPasswordError: status.HTTP_400_BAD_REQUEST,
        UserAlreadyExistsWithThisEmailError: status.HTTP_400_BAD_REQUEST,
        PasswordsNotMatchError: status.HTTP_400_BAD_REQUEST,
        UnauthorizedError: status.HTTP_400_BAD_REQUEST,
        ConfirmationTokenExpiredError: status.HTTP_401_UNAUTHORIZED
    }
