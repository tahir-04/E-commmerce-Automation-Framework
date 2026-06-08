from utilities.driver_factory import DriverFactory

def test_browser_launch():

    driver = DriverFactory.get_driver()

    driver.get("https://www.google.com")

    assert "Google" in driver.title

    driver.quit()