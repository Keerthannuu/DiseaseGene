import pytest
import os
from pathlib import Path
from tests.appium.config.config import settings
from tests.appium.utils.driver_factory import AppiumDriverFactory
from tests.appium.utils.reporter import save_appium_failure_artifacts

def pytest_configure(config):
    settings.REPORT_DIR.mkdir(parents=True, exist_ok=True)
    settings.SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    settings.LOGS_DIR.mkdir(parents=True, exist_ok=True)
    config.addinivalue_line("markers", "test_id(id): Unique test case identifier (APP-XXX)")
    config.addinivalue_line("markers", "category(name): Functional category of the mobile test")

@pytest.fixture(scope="function")
def appium_driver(request):
    driver_instance = None
    try:
        driver_instance = AppiumDriverFactory.get_driver()
        yield driver_instance
    except Exception as e:
        pytest.skip(f"Appium server or Android emulator unavailable: {e}")
    finally:
        if driver_instance:
            try:
                driver_instance.quit()
            except Exception:
                pass

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("appium_driver", None)
        test_id_marker = item.get_closest_marker("test_id")
        test_id = test_id_marker.args[0] if test_id_marker else item.name
        
        if driver:
            screenshot, log = save_appium_failure_artifacts(driver, test_id, report.longreprtext)
            report.sections.append(("Failure Artifacts", f"Screenshot: {screenshot}\nLog: {log}"))
