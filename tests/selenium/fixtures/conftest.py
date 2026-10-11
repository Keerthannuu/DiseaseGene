import pytest
import os
from pathlib import Path
from tests.selenium.config.config import settings
from tests.selenium.utils.driver_factory import DriverFactory
from tests.selenium.utils.reporter import save_failure_artifacts

def pytest_configure(config):
    settings.REPORT_DIR.mkdir(parents=True, exist_ok=True)
    settings.SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    settings.LOGS_DIR.mkdir(parents=True, exist_ok=True)
    config.addinivalue_line("markers", "test_id(id): Unique test case identifier (SEL-XXX)")
    config.addinivalue_line("markers", "category(name): Functional category of the test case")

@pytest.fixture(scope="session")
def driver(request):
    driver_instance = DriverFactory.get_driver()
    yield driver_instance
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
        driver_inst = item.funcargs.get("driver", None)
        test_id_marker = item.get_closest_marker("test_id")
        test_id = test_id_marker.args[0] if test_id_marker else item.name
        
        if driver_inst:
            screenshot, log = save_failure_artifacts(driver_inst, test_id, report.longreprtext)
            report.sections.append(("Failure Artifacts", f"Screenshot: {screenshot}\nLog: {log}"))
