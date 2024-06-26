from selenium.webdriver.common.by import By


class LoginLocators:
    # Локаторы авторизации
    RECOVER_PASSWORD = By.XPATH, "//a[contains(text(), 'Восстановить пароль')]"  # Кнопка восстановления пароля
    EMAIL_FIELD = By.XPATH, "//label[contains(text(), 'Email')]/parent::div/input"  # Поле ввоода email
    PASSWORD_FIELD = By.XPATH, "//label[contains(text(), 'Пароль')]/parent::div/input"  # Поле ввоода password
    ENTER_BUTTON = By.XPATH, "//button[contains(text(), 'Войти')]"  # Кнопка "Войти"