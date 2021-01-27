from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import Locators
from functions import Functions


class Test(unittest.TestCase):
    def runProject(self):
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 10)
        driver.get("http://www.amazon.com")
        driver.maximize_window()
        assert 'Amazon.com' in driver.title
        time.sleep(3)
        functions = Functions(driver)
        functions.login("ilknur.ozcan@useinsider.com", "test123")
        time.sleep(3)
        functions.search("Samsung")
        functions.category_page()
        functions.product_page()
        time.sleep(3)
        functions.hoverClick()
        time.sleep(2)
        functions.deleteWishList()
        time.sleep(3)


test = Test()
test.runProject()
