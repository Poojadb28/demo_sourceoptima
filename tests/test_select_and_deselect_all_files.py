import pytest
import json
from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.config import BASE_URL


@pytest.mark.regression
def test_select_and_deselect_all_button(browser):

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
    projects.open_project("TestFile")

    # Select all files
    projects.select_all_files()
    assert projects.verify_deselect_visible(), "Deselect All button not visible"

    # Deselect all files
    projects.deselect_all_files()
    assert projects.verify_select_visible(), "Select All button not visible again"