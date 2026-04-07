import pytest
import json
from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.config import BASE_URL

@pytest.mark.smoke
def test_create_root_space(browser):

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

    projects.open_projects()

    projects.right_click_projects_area()

    projects.click_new_root_space()

    projects.enter_space_name("TestSpace1")

    projects.choose_icon()

    projects.select_blue_color()

    projects.click_create_space()

    success_msg = projects.get_success_message()

    assert success_msg == "Space created successfully!"