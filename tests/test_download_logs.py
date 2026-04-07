import pytest
import json
import os
import time
from datetime import datetime

from pages.login_page import LoginPage
from pages.system_stats_page import SystemStatsPage
from config.config import BASE_URL


DOWNLOAD_PATH = r"C:\Users\pooja.db\Downloads"


def wait_for_new_file(prefix, previous_count, timeout=20):

    for _ in range(timeout):

        files = [f for f in os.listdir(DOWNLOAD_PATH) if f.startswith(prefix)]

        if len(files) > previous_count:
            return True

        time.sleep(1)

    return False


def clean_old_files(prefix):

    for file in os.listdir(DOWNLOAD_PATH):
        if file.startswith(prefix):
            os.remove(os.path.join(DOWNLOAD_PATH, file))

@pytest.mark.regression
def test_download_logs(browser):

    browser.get(BASE_URL)

    # Load login data
    with open("testdata/login_data.json") as file:
        data = json.load(file)

    email = data["system_admin_login"]["email"]
    password = data["system_admin_login"]["password"]

    # Login
    login = LoginPage(browser)
    login.login(email, password)

    system_stats = SystemStatsPage(browser)

    time_ranges = [
        system_stats.time_range_today,
        system_stats.time_range_2_days,
        system_stats.time_range_3_days,
        system_stats.time_range_5_days,
        system_stats.time_range_7_days
    ]

    today_date = datetime.today().strftime("%Y-%m-%d")
    file_prefix = f"sourceoptima_logs_{today_date}"

    # Clean old downloads
    clean_old_files(file_prefix)

    for time_range in time_ranges:

        existing_files = [f for f in os.listdir(DOWNLOAD_PATH) if f.startswith(file_prefix)]
        previous_count = len(existing_files)

        # Select time range
        system_stats.select_time_range(time_range)

        # Click download
        system_stats.click_download_logs()

        # Wait for new file
        assert wait_for_new_file(file_prefix, previous_count), "Log file was not downloaded"

    # Collect all downloaded files
    all_logs = [f for f in os.listdir(DOWNLOAD_PATH) if f.startswith(file_prefix)]

    print("Downloaded log files:", all_logs)

    # Assert all logs downloaded
    assert len(all_logs) == 5, "Not all log files were downloaded"

    # Verify files are not empty
    for file in all_logs:

        file_path = os.path.join(DOWNLOAD_PATH, file)

        assert os.path.getsize(file_path) > 0, f"{file} is empty"