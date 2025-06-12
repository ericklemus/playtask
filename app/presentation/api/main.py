from fastapi import FastAPI
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from app.presentation.api.commons.exception_handlers import (
    generic_exception_handler,
    not_found_exception_handler,
    validation_error_exception_handler,
)
from app.presentation.api.resources.task.routes import task_router


def init_app() -> FastAPI:
    app = FastAPI()

    origins = ["http://localhost", "http://localhost:8080"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    common_router_args = {}

    app.include_router(task_router, **common_router_args)

    app.add_exception_handler(Exception, handler=generic_exception_handler)
    app.add_exception_handler(HTTPException, handler=not_found_exception_handler)
    app.add_exception_handler(RequestValidationError, handler=validation_error_exception_handler)

    return app


app = init_app()

@app.get("/")
def hello_world():
    return {"Hello": "Erick"}
