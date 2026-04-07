import pytest
import json
from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from pages.cost_reduction_play_page import CostReductionPage
from config.config import BASE_URL

@pytest.mark.regression
def test_cost_reduction_play(browser):

    browser.get(BASE_URL)

    login = LoginPage(browser)
    project = ProjectsPage(browser)
    cost = CostReductionPage(browser)

    # Load data
    with open("testdata/login_data.json") as file:
        data = json.load(file)

    email = data["system_admin_login"]["email"]
    password = data["system_admin_login"]["password"]

    # FLOW

    login.login(email, password)

    project.open_projects()
    project.open_root_space("TestSpace_1")
    project.open_project("TestFile")
    project.select_all_files()

    cost.select_cost_reduction()
    cost.click_run()

    cost.wait_for_processing()

    cost.click_view_results()
    cost.click_view_details()
    cost.open_report_tab()

    cost.take_screenshot()
    cost.close_popup()