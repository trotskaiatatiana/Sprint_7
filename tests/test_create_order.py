import allure
import pytest

from data import OrderData
from methods import OrderMethods


@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.title('Создание заказа с разными вариантами цвета')
    @pytest.mark.parametrize(
        'color',
        [
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            None
        ]
    )
    def test_create_order_different_colors_success(self, color):
        order_data = OrderData.ORDER.copy()

        if color is not None:
            order_data["color"] = color

        response = OrderMethods.create_order(order_data)

        assert response.status_code == 201
        assert "track" in response.json()