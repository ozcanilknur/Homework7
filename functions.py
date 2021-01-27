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
        category_element = self.wait.until(EC.presence_of_element_located(Locators.SEARCH_LIST))
        self.assertEqual(1, category_element.is_displayed())

    def category_page(self):
        self.wait.until(EC.element_to_be_clickable(Locators.SECOND_PAGE)).click()
        category_page_two = self.wait.until(EC.presence_of_element_located(Locators.SECOND_PAGE_ASSERT)).text
        self.assertEqual(category_page_two, "2")
        self.wait.until(EC.element_to_be_clickable(Locators.SELECT_PRODUCT)).click()

    def product_page(self):
        product_name = self.wait.until(EC.presence_of_element_located(Locators.PRODUCT_NAME)).text
        self.wait.until(EC.element_to_be_clickable(Locators.WISH_LIST_BUTTON)).click()
        self.wait.until(EC.presence_of_element_located(Locators.CONTINUE_SHOPPING_BUTTON)).click()
        return str(product_name)

    def hoverClick(self, smt):
        element_hover = self.driver.find_element_by_id("nav-link-accountList")
        hover = ActionChains(self.driver).move_to_element(element_hover)
        hover.perform()
        self.wait.until(EC.element_to_be_clickable(Locators.WISH_LIST)).click()
        product_name_wishlist = self.wait.until(EC.presence_of_element_located(Locators.PRODUCT_NAME_WISH_LIST)).text
        self.assertEqual(product_name_wishlist, smt)

    def deleteWishList(self):
        self.wait.until(EC.presence_of_element_located(Locators.DELETE_ITEM)).click()
        deleted_product = self.wait.until(EC.presence_of_element_located(Locators.NO_PRODUCT))
        self.assertEqual(1, deleted_product.is_displayed())
