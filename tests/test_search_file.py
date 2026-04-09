import pytest
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.config import BASE_URL

@pytest.mark.order(18)
@pytest.mark.regression
def test_search_field(browser, test_data):

    wait = WebDriverWait(browser, 20)

    browser.get(BASE_URL)

    email = test_data["system_admin_login"]["email"]
    password = test_data["system_admin_login"]["password"]

    login = LoginPage(browser)
    login.login(email, password)

    projects = ProjectsPage(browser)

    projects.open_projects()
    projects.open_root_space("TestSpace1")
    projects.open_project("TestFile")

    search_value = "0187.pdf"

    projects.search_file(search_value)

    wait.until(lambda d: projects.verify_file_present(search_value))

    assert projects.verify_file_present(search_value), "Searched file not displayed"