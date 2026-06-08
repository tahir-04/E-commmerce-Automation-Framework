import os
from datetime import datetime

class ScreenshotUtil:

    @staticmethod
    def capture(driver, name):

        os.makedirs(
            "screenshots",
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        filepath = (
            f"screenshots/"
            f"{name}_{timestamp}.png"
        )

        driver.save_screenshot(filepath)

        return filepath