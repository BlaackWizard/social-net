from social_net.auth.application.common.exceptions.base import ApplicationError


class PasswordsNotMatchError(ApplicationError): # type: ignore[misc]
    ...


class UserAlreadyExistsWithThisEmailError(ApplicationError): # type: ignore[misc]
    ...


class UserNameIsOccupiedError(ApplicationError): # type: ignore[misc]
    ...


class InvalidPasswordError(ApplicationError): # type: ignore[misc]
    ...


class UnauthorizedError(ApplicationError): # type: ignore[misc]
    ...


class IncorrectEmailData(ApplicationError): # type: ignore[misc]
    ...
