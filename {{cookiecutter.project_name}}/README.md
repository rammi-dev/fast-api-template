# Application name

##{{cookiecutter.project_main_python_module}}
###<Please update all template file.>###


## A typical top-level directory layout

    .
    ├── docs                           # Documentation files
    ├── src                            # Source files
    │   └─── {{cookiecutter.project_main_python_module}}                       # Folder for FastAPI backbone
    │      ├── config                  # Configuration folder for app. Store all you json/yaml/csv files here
    │      │   ├── app_config_base.py  # Baic env configuration
    │      │   └── logging.conf        # logger configuration
    │      ├── routers                 # Standard routers
    │      │   ├── core_endpoints.py   # Basic endpoints implementation
    │      │   └── models              # Endpoints models
    │      └── utilities               # Helper folder for FastApi application
    │      │    ├── exceptions         # definition of custom FastAPI exceptions
    │      │    │   └── handlers.py    # registration of exceptions
    │      │    └──instrumentation.py  # dedicated to prometheus metrics definition
    │      └── __main__.py             # main application module
    ├── tests                          # Automated tests
    ├── .coveragerc                    # Pytest coverage configuration
    ├── .gitignore
    ├── .gitlab-ci.yaml                # CI/CD pipeline configuration
    ├── .pre-commit-config.yaml        # Helper utilities for code management
    ├── .dockerignore
    ├── MANIFEST.in                    # Static files include
    ├── pyproject.toml                 # To make sure tests are executed in pipeline integrate dev deps to requiremnts.txt
    ├── Dockerfile
    ├── requirements.txt               # requirements locked - either manually set or build by pip-compile from requirements.in
    ├── requirements.in                # Libraries configuration
    ├── requirements-dev.txt           # requirements for testing.
    └── README.md

## Description
This repository contains template fastApi application. It should be used for a single process use cases. Please modify all files with '-tmpl' postfix. There placeholders inside files (marked wiht double '#') you need to customize. Please make sure that for the production run application should be further adjusted according to your use case. Proper applicatiom name should be of the key element

## Installation
For K8s deployment please refer to the https://iffprod.atlassian.net/wiki/spaces/KCD/pages/19365892/New+Apps+Onboarding

## Usage
To run the application for development purposes use virtual environment.
In production mode make sure you give the app proper name use requirements.txt. Here there is only example for development

Install applicatioin in editable mode eg.

    python3 -m pip install -e .

You can use makefile and check available commands.

Make sure your .env-sample is sourced and all variables are set in you terminal:
eg.

    set -a
    . .env-sample
    set +a

You can also copy .env-sample -> .env. Make sure that gitignore is configred not to sync it to repo

Application can be run in several ways in dev mode:

As a module.

    python3 -m {{cookiecutter.project_main_python_module}}

As standalone uvicorn app (it allows automatic reload)

    uvicorn {{cookiecutter.project_main_python_module}}.__main__:app --log-config ./src/{{cookiecutter.project_main_python_module}}/config/logging.conf --port 10002 --log-level=info --reload

As python script

    python3 ./src/{{cookiecutter.project_main_python_module}}/__main__.py

Demonstration Swagger interface should be accesible under http://localhost:10002//{{cookiecutter.project_name}}/documentation (please make sure you adjust port and app name if needed)

Build docker image localy

    docker build --secret id=netrc,src=<path to you secrets>.netrc -t <image_tag> .

Path to [netrc](https://www.gnu.org/software/inetutils/manual/html_node/The-_002enetrc-file.html) - should be provided\
example:\
&nbsp;&nbsp;&nbsp;machine gitlab.com\
&nbsp;&nbsp;&nbsp;login __token__\
&nbsp;&nbsp;&nbsp;password \<your passowrd to the repo token\>

To perform unit test please execute:

Install testing dependncies:

    pip install -e .[test]

Execute tests:

    python3 -m pytest

## Contributing
Everyone is welcome to introduce improvements. Please, assign one of BO team member for review. We are eager to learn from you.

## Authors and acknowledgment
IFF BackOffice team

## License
IFF
