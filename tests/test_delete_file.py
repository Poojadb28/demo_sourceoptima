import pytest
import pytest
import json
from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.config import BASE_URL

@pytest.mark.smoke
def test_delete_file(browser):

    browser.get(BASE_URL)

    with open("testdata/login_data.json") as file:
        data = json.load(file)

    email = data["system_admin_login"]["email"]
    password = data["system_admin_login"]["password"]

    login = LoginPage(browser)
    login.login(email, password)

    projects = ProjectsPage(browser)

    projects.open_projects()

    projects.open_root_space("TestSpace1")

    projects.open_project("TestFile_1")

    file_name = "0187.pdf"

    projects.delete_file(file_name)

    assert projects.is_file_deleted(file_name), "File deletion failed"