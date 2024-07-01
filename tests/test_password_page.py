import allure

from urls import Urls


class TestPasswordPage:

    @allure.title("Проверка ввода email")
    def test_insert_email(self, get_password_page_instance, get_new_user):
        email = get_new_user[1]["email"]

        assert get_password_page_instance.insert_email_address(email) == Urls.RESET_PASS

    @allure.title("Проверка подсветки поля пароль при нажатии кнопки 'Показать/скрыть пароль'")
    def test_show_password(self, get_password_page_instance, get_new_user):
        email = get_new_user[1]["email"]
        get_password_page_instance.insert_email_address(email)
        elements_class = get_password_page_instance.check_password_field()

        assert "input__placeholder-focused" in elements_class