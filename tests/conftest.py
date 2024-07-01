import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from helpers import NewUserCreds, User
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeed
from pages.password_page import PasswordPage


@pytest.fixture(scope='function', params=["chrome", "firefox"])
def get_driver(request):
    driver = None
    if request.param == "chrome":
        options = ChromeOptions()
        options.add_argument('--window-size=1024,768')
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.set_window_size(1920, 1080)
    elif request.param == "firefox":
        options = FirefoxOptions()
        options.add_argument('--window-size=1024,768')
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        driver.set_window_size(1920, 1080)

    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def get_new_user():
    new_user_creds = NewUserCreds.generate_creds_set()
    new_user_response = User.create_user(new_user_creds)
    if 'accessToken' not in new_user_response.json():
        pytest.fail("User creation failed, 'accessToken' not found in response.")

    yield new_user_response, new_user_creds
    User.delete_user(new_user_response.json()["accessToken"])


@pytest.fixture(scope='function')
def get_logged_driver(get_driver, get_new_user):
    main_page = MainPage(get_driver)
    main_page.login_user(get_new_user)
    yield get_driver


@pytest.fixture(scope="function")
def get_account_page(get_logged_driver):
    return AccountPage(get_logged_driver)


@pytest.fixture(scope='function')
def get_login_page(get_driver):
    return LoginPage(get_driver)


@pytest.fixture(scope='function')
def get_main_page(get_driver):
    return MainPage(get_driver)


@pytest.fixture(scope='function')
def get_order_feed_instance(get_driver):
    return OrderFeed(get_driver)


@pytest.fixture(scope="function")
def get_password_page_instance(get_driver):
    return PasswordPage(get_driver)
