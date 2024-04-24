import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as ServiceFireFox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FireFoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Select a language using the command: --language= ")


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == 'chrome':
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    if browser_name == 'firefox':
        print("\nstart firefox browser for test..")
        options = FireFoxOptions()
        options.set_preference("intl.accept_languages", user_language)
        service = ServiceFireFox(
            executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)

    yield driver
    print("\nquit browser..")
    driver.quit()
