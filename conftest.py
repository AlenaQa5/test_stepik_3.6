import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store',
                     default=None, help="Choose language: ru or fr or es")


@pytest.fixture(scope="function")
def browser():
    print("\n start browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\n quit from browser..")
    browser.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="fr", help="Chose language : fr or es"
    )
@pytest.fixture
def language(request):
    return request.config.getoption("--language")