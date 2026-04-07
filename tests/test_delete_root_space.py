import pytest
import json
from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.config import BASE_URL

@pytest.mark.smoke
def test_delete_root_space(browser):

    browser.get(BASE_URL)

    # Load login data
    with open("testdata/login_data.json") as file:
        data = json.load(file)

    email = data["system_admin_login"]["email"]
    password = data["system_admin_login"]["password"]

    # Login
    login = LoginPage(browser)
    login.login(email, password)

    projects = ProjectsPage(browser)

    # Navigate to Projects
    projects.open_projects()

    space_name = "TestSpace_2"

    # Right click on space
    projects.right_click_space(space_name)

    # Click Delete option
    projects.click_delete_space()

    # Accept browser alert
    projects.accept_delete_alert()

    # Verify deletion
    assert projects.verify_space_deleted(space_name), "Space deletion failed"