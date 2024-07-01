import allure

from urls import Urls


class TestAccountPage:
    @allure.title("Проверка нажатия на кнопку 'История заказов'")
    def test_click_to_order_history(self, get_account_page):
        assert get_account_page.click_to_order_history() == Urls.ORDER_HISTORY

    @allure.title("Проверка нажатия на кнопку 'Выход'")
    def test_click_to_exit(self, get_account_page):
        assert get_account_page.click_to_exit_button() == Urls.LOGIN

    @allure.title("Проверка нажатия на кнопку 'Конструктор'")
    def test_click_to_constructor(self, get_account_page):
        assert get_account_page.click_to_constructor_button() == Urls.MAIN