from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class ProductPage(BasePage):

    ADD_TO_CART = (
        By.XPATH,
        "//a[text()='Add to cart']"
    )

    def add_product_to_cart(self):

        self.click(
            self.ADD_TO_CART
        )