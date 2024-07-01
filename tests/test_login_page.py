import allure

from urls import Urls


class TestLoginPage:
    @allure.title("Проверка нажатия на кнопку 'Восстановить пароль'")
    def test_click_to_recover_password_success(self, get_login_page):
        assert get_login_page.click_to_recover_password() == Urls.FORGOT_PASS