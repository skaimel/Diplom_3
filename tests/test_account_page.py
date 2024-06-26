import allure

from pages.account_page import AccountPage
from urls import Urls


class TestAccount:
    @allure.title("Проверка нажатия на кнопку 'История заказов'")
    def test_click_to_order_history(self, get_driver, get_logged_driver):
        account_page = AccountPage(get_driver)

        assert account_page.click_to_order_history() == Urls.ORDER_HISTORY

    @allure.title("Проверка нажатия на кнопку 'Выход'")
    def test_click_to_exit(self, get_driver, get_logged_driver):
        account_page = AccountPage(get_driver)

        assert account_page.click_to_exit_button() == Urls.LOGIN

    @allure.title("Проверка нажатия на кнопку 'Конструктор'")
    def test_click_to_constructor(self, get_driver, get_logged_driver):
        account_page = AccountPage(get_driver)

        assert account_page.click_to_constructor_button() == Urls.MAIN