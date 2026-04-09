import pytest
import os
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from pages.system_stats_page import SystemStatsPage
from config.config import BASE_URL

@pytest.mark.order(3)
@pytest.mark.regression
def test_download_logs(browser, test_data):

    wait = WebDriverWait(browser, 20)

    browser.get(BASE_URL)

    email = test_data["logins"]["system_admin"]["email"]
    password = test_data["logins"]["system_admin"]["password"]

    login = LoginPage(browser)
    login.login(email, password)

    system_stats = SystemStatsPage(browser)

    download_dir = os.path.abspath("downloads")
    os.makedirs(download_dir, exist_ok=True)

    time_ranges = [
        system_stats.time_range_today,
        system_stats.time_range_2_days,
        system_stats.time_range_3_days,
        system_stats.time_range_5_days,
        system_stats.time_range_7_days
    ]

    for time_range in time_ranges:

        system_stats.select_time_range(time_range)
        system_stats.click_download_logs()

        # Use page method wait
        system_stats.wait_for_logs_download(download_dir)

    files = os.listdir(download_dir)

    assert len(files) >= 5, "Logs not downloaded"