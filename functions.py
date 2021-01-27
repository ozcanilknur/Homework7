from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import Locators
from selenium.webdriver.common.action_chains import ActionChains
import unittest

class Functions(unittest.TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, email, password):
        self.wait.until(EC.presence_of_element_located(Locators.SING_IN)).click()
        self.wait.until(EC.presence_of_element_located(Locators.EMAIL)).send_keys(email)
        self.wait.until(EC.presence_of_element_located(Locators.CONTINUE_BUTTON)).click()
        self.wait.until(EC.presence_of_element_located(Locators.PASSWORD)).send_keys(password)
        self.wait.until(EC.presence_of_element_located(Locators.SING_IN_BUTTON)).click()

    def search(self, keyword):
        self.wait.until(EC.presence_of_element_located(Locators.SEARCH_BOX)).send_keys(keyword)
        self.wait.until(EC.presence_of_element_located(Locators.SEARCH_SUBMIT_BUTTON)).click()

    def category_page(self):
        self.wait.until(EC.presence_of_element_located(Locators.SEARCH_LIST))[0].is_displayed()
        self.wait.until(EC.element_to_be_clickable(Locators.SECOND_PAGE)).click()
        self.wait.until(EC.element_to_be_clickable(Locators.SELECT_PRODUCT)).click()

    def product_page(self):
        self.wait.until(EC.element_to_be_clickable(Locators.WISH_LIST_BUTTON)).click()
        self.wait.until(EC.presence_of_element_located(Locators.CONTINUE_SHOPPING_BUTTON)).click()

    def hoverClick(self):
        element_hover = self.driver.find_element_by_id("nav-link-accountList")
        hover = ActionChains(self.driver).move_to_element(element_hover)
        hover.perform()
        self.wait.until(EC.element_to_be_clickable(Locators.WISH_LIST)).click()

    def deleteWishList(self):
        self.wait.until(EC.presence_of_element_located(Locators.DELETE_ITEM)).click()
