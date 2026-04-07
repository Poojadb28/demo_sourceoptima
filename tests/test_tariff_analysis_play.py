import pytest
import json
from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from pages.tariff_play_page import TariffPage
from config.config import BASE_URL

@pytest.mark.regression
def test_tariff_analysis_play(browser):

    browser.get(BASE_URL)

    # Load data
    with open("testdata/login_data.json") as file:
        data = json.load(file)

    email = data["system_admin_login"]["email"]
    password = data["system_admin_login"]["password"]

    download_dir = r"C:\Users\pooja.db\Downloads"

    # Pages
    login = LoginPage(browser)
    project = ProjectsPage(browser)
    tariff = TariffPage(browser)

    # ---------------- FLOW ----------------

    login.login(email, password)

    project.open_projects()
    project.open_root_space("TestSpace_1")
    project.open_project("TestFile")
    project.select_all_files()

    tariff.select_tariff_analysis()
    tariff.treat_as_assembly()
    tariff.set_top_level()
    tariff.run_tariff_analysis()

    # Export BOM
    tariff.export_bom(download_dir)

    # Approve BOM
    tariff.approve_bom()

    # Export Tariff
    tariff.export_tariff(download_dir)

    #  Go Back
    tariff.go_back()