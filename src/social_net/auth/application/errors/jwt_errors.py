from social_net.auth.application.common.exceptions.base import AccessDeniedError


class JWTError(AccessDeniedError): # type: ignore[misc]
    ...


class JWTDecodeError(JWTError):
    ...


class JWTExpiredError(JWTError):
    ...


class ConfirmationTokenСorruptedError(JWTError):
    ...


class AccessTokenСorruptedError(JWTError):
    ...

class ConfirmationTokenExpiredError(JWTError): ...