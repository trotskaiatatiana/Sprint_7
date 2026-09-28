import allure
import pytest

from helpers import generate_courier_data
from methods import CourierMethods


@allure.feature('Создание курьера')
class TestCreateCourier:

    @allure.title('Успешное создание курьера')
    def test_create_courier_success(self, new_courier):
        response = CourierMethods.create_courier(new_courier)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_duplicate_courier_error(self, courier):
        response = CourierMethods.create_courier(courier)

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

        response = CourierMethods.create_courier(courier_data)

        assert response.status_code == 400
        assert response.json()["message"] == (
            "Недостаточно данных для создания учетной записи"
        )