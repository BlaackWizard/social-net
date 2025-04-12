from abc import abstractmethod
from typing import Protocol

from src.auth.application.dto.user import UserConfirmationTokenDTO


class TokenSender(Protocol):
    @abstractmethod
    def send(self, data: UserConfirmationTokenDTO, user_email: str) -> None:
        ...
