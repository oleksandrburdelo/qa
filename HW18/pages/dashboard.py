from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from .base_page import BasePage


class Dashboard(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)


    def change_lang_on_russian(self, name: str) -> None:
         self._click((By.XPATH, f"//a[text() = '{name}']"))

    def change_lang_on_english(self, name: str) -> None:
         self._click((By.XPATH, f"//a[text() = '{name}']"))

    def change_lang_on_ukrainian(self, name: str) -> None:
         self._click((By.XPATH, f"//a[text() = '{name}']"))

    def check_policy_service(self) -> None:
        self._scroll_page((By.XPATH, "//a[@href='https://docs.radarscreen.com.ua/docs/ua/polisy_servise.html']"))

    def check_policy(self) -> None:
        self._scroll_page((By.XPATH, "//a[@href='https://docs.radarscreen.com.ua/docs/ua/polisy.html']"))

    def check_rules(self) -> None:
        self._scroll_page((By.XPATH, "//a[@href='https://docs.radarscreen.com.ua/docs/ua/rules.html']"))

    def check_test_send_SMS(self) -> None:
        self._click((By.XPATH, f"//span[text()='Завантажити додаток']"))
        self._send_keys((By.XPATH, f"//input[1]"), "380996021362")
        self._send_enter((By.XPATH, f"//input[1]"))
