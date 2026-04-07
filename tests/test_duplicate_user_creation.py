import pytest
import json
from pages.login_page import LoginPage
from pages.system_admin_page import SystemAdminPage
from config.config import BASE_URL

@pytest.mark.regression
def test_duplicate_create_user(browser):

    browser.get(BASE_URL)

    with open("testdata/user_data.json") as file:
        data = json.load(file)

    login_data = data["system_admin_login"]
    user_data = data["create_user"]

    login = LoginPage(browser)
    login.login(login_data["email"], login_data["password"])

    admin = SystemAdminPage(browser)

    admin.open_user_admin()

    admin.click_create_user()

    # Attempt to create the same user again
    admin.fill_user_details(
        user_data["full_name"],
        user_data["email"],   # same email already exists
        user_data["password"]
    )

    admin.submit_user()

    error_msg = admin.get_duplicate_user_error()

    assert error_msg == "Failed to create user"