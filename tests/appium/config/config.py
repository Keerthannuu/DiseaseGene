import os
from pathlib import Path
from pydantic_settings import BaseSettings

class AppiumConfig(BaseSettings):
    APPIUM_SERVER_URL: str = os.getenv("APPIUM_SERVER_URL", "http://localhost:4723")
    PLATFORM_NAME: str = "Android"
    AUTOMATION_NAME: str = "UiAutomator2"
    DEVICE_NAME: str = os.getenv("ANDROID_DEVICE_NAME", "emulator-5554")
    PLATFORM_VERSION: str = os.getenv("ANDROID_PLATFORM_VERSION", "13.0")
    APP_PACKAGE: str = os.getenv("ANDROID_APP_PACKAGE", "com.romcom.diseasegenemap")
    APP_ACTIVITY: str = os.getenv("ANDROID_APP_ACTIVITY", ".MainActivity")
    APP_PATH: str = os.getenv("ANDROID_APP_PATH", "frontend/android/app/build/outputs/apk/debug/app-debug.apk")
    COMMAND_TIMEOUT: int = int(os.getenv("APPIUM_COMMAND_TIMEOUT", "60"))
    
    REPORT_DIR: Path = Path(__file__).resolve().parent.parent / "reports"
    SCREENSHOT_DIR: Path = REPORT_DIR / "screenshots"
    LOGS_DIR: Path = REPORT_DIR / "logs"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = AppiumConfig()
