import pytest
import json
from pages.login_page import LoginPage
from config.config import BASE_URL

@pytest.mark.regression
def test_user_invalid_login(browser):

    browser.get(BASE_URL)

    # Load test data
    with open("testdata/login_data.json") as file:
        data = json.load(file)

    email = data["user_invalid_login"]["email"]
    password = data["user_invalid_login"]["password"]

    login = LoginPage(browser)

    login.click_login_button()
    login.enter_email(email)
    login.enter_password(password)
    login.click_eye_icon()
    login.click_submit()

    error_msg = login.get_error_message()

    assert error_msg.strip() == "Error during login. Please try again.", \
        f"Expected 'Error during login. Please try again.', but got '{error_msg}'"