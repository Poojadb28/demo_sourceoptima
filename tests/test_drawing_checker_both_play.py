import pytest
import json
from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from pages.drawing_checker_both_play_page import DrawingCheckerPage
from config.config import BASE_URL

@pytest.mark.regression
def test_drawing_checker_both_play(browser):

    browser.get(BASE_URL)

    login = LoginPage(browser)
    project = ProjectsPage(browser)
    drawing = DrawingCheckerPage(browser)

    # Load data
    with open("testdata/login_data.json") as file:
        data = json.load(file)

    email = data["system_admin_login"]["email"]
    password = data["system_admin_login"]["password"]

    download_dir = r"C:\Users\pooja.db\Downloads"

    # ---------------- FLOW ----------------

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