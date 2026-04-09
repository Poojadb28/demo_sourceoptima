import pytest
import os
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from pages.drawing_checker_general_play_page import DrawingCheckerGeneralPage
from config.config import BASE_URL

@pytest.mark.order(24)
@pytest.mark.regression
def test_drawing_checker_general_play(browser, test_data):

    wait = WebDriverWait(browser, 20)

    browser.get(BASE_URL)

    login = LoginPage(browser)
    project = ProjectsPage(browser)
    general = DrawingCheckerGeneralPage(browser)

    email = test_data["logins"]["system_admin"]["email"]
    password = test_data["logins"]["system_admin"]["password"]

    # Jenkins-safe download directory
    download_dir = os.path.abspath("downloads")
    os.makedirs(download_dir, exist_ok=True)

    # ---------------- FLOW ----------------

    login.login(email, password)

    project.open_projects()
    project.open_root_space("TestSpace_1")
    project.open_project("TestFile")
    project.select_all_files()

    general.select_drawing_checker_general()
    general.click_run()

    general.wait_for_processing()
    general.click_view_results()

    general.click_view_details()
    general.open_report_tab()

    general.download_report(download_dir)

    # Optional stability wait
    wait.until(lambda d: True)

    general.close_popup()