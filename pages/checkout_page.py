from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class CheckoutPage(BasePage):

    NAME = (
        By.ID,
        "name"
    )

    COUNTRY = (
        By.ID,
        "country"
    )

    CITY = (
        By.ID,
        "city"
    )

    CARD = (
        By.ID,
        "card"
    )

    MONTH = (
        By.ID,
        "month"
    )

    YEAR = (
        By.ID,
        "year"
    )

    PURCHASE = (
        By.XPATH,
        "//button[text()='Purchase']"
    )

    def complete_checkout(
        self,
        name,
        country,
        city,
        card,
        month,
        year
    ):

        self.type(self.NAME, name)
        self.type(self.COUNTRY, country)
        self.type(self.CITY, city)
        self.type(self.CARD, card)
        self.type(self.MONTH, month)
        self.type(self.YEAR, year)

        self.click(self.PURCHASE)