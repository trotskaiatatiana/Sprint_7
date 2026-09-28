import allure
import requests

from urls import Urls


class CourierMethods:

    @staticmethod
    @allure.step('Создать курьера')
    def create_courier(courier_data):
        return requests.post(
            Urls.CREATE_COURIER,
            json=courier_data
        )

    @staticmethod
    @allure.step('Авторизовать курьера')
    def login_courier(login_data):
        return requests.post(
            Urls.LOGIN_COURIER,
            json=login_data
        )

    @staticmethod
    @allure.step('Удалить курьера')
    def delete_courier(courier_id):
        return requests.delete(
            f'{Urls.CREATE_COURIER}/{courier_id}'
        )


class OrderMethods:

    @staticmethod
    @allure.step('Создать заказ')
    def create_order(order_data):
        return requests.post(
            Urls.CREATE_ORDER,
            json=order_data
        )

    @staticmethod
    @allure.step('Получить список заказов')
    def get_orders():
        return requests.get(Urls.ORDERS_LIST)