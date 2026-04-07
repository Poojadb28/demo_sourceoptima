import pytest
import json
from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from pages.drawing_checker_veeco_play_page import DrawingCheckerVeecoPage
from config.config import BASE_URL

@pytest.mark.regression
def test_drawing_checker_veeco_play(browser):

    browser.get(BASE_URL)

    login = LoginPage(browser)
    project = ProjectsPage(browser)
    veeco = DrawingCheckerVeecoPage(browser)

    # Load test data
    with open("testdata/login_data.json") as file:
        data = json.load(file)

    email = data["system_admin_login"]["email"]
    password = data["system_admin_login"]["password"]

    download_dir = r"C:\Users\pooja.db\Downloads"

    # FLOW
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

    veeco.close_popup()

