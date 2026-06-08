from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utilities.config_reader import ConfigReader
from utilities.logger import get_logger

log = get_logger()

class DriverFactory:

    @staticmethod
    def get_driver():

        browser = ConfigReader.get_browser()

        if browser.lower() == "chrome":

            log.info("Launching Chrome Browser")

            driver = webdriver.Chrome(
                service=Service(
                    ChromeDriverManager().install()
                )
            )

            log.info("Browser Launch Successful")

            driver.maximize_window()

            return driver
        else:
            log.error(f"Browser '{browser}' is not supported.")
            raise ValueError(f"Browser '{browser}' is not supported.")