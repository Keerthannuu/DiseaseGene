from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tests.selenium.config.config import settings

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = settings.BASE_URL
        self.wait = WebDriverWait(driver, settings.EXPLICIT_WAIT)

    def open(self, path=""):
        url = f"{self.base_url}{path}" if not path.startswith("http") else path
        self.driver.get(url)
        return self

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def type_text(self, locator, text, clear=True):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        if clear:
            element.clear()
        element.send_keys(text)
        return element

    def get_text(self, locator):
        return self.find(locator).text

    def is_visible(self, locator, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url
