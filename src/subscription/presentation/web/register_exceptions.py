from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .error_code import exception_codes
from .error_messages import exception_messages

def register_exceptions(app: FastAPI):
    messages = exception_messages()
    codes = exception_codes()

    for exc_class, message in messages.items():
        status_code = codes.get(exc_class, 400)

        def create_exception_handler(exc_class, message, status_code):
            async def handler(request: Request, exc: exc_class):
                return JSONResponse(
                    status_code=status_code,
                    content={'message': message, 'status_code': status_code}
                )
            return handler

        app.add_exception_handler(exc_class, create_exception_handler(exc_class, message, status_code))
