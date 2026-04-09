import pytest
import json
import os
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from pages.drawing_checker_veeco_play_page import DrawingCheckerVeecoPage
from config.config import BASE_URL

@pytest.mark.order(25)
@pytest.mark.regression
def test_drawing_checker_veeco_play(browser, test_data):

    wait = WebDriverWait(browser, 20)

    browser.get(BASE_URL)

    login = LoginPage(browser)
    project = ProjectsPage(browser)
    veeco = DrawingCheckerVeecoPage(browser)

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

    veeco.select_drawing_checker_veeco()
    veeco.click_run()

    veeco.wait_for_processing()
    veeco.click_view_results()

    veeco.click_view_details()
    veeco.open_report_tab()

    veeco.download_report(download_dir)

    # Optional stability wait
    wait.until(lambda d: True)

    veeco.close_popup()