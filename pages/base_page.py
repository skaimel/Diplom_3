import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from locators.login_page_locators import LoginLocators
from urls import Urls


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ждем и ищем элемент по локатору")
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 10).until((EC.visibility_of_element_located(locator)))

        return self.driver.find_element(*locator)

    @allure.step("Вбиваем текст в элемент найденный по локатору")
    def send_keys_to_locator(self, locator, text):
        self.wait_and_find_element(locator).send_keys(text)

    @allure.step("Получаем текст элемента найденного по локатору")
    def get_text_locator(self, locator):
        return self.wait_and_find_element(locator).text

    @allure.step("Ждем пока элемент не станет кликабельным и кликаем по нему")
    def click_to_element(self, locator):

        WebDriverWait(self.driver, 10).until((EC.element_to_be_clickable(locator)))
        element = self.driver.find_element(*locator)

        attempt_count = 1000000
        for i in range(attempt_count):
            try:
                element.click()
                break
            except ElementClickInterceptedException:
                pass

    @allure.step("Открываем страницу по URL")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Проверяем что элемент отображается на странице")
    def check_element_is_displayed(self, locator):
        return self.wait_and_find_element(locator).is_displayed()

    @staticmethod
    @allure.step("Генерируем локатор из динамических данных")
    def format_locator(locator, param):
        search_type, search_text = locator

        return search_type, search_text.format(param)

    @allure.step("Возвращаем url текущей страницы")
    def return_page_url(self):
        return self.driver.current_url

    @allure.step("Перетягиваем элемент из одного локатора в другой")
    def drag_element_to_target(self, locator_from, locator_to):
        element_from = self.wait_and_find_element(locator_from)
        element_to = self.wait_and_find_element(locator_to)
        actions_chain = ActionChains(self.driver)
        actions_chain.drag_and_drop(element_from, element_to).pause(5).perform()

    @allure.step("Выполним скрипт")
    def execute_script(self, script, arg):
        self.driver.execute_script(script, arg)

    @allure.step("Авторизация пользователя")
    def login_user(self, new_user):
        base_page = BasePage(self.driver)
        base_page.open_page(Urls.LOGIN)
        base_page.send_keys_to_locator(LoginLocators.EMAIL_FIELD, new_user[1]["email"])
        base_page.send_keys_to_locator(LoginLocators.PASSWORD_FIELD, new_user[1]["password"])

        element = base_page.wait_and_find_element(LoginLocators.ENTER_BUTTON)
        base_page.execute_script("arguments[0].click();", element)

    @allure.step("Ожидание загрузки страницы")
    def wait_for_load_window(self, link):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(link))

    @allure.step("Ожидание кликабельности локатора")
    def wait_element_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))