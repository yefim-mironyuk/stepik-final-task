from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Choose language")


@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption("language")
    if user_language is None:
        user_language = 'en'
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print('\nStarting browser...')
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\nQuitting browser...')
    browser.quit()





