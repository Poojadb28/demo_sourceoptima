import pytest
import json
from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.config import BASE_URL

@pytest.mark.smoke
def test_add_sub_space(browser):

    browser.get(BASE_URL)

    with open("testdata/login_data.json") as file:
        data = json.load(file)

    email = data["system_admin_login"]["email"]
    password = data["system_admin_login"]["password"]

    # Login
    login = LoginPage(browser)
    login.login(email, password)

    projects = ProjectsPage(browser)

    # Navigate
    projects.open_projects()

    projects.right_click_root_space("TestSpace1")

    projects.click_add_sub_space()

    sub_space_name = "TestSubSpace1"

    projects.enter_sub_space_name(sub_space_name)

    projects.choose_icon()

    projects.select_color()

    projects.click_create_space()

    # Assertion
    assert projects.verify_sub_space_created(sub_space_name), "Sub-space not created"