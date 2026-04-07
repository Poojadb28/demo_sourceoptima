import pytest
import json
from pages.login_page import LoginPage
from pages.system_admin_page import SystemAdminPage
from config.config import BASE_URL

@pytest.mark.regression
def test_available_plays_enable_or_disable_actions(browser):

    browser.get(BASE_URL)

    # Load login data
    with open("testdata/login_data.json") as file:
        data = json.load(file)

    email = data["system_admin_login"]["email"]
    password = data["system_admin_login"]["password"]

    # Login
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

        # Disable play
        admin.toggle_play_by_name(play)
        assert admin.get_disable_success_message() == "Play disabled successfully"

        # Enable play
        admin.toggle_play_by_name(play)
        assert admin.get_enable_success_message() == "Play enabled successfully"