from selenium.webdriver.common.by import By
from tests.selenium.pages.base_page import BasePage

class RegisterPage(BasePage):
    PATH = "/signup"

    USERNAME_INPUT = (By.CSS_SELECTOR, "input[name='username'], input[placeholder*='username' i]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email'], input[type='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password'], input[type='password']")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='confirm_password'], input[name='confirmPassword']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_ALERT = (By.CSS_SELECTOR, "[role='alert'], .error-message, .text-red-500")

    def open_register(self):
        return self.open(self.PATH)

    def register(self, username, email, password, confirm_password=None):
        confirm = confirm_password if confirm_password is not None else password
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        if self.is_visible(self.CONFIRM_PASSWORD_INPUT, timeout=1):
            self.type_text(self.CONFIRM_PASSWORD_INPUT, confirm)
        self.click(self.SUBMIT_BUTTON)
        return self

    def get_error_message(self):
        if self.is_visible(self.ERROR_ALERT):
            return self.get_text(self.ERROR_ALERT)
        return ""
