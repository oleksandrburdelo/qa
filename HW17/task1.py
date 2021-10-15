"""Test commit to GitHub in HW17 branch"""
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


def test_01():
    driver = Chrome("./drivers/chromedriver")
    search_input_result_locator = "//input[@title='Поиск']"
    first_link_in_search_result_locator = "//h3[1]"
    # watching_porn_locator = "//a[16]"
    all_cetegory_locator = "//li/a[@data-href='/categories']"
    japanise_category_locator = '//li[@data-category="111"]/div/a[@data-mxptext]/img'
    video_locator = '//li[@id="v395642351"]'
    ads_locator = '//div[@class="mgp_preRollSkipButton mgp_skipable"]'
    btn_maximaze_locator = '//div[@class="mgp_btn mgp_maximize mgp_icon mgp_icon-fullscreen"]'

    driver.maximize_window()

    driver.get("https://google.com")
    search_input_field: WebElement = driver.find_element_by_xpath(search_input_result_locator)
    search_input_field.send_keys("pornhub")
    time.sleep(1)
    search_input_field.send_keys(Keys.ENTER)
    time.sleep(2)
    first_link_in_search_result: WebElement = driver.find_element_by_xpath(first_link_in_search_result_locator)
    first_link_in_search_result.click()



    category = driver.find_element_by_xpath(all_cetegory_locator)
    category.click()

    time.sleep(2)
    japanise_block = driver.find_element_by_xpath(japanise_category_locator)
    japanise_block.click()
    time.sleep(2)

    ###This commands had to include video but in isn't working cause Hub had been updated new video collection###
    # hot_video = driver.find_element_by_xpath(video_locator)
    # hot_video.click()
    # time.sleep(3)

    ###This commands had to turn off ads when it available###
    # ads_button = driver.find_element_by_xpath(ads_locator)
    # ads_button.click()
    # # time.sleep(2)

    ###This commands had to turn on full screen video###
    # big_video = driver.find_element_by_xpath(btn_maximaze_locator)
    # big_video.click()
    time.sleep(300)



    driver.quit()
