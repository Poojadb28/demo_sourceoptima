import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from config.config import BASE_URL

@pytest.mark.order(30)
@pytest.mark.smoke
def test_admin_login(browser, test_data):

    wait = WebDriverWait(browser, 20)

    browser.get(BASE_URL)

    email = test_data["logins"]["admin"]["email"]
    password = test_data["logins"]["admin"]["password"]

    login = LoginPage(browser)

    # Wait for login page ready
    wait.until(EC.presence_of_element_located(login.USERNAME_INPUT))

    login.click_login_button()
    login.enter_email(email)
    login.enter_password(password)
    login.click_eye_icon()
    login.click_submit()

    expected_url = f"{BASE_URL}admin/dashboard"

    # Wait for navigation
    wait.until(EC.url_contains("dashboard"))

    assert "dashboard" in browser.current_url