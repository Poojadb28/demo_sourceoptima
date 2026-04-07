import os
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# ===================== BROWSER FIXTURE =====================
@pytest.fixture(scope="function")
def browser():

    options = Options()

    # MUST for Jenkins
    options.add_argument("--headless=new")

    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Fix downloads (no popup)
    download_dir = os.path.abspath("downloads")

    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "profile.default_content_setting_values.automatic_downloads": 1
    }

    options.add_experimental_option("prefs", prefs)

    # Selenium 4 fix (NO executable_path)
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.implicitly_wait(10)

    yield driver

    driver.quit()


# ===================== SCREENSHOT ON FAILURE =====================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("browser", None)

        if driver:

            screenshots_dir = os.path.abspath("screenshots")

            if not os.path.exists(screenshots_dir):
                os.makedirs(screenshots_dir)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join(screenshots_dir, file_name)

            driver.save_screenshot(file_path)
            print(f"Screenshot saved: {file_path}")

            # Attach to pytest-html report
            if item.config.pluginmanager.hasplugin("html"):
                pytest_html = item.config.pluginmanager.getplugin("html")
                extra = getattr(report, "extra", [])
                extra.append(pytest_html.extras.image(file_path))
                report.extra = extra



