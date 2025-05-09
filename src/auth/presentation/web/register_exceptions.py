from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from src.auth.presentation.web.exception_code import get_error_codes
from src.auth.presentation.web.exception_message import get_error_messages


def register_exceptions(app: FastAPI):
    messages = get_error_messages()
    codes = get_error_codes()

    for exc, message in messages.items():
        status_code = codes[exc]

        def create_exception(exc, message, status_code):
            async def handler(request: Request, exc_class: exc):
                return JSONResponse(
                    content={"message": message},
                    status_code=status_code
                )

            return handler
        app.add_exception_handler(exc, create_exception(exc, message, status_code))
