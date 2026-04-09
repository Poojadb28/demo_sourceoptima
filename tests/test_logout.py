import pytest
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from config.config import BASE_URL

@pytest.mark.order(34)
@pytest.mark.smoke
def test_logout(browser, test_data):

    wait = WebDriverWait(browser, 20)

    browser.get(BASE_URL)

    email = test_data["logins"]["system_admin"]["email"]
    password = test_data["logins"]["system_admin"]["password"]

    login = LoginPage(browser)

    # Login
    login.login(email, password)

    # Logout
    login.logout()

    # Wait for login page again
    wait.until(lambda d: BASE_URL in d.current_url)