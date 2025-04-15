from typing import Annotated

from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter
from fastapi.params import Depends

from src.auth.application.delete_user import DeleteUser
from src.auth.application.dto.user import TokenResponse, UserRegisterResponse
from src.auth.application.register_user import RegisterUser, UserRegisterRequest
from src.auth.application.verify_user import VerifyUser
from src.auth.application.authorize_user import UserAuthorizeRequest, AuthorizeUser
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

router = APIRouter(
    prefix='/auth',
    tags=['Авторизация и аутентификация'],
    route_class=DishkaRoute
)


@router.post('/register-user')
async def register_user(
    schema: UserRegisterRequest,
    interactor: FromDishka[RegisterUser]
) -> UserRegisterResponse:
    return await interactor.execute(schema)

@router.post('/verify-user/{token}')
async def verify_user(
    token: str,
    interactor: FromDishka[VerifyUser]
) -> TokenResponse:
    return await interactor.execute(token)

@router.post('/login-user')
async def login_user(
    schema: UserAuthorizeRequest,
    interactor: FromDishka[AuthorizeUser]
) -> TokenResponse:
    return await interactor.execute(schema)

@router.delete('/delete-user')
async def delete_user(
    _token: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer)],
    interactor: FromDishka[DeleteUser]
) -> UserRegisterResponse:
    return await interactor.execute()
