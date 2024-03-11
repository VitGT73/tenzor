import shutil
import os
import pytest
from selenium import webdriver
from core.config.settings import Settings

# Imports to get chrome driver working
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Imports to get firefox driver working
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session", autouse=True)
def remove_download_directory():
    # Путь к папке, которую нужно удалить
    directory_path = Settings.DOWNLOAD_PATH

    # Удаление папки, если она существует
    if os.path.exists(directory_path):
        shutil.rmtree(directory_path)
        print(f"\nПапка {directory_path} успешно удалена перед началом тестов.")


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Send 'chrome' or 'firefox' as parameter for execution",
    )


@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    print('\nSELENIUM_GRID_USE: ', Settings.SELENIUM_GRID_USE)
    if Settings.SELENIUM_GRID_USE=='1':
        options.add_argument("--ignore-ssl-errors=yes")
        options.add_argument("--ignore-certificate-errors")
        driver = webdriver.Remote(
            command_executor="http://selenium-hub:4444/wd/hub", options=options
        )
    else:
        # For run in Docker
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        # Setup
        print(f"\nSetting up: {browser} driver")
        if browser == "firefox":
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install())
            )
        else:
            preferences = {
                "download.default_directory": Settings.DOWNLOAD_PATH,
            }
            options.add_experimental_option("prefs", preferences)

            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()), options=options
            )

    # Implicit wait setup for our framework
    driver.implicitly_wait(10)
    yield driver
    # Tear down
    print(f"\nTear down: {browser} driver")
    driver.quit()
