import pytest
import os

from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from utils.filter_utils import apply_filter, safe_clear_filter
from config.config import BASE_URL

@pytest.mark.order(17)
@pytest.mark.regression
def test_filter_labels(browser, test_data):

    # Ensure screenshots folder exists
    screenshots_dir = os.path.abspath("screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)

    # Open URL
    browser.get(BASE_URL)

    email = test_data["logins"]["system_admin"]["email"]
    password = test_data["logins"]["system_admin"]["password"]

    # Login
    login = LoginPage(browser)
    login.login(email, password)

    # Navigate to project
    projects = ProjectsPage(browser)
    projects.open_projects()
    projects.open_root_space("TestSpace1")
    projects.open_project("TestFile")

    dropdown = projects.get_filter_dropdown()

    # -------- All Labels --------
    apply_filter(browser, dropdown, "All Labels")

    WebDriverWait(browser, 10).until(lambda d: True)

    browser.save_screenshot(
        os.path.join(screenshots_dir, "All_Labels_Filter.png")
    )

    # -------- CAD Drawing Filter --------
    apply_filter(browser, dropdown, "CAD Drawing")

    WebDriverWait(browser, 10).until(lambda d: True)

    browser.save_screenshot(
        os.path.join(screenshots_dir, "CAD_Drawing_Filter.png")
    )

    safe_clear_filter(browser)

    # -------- Technical Specification --------
    apply_filter(browser, dropdown, "Technical Specification")

    WebDriverWait(browser, 10).until(lambda d: True)

    browser.save_screenshot(
        os.path.join(screenshots_dir, "Technical_Specification_Filter.png")
    )

    safe_clear_filter(browser)