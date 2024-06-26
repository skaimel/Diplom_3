from selenium.webdriver.common.by import By


class FeedLocators:
    # Локаторы ленты заказов
    ORDER_NUMBER_IN_FEED = By.XPATH, "//p[contains(@class, 'text_type_digits-default')]"  # Номер заказа в ленте
    ORDER_INFO_TEXT = By.XPATH, "//p[contains(text(), 'Cостав')]"  # Текст 'Состав' в инфо о заказе
    ORDER_BY_ID = By.XPATH, "//a[@href='/feed/{}']"  # Шаблон локатора для поиска заказа по ID
    CREATED_ALL_TIME_ORDERS = By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p"  # Счетчик всех заказов
    CREATED_TODAY_ORDERS = By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p"  # Счетчик заказов сегодня
    ORDER_IN_PROGRESS = (By.XPATH, "//li[contains(@class, 'text_type_digits-default')]")  # Номер заказа в работе