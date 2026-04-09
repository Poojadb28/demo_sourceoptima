import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.config import BASE_URL

@pytest.mark.order(9)
@pytest.mark.smoke
def test_create_root_space(browser, test_data):

    wait = WebDriverWait(browser, 20)

    browser.get(BASE_URL)

    email = test_data["system_admin_login"]["email"]
    password = test_data["system_admin_login"]["password"]

    login = LoginPage(browser)
    login.login(email, password)

    projects = ProjectsPage(browser)

    projects.open_projects()
    projects.right_click_projects_area()

    projects.click_new_root_space()

    # Dynamic name
    space_name = f"TestSpace_{int(time.time())}"

    projects.enter_space_name(space_name)
    projects.choose_icon()
    projects.select_blue_color()
    projects.click_create_space()

    wait.until(lambda d: "success" in projects.get_success_message().lower())

    assert projects.get_success_message() == "Space created successfully!"