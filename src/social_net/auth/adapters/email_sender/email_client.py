from abc import abstractmethod
from dataclasses import dataclass
from email.message import Message
from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from typing import Protocol

from social_net.auth.adapters.email_sender.config import SMTPConfig
from social_net.auth.application.errors.user_request import IncorrectEmailData


@dataclass
class EmailClient(Protocol):
    @abstractmethod
    def send(self, message: Message, email_to: str, email_from: str) -> None:
        ...


@dataclass
class EmailClientImpl(EmailClient):
    smtp_config: SMTPConfig

    def _client(self) -> SMTP:
        try:
            server = SMTP(self.smtp_config.host, self.smtp_config.port)
            server.starttls()
            server.login(self.smtp_config.user, self.smtp_config.password)
            return server
        except SMTPAuthenticationError:
            raise IncorrectEmailData("Неверные учетные данные для SMTP.")
        except SMTPException as e:
            raise IncorrectEmailData(f"SMTP ошибка: {str(e)}")
        except Exception as e:
            raise IncorrectEmailData(f"Ошибка SMTP клиента: {str(e)}")

    def send(self, message: Message, email_to: str, email_from: str) -> None:
        try:
            with self._client() as client:
                client.send_message(message, from_addr=email_from, to_addrs=email_to)
        except Exception as e:
            raise IncorrectEmailData(f"Не удалось отправить email: {str(e)}")
