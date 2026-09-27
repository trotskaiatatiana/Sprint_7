import allure
import pytest
import requests

from data import OrderData
from urls import Urls


@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.title('Создание заказа с разными вариантами цвета')
    @pytest.mark.parametrize(
        'color',
        [
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            []
        ]
    )
    def test_create_order_different_colors_success(self, color):
        order_data = OrderData.ORDER.copy()
        order_data["color"] = color

        response = requests.post(
            Urls.CREATE_ORDER,
            json=order_data
        )

        assert response.status_code == 201
        assert "track" in response.json()