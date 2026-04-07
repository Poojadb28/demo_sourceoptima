import pytest 
import json
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.config import BASE_URL

@pytest.mark.smoke
def test_create_new_project(browser):

    browser.get(BASE_URL)

    # Load login data
    with open("testdata/login_data.json") as file:
        data = json.load(file)

    email = data["system_admin_login"]["email"]
    password = data["system_admin_login"]["password"]

    # Login
    login = LoginPage(browser)
    login.login(email, password)

    # Wait for dashboard to load
    WebDriverWait(browser, 30).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(text(),'Projects')]")
        )
    )

    projects = ProjectsPage(browser)

    # Navigate to Projects
    projects.open_projects()

    # Right-click root space
    projects.right_click_root_space("TestSpace1")

    # Click Create New Project
    projects.click_create_new_project()

    # Enter project name
    project_name = "TestFile_1"
    projects.enter_project_name(project_name)

    # Upload file from project folder
    file_path = os.path.join(os.getcwd(), "testdata", "files", "0159.pdf")

    projects.upload_file(file_path)

    # Click upload
    projects.click_upload()

    # Verify project created
    assert projects.verify_project_created(project_name), "Project not created"