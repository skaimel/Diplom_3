from selenium.webdriver.common.by import By


class MainPageLocators:
    # Локаторы главной страницы
    PERSONAL_AREA_BUTTON = By.XPATH, "//p[contains(text(), 'Личный Кабинет')]"  # Кнопка личного кабинета
    ORDERS_FEED_BUTTON = By.XPATH, "//p[contains(text(), 'Лента Заказов')]"  # Кнопка ленты заказов
    INGREDIENT = By.XPATH, "//a[@href='/ingredient/{}']"  # Шаблон локатора ингредиента из конструктора
    INGREDIENT_COUNTER = By.XPATH, "//a[@href='/ingredient/{}']/div/p"  # Шаблон локаторы счетчика ингредиента

    INGREDIENT_DETAILS_TEXT = By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]"  # Текст с инфо об ингредиенте
    CLOSE_INGREDIENT_DETAILS_BUTTON = By.XPATH, "//button[contains(@class, '_close')]"  # Крестик закрытия окна
    BUN_R2_D3 = By.XPATH, "//p[contains(text(), 'Флюоресцентная булка R2-D3')]"  # Локатор булочки

    ORDER_BOX = (By.XPATH, ".//div[contains(@class, 'constructor-element_pos_top')]")  # Корзина заказа
    ORDER_ID_TEXT = By.XPATH, "//p[contains(text(), 'идентификатор заказа')]"  # Текст идентификатор заказа
    CREATE_ORDER_BUTTON = By.XPATH, "//button[contains(text(), 'Оформить заказ')]"  # Кнопка оформления заказа