import pytest
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.config import BASE_URL

@pytest.mark.order(26)
@pytest.mark.smoke
def test_delete_file(browser, test_data):

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

    file_name = "0187.pdf"

    projects.delete_file(file_name)

    wait.until(lambda d: projects.is_file_deleted(file_name))

    assert projects.is_file_deleted(file_name)