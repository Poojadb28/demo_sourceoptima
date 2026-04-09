import pytest
import os
import time
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.config import BASE_URL

@pytest.mark.order(13)
@pytest.mark.smoke
def test_add_new_project(browser, test_data):

    browser.get(BASE_URL)

    #  Use fixture instead of file open
    email = test_data["system_admin_login"]["email"]
    password = test_data["system_admin_login"]["password"]

    # Login
    login = LoginPage(browser)
    login.login(email, password)

    projects = ProjectsPage(browser)

    projects.open_projects()
    projects.open_root_space("TestSpace1")

    # Unique project name (avoid duplicate failure)
    project_name = f"TestFile_{int(time.time())}"

    projects.click_new_upload()
    projects.enter_project_name(project_name)

    file_name = "0194.pdf"

    # Jenkins-safe path
    file_path = os.path.abspath(f"testdata/{file_name}")

    assert os.path.exists(file_path), "File not found in testdata folder"

    projects.upload_file(file_path)
    projects.click_upload()

    # Wait for project creation
    WebDriverWait(browser, 20).until(
        lambda d: projects.verify_project_created(project_name)
    )

    assert projects.verify_project_created(project_name), "Project not created"