from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, field_validator
from pydantic_core.core_schema import ValidationInfo

from src.auth.application.errors.user_request import PasswordsNotMatchError


class TokenResponse(BaseModel):
    uid: UUID
    access_token: str


class UserRegisterRequest(BaseModel):
    email: EmailStr
    username: str
    password1: str
    password2: str

    @field_validator("password2")
    @classmethod
    def passwords_match(cls, v: str, info: ValidationInfo) -> str:
        if "password1" in info.data and v != info.data["password1"]:
            raise ValueError("passwords do not match")
        return v

class UserAuthorizeRequest(BaseModel):
    email: EmailStr
    password: str


class UserConfirmationTokenDTO(BaseModel):
    token_id: UUID
    uid: UUID
    expires_in: datetime


class AccessTokenDTO(BaseModel):
    token_id: UUID
    uid: UUID
    expires_in: datetime


class UserRegisterResponse(BaseModel):
    message: str


class UserDTO(BaseModel):
    username: str
    email: str
    hashed_password: str
