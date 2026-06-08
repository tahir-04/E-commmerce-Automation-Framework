from utilities.driver_factory import DriverFactory
from utilities.screenshot import ScreenshotUtil

def test_screenshot():

    driver = DriverFactory.get_driver()

    driver.get("https://www.demoblaze.com")

    ScreenshotUtil.capture(
        driver,
        "homepage"
    )

    driver.quit()