import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from tests.selenium.config.config import settings

class DriverFactory:
    @staticmethod
    def get_driver():
        browser = settings.BROWSER.lower()
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
            options.set_capability("goog:loggingPrefs", {"browser": "ALL", "performance": "ALL"})
            
            driver = webdriver.Chrome(options=options)
        elif browser == "firefox":
            options = FirefoxOptions()
            if settings.HEADLESS:
                options.add_argument("-headless")
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
            driver = webdriver.Firefox(options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser}")
            
        if settings.IMPLICIT_WAIT > 0:
            driver.implicitly_wait(settings.IMPLICIT_WAIT)
            
        return driver
