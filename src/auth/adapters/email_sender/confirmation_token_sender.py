from src.auth.adapters.email_sender.config import ConfirmationEmailConfig
from src.auth.application.common.jwt.confirmation_token_processor import ConfirmationTokenProcessor
from src.auth.application.common.token_sender import TokenSender
from src.auth.application.dto.user import UserConfirmationTokenDTO
from email.mime.text import MIMEText
from dataclasses import dataclass

@dataclass
class ConfirmationTokenSender(TokenSender):
    token_processor: ConfirmationTokenProcessor
    config: ConfirmationEmailConfig

    def send(self, data: UserConfirmationTokenDTO, user_email: str) -> None:
        jwt_token = self.token_processor.encode(data)

        link = self.config.confirmation_link.format_map(
            {
                "token": jwt_token
            }
        )

        text = f"Перейдите по ссылке чтобы подтвердить свою почту: {link}"
        message = MIMEText(text)
        message['Subject'] = self.config.subject

        self.client.send(message, self.config.email_from, user_email)
