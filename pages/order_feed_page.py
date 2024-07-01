import allure

from locators.feed_page_locators import FeedLocators
from pages.base_page import BasePage
from urls import Urls
from helpers import Order


class OrderFeed(BasePage):
    @allure.step("Проверка информации о заказе")
    @allure.description("1. Открываем страницу с заказами"
                        "2. Нажимаем на последний заказ"
                        "3. Проверяем, что открылось окно с информацией о заказе")
    def open_order_info(self):
        self.open_page(Urls.ORDER_FEED)
        self.click_to_element(FeedLocators.ORDER_NUMBER_IN_FEED)

        return self.check_element_is_displayed(FeedLocators.ORDER_INFO_TEXT)

    @allure.step("Проверка личного заказа в общей ленте")
    @allure.description("1. Создаем заказ через API и получаем его ID"
                        "2. Открываем страницу с лентой заказов"
                        "3. Находим заказ по ID")
    def check_private_orders_in_feed(self, new_user):
        token = new_user[0].json()["accessToken"]
        ingredients = Order().create_burger()
        order_id = Order().create_order(ingredients, token).json()['order']['_id']

        self.open_page(Urls.ORDER_FEED)
        order_locator = self.format_locator(FeedLocators.ORDER_BY_ID, order_id)

        return self.wait_and_find_element(order_locator)

    @allure.step("Проверка счетчиков заказов")
    @allure.description("1. Получаем текущие счетчики заказов за сегодня и за все время"
                        "2. Создаем заказ через API"
                        "3. Получаем текущие счетчики заказов за сегодня и за все время"
                        "4. Сравниваем счетчики")
    def check_order_counter(self, new_user):
        self.open_page(Urls.ORDER_FEED)
        all_time_counter_before = self.get_text_locator(FeedLocators.CREATED_ALL_TIME_ORDERS)
        today_counter_before = self.get_text_locator(FeedLocators.CREATED_TODAY_ORDERS)

        token = new_user[0].json()["accessToken"]
        ingredients = Order().create_burger()
        Order().create_order(ingredients, token)

        all_time_counter_after = self.get_text_locator(FeedLocators.CREATED_ALL_TIME_ORDERS)
        today_counter_after = self.get_text_locator(FeedLocators.CREATED_TODAY_ORDERS)

        return all_time_counter_before < all_time_counter_after and today_counter_before < today_counter_after

    @allure.step("Проверка что созданный заказ отображается в поле 'В работе'")
    @allure.description("1. Открываем страницу с заказами"
                        "2. Создаем заказ через API и получаем его номер"
                        "3. Получаем номер заказа в поле 'В работе'"
                        "4. Сравниваем номера")
    def check_order_in_progress(self, new_user):
        self.open_page(Urls.ORDER_FEED)
        token = new_user[0].json()["accessToken"]
        ingredients = Order().create_burger()
        order_number = Order().create_order(ingredients, token).json()['order']['number']

        order_number_from_locator = self.get_text_locator(FeedLocators.ORDER_IN_PROGRESS)

        return int(order_number) == int(order_number_from_locator)