import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.system_admin_page import SystemAdminPage
from config.config import BASE_URL

@pytest.mark.order(2)
@pytest.mark.regression
def test_available_plays_enable_or_disable_actions(browser, test_data):

    wait = WebDriverWait(browser, 20)

    browser.get(BASE_URL)

    email = test_data["logins"]["system_admin"]["email"]
    password = test_data["logins"]["system_admin"]["password"]

    login = LoginPage(browser)
    login.login(email, password)

    admin = SystemAdminPage(browser)

    admin.open_user_admin()
    admin.scroll_to_available_plays()

    plays = [
        "Tariff Analysis",
        "Cost Reduction Analysis",
        "Design Review",
        "Drawing Checker - Both",
        "Drawing Checker - Veeco",
        "Drawing Checker - General"
    ]

    for play in plays:

        admin.toggle_play_by_name(play)

        wait.until(lambda d: "disabled" in admin.get_disable_success_message().lower())
        assert admin.get_disable_success_message() == "Play disabled successfully"

        admin.toggle_play_by_name(play)

        wait.until(lambda d: "enabled" in admin.get_enable_success_message().lower())
        assert admin.get_enable_success_message() == "Play enabled successfully"