from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, field_validator

from src.auth.application.errors.user_request import PasswordsNotMatchError


class TokenResponse(BaseModel):
    uid: UUID
    access_token: str


class UserRegisterRequest(BaseModel):
    email: EmailStr
    username: str
    password1: str
    password2: str

    @field_validator('password2')
    def match_password(self, v, values):
        if 'password1' not in values or v != values['password1']:
            raise PasswordsNotMatchError


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
