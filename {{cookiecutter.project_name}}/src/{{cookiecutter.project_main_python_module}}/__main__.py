"""FastAPI minimal microservice application

The script provides minimal code to start standalone single process server

Aplpication is configured via common ServerAppBaseConf class.
Feature related configuration should be store in feature package

"""
import logging

import uvicorn
from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from starlette.middleware.cors import CORSMiddleware

from {{cookiecutter.project_main_python_module}}.config.app_config_base import AppConfigBaseEnv, get_base_env
from {{cookiecutter.project_main_python_module}}.routers.core_endpoints import router as util_router
from {{cookiecutter.project_main_python_module}}.routers.core_endpoints import utilities_tag_data
from {{cookiecutter.project_main_python_module}}.utilities.exceptions.handlers import register_exceptions
from {{cookiecutter.project_main_python_module}}.utilities.instrumentation import PrometheusMiddleware, handle_metrics

env: AppConfigBaseEnv = get_base_env()

app_root_path: str = env.app_config.root_path
config_root_path: str = env.app_config.config_root_path
endpoint_prefix: str = env.app_config.app_endpoint_root_prefix
log_config_file = env.app_config.log_config_file
log_config_path = f"{app_root_path}/{config_root_path}/{log_config_file}"
logger = logging.getLogger(__name__)

# Tags metadata is use by Swagger documentation page
# Please provide description for each endpoint
tags_metadata = utilities_tag_data

# Add additionals tags:
# tags_metadata.append(your tags)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialization.shutdown tasks to be put here.
    Only for a single process (worker) app it is a singleton

    Parameters
    ----------

    Raises
    ------

    """
    logger.info("Initialize environment")

    yield

    logger.info("Shutdown environment")


# Main application object
app = FastAPI(
    title="{{cookiecutter.project_main_python_module}}",
    description="{{cookiecutter.project_description}}",
    version="0.0.1",
    contact={
        "name": "Support team name",
        "email": "support_team_email@iff.com",
    },
    openapi_tags=tags_metadata,
    openapi_url=f"{endpoint_prefix}/openapi.json",
    docs_url=f"{endpoint_prefix}/documentation",
    lifespan=lifespan,
)

# Register custom excptoins if needed
register_exceptions(app)

app.add_middleware(
    PrometheusMiddleware,
    labels={"app_group": "{{cookiecutter.project_group}}", "app_name": "{{cookiecutter.project_name}}"},
    skip_paths=[f"{endpoint_prefix}/metrics", f"{endpoint_prefix}/utilities/healthcheck"],
)
app.add_route(f"{endpoint_prefix}/metrics", handle_metrics)
app.include_router(util_router, prefix=endpoint_prefix)

# CORS support added by default https://fastapi.tiangolo.com/tutorial/cors/
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    """
    Use it as test initialization. It should be used only for single process app
    For multi-porcess application use template with gunivorn support
    """

    uvicorn.run(
        app,
        host=env.app_config.hostname,
        port=env.app_config.port,
        log_config=log_config_path,
        log_level=logging.getLevelName(env.app_config.log_level).lower(),
    )
