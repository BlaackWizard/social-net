from .common import AccessDeniedError


class JWTError(AccessDeniedError):
    ...


class JWTDecodeError(JWTError):
    ...


class JWTExpiredError(JWTError):
    ...


class ConfirmationTokenСorruptedError(JWTError):
    ...


class AccessTokenСorruptedError(JWTError):
    ...
