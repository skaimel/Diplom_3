import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from urls import Urls
import helpers


class MainPage(BasePage):

    @allure.step("Клик по кнопке личный кабинет")
    def click_to_personal_area(self):
        self.click_to_element(MainPageLocators.PERSONAL_AREA_BUTTON)
        self.wait_for_load_window(Urls.PERSONAL_AREA)

        return self.return_page_url()

    @allure.step("Клик по кнопке лента заказов")
    def click_to_orders_feed(self):
        self.click_to_element(MainPageLocators.ORDERS_FEED_BUTTON)
        self.wait_for_load_window(Urls.ORDER_FEED)

        return self.return_page_url()

    @allure.step("Клик по ингредиенту")
    def click_to_ingredient(self, ingredient_id):
        self.open_page(Urls.MAIN)
        self.click_to_element(self.format_locator(MainPageLocators.INGREDIENT, ingredient_id))

        return self.get_text_locator(MainPageLocators.INGREDIENT_DETAILS_TEXT)

    @allure.step("Клик по ингредиенту и закрытие окна с информацией об ингредиенте")
    def click_to_ingredient_and_close(self):
        self.open_page(Urls.MAIN)
        self.click_to_element(MainPageLocators.BUN_R2_D3)

        self.click_to_element(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)
        self.wait_element_clickable(MainPageLocators.INGREDIENT_DETAILS_TEXT)

        return self.check_element_is_displayed(MainPageLocators.ORDERS_FEED_BUTTON)

    @allure.step("Добавление ингредиента 'Флюоресцентная булка R2-D3 'в заказ")
    def add_bun_to_order(self):
        self.open_page(Urls.MAIN)
        ingredient_id = helpers.Order.get_ingredients()[1][0]  # Получаем первый элемент списка ингредиентов
        ingredient_locator = self.format_locator(MainPageLocators.INGREDIENT, ingredient_id)
        self.drag_element_to_target(ingredient_locator, MainPageLocators.ORDER_BOX)

    @allure.step("Проверка, что счетчик ингредиента увеличивается при добавлении его в заказ")
    def check_counter_of_ingredient(self):
        self.open_page(Urls.MAIN)
        ingredient_id = helpers.Order.get_ingredients()[1][0]  # Получаем первый элемент списка ингредиентов

        ingredient_locator = self.format_locator(MainPageLocators.INGREDIENT, ingredient_id)
        ingredient_count_locator = self.format_locator(MainPageLocators.INGREDIENT_COUNTER, ingredient_id)
        ingredient_count_before = self.get_text_locator(ingredient_count_locator)

        self.drag_element_to_target(ingredient_locator, MainPageLocators.ORDER_BOX)

        ingredient_count_after = self.get_text_locator(ingredient_count_locator)

        return ingredient_count_before < ingredient_count_after

    @allure.step("Нажатие на кнопку 'Оформить заказ'")
    def create_order(self):
        self.click_to_element(MainPageLocators.CREATE_ORDER_BUTTON)

        return self.check_element_is_displayed(MainPageLocators.ORDER_ID_TEXT)