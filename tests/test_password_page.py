import allure

from pages.password_page import PasswordPage
from urls import Urls


class TestPasswordPage:
    @allure.title("Проверка ввода email")
    def test_insert_email(self, get_driver, get_new_user):
        password_page = PasswordPage(get_driver)
        email = get_new_user[1]["email"]

        assert password_page.insert_email_address(email) == Urls.RESET_PASS

    @allure.title("Проверка подсветки поля пароль при нажатии кнопки 'Показать/скрыть пароль'")
    def test_show_password(self, get_driver, get_new_user):
        password_page = PasswordPage(get_driver)
        email = get_new_user[1]["email"]
        password_page.insert_email_address(email)

        elements_class = password_page.check_password_field()

        assert "input__placeholder-focused" in elements_class