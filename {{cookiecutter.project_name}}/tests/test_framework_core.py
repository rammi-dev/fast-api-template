import json

from {{cookiecutter.project_main_python_module}}.__main__ import app, endpoint_prefix
from fastapi.testclient import TestClient

client = TestClient(app)

REQUEST_SUCCESS = 200


def test_sanity_core():
    response = client.get(f"{endpoint_prefix}/utilities/healthcheck")

    assert response.status_code == REQUEST_SUCCESS


def test_loglevel():
    response = client.post(f"{endpoint_prefix}/utilities/loglevel/INFO")

    assert response.status_code == REQUEST_SUCCESS

    response = client.get(f"{endpoint_prefix}/utilities/loglevel")

    response_content = json.loads(response.content)
    assert response_content["loglevel"] == "INFO"

    assert response.status_code == REQUEST_SUCCESS
