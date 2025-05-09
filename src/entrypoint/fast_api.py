import logging
from contextlib import asynccontextmanager
from typing import AsyncIterator

import uvicorn
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.auth.presentation.web.endpoints.user import router as auth_router
from src.auth.presentation.web.register_exceptions import \
    register_exceptions as auth_register_exceptions
from src.entrypoint.container import get_container
from src.subscription.presentation.web.endpoints import \
    router as subscription_router
from src.subscription.presentation.web.register_exceptions import \
    register_exceptions as subscription_register_exceptions

log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console"],
    },
}


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    yield
    await app.state.dishka_container.close()


def run_api() -> None:
    app = FastAPI(
        lifespan=lifespan,
        docs_url="/docs",
        title="Social-net",
        description="API соц.сети",
    )
    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    container = get_container()

    setup_dishka(container=container, app=app)

    logging.info("FastAPI app created.")

    app.include_router(auth_router)
    app.include_router(subscription_router)
    subscription_register_exceptions(app)
    auth_register_exceptions(app)

    uvicorn.run(
        app,
        port=8000,
        host="localhost",
        log_config=log_config,
    )


if __name__ == "__main__":
    run_api()
