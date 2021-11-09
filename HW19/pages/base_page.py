from selenium.webdriver.chrome.webdriver import WebDriver

from HW19.core.cookie import Cookie
from HW19.core.local_storage import LocalStorage


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._base_url = "https://radarscreen.com.ua"
        self._cookie = Cookie(self._driver)
        self._local_storage = LocalStorage(self._driver)