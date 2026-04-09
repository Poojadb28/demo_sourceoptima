import pytest
import os

from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from pages.drawing_checker_both_play_page import DrawingCheckerPage
from config.config import BASE_URL

@pytest.mark.order(23)
@pytest.mark.regression
def test_drawing_checker_both_play(browser, test_data):

    browser.get(BASE_URL)

    login = LoginPage(browser)
    project = ProjectsPage(browser)
    drawing = DrawingCheckerPage(browser)

    email = test_data["logins"]["system_admin"]["email"]
    password = test_data["logins"]["system_admin"]["password"]

    download_dir = os.path.abspath("downloads")
    os.makedirs(download_dir, exist_ok=True)

    login.login(email, password)

    project.open_projects()
    project.open_root_space("TestSpace_1")
    project.open_project("TestFile")
    project.select_all_files()

    drawing.select_drawing_checker()
    drawing.click_run()

    drawing.wait_for_processing()
    drawing.click_view_results()

    drawing.click_view_details()
    drawing.open_report_tab()

    drawing.download_report(download_dir)

    drawing.close_popup()