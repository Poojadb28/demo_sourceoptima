import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TariffPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 120)

    # ---------------- LOCATORS ----------------

    dropdown = (By.XPATH, "//select[contains(@class,'text-sm')]")
    tariff_option = (By.XPATH, "//option[normalize-space()='Tariff Analysis']")
    treat_checkbox = (By.XPATH, "//input[contains(@class,'w-4 h-4')]")
    set_top = (By.XPATH, "//button[normalize-space()='Set as Top Level']")
    run_btn = (By.XPATH, "//button[contains(normalize-space(),'Run Tariff Analysis')]")

    # Separate export buttons
    bom_export_btn = (By.XPATH, "(//button[normalize-space()='Export to Excel'])[1]")
    tariff_export_btn = (By.XPATH, "(//button[normalize-space()='Export to Excel'])[2]")

    approve_bom_btn = (By.XPATH, "//span[normalize-space()='Approve BOM']")
    tariff_heading = (By.XPATH, "//h2[contains(text(),'Tariff Analysis')]")

    back_project = (By.XPATH, "//span[normalize-space()='Back to Project']")
    back_btn = (By.XPATH, "//span[normalize-space()='Back']")

    # ---------------- ACTIONS ----------------

    def select_tariff_analysis(self):
        self.wait.until(EC.element_to_be_clickable(self.dropdown)).click()
        self.wait.until(EC.element_to_be_clickable(self.tariff_option)).click()

    def treat_as_assembly(self):
        checkbox = self.wait.until(EC.presence_of_element_located(self.treat_checkbox))
        self.driver.execute_script("arguments[0].click();", checkbox)

    def set_top_level(self):
        elements = self.driver.find_elements(*self.set_top)
        if elements:
            self.driver.execute_script("arguments[0].click();", elements[0])

    def run_tariff_analysis(self):
        self.wait.until(EC.element_to_be_clickable(self.run_btn)).click()

    # # ---------------- BOM EXPORT ----------------

    # def export_bom(self, download_dir):

    #     before_files = set(os.listdir(download_dir))

    #     self.wait.until(EC.element_to_be_clickable(self.bom_export_btn)).click()

    #     # Wait until .xlsx file appears (NOT temp file)
    #     WebDriverWait(self.driver, 60).until(
    #         lambda d: any(
    #             f.lower().endswith(".xlsx") and "bom" in f.lower()
    #             for f in os.listdir(download_dir)
    #         )
    #     )

    #     files = os.listdir(download_dir)

    #     print("Final Files:", files)

    #     assert any(
    #         f.lower().endswith(".xlsx") and "bom" in f.lower()
    #         for f in files
    #     ), "BOM file not downloaded"

    # ---------------- APPROVE BOM ----------------

    # def approve_bom(self):

    #     element = self.wait.until(EC.element_to_be_clickable(self.approve_bom_btn))
    #     self.driver.execute_script("arguments[0].click();", element)

    #     # Wait for tariff page to load
    #     self.wait.until(EC.element_to_be_clickable(self.tariff_export_btn))

    #     print("Tariff page loaded successfully")

    def approve_bom(self):

        element = self.wait.until(EC.element_to_be_clickable(self.approve_bom_btn))
        self.driver.execute_script("arguments[0].click();", element)

        # Wait until old element becomes stale (VERY IMPORTANT)
        old_button = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Export to Excel']")
        ))

        self.wait.until(EC.staleness_of(old_button))

        # Now wait for new export button
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Export to Excel']")
        ))

    def export_bom(self, download_dir):

        before_files = set(os.listdir(download_dir))

        # WAIT until button is clickable (after processing)
        button = WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable(self.bom_export_btn)
        )

        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        self.driver.execute_script("arguments[0].click();", button)

        # Wait for download
        WebDriverWait(self.driver, 60).until(
            lambda d: len(set(os.listdir(download_dir)) - before_files) > 0
        )

        after_files = set(os.listdir(download_dir))
        new_files = after_files - before_files

        print("BOM Downloaded:", new_files)

        assert new_files, "BOM file not downloaded"


    # ---------------- TARIFF EXPORT ----------------

    # def export_tariff(self, download_dir):

    #     self.wait.until(EC.element_to_be_clickable(self.tariff_export_btn)).click()

    #     WebDriverWait(self.driver, 60).until(
    #         lambda d: any(
    #             f.lower().endswith(".xlsx") and "tariff" in f.lower()
    #             for f in os.listdir(download_dir)
    #         )
    #     )

    #     files = os.listdir(download_dir)

    #     print("Final Files:", files)

    #     assert any(
    #         "tariff" in f.lower() and f.endswith(".xlsx")
    #         for f in files
    #     ), "Tariff file not downloaded"

    def export_tariff(self, download_dir):

        button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Export to Excel']")
        ))

        self.driver.execute_script("arguments[0].click();", button)

        WebDriverWait(self.driver, 60).until(
            lambda d: any(
                f.lower().endswith(".xlsx") and "tariff" in f.lower()
                for f in os.listdir(download_dir)
            )
        )

        files = os.listdir(download_dir)

        assert any(
            "tariff" in f.lower() and f.endswith(".xlsx")
            for f in files
        ), "Tariff file not downloaded"


    # ---------------- NAVIGATION ----------------
    def go_back(self):
        self.wait.until(EC.element_to_be_clickable(self.back_project)).click()
        self.wait.until(EC.element_to_be_clickable(self.back_btn)).click()
        