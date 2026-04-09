import pytest
import os

from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from pages.tariff_play_page import TariffPage
from config.config import BASE_URL

@pytest.mark.order(20)
@pytest.mark.regression
def test_tariff_analysis_play(browser, test_data):

    browser.get(BASE_URL)

    email = test_data["system_admin_login"]["email"]
    password = test_data["system_admin_login"]["password"]

    # Jenkins-safe download directory
    download_dir = os.path.abspath("downloads")
    os.makedirs(download_dir, exist_ok=True)

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

    # Go Back
    tariff.go_back()