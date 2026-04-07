import pytest
import json
from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.config import BASE_URL


# def test_create_project(browser):

#     browser.get(BASE_URL)

#     with open("testdata/login_data.json") as file:
#         data = json.load(file)

#     email = data["system_admin_login"]["email"]
#     password = data["system_admin_login"]["password"]

#     login = LoginPage(browser)
#     login.login(email, password)

#     projects = ProjectsPage(browser)

#     projects.open_projects()

#     projects.open_root_space("TestSpace_1")

#     projects.click_new_upload()

#     project_name = "TestFile"

#     projects.enter_project_name(project_name)

#     projects.upload_file(r"C:\Users\pooja.db\Downloads\0254 3.zip")

#     projects.click_upload()

#     assert projects.verify_project_created(project_name)

@pytest.mark.smoke
def test_create_project(browser):

    browser.get(BASE_URL)

    with open("testdata/login_data.json") as file:
        data = json.load(file)

    email = data["system_admin_login"]["email"]
    password = data["system_admin_login"]["password"]

    login = LoginPage(browser)
    login.login(email, password)

    projects = ProjectsPage(browser)

    projects.open_projects()
    projects.open_root_space("TestSpace_1")

    project_name = "TestFile"

    projects.create_project(
        project_name,
        r"C:\Users\pooja.db\Downloads\0254 3.zip"
    )

    assert projects.verify_project_created(project_name), \
        "Project not created"