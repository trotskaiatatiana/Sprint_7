import allure
import requests

from urls import Urls


@allure.feature('Список заказов')
class TestOrdersList:

    @allure.title('В ответе возвращается список заказов')
    def test_get_orders_list_success(self):
        response = requests.get(Urls.ORDERS_LIST)

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)