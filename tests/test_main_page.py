import allure
import pytest

from pages.main_page import MainPage
from urls import Urls
import helpers


class TestMainPage:
    @allure.title("Проверка перехода в личный кабинет")
    def test_click_personal_area(self, get_main_page, get_logged_driver):
        assert get_main_page.click_to_personal_area() == Urls.PERSONAL_AREA

    @allure.title("Проверка перехода на ленту заказов")
    def test_click_to_orders_feed(self, get_main_page, get_logged_driver):
        assert get_main_page.click_to_orders_feed() == Urls.ORDER_FEED

    @allure.title("Проверка нажатия на ингредиент. Открытие формы с описанием ингредиента")
    @pytest.mark.parametrize("ingredient", helpers.Order.get_ingredients()[1])
    def test_click_to_ingredient(self, get_main_page, ingredient):
        assert get_main_page.click_to_ingredient(ingredient) == "Детали ингредиента"

    @allure.title("Проверка нажатия на кнопку закрытия формы деталей ингредиента")
    def test_close_ingredient_details(self, get_main_page):
        assert get_main_page.click_to_ingredient_and_close()

    @allure.title("Проверка, что при добавлении ингредиента в заказ счетчик ингредиента увеличивается")
    def test_add_ingredient_check_counter(self, get_main_page):
        assert get_main_page.check_counter_of_ingredient()

    @allure.title("Проверка возможности залогиненного пользователя создать заказ")
    def test_user_create_order(self, get_main_page, get_logged_driver):
        assert get_main_page.create_order()