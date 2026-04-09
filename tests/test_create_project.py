import pytest
import os
import time
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.config import BASE_URL

@pytest.mark.order(10)
@pytest.mark.smoke
def test_create_project(browser, test_data):

    wait = WebDriverWait(browser, 20)

    browser.get(BASE_URL)

    email = test_data["system_admin_login"]["email"]
    password = test_data["system_admin_login"]["password"]

    login = LoginPage(browser)
    login.login(email, password)

    projects = ProjectsPage(browser)

    projects.open_projects()
    projects.open_root_space("TestSpace_1")

    # Dynamic name
    project_name = f"TestFile_{int(time.time())}"

    file_path = os.path.abspath("testdata/files/0254_3.zip")
    assert os.path.exists(file_path), "File not found"

    projects.create_project(project_name, file_path)

    wait.until(lambda d: projects.verify_project_created(project_name))

    assert projects.verify_project_created(project_name), "Project not created"