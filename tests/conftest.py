import pytest

from utilities.driver_factory import DriverFactory
from utilities.screenshot import ScreenshotUtil

@pytest.fixture()
def driver():

    driver = DriverFactory.get_driver()

    yield driver

    driver.quit()

@pytest.hookimpl(hookwrapper=True)

def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            ScreenshotUtil.capture(
                driver,
                item.name
            )