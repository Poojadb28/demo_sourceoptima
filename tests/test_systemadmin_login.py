import pytest
import json
from pages.login_page import LoginPage
from config.config import BASE_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.smoke
def test_system_admin_login(browser):

    wait = WebDriverWait(browser, 20)

    browser.get(BASE_URL)

    # Load test data
    with open("testdata/login_data.json") as file:
        data = json.load(file)

    email = data["system_admin_login"]["email"]
    password = data["system_admin_login"]["password"]

    login = LoginPage(browser)

    login.click_login_button()
    login.enter_email(email)
    login.enter_password(password)
    login.click_eye_icon()
    login.click_submit()

    expected_url = "https://testing.sourceoptima.com/system-admin"

    wait.until(EC.url_to_be(expected_url))

    assert browser.current_url == expected_url