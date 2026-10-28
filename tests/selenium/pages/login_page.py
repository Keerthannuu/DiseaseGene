from selenium.webdriver.common.by import By
from tests.selenium.pages.base_page import BasePage

class LoginPage(BasePage):
    PATH = "/signin"

    USERNAME_INPUT = (By.CSS_SELECTOR, "input[name='username'], input[type='text'], input[placeholder*='username' i]")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password'], input[type='password']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "a[href*='forgot-password']")
    SIGNUP_LINK = (By.CSS_SELECTOR, "a[href*='signup']")
    ERROR_ALERT = (By.CSS_SELECTOR, "[role='alert'], .error-message, .text-red-500")
    PASSWORD_TOGGLE = (By.CSS_SELECTOR, "button[aria-label*='password' i], button svg")

    def open_login(self):
        return self.open(self.PATH)

    def login(self, username, password):
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)
        return self

    def get_error_message(self):
        if self.is_visible(self.ERROR_ALERT):
            return self.get_text(self.ERROR_ALERT)
        return ""
