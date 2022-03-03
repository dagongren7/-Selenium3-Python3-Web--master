from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

def driver_init():
    driver.get("http://www.5itest.cn/register") #打开页面
    driver.maximize_window() #窗口最大化
    time.sleep(5)

def keysTab():
    driver_init()
    ActionChains(driver).send_keys(Keys.TAB).perform()

keysTab()