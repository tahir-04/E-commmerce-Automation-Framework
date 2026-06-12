from selenium.webdriver.common.by import By
from pages.base_page import BasePage

from utilities.logger import get_logger

log = get_logger()

WELCOME_USER = (
    By.ID,
    "nameofuser"
)

def get_logged_user(self):

    return self.get_text(
        self.WELCOME_USER
    )

class LoginPage(BasePage):

    LOGIN_MENU = (By.ID, "login2")

    USERNAME = (By.ID, "loginusername")

    PASSWORD = (By.ID, "loginpassword")

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[text()='Log in']"
    )

    def open_login_popup(self):

        self.click(self.LOGIN_MENU)

    def enter_username(self, username):

        self.type(
            self.USERNAME,
            username
        )

    def enter_password(self, password):

        self.type(
            self.PASSWORD,
            password
        )

    def click_login(self):

        self.click(
            self.LOGIN_BUTTON
        )

    def login(self, username, password):

        self.open_login_popup()

        self.enter_username(username)

        self.enter_password(password)

        self.click_login()