from dataclasses import dataclass

from src.auth.adapters.email_sender.config import SMTPConfig
from src.auth.application.common.token_sender import TokenSender
from src.auth.application.dto.user import UserConfirmationTokenDTO

from email.message import Message
from typing import Any
from smtplib import SMTP

from src.auth.application.errors.user_request import IncorrectEmailData


@dataclass
class EmailClient:
    smtp_config: SMTPConfig

    def _client(self):
        server = SMTP(self.smtp_config.host, self.smtp_config.port)
        if self.smtp_config.use_tls:
            server.starttls()
        try:
            server.login(self.smtp_config.user, self.smtp_config.password)
        except:
            raise IncorrectEmailData
        return server
    def send(self, message: Message, email_to: str, email_from: str) -> None:
        client = self._client()
        client.send_message(message, email_from, email_to)
