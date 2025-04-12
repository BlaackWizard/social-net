from .common import ApplicationError


class PasswordsNotMatchError(ApplicationError):
    ...


class UserAlreadyExistsWithThisEmailError(ApplicationError):
    ...


class UserNameIsOccupiedError(ApplicationError):
    ...


class InvalidPasswordError(ApplicationError):
    ...


class UnauthorizedError(ApplicationError):
    ...


class IncorrectEmailData(ApplicationError):
    ...
