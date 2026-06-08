from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class CartPage(BasePage):

    CART_LINK = (
        By.ID,
        "cartur"
    )

    PLACE_ORDER = (
        By.XPATH,
        "//button[text()='Place Order']"
    )

    def open_cart(self):

        self.click(
            self.CART_LINK
        )

    def click_place_order(self):

        self.click(
            self.PLACE_ORDER
        )