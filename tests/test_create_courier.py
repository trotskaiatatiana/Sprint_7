import allure
import pytest
import requests

from helpers import generate_courier_data
from urls import Urls


@allure.feature('Создание курьера')
class TestCreateCourier:

    @allure.title('Успешное создание курьера')
    def test_create_courier_success(self):
        courier_data = generate_courier_data()
        courier_id = None

        try:
            response = requests.post(
                Urls.CREATE_COURIER,
                json=courier_data
            )

            assert response.status_code == 201
            assert response.json() == {"ok": True}

            login_response = requests.post(
                Urls.LOGIN_COURIER,
                json={
                    "login": courier_data["login"],
                    "password": courier_data["password"]
                }
            )

            courier_id = login_response.json()["id"]

        finally:
            if courier_id:
                requests.delete(
                    f'{Urls.CREATE_COURIER}/{courier_id}'
                )

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_duplicate_courier_error(self, courier):
        response = requests.post(
            Urls.CREATE_COURIER,
            json=courier
        )

        assert response.status_code == 409
        assert response.json()["message"] == (
            "Этот логин уже используется. Попробуйте другой."
        )

    @allure.title('Нельзя создать курьера без обязательного поля: {missing_field}')
    @pytest.mark.parametrize(
        'missing_field',
        [
            'login',
            'password'
        ]
    )
    def test_create_courier_without_required_field_error(self, missing_field):
        courier_data = generate_courier_data()
        courier_data.pop(missing_field)

        response = requests.post(
            Urls.CREATE_COURIER,
            json=courier_data
        )

        assert response.status_code == 400
        assert "message" in response.json()