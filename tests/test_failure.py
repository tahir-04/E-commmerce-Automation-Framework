def test_fail(driver):

    driver.get(
        "https://www.google.com"
    )

    assert "Google" in driver.title