import logging.config

from {{cookiecutter.project_main_python_module}}.config.app_config_base import AppConfigBaseEnv, get_base_env

env: AppConfigBaseEnv = get_base_env()

app_root_path: str = env.app_config.root_path
config_root_path: str = env.app_config.config_root_path
endpoint_prefix: str = env.app_config.app_endpoint_root_prefix
log_config_file = env.app_config.log_config_file
log_config_path = f"{app_root_path}/{config_root_path}/{log_config_file}"

logging.config.fileConfig(log_config_path, disable_existing_loggers=False)

logging.captureWarnings(True)

logging.root.setLevel(env.app_config.log_level)
