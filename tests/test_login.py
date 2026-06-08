from pages.login_page import LoginPage

def test_login(driver):

    driver.get(
        "https://www.demoblaze.com/"
    )

    login_page = LoginPage(driver)

    login_page.login(
        "testuser",
        "test123"
    )