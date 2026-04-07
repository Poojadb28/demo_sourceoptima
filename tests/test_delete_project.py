import pytest
import json
from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.config import BASE_URL

@pytest.mark.smoke
def test_delete_project(browser):

    browser.get(BASE_URL)

    with open("testdata/login_data.json") as file:
        data = json.load(file)

    email = data["system_admin_login"]["email"]
    password = data["system_admin_login"]["password"]

    # Login
    login = LoginPage(browser)
    login.login(email, password)

    projects = ProjectsPage(browser)

    projects.open_projects()

    projects.open_root_space("TestSpace1")

    projects.open_project("TestFile_1")

    # Delete project
    projects.click_delete_project()

    projects.confirm_delete()

    assert projects.verify_project_deleted(), "Project deletion failed"