import pytest
import os
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.config import BASE_URL


@pytest.mark.order(14)
@pytest.mark.regression
def test_upload_new_file(browser, test_data):

    browser.get(BASE_URL)

    #  Use fixture instead of file open
    email = test_data["logins"]["system_admin"]["email"]
    password = test_data["logins"]["system_admin"]["password"]

    login = LoginPage(browser)
    login.login(email, password)

    projects = ProjectsPage(browser)

    projects.open_projects()
    projects.open_root_space("TestSpace1")
    projects.open_project("TestFile_1")

    projects.click_new_upload()

    file_name = "0187.pdf"

    # Jenkins-safe absolute path
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR, "testdata", file_name)

    assert os.path.exists(file_path), "File not found in testdata folder"

    projects.upload_new_file(file_path)
    projects.click_upload()

    # Wait after upload
    WebDriverWait(browser, 20).until(
        lambda d: projects.verify_file_uploaded(file_name)
    )

    assert projects.verify_file_uploaded(file_name), "New file not uploaded"