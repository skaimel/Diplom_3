import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from helpers import NewUserCreds, User
from pages.main_page import MainPage


@pytest.fixture(scope='function', params=["chrome", "firefox"])
def get_driver(request):
    driver = None
    if request.param == "chrome":
        options = ChromeOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif request.param == "firefox":
        options = FirefoxOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def get_new_user():
    new_user_creds = NewUserCreds.generate_creds_set()
    new_user_response = User.create_user(new_user_creds)

    yield new_user_response, new_user_creds
    User.delete_user(new_user_response.json()["accessToken"])


@pytest.fixture(scope='function')
def get_logged_driver(get_driver, get_new_user):

    main_page = MainPage(get_driver)
    main_page.login_user(get_new_user)