from pages.home_page import HomePage

def test_home_page(driver):

    driver.get(
        "https://www.demoblaze.com/"
    )

    home = HomePage(driver)

    assert home.verify_home_page()