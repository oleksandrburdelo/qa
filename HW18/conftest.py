import time

import pytest
from selenium.webdriver import Chrome

from HW18.pages.dashboard import Dashboard


@pytest.fixture(scope="session")
def driver() -> Chrome:
    driver = Chrome("../drivers/chromedriver")
    driver.maximize_window()
    driver.get("https://radarscreen.com.ua")
    time.sleep(2)
    yield driver

    driver.quit()


@pytest.fixture
def dashboard(driver) -> Dashboard:
    yield Dashboard(driver)