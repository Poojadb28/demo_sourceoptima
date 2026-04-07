import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class DrawingCheckerGeneralPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 120)

    # LOCATORS
    dropdown = (By.XPATH, "//select[contains(@class,'text-sm')]")
    option = (By.XPATH, "//option[normalize-space()='Drawing Checker - General']")
    run_btn = (By.XPATH, "//button[contains(text(),'Run Drawing Checker - General')]")
    view_results = (By.XPATH, "//button[normalize-space()='View Results']")
    view_details = (By.XPATH, "//button[normalize-space()='View Details']")

    popup_overlay = (By.XPATH, "//div[contains(@class,'fixed inset-0')]")

    report_tab = (By.XPATH, "//div[contains(@class,'fixed')]//button[normalize-space()='Drawing Checker - General']")
    download_btn = (By.XPATH, "//button[contains(@title,'Download Drawing Checker')]")

    close_icon = (By.XPATH, "//button[contains(@class,'p-2')]")

    # ---------------- ACTIONS ----------------

    def select_drawing_checker_general(self):
        self.wait.until(EC.element_to_be_clickable(self.dropdown)).click()
        self.wait.until(EC.element_to_be_clickable(self.option)).click()

    def click_run(self):
        self.wait.until(EC.element_to_be_clickable(self.run_btn)).click()

    def wait_for_processing(self):
        self.wait.until(EC.element_to_be_clickable(self.view_details))

    def click_view_results(self):
        self.wait.until(EC.element_to_be_clickable(self.view_results)).click()

    def click_view_details(self):
        self.wait.until(EC.element_to_be_clickable(self.view_details)).click()

    def open_report_tab(self):
        popup = self.wait.until(
            EC.visibility_of_element_located(self.popup_overlay)
        )

        tab = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[.//text()[contains(.,'Drawing Checker - General')]]")
            )
        )

        self.driver.execute_script("arguments[0].scrollIntoView(true);", tab)

        import time
        time.sleep(2)

        try:
            ActionChains(self.driver)\
                .move_to_element(tab)\
                .pause(1)\
                .click()\
                .perform()
        except:
            self.driver.execute_script("arguments[0].click();", tab)

        time.sleep(5)

        # VERIFY TAB SWITCH (CRITICAL)
        content_loaded = len(self.driver.find_elements(
            By.XPATH, "//button[@title='Download Drawing Checker PDF Report']"
        ))

        if content_loaded == 0:
            
            # Retry once more (important)
            self.driver.execute_script("arguments[0].click();", tab)
            time.sleep(5)

        # Final check
        buttons = self.driver.find_elements(
            By.XPATH, "//button[@title='Download Drawing Checker PDF Report']"
        )

        if len(buttons) == 0:
            raise Exception("Tab NOT switched → UI issue or wrong locator")

    def download_report(self, download_dir):

        before_files = set(os.listdir(download_dir))

        #USE FLEXIBLE LOCATOR
        element = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@title,'Download Drawing Checker')]")
            )
        )

        self.driver.execute_script("arguments[0].click();", element)

        # WAIT FOR NEW FILE (BEST PRACTICE)
        def file_downloaded(driver):
            after_files = set(os.listdir(download_dir))
            new_files = after_files - before_files
            return any(f.endswith(".pdf") for f in new_files)

        WebDriverWait(self.driver, 120).until(file_downloaded)

        after_files = set(os.listdir(download_dir))
        new_files = after_files - before_files

        assert any(f.endswith(".pdf") for f in new_files), \
            "File NOT downloaded"

    def close_popup(self):

        element = self.wait.until(EC.element_to_be_clickable(self.close_icon))
        self.driver.execute_script("arguments[0].click();", element)

        self.wait.until(EC.element_to_be_clickable(self.dropdown))

    