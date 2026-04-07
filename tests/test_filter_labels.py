import pytest
import json
import os
import time

from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from utils.filter_utils import apply_filter, safe_clear_filter
from config.config import BASE_URL

@pytest.mark.regression
def test_filter_labels(browser):

    # Ensure screenshots folder exists
    screenshots_dir = os.path.join(os.getcwd(), "screenshots")

    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    browser.get(BASE_URL)

    with open("testdata/login_data.json") as file:
        data = json.load(file)

    email = data["system_admin_login"]["email"]
    password = data["system_admin_login"]["password"]

    # Login
    login = LoginPage(browser)
    login.login(email, password)

    projects = ProjectsPage(browser)

    projects.open_projects()
    projects.open_root_space("TestSpace1")
    projects.open_project("TestFile")

    dropdown = projects.get_filter_dropdown()

     # -------- All Labels --------
    apply_filter(browser, dropdown, "All Labels")
    time.sleep(6)

    browser.save_screenshot(
        os.path.join(screenshots_dir, "All_Labels_Filter.png")
    )

    # -------- CAD Drawing Filter --------
    apply_filter(browser, dropdown, "CAD Drawing")
    time.sleep(5)

    browser.save_screenshot(
        os.path.join(screenshots_dir, "CAD_Drawing_Filter.png")
    )

    safe_clear_filter(browser)


    # -------- Technical Specification --------
    apply_filter(browser, dropdown, "Technical Specification")
    time.sleep(8)

    browser.save_screenshot(
        os.path.join(screenshots_dir, "Technical_Specification_Filter.png")
    )

    safe_clear_filter(browser)

   