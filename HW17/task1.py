"""Test commit to GitHub in HW17 branch"""
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


def test_01():
    driver = Chrome("./drivers/chromedriver")
    search_input_result_locator = "//input[@title='Поиск']"
    first_link_in_search_result_locator = "//h3[1]"
    watching_porn_locator = "//a[16]"

    driver.maximize_window()

    driver.get("https://google.com")
    search_input_field: WebElement = driver.find_element_by_xpath(search_input_result_locator)
    search_input_field.send_keys("pornhub")
    time.sleep(1)
    search_input_field.send_keys(Keys.ENTER)
    time.sleep(2)
    first_link_in_search_result: WebElement = driver.find_element_by_xpath(first_link_in_search_result_locator)
    first_link_in_search_result.click()
    watching_porn_result: WebElement.find_element_by_xpath(watching_porn_locator)
    watching_porn_result.click()

    time.sleep(3)



    driver.quit()
