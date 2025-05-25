from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from typing import Callable, Awaitable, Type, Dict
from .error_code import exception_codes
from .error_messages import exception_messages

def create_exception_handler(
    exc_class: Type[Exception],
    message: str,
    status_code: int
) -> Callable[[Request, Exception], Awaitable[JSONResponse]]:
    async def handler(request: Request, exc: Exception) -> JSONResponse:
        return JSONResponse(
            status_code=status_code,
            content={'message': message, 'status_code': status_code}
        )
    return handler


def register_exceptions(app: FastAPI) -> None:
    messages: Dict[Type[Exception], str] = exception_messages()
    codes: Dict[Type[Exception], int] = exception_codes()

    for exc_class, message in messages.items():
        status_code = codes.get(exc_class, 400)
        app.add_exception_handler(
            exc_class,
            create_exception_handler(exc_class, message, status_code)
        )
