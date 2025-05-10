from typing import Annotated

from dishka import FromComponent
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from starlette.responses import JSONResponse

from src.auth.application.authorize_user import (AuthorizeUser,
                                                 UserAuthorizeRequest)
from src.auth.application.delete_user import DeleteUser
from src.auth.application.dto.user import (TokenResponse, UserInfoResponse,
                                           UserRegisterResponse)
from src.auth.application.me import Me
from src.auth.application.register_user import (RegisterUser,
                                                UserRegisterRequest)
from src.auth.application.verify_user import VerifyUser

router = APIRouter(
    prefix='/auth',
    tags=['Авторизация и аутентификация'],
    route_class=DishkaRoute,
)


@router.post('/register-user')
async def register_user(
    schema: UserRegisterRequest,
    interactor: Annotated[RegisterUser, FromComponent("auth")],
) -> UserRegisterResponse:
    return await interactor.execute(schema)


@router.post('/verify-user/{token}')
async def verify_user(
    token: str,
    interactor: Annotated[VerifyUser, FromComponent("auth")],
) -> JSONResponse:
    result = await interactor.execute(token)
    response = JSONResponse(content={"message": "Вы успешно подтвердили свой аккаунт!"})
    response.set_cookie(
        key="access_token",
        value=result.access_token,
        httponly=True,
        secure=True,
        max_age=2592000,
    )
    return response

@router.post('/login-user')
async def login_user(
    schema: UserAuthorizeRequest,
    interactor: Annotated[AuthorizeUser, FromComponent("auth")],
) -> JSONResponse:
    result = await interactor.execute(schema)

    response = JSONResponse(content={"message": "Вы успешно вошли в свой аккаунт!"})
    response.set_cookie(
        key="access_token",
        value=result.access_token,
        httponly=True,
        secure=True,
        max_age=2592000,
    )
    return response


@router.delete('/delete-user')
async def delete_user(
    _token: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer)],
    interactor: Annotated[DeleteUser, FromComponent("auth")],
) -> UserRegisterResponse:
    return await interactor.execute()


@router.get('/me')
async def me(
    _token: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer)],
    interactor: Annotated[Me, FromComponent("auth")],
) -> UserInfoResponse:
    return await interactor.execute()
