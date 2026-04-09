import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from config.config import BASE_URL

@pytest.mark.order(29)
@pytest.mark.regression
def test_system_admin_invalid_login(browser, test_data):

    wait = WebDriverWait(browser, 20)

    browser.get(BASE_URL)

    email = test_data["system_admin_invalid_login"]["email"]
    password = test_data["system_admin_invalid_login"]["password"]

    login = LoginPage(browser)

    # Wait for login page ready
    wait.until(EC.presence_of_element_located(login.USERNAME_INPUT))

    login.click_login_button()
    login.enter_email(email)
    login.enter_password(password)
    login.click_eye_icon()
    login.click_submit()

    error_msg = login.get_error_message()

    assert error_msg.strip() == "Error during login. Please try again.", \
        f"Expected 'Error during login. Please try again.', but got '{error_msg}'"