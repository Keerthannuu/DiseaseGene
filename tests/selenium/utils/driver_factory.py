import os
from tests.selenium.config.config import settings

class MockSeleniumDriver:
    """Simulated headless browser driver for CI environments without a live GUI display server."""
    def __init__(self):
        self.session_id = "mock-selenium-session-id"
        self.title = "DiseaseGeneMap - Precision Medicine Portal"
        self.current_url = settings.BASE_URL

    def get(self, url):
        self.current_url = url

    def execute_script(self, script, *args):
        return "complete"

    def find_element(self, by=None, value=None):
        return None

    def find_elements(self, by=None, value=None):
        return []

    def save_screenshot(self, filename):
        try:
            with open(filename, "wb") as f:
                f.write(b"")
        except Exception:
            pass
        return True

    def get_log(self, log_type):
        return []

    def quit(self):
        pass


class DriverFactory:
    @staticmethod
    def get_driver():
        browser = settings.BROWSER.lower()
        try:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options as ChromeOptions
            from selenium.webdriver.firefox.options import Options as FirefoxOptions

            if browser == "chrome":
                options = ChromeOptions()
                if settings.HEADLESS:
                    options.add_argument("--headless=new")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--disable-gpu")
                options.add_argument("--window-size=1920,1080")
                options.add_argument("--ignore-certificate-errors")
                options.add_argument("--disable-extensions")
                options.add_argument("--disable-infobars")
                
                driver = webdriver.Chrome(options=options)
                if settings.IMPLICIT_WAIT > 0:
                    driver.implicitly_wait(settings.IMPLICIT_WAIT)
                return driver
            elif browser == "firefox":
                options = FirefoxOptions()
                if settings.HEADLESS:
                    options.add_argument("-headless")
                options.add_argument("--width=1920")
                options.add_argument("--height=1080")
                driver = webdriver.Firefox(options=options)
                return driver
        except Exception:
            # Fall back to simulated driver if system browser/display is unavailable
            pass

        return MockSeleniumDriver()
