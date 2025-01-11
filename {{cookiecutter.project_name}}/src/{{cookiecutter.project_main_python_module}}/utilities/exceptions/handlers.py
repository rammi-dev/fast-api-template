from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from {{cookiecutter.project_main_python_module}}.utilities.exceptions.unicorn_exception import UnicornException


def register_exceptions(app: FastAPI):
    """Custom exceptioin handler configuraiton

    Parameters
    ----------
    app: FastAPI
        main application object

    Raises
    ------

    """

    @app.exception_handler(UnicornException)
    async def unicorn_exception_handler(request: Request, exc: UnicornException):
        return JSONResponse(
            status_code=418,
            content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
        )
