from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    # LOGIN PAGE LOCATORS

    # Login button on the home page
    login_button = (By.XPATH, "//a[normalize-space()='Login']")

    # Email input field
    email_field = (By.ID, "email")

    # Password input field
    password_field = (By.ID, "password")

    # Eye icon used to show/hide password
    eye_icon = (By.XPATH, "//*[name()='path' and contains(@d,'M320 400c-')]")

    # Submit button to perform login
    submit_button = (By.XPATH, "//button[normalize-space()='Submit']")

    # Error message displayed for invalid login
    error_message = (By.XPATH, "//div[text()='Error during login. Please try again.']")

     # LOGOUT LOCATOR
    logout_button = (By.XPATH, "//button[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # INITIALIZATION
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # LOGIN ACTION METHODS

    # Click the login button on the home page
    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    # Enter email into email field
    def enter_email(self, email):
        self.wait.until(EC.presence_of_element_located(self.email_field)).send_keys(email)

    # Enter password into password field
    def enter_password(self, password):
        self.wait.until(EC.presence_of_element_located(self.password_field)).send_keys(password)

    # Click the eye icon to reveal password
    def click_eye_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.eye_icon)).click()

    # Click the submit button to login
    def click_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.submit_button)).click()

    # COMPLETE LOGIN FLOW
    
    # Perform the complete login process
    def login(self, email, password):
        self.click_login_button()
        self.enter_email(email)
        self.enter_password(password)
        self.click_eye_icon()
        self.click_submit()

    # VALIDATION METHODS

    # Get error message for invalid login
    def get_error_message(self):
        return self.wait.until(EC.presence_of_element_located(self.error_message)).text
    
    # LOGOUT METHOD
    def logout(self):

        self.wait.until(
            EC.element_to_be_clickable(self.logout_button)
        ).click()




