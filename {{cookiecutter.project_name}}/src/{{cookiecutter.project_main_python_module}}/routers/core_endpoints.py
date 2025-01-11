"""Base router for application utility

"""
import logging

from fastapi import APIRouter, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from {{cookiecutter.project_main_python_module}}.routers.models.log_level_model import LogLevelModel

# Logger
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get(
    "/utilities/loglevel",
    response_class=Response,
    responses={
        200: {
            "content": {"application/json": {}},
            "description": "Return the loglevel of server",
            "media-type": {"application/json": {}},
        }
    },
    tags=["check server loglevel"],
)
async def get_log_level():
    """GET loglevel from application

    Parameters
    ----------

    Raises
    ------

    """
    logger.debug("check server loglevel")
    respose_content = {"loglevel": logging.getLevelName(logger.root.getEffectiveLevel())}
    response_json = jsonable_encoder(respose_content)

    return JSONResponse(content=response_json)


@router.post(
    "/utilities/loglevel/{level}",
    response_class=Response,
    responses={
        404: {"content": {"text/plain": {}}, "description": "Resource not supported"},
        200: {
            "content": {"text/plain": {}},
            "description": "Set loglevel",
            "media-type": {"text/plain": {}},
        },
    },
    tags=["set log level"],
)
async def set_log_level(level: LogLevelModel):
    """POST new loglevel to application

    Parameters
    ----------
    level: LogLevelModel
        log level defined in LogLevelModel class

    Raises
    ------

    """
    logger.debug(f"setting level {level.capitalize()}")

    logging.getLogger("uvicorn").setLevel(level.upper())
    logging.getLogger("uvicorn.access").setLevel(level.upper())
    logging.getLogger("uvicorn.error").setLevel(level.upper())
    logging.root.setLevel(level.upper())

    return f"Log level set to: {level.upper()}"


@router.get(
    "/utilities/healthcheck",
    response_class=Response,
    responses={
        200: {
            "content": {"application/json": {}},
            "description": "Return the status of server",
            "media-type": {"application/json": {}},
        },
        406: {
            "content": {"application/json": {}},
            "description": "Application is not healthy",
            "media-type": {"application/json": {}},
        },
    },
    tags=["check server liveliness"],
)
async def server_up():
    """Validated liviness of server

    Additional logic can be implemented to validate the status.
    This endpoint should be configured for liviness probe.

    Parameters
    ----------

    Raises
    ------

    """
    logger.debug("Metric extract")

    status_code = 200

    return JSONResponse(status_code=status_code, content={"status": "OK"})


# Description of endpoints for Swagger documentation.
utilities_tag_data = [
    {
        "name": "check server liveliness",
        "description": "check if application runs properly",
    },
    {
        "name": "check server loglevel",
        "description": "Check log level of application.",
    },
    {
        "name": "set log level",
        "description": "Set log level of application.",
    },
]
