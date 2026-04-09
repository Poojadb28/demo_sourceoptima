import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.config import BASE_URL

@pytest.mark.order(15)
@pytest.mark.regression
def test_edit_details(browser, test_data):

    wait = WebDriverWait(browser, 20)

    browser.get(BASE_URL)

    email = test_data["system_admin_login"]["email"]
    password = test_data["system_admin_login"]["password"]

    login = LoginPage(browser)
    login.login(email, password)

    projects = ProjectsPage(browser)

    projects.open_projects()

    projects.right_click_space("TestSpace1")

    projects.click_edit_details()

    # Dynamic name to avoid conflicts
    updated_name = f"TestSpace_{int(time.time())}"

    projects.edit_space_name(updated_name)

    projects.change_icon()
    projects.select_purple_color()
    projects.save_changes()

    wait.until(lambda d: projects.verify_space_updated())

    assert projects.verify_space_updated(), "Space update failed"