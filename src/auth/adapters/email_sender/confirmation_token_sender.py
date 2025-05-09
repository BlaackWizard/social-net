import logging
from dataclasses import dataclass
from email.mime.text import MIMEText

from src.auth.adapters.email_sender.config import ConfirmationEmailConfig
from src.auth.adapters.email_sender.email_client import EmailClient
from src.auth.application.common.jwt.confirmation_token_processor import \
    ConfirmationTokenProcessor
from src.auth.application.common.token_sender import TokenSender
from src.auth.application.dto.user import UserConfirmationTokenDTO


@dataclass
class ConfirmationTokenSender(TokenSender):
    token_processor: ConfirmationTokenProcessor
    config: ConfirmationEmailConfig
    client: EmailClient

    def send(self, data: UserConfirmationTokenDTO, user_email: str) -> None:
        try:
            jwt_token = self.token_processor.encode(data.model_dump())

            link = self.config.confirmation_link + jwt_token

            text = f"Перейдите по ссылке, чтобы подтвердить свою почту: {link}"
            message = MIMEText(text)
            message['Subject'] = self.config.subject
            message['From'] = self.config.email_from
            message['To'] = user_email

            logging.info(f"[SEND EMAIL] To: {user_email}, Link: {link}")

            self.client.send(
                message,
                email_to=user_email,
                email_from=self.config.email_from,
            )

            logging.info(f"[EMAIL SENT] Email успешно отправлен: {user_email}")
        except Exception as e:
            logging.error(f"[EMAIL ERROR] Ошибка при отправке письма: {str(e)}")
            raise
