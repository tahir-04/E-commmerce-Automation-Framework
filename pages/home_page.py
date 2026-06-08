from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class HomePage(BasePage):

    HOME_LOGO = (
        By.ID,
        "nava"
    )

    def verify_home_page(self):

        return self.is_displayed(
            self.HOME_LOGO
        )