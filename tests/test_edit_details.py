import pytest
import json
from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.config import BASE_URL

@pytest.mark.regression
def test_edit_details(browser):

    browser.get(BASE_URL)

    with open("testdata/login_data.json") as file:
        data = json.load(file)

    email = data["system_admin_login"]["email"]
    password = data["system_admin_login"]["password"]

    # Login
    login = LoginPage(browser)
    login.login(email, password)

    projects = ProjectsPage(browser)

    # Open Projects
    projects.open_projects()

    # Right click root space
    projects.right_click_space("TestSpace1")

    # Click Edit Details
    projects.click_edit_details()

    # Edit space name
    projects.edit_space_name("TestSpace_1")

    # Change icon
    projects.change_icon()

    # Select color
    projects.select_purple_color()

    # Save changes
    projects.save_changes()

    # Assertion
    assert projects.verify_space_updated(), "Space update failed"