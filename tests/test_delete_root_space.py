import pytest
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.config import BASE_URL

@pytest.mark.order(28)
@pytest.mark.smoke
def test_delete_root_space(browser, test_data):

    wait = WebDriverWait(browser, 20)

    browser.get(BASE_URL)

    email = test_data["logins"]["system_admin"]["email"]
    password = test_data["logins"]["system_admin"]["password"]

    login = LoginPage(browser)
    login.login(email, password)

    projects = ProjectsPage(browser)

    projects.open_projects()

    space_name = "TestSpace_1"

    projects.right_click_space(space_name)
    projects.click_delete_space()
    projects.accept_delete_alert()

    wait.until(lambda d: projects.verify_space_deleted(space_name))

    assert projects.verify_space_deleted(space_name)