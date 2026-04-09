import pytest
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.config import BASE_URL

@pytest.mark.order(19)
@pytest.mark.regression
def test_select_and_deselect_all_button(browser, test_data):

    wait = WebDriverWait(browser, 20)

    browser.get(BASE_URL)

    email = test_data["logins"]["system_admin"]["email"]
    password = test_data["logins"]["system_admin"]["password"]

    login = LoginPage(browser)
    login.login(email, password)

    projects = ProjectsPage(browser)

    projects.open_projects()
    projects.open_root_space("TestSpace_1")
    projects.open_project("TestFile")

    # Select all files
    projects.select_all_files()

    wait.until(lambda d: projects.verify_deselect_visible())

    assert projects.verify_deselect_visible(), "Deselect All button not visible"

    # Deselect all files
    projects.deselect_all_files()

    wait.until(lambda d: projects.verify_select_visible())

    assert projects.verify_select_visible(), "Select All button not visible again"