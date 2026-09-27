import allure
import pytest
import requests

from urls import Urls


@allure.feature('Логин курьера')
class TestLoginCourier:

    @allure.title('Курьер может авторизоваться')
    def test_login_courier_success(self, courier):
        response = requests.post(
            Urls.LOGIN_COURIER,
            json={
                "login": courier["login"],
                "password": courier["password"]
            }
        )

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title('Нельзя авторизоваться без обязательного поля: {missing_field}')
    @pytest.mark.parametrize(
        'missing_field',
        [
            'login',
            'password'
        ]
    )
    def test_login_without_required_field_error(self, courier, missing_field):
        login_data = {
            "login": courier["login"],
            "password": courier["password"]
        }

        login_data.pop(missing_field)

        response = requests.post(
            Urls.LOGIN_COURIER,
            json=login_data
        )

        assert response.status_code == 400
        assert "message" in response.json()

    @allure.title('Ошибка при неправильном логине')
    def test_login_with_wrong_login_error(self, courier):
        response = requests.post(
            Urls.LOGIN_COURIER,
            json={
                "login": courier["login"] + "wrong",
                "password": courier["password"]
            }
        )

        assert response.status_code == 404
        assert "message" in response.json()

    @allure.title('Ошибка при неправильном пароле')
    def test_login_with_wrong_password_error(self, courier):
        response = requests.post(
            Urls.LOGIN_COURIER,
            json={
                "login": courier["login"],
                "password": courier["password"] + "wrong"
            }
        )

        assert response.status_code == 404
        assert "message" in response.json()