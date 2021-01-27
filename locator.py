from selenium.webdriver.common.by import By

class Locators:
    sign_in_assert = (By.CLASS_NAME, "nav-line-1-container")
    SING_IN = (By.XPATH, "(//*[@class= 'nav-a nav-a-2   nav-progressive-attribute'])[1]")
    EMAIL = (By.ID, "ap_email")
    CONTINUE_BUTTON = (By.ID, "continue")
    PASSWORD = (By.ID, "ap_password")
    SING_IN_BUTTON = (By.ID, "signInSubmit")
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_SUBMIT_BUTTON = (By.ID, "nav-search-submit-button")
    SECOND_PAGE = (By.XPATH, "(//*[@class='a-normal'])[1]")
    SELECT_PRODUCT = (By.XPATH, "(//*[@class='a-size-medium a-color-base a-text-normal'])[3]")
    WISH_LIST_BUTTON = (By.ID, "add-to-wishlist-button-submit")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "WLHUC_continue")
    HOVER_ITEM = (By.ID, "nav-link-accountList")
    WISH_LIST = (By.CSS_SELECTOR, "#nav-flyout-wl-items > div > a > span")
    DELETE_ITEM = (By.CSS_SELECTOR,  ".g-move-delete-buttons > span")

    #ASSERT
    SEARCH_LIST = (By.CLASS_NAME, "s-result-item")