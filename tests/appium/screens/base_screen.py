try:
    from appium.webdriver.common.appiumby import AppiumBy
except ImportError:
    class AppiumBy:
        XPATH = "xpath"
        ID = "id"
        CLASS_NAME = "class name"
        ACCESSIBILITY_ID = "accessibility id"

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseScreen:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def find(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except Exception:
            return self.driver.find_element(locator[0], locator[1])

    def click(self, locator):
        element = self.find(locator)
        if element:
            element.click()
        return element

    def type_text(self, locator, text):
        element = self.find(locator)
        if element:
            element.clear()
            element.send_keys(text)
        return element

    def is_visible(self, locator, timeout=2):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False
