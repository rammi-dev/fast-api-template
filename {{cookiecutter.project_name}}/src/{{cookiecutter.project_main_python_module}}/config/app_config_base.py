"""
Application should provide environment class with:
    - General purpose settings - AppConfig
"""
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

class ServerAppBaseConf(BaseModel):
    root_path: str
    config_root_path: str
    app_endpoint_root_prefix: str
    log_level: str
    hostname: str
    port: int
    log_config_file: str


    

class AppConfigBaseEnv(BaseSettings):
    """
    A class used to represent base application configuration.
    It should should inculde common server configuration ServerAppBaseConf
    If FastAPI aplication needs more parametrs please add it here.
    Feature specific parametrs should be stored src.<feature_name>.config.<feature_name>_env.py

    ...

    Attributes
    ----------
    app_config : ServerAppBaseConf
        standard server configuraiton parameters
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)

    """
    model_config = SettingsConfigDict(env_file='.env',
                                      env_file_encoding='utf-8',
                                      env_nested_delimiter = "__",
                                  #    extra = 'ignore' 
                                      )
    def __init__(self) -> None:
        super().__init__()

    # Mandatory config inherited by all K8s FASTAPI application
    app_config: ServerAppBaseConf



@lru_cache
def get_base_env():
    """Provides baseline configuration on FastAPI level

    Parameters
    ----------

    Raises
    ------

    """
    env = AppConfigBaseEnv()
    env.app_config.root_path = env.app_config.root_path or "./"
    env.app_config.config_root_path = env.app_config.config_root_path or "src/{{cookiecutter.project_main_python_module}}/config"
    env.app_config.log_config_file = env.app_config.log_config_file or "logging.conf"
    env.app_config.app_endpoint_root_prefix = env.app_config.app_endpoint_root_prefix or "/{{cookiecutter.project_name}}"
    return env
