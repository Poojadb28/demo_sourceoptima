import pytest
import os
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.config import BASE_URL

@pytest.mark.order(16)
@pytest.mark.regression
def test_export_classification_to_excel(browser, test_data):

    wait = WebDriverWait(browser, 30)

    browser.get(BASE_URL)

    email = test_data["system_admin_login"]["email"]
    password = test_data["system_admin_login"]["password"]

    login = LoginPage(browser)
    login.login(email, password)

    projects = ProjectsPage(browser)

    projects.open_projects()
    projects.open_root_space("TestSpace1")
    projects.open_project("TestFile")

    projects.click_export_classification()

    # Jenkins-safe download dir
    download_dir = os.path.abspath("downloads")
    os.makedirs(download_dir, exist_ok=True)

    wait.until(lambda d: projects.is_classification_downloaded(download_dir))

    assert projects.is_classification_downloaded(download_dir), \
        "Classification Excel file was not downloaded"