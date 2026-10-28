from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from tests.selenium.config.config import settings

def wait_for_element(driver, locator, timeout=None):
    timeout = timeout or settings.EXPLICIT_WAIT
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

def wait_for_clickable(driver, locator, timeout=None):
    timeout = timeout or settings.EXPLICIT_WAIT
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))

def wait_for_url_contains(driver, substring, timeout=None):
    timeout = timeout or settings.EXPLICIT_WAIT
    return WebDriverWait(driver, timeout).until(EC.url_contains(substring))

def is_element_present(driver, locator, timeout=2):
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
        return True
    except (TimeoutException, NoSuchElementException):
        return False
