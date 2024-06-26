import allure

from locators.account_page_locators import AccountLocators
from pages.base_page import BasePage
from urls import Urls


class AccountPage(BasePage):

    @allure.step("Клик по истории заказов в личном кабинете")
    def click_to_order_history(self):
        self.click_to_element(AccountLocators.PERSONAL_AREA_BUTTON)
        self.click_to_element(AccountLocators.ORDER_HISTORY)

        return self.return_page_url()

    @allure.step("Клик по кнопке выход в личном кабинете")
    def click_to_exit_button(self):
        self.click_to_element(AccountLocators.PERSONAL_AREA_BUTTON)
        self.click_to_element(AccountLocators.EXIT_BUTTON)
        self.wait_for_load_window(Urls.LOGIN)

        return self.return_page_url()

    @allure.step("Клик по кнопке конструктор")
    def click_to_constructor_button(self):
        self.click_to_element(AccountLocators.PERSONAL_AREA_BUTTON)
        self.click_to_element(AccountLocators.CONSTRUCTOR_BUTTON)

        return self.return_page_url()