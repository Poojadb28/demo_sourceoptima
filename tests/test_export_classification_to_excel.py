import pytest
import json
import os
from selenium.webdriver.support.ui import WebDriverWait
from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.config import BASE_URL

@pytest.mark.regression
def test_export_classification_to_excel(browser):

    browser.get(BASE_URL)

    # Load login data
    with open("testdata/login_data.json") as file:
        data = json.load(file)

    email = data["system_admin_login"]["email"]
    password = data["system_admin_login"]["password"]

    # Login
    login = LoginPage(browser)
    login.login(email, password)

    projects = ProjectsPage(browser)

    # Navigate to project
    projects.open_projects()

    projects.open_root_space("TestSpace1")

    projects.open_project("TestFile")

    # Click Export Classification
    projects.click_export_classification()

    # Download folder
    download_dir = r"C:\Users\pooja.db\Downloads"

    # Wait for download
    WebDriverWait(browser, 120).until(
        lambda driver: projects.is_classification_downloaded(download_dir)
    )

    # Assertion
    assert projects.is_classification_downloaded(download_dir), \
        "Classification Excel file was not downloaded"