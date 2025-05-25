from abc import abstractmethod, ABC

from social_net.auth.application.dto.user import UserConfirmationTokenDTO


class TokenSender(ABC):
    @abstractmethod
    def send(self, data: UserConfirmationTokenDTO, user_email: str) -> None:
        ...
