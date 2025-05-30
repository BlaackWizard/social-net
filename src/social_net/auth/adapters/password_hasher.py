from dataclasses import dataclass

from argon2 import PasswordHasher as ArgonHasher
from argon2.exceptions import VerifyMismatchError

from social_net.auth.application.common.password_hasher import (HASHED_PASSWORD,
                                                         PasswordHasher)
from social_net.auth.application.errors.user_request import PasswordsNotMatchError


@dataclass
class Argon2PasswordHasher(PasswordHasher): # type: ignore[misc]
    hasher = ArgonHasher()

    def hash_password(self, password: str) -> HASHED_PASSWORD:
        return self.hasher.hash(password)

    def check_password(self, password: str, hashed_password: HASHED_PASSWORD) -> bool:
        try:
            return bool(self.hasher.verify(hashed_password, password))
        except VerifyMismatchError as exc:
            raise PasswordsNotMatchError from exc
