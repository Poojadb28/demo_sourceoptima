import pytest
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.config import BASE_URL

@pytest.mark.order(27)
@pytest.mark.smoke
def test_delete_project(browser, test_data):

    wait = WebDriverWait(browser, 20)

    browser.get(BASE_URL)

    email = test_data["logins"]["system_admin"]["email"]
    password = test_data["logins"]["system_admin"]["password"]

    login = LoginPage(browser)
    login.login(email, password)

    projects = ProjectsPage(browser)

    projects.open_projects()
    projects.open_root_space("TestSpace_1")
    projects.open_project("TestFile_1")

    projects.click_delete_project()
    projects.confirm_delete()

    wait.until(lambda d: projects.verify_project_deleted())

    assert projects.verify_project_deleted()