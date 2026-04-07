import pytest
import json
from pages.login_page import LoginPage
from pages.system_admin_page import SystemAdminPage
from config.config import BASE_URL

@pytest.mark.regression
def test_export_credit_history(browser):

    browser.get(BASE_URL)

    # Load test data
    with open("testdata/login_data.json") as file:
        data = json.load(file)

    email = data["system_admin_login"]["email"]
    password = data["system_admin_login"]["password"]

    # Perform login
    login = LoginPage(browser)
    login.login(email, password)

    admin = SystemAdminPage(browser)

    admin.open_user_admin()

    download_dir = r"C:\Users\pooja.db\Downloads"

    admin.click_export_credit_history()

    admin.wait_for_credit_history_download(download_dir)