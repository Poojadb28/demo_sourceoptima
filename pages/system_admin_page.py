from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class SystemAdminPage:
   
    # USER ADMIN NAVIGATION

    # Button to open User Admin section
    user_admin_view = (By.XPATH, "//button[normalize-space()='User Admin View']")

    # Button to open Create User form
    create_user_button = (By.XPATH, "//button[normalize-space()='Create User']")
    
    # CREATE USER FORM FIELDS

    # Input fields in Create User form
    full_name = (By.XPATH, "//input[contains(@placeholder,'full name')]")
    email = (By.XPATH, "//input[contains(@placeholder,'user@example.com')]")
    password = (By.XPATH, "//input[contains(@placeholder,'Enter secure password')]")
    confirm_password = (By.XPATH, "//input[contains(@placeholder,'Re-enter password')]")

    # Role selection dropdown and option
    role_dropdown = (By.XPATH, "//select[contains(@class,'w-full')]")
    # role_option = (By.XPATH, "//option[normalize-space()='Admin - Organization Administrator']")
    role_option = (By.XPATH, "//option[normalize-space()='Customer - Standard User']")

    # Submit button to create user
    submit_button = (By.XPATH, "//button[@type='submit']")

    # SUCCESS & ERROR MESSAGES

    # Success message after user creation
    success_message = (By.XPATH, "//div[text()='User created successfully']")

    # Error message for duplicate user creation
    duplicate_user_error = (By.XPATH, "//div[contains(text(),'Failed to create user')]")

    # EXPORT CREDIT HISTORY
    
    # Button to export credit history
    export_credit_history_button = (By.XPATH,"//button[normalize-space()='Export Credit History']")

    # INITIALIZATION

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # NAVIGATION METHODS

    # Open the User Admin section
    def open_user_admin(self):
        self.wait.until(EC.element_to_be_clickable(self.user_admin_view)).click()

    # Click the Create User button
    def click_create_user(self):
        self.wait.until(EC.element_to_be_clickable(self.create_user_button)).click()

    # CREATE USER METHODS

    # Fill the Create User form fields
    def fill_user_details(self, name, email, password):

        self.wait.until(EC.visibility_of_element_located(self.full_name)).send_keys(name)
        self.wait.until(EC.visibility_of_element_located(self.email)).send_keys(email)
        self.wait.until(EC.visibility_of_element_located(self.password)).send_keys(password)

        # Confirm password uses same password
        self.wait.until(EC.visibility_of_element_located(self.confirm_password)).send_keys(password)

        # Select user role
        self.wait.until(EC.element_to_be_clickable(self.role_dropdown)).click()
        self.wait.until(EC.element_to_be_clickable(self.role_option)).click()

    # Submit the user creation form
    def submit_user(self):
        self.wait.until(EC.element_to_be_clickable(self.submit_button)).click()

    # VALIDATION METHODS

    # Get success message after creating user
    def get_success_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.success_message)).text

    # Get error message when duplicate user is created
    def get_duplicate_user_error(self):
        return self.wait.until(EC.visibility_of_element_located(self.duplicate_user_error)).text

    # EXPORT CREDIT HISTORY

    # Click Export Credit History button
    def click_export_credit_history(self):
        self.wait.until(EC.element_to_be_clickable(self.export_credit_history_button)).click()

    # Wait until credit history file is downloaded
    def wait_for_credit_history_download(self, download_dir):
        self.wait.until(
            lambda driver: any(
                f.lower().startswith("credit_history")
                and f.lower().endswith(".xlsx")
                for f in os.listdir(download_dir)
            )
        )

    # AVAILABLE PLAYS LOCATORS

    available_plays_section = (By.XPATH, "//h2[normalize-space()='Available Plays']")

    disable_success_message = (By.XPATH, "//div[contains(text(),'Play disabled successfully')]")
    enable_success_message = (By.XPATH, "//div[contains(text(),'Play enabled successfully')]")

    # AVAILABLE PLAYS METHODS

    def scroll_to_available_plays(self):

        section = self.wait.until(
            EC.visibility_of_element_located(self.available_plays_section)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", section
        )


    def toggle_play_by_name(self, play_name):

        toggle_button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//*[contains(text(),'{play_name}')]/ancestor::div[contains(@class,'rounded')]//button[contains(@class,'inline-flex')]"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", toggle_button
        )

        toggle_button.click()


    def get_disable_success_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.disable_success_message)
        ).text


    def get_enable_success_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.enable_success_message)
        ).text