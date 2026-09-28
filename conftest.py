import pytest

from helpers import generate_courier_data
from methods import CourierMethods


@pytest.fixture
def courier():
    courier_data = generate_courier_data()

    CourierMethods.create_courier(courier_data)

    yield courier_data

    login_data = {
        "login": courier_data["login"],
        "password": courier_data["password"]
    }

    login_response = CourierMethods.login_courier(login_data)

    if login_response.status_code == 200:
        courier_id = login_response.json()["id"]
        CourierMethods.delete_courier(courier_id)


@pytest.fixture
def new_courier():
    courier_data = generate_courier_data()

    yield courier_data

    login_data = {
        "login": courier_data["login"],
        "password": courier_data["password"]
    }

    login_response = CourierMethods.login_courier(login_data)

    if login_response.status_code == 200:
        courier_id = login_response.json()["id"]
        CourierMethods.delete_courier(courier_id)