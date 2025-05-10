from src.auth.application.errors.jwt_errors import \
    ConfirmationTokenСorruptedError, ConfirmationTokenExpiredError
from src.auth.application.errors.user_errors import UserNotFoundError
from src.auth.application.errors.user_request import (
    IncorrectEmailData, InvalidPasswordError, PasswordsNotMatchError,
    UnauthorizedError, UserAlreadyExistsWithThisEmailError,
    UserNameIsOccupiedError)


def get_error_messages() -> dict:
    return {
        UserNotFoundError: "Пользователь не найден.",
        UserNameIsOccupiedError: "Имя пользователя уже занят.",
        ConfirmationTokenСorruptedError: "Токен подтверждения поврежден.",
        IncorrectEmailData: "Неправильный e-mail!",
        InvalidPasswordError: "Неправильный пароль!",
        UserAlreadyExistsWithThisEmailError: "Аккаунт с такой почтой уже существует!",
        PasswordsNotMatchError: "Пароли не совпадают",
        UnauthorizedError: "Вы не авторизованы.",
        ConfirmationTokenExpiredError: "Срок подтверждения токена истëк."
    }
