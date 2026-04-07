import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class DrawingCheckerPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 120)

    # LOCATORS
    dropdown = (By.XPATH, "//select[contains(@class,'text-sm')]")
    option = (By.XPATH, "//option[normalize-space()='Drawing Checker - Both']")
    run_btn = (By.XPATH, "//button[contains(text(),'Run Drawing Checker - Both')]")
    view_results = (By.XPATH, "//button[normalize-space()='View Results']")
    view_details = (By.XPATH, "//button[normalize-space()='View Details']")

    popup_overlay = (By.XPATH, "//div[contains(@class,'fixed inset-0')]")
    report_tab = (By.XPATH, ".//button[normalize-space()='Drawing Checker - Both']")

    # parent button (NOT svg)
    # download_btn = (By.XPATH, "//button[contains(@title,'Drawing Checker')]")
    download_btn = (By.XPATH, "//button[@title='Download Drawing Checker PDF Report']")

    close_icon = (By.XPATH, "//button[contains(@class,'p-2')]")

    # ---------------- ACTIONS ----------------

    def select_drawing_checker(self):
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
        popup = self.wait.until(EC.visibility_of_element_located(self.popup_overlay))

        # tabs = popup.find_elements(By.XPATH, "//button[normalize-space()='Drawing Checker - Both']")
        tabs = popup.find_elements(By.XPATH, ".//button[normalize-space()='Drawing Checker - Both']")

        for tab in tabs:
            if tab.is_displayed():

                # Scroll
                self.driver.execute_script("arguments[0].scrollIntoView(true);", tab)

                try:
                    tab.click()
                except:
                    ActionChains(self.driver).move_to_element(tab).click().perform()

                break
        else:
            raise Exception("No visible Drawing Checker tab found")

        # VERIFY TAB SWITCH (VERY IMPORTANT)
        try:
            self.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//button[@title='Download Drawing Checker PDF Report']")
            ))
        except:
            self.driver.execute_script("arguments[0].click();", tab)

            self.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//button[@title='Download Drawing Checker PDF Report']")
            ))


    # def download_report(self, download_dir):

    #     element = self.wait.until(EC.visibility_of_element_located(self.download_btn))
    #     try:
    #         element.click()
    #     except:
    #         self.driver.execute_script("arguments[0].click();", element)

    #     # Wait for PDF download
    #     WebDriverWait(self.driver, 60).until(
    #         lambda d: any(
    #             "drawing_checker" in f.lower() and f.endswith(".pdf")
    #             for f in os.listdir(download_dir)
    #         )
    #     )

    #     files = os.listdir(download_dir)
    #     print("Downloaded files:", files)

    #     assert any(
    #         "drawing_checker" in f.lower() and f.endswith(".pdf")
    #         for f in files
    #     ), "Drawing Checker file not downloaded"

    def download_report(self, download_dir):

        # Remove old files
        before_files = set(os.listdir(download_dir))

        # Click ACTUAL BUTTON
        button = self.wait.until(EC.element_to_be_clickable(self.download_btn))
        self.driver.execute_script("arguments[0].click();", button)

        # Wait for NEW file (not old ones)
        def new_file_downloaded(driver):
            after_files = set(os.listdir(download_dir))
            new_files = after_files - before_files

            for f in new_files:
                if f.endswith(".pdf"):
                    return True
            return False

        WebDriverWait(self.driver, 120).until(new_file_downloaded)

        # Get new files
        final_files = set(os.listdir(download_dir))
        downloaded_files = final_files - before_files

        print("Downloaded files:", downloaded_files)

        assert any(f.endswith(".pdf") for f in downloaded_files), \
            "Drawing Checker file not downloaded"

    def close_popup(self):

        element = self.wait.until(EC.element_to_be_clickable(self.close_icon))
        self.driver.execute_script("arguments[0].click();", element)

        self.wait.until(EC.element_to_be_clickable(self.dropdown))
