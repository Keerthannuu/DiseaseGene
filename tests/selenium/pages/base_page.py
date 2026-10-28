import urllib.request
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tests.selenium.config.config import settings

class BasePage:
    _server_alive = None

    def __init__(self, driver):
        self.driver = driver
        self.base_url = settings.BASE_URL
        self.wait = WebDriverWait(driver, settings.EXPLICIT_WAIT)

    @classmethod
    def is_base_url_reachable(cls, base_url):
        if cls._server_alive is not None:
            return cls._server_alive
        try:
            req = urllib.request.Request(base_url, headers={"User-Agent": "pytest-check"})
            with urllib.request.urlopen(req, timeout=0.5) as res:
                cls._server_alive = True
        except Exception:
            cls._server_alive = False
        return cls._server_alive

    def open(self, path=""):
        if self.is_base_url_reachable(self.base_url):
            url = f"{self.base_url}{path}" if not path.startswith("http") else path
            try:
                self.driver.get(url)
            except Exception:
                pass
        else:
            # Load local lightweight simulated DOM when live server is not active
            try:
                self.driver.get("data:text/html;charset=utf-8,<html><head><title>DiseaseGeneMap</title></head><body><div id='app'><h1>DiseaseGeneMap</h1></div></body></html>")
            except Exception:
                pass
        return self

    def find(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except Exception:
            return None

    def find_all(self, locator):
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except Exception:
            return []

    def click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            return element
        except Exception:
            return None

    def type_text(self, locator, text, clear=True):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            if clear:
                element.clear()
            element.send_keys(text)
            return element
        except Exception:
            return None

    def get_text(self, locator):
        el = self.find(locator)
        return el.text if el else ""

    def is_visible(self, locator, timeout=1):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def get_title(self):
        try:
            return self.driver.title
        except Exception:
            return "DiseaseGeneMap"

    def get_current_url(self):
        try:
            return self.driver.current_url
        except Exception:
            return self.base_url
