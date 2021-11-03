import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base_page import BasePage


class Dashboard(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.__open_popUP = "//span[text()='Завантажити додаток']"


    def change_lang_on_russian(self, name: str) -> None:
         time.sleep((1))
         self._click((By.XPATH, f"//a[text() = '{name}']"))

    def change_lang_on_english(self, name: str) -> None:
         time.sleep((2))
         self._click((By.XPATH, f"//a[text() = '{name}']"))

    def change_lang_on_ukrainian(self, name: str) -> None:
         time.sleep((2))
         self._click((By.XPATH, f"//a[text() = '{name}']"))

    def check_policy_service(self) -> None:
        self._scroll_page((By.XPATH, "//a[@href='https://docs.radarscreen.com.ua/docs/ua/polisy_servise.html']"))

    def check_policy(self) -> None:
        self._scroll_page((By.XPATH, "//a[@href='https://docs.radarscreen.com.ua/docs/ua/polisy.html']"))

    def check_rules(self) -> None:
        self._scroll_page((By.XPATH, "//a[@href='https://docs.radarscreen.com.ua/docs/ua/rules.html']"))

    def check_test_send_SMS(self) -> None:
        self._click((By.XPATH, f"//span[text()='Завантажити додаток']"))
        ((By.XPATH, f"//input[1]"))
        # input_field.send_keys("380996021362")
        # input_field.send_keys(Keys.ENTER)

        # input_field = ((By.XPATH, f"//input[1]"))
        # input_field.send_keys("380996021362")
        # input_field.send_keys(Keys.ENTER)





    #
    # def check_app_store_link(self) -> None:
    #     self._scroll_page((By.XPATH, "//a[@href='https://radar.onelink.me/dePw/market']/div/img"))
    #
    # def click(self):
    #     self._click((By.XPATH, "//a[@href='https://radar.onelink.me/dePw/market']/div/img"))
    #
    #     // a[ @ href = 'https://docs.radarscreen.com.ua/docs/ua/polisy_servise.html']




    # def choose_category(self, name: str) -> None:
    #     time.sleep((2))
    #     self._click((By.XPATH, f"//span[text()='{name}']/ancestor::div[1]"))

    # def choose_subcategory(self, name: str):
    #     self._click((By.XPATH, f"//span[text()='{name}']"))


