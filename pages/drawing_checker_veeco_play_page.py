import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class DrawingCheckerVeecoPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 120)

    # LOCATORS
    dropdown = (By.XPATH, "//select[contains(@class,'text-sm')]")
    option = (By.XPATH, "//option[normalize-space()='Drawing Checker - Veeco']")
    run_btn = (By.XPATH, "//button[contains(text(),'Run Drawing Checker - Veeco')]")
    view_results = (By.XPATH, "//button[normalize-space()='View Results']")
    view_details = (By.XPATH, "//button[normalize-space()='View Details']")

    popup_overlay = (By.XPATH, "//div[contains(@class,'fixed inset-0')]")

    # SAME AS BOTH (important)
    download_btn = (By.XPATH, "//button[@title='Download Drawing Checker PDF Report']")

    close_icon = (By.XPATH, "//button[contains(@class,'p-2')]")

    # ---------------- ACTIONS ----------------

    def select_drawing_checker_veeco(self):
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

    # FIXED TAB SWITCH (SAME AS BOTH)
    def open_report_tab(self):

        popup = self.wait.until(EC.visibility_of_element_located(self.popup_overlay))

        tabs = popup.find_elements(
            By.XPATH,
            ".//button[normalize-space()='Drawing Checker - Veeco']"
        )

        for tab in tabs:
            if tab.is_displayed():

                self.driver.execute_script("arguments[0].scrollIntoView(true);", tab)

                try:
                    tab.click()
                except:
                    ActionChains(self.driver).move_to_element(tab).click().perform()

                break
        else:
            raise Exception("No visible Veeco tab found")


        # VERIFY TAB SWITCH
        try:
            self.wait.until(EC.presence_of_element_located(self.download_btn))
        except:
            print("Retrying with JS click...")
            self.driver.execute_script("arguments[0].click();", tab)

            self.wait.until(EC.presence_of_element_located(self.download_btn))

    # FINAL DOWNLOAD FIX
    def download_report(self, download_dir):

        # Step 1: capture existing files
        before_files = set(os.listdir(download_dir))

        # Step 2: click download
        button = self.wait.until(EC.element_to_be_clickable(self.download_btn))
        self.driver.execute_script("arguments[0].click();", button)

        # Step 3: handle chrome popup
        time.sleep(2)
        try:
            self.driver.execute_script("""
                document.body.dispatchEvent(new KeyboardEvent('keydown', {key: 'Tab'}));
                document.body.dispatchEvent(new KeyboardEvent('keydown', {key: 'Tab'}));
                document.body.dispatchEvent(new KeyboardEvent('keydown', {key: 'Enter'}));
            """)
            print("Handled Chrome popup")
        except:
            print("No popup")

        # Step 4: wait for new file
        def new_file_downloaded(driver):
            after_files = set(os.listdir(download_dir))
            new_files = after_files - before_files

            for f in new_files:
                if f.lower().endswith(".pdf"):
                    return True
            return False

        WebDriverWait(self.driver, 120).until(new_file_downloaded)

        # Step 5: verify download
        after_files = set(os.listdir(download_dir))
        downloaded_files = after_files - before_files

        print("Downloaded files:", downloaded_files)

        assert any(f.lower().endswith(".pdf") for f in downloaded_files), \
            "Drawing Checker Veeco file not downloaded"


    def close_popup(self):
        element = self.wait.until(EC.element_to_be_clickable(self.close_icon))
        self.driver.execute_script("arguments[0].click();", element)

