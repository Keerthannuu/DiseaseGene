import os
import json
from datetime import datetime
from pathlib import Path
from tests.selenium.config.config import settings

def save_failure_artifacts(driver, test_id, error_message):
    settings.SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    settings.LOGS_DIR.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = settings.SCREENSHOT_DIR / f"{test_id}_{timestamp}.png"
    log_path = settings.LOGS_DIR / f"{test_id}_{timestamp}.log"
    
    # Save screenshot
    try:
        driver.save_screenshot(str(screenshot_path))
    except Exception as e:
        screenshot_path = f"Screenshot capture failed: {e}"
        
    # Save browser console logs
    browser_logs = []
    try:
        browser_logs = driver.get_log("browser")
    except Exception:
        pass
        
    log_data = {
        "test_id": test_id,
        "timestamp": timestamp,
        "current_url": driver.current_url if driver else "N/A",
        "error": str(error_message),
        "browser_logs": browser_logs
    }
    
    try:
        with open(log_path, "w", encoding="utf-8") as f:
            json.dump(log_data, f, indent=2)
    except Exception:
        pass
        
    return str(screenshot_path), str(log_path)
