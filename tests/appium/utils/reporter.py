import json
from datetime import datetime
from pathlib import Path
from tests.appium.config.config import settings

def save_appium_failure_artifacts(driver, test_id, error_message):
    settings.SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    settings.LOGS_DIR.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = settings.SCREENSHOT_DIR / f"{test_id}_{timestamp}.png"
    log_path = settings.LOGS_DIR / f"{test_id}_{timestamp}.log"
    device_info_path = settings.LOGS_DIR / f"{test_id}_{timestamp}_device_info.txt"
    
    # Capture screenshot
    try:
        driver.save_screenshot(str(screenshot_path))
    except Exception as e:
        screenshot_path = f"Screenshot capture failed: {e}"

    # Capture Appium/logcat logs
    logcat = []
    try:
        logcat = driver.get_log("logcat")[-100:]  # Last 100 entries
    except Exception:
        pass

    # Capture device info
    try:
        capabilities = driver.capabilities
        with open(device_info_path, "w", encoding="utf-8") as f:
            for k, v in capabilities.items():
                f.write(f"{k}: {v}\n")
    except Exception:
        pass

    log_data = {
        "test_id": test_id,
        "timestamp": timestamp,
        "error": str(error_message),
        "recent_logcat": logcat
    }

    try:
        with open(log_path, "w", encoding="utf-8") as f:
            json.dump(log_data, f, indent=2)
    except Exception:
        pass

    return str(screenshot_path), str(log_path)
