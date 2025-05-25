from collections.abc import Awaitable
from typing import Callable, Dict, Type

from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from social_net.auth.presentation.web.exception_code import get_error_codes
from social_net.auth.presentation.web.exception_message import get_error_messages


def create_exception(
    exc: Type[Exception],
    message: str,
    status_code: int
) -> Callable[[Request, Exception], Awaitable[JSONResponse]]:
    async def handler(request: Request, exc_class: Exception) -> JSONResponse:
        return JSONResponse(
            content={"message": message},
            status_code=status_code
        )
    return handler


def register_exceptions(app: FastAPI) -> None:
    messages: Dict[Type[Exception], str] = get_error_messages()
    codes: Dict[Type[Exception], int] = get_error_codes()

    for exc, message in messages.items():
        status_code = codes[exc]
        app.add_exception_handler(exc, create_exception(exc, message, status_code))
