import allure

from pages.login_page import LoginPage
from urls import Urls


class TestLoginPage:
    @allure.title("Проверка нажатия на кнопку 'Восстановить пароль'")
    def test_click_to_recover_password_success(self, get_driver):
        login_page = LoginPage(get_driver)

        assert login_page.click_to_recover_password() == Urls.FORGOT_PASS