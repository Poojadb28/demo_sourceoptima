import pytest
import json
from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.config import BASE_URL

@pytest.mark.regression
def test_upload_new_file(browser):

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

    projects.click_new_upload()

    file_name = "0187.pdf"

    projects.upload_new_file(r"C:\Users\pooja.db\Downloads\0187.pdf")

    projects.click_upload()

    assert projects.verify_file_uploaded(file_name), "New file not uploaded"