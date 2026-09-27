import pytest
import requests

from helpers import generate_courier_data
from urls import Urls


@pytest.fixture
def courier():
    courier_data = generate_courier_data()

    create_response = requests.post(
        Urls.CREATE_COURIER,
        json=courier_data
    )

    assert create_response.status_code == 201

    yield courier_data

    login_response = requests.post(
        Urls.LOGIN_COURIER,
        json={
            "login": courier_data["login"],
            "password": courier_data["password"]
        }
    )

    if login_response.status_code == 200:
        courier_id = login_response.json()["id"]

        requests.delete(
            f'{Urls.CREATE_COURIER}/{courier_id}'
        )