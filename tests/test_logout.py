import pytest
import json
from pages.login_page import LoginPage
from config.config import BASE_URL

@pytest.mark.smoke
def test_logout(browser):

    browser.get(BASE_URL)

    # Load login data
    with open("testdata/login_data.json") as file:
        data = json.load(file)

    email = data["system_admin_login"]["email"]
    password = data["system_admin_login"]["password"]

    login = LoginPage(browser)

    # Login
    login.login(email, password)

    # Logout
    login.logout()