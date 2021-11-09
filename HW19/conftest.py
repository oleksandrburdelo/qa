import time
from pathlib import Path

import pytest
from selenium.webdriver import Chrome

from HW19.pages.home_page import HomePage


@pytest.fixture(scope="function")
def driver() -> Chrome:
    driver_folder = Path(__file__).parent / "drivers"
    driver_path = driver_folder / "chromedriver"
    driver = Chrome(driver_path)
    driver.maximize_window()
    yield driver

    time.sleep(25)

    driver.quit()


@pytest.fixture
def homepage(driver) -> HomePage:
    homepage = HomePage(driver)
    homepage.open()
    yield homepage