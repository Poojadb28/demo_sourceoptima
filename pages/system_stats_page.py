from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SystemStatsPage:

    time_range_today = (By.XPATH, "//button[normalize-space()='Today']")
    time_range_2_days = (By.XPATH, "//button[normalize-space()='2 days']")
    time_range_3_days = (By.XPATH, "//button[normalize-space()='3 days']")
    time_range_5_days = (By.XPATH, "//button[normalize-space()='5 days']")
    time_range_7_days = (By.XPATH, "//button[normalize-space()='7 days']")

    download_logs_button = (By.XPATH, "//button[normalize-space()='Download Logs (.txt)']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def select_time_range(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def click_download_logs(self):
        self.wait.until(
            EC.element_to_be_clickable(self.download_logs_button)
        ).click()