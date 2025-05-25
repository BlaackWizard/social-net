from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, field_validator
from pydantic_core.core_schema import ValidationInfo


class TokenResponse(BaseModel): # type: ignore[misc]
    uid: UUID
    access_token: str


class UserRegisterRequest(BaseModel): # type: ignore[misc]
    email: EmailStr
    username: str
    password1: str
    password2: str

    @field_validator("password2") # type: ignore[misc]
    @classmethod
    def passwords_match(cls, v: str, info: ValidationInfo) -> str:
        if "password1" in info.data and v != info.data["password1"]:
            raise ValueError("passwords do not match")
        return v


class UserAuthorizeRequest(BaseModel): # type: ignore[misc]
    email: EmailStr
    password: str


class UserConfirmationTokenDTO(BaseModel): # type: ignore[misc]
    token_id: UUID
    uid: UUID
    expires_in: datetime


class AccessTokenDTO(BaseModel): # type: ignore[misc]
    token_id: UUID
    uid: UUID
    expires_in: datetime


class UserRegisterResponse(BaseModel): # type: ignore[misc]
    message: str


class UserDTO(BaseModel): # type: ignore[misc]
    username: str
    email: str
    hashed_password: str


class UserInfoResponse(BaseModel): # type: ignore[misc]
    uid: UUID
    username: str
    email: str
