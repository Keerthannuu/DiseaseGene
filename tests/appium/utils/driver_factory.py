import os
import urllib.request
import json
from appium import webdriver
from appium.options.android import UiAutomator2Options
from tests.appium.config.config import settings

class AppiumDriverFactory:
    _server_checked = False
    _server_available = False

    @classmethod
    def is_server_ready(cls, timeout=1.0):
        if cls._server_checked:
            return cls._server_available
            
        try:
            url = f"{settings.APPIUM_SERVER_URL.rstrip('/')}/status"
            req = urllib.request.Request(url, headers={"User-Agent": "pytest-check"})
            with urllib.request.urlopen(req, timeout=timeout) as response:
                if response.status == 200:
                    cls._server_available = True
        except Exception:
            cls._server_available = False
            
        cls._server_checked = True
        return cls._server_available

    @classmethod
    def get_driver(cls):
        if not cls.is_server_ready():
            raise ConnectionError(f"Appium server not reachable at {settings.APPIUM_SERVER_URL}")

        options = UiAutomator2Options()
        options.platform_name = settings.PLATFORM_NAME
        options.automation_name = settings.AUTOMATION_NAME
        options.device_name = settings.DEVICE_NAME
        options.platform_version = settings.PLATFORM_VERSION
        options.app_package = settings.APP_PACKAGE
        options.app_activity = settings.APP_ACTIVITY
        options.new_command_timeout = settings.COMMAND_TIMEOUT
        options.auto_grant_permissions = True
        options.no_reset = True
        
        # If APK path exists, install/use it
        if os.path.exists(settings.APP_PATH):
            options.app = os.path.abspath(settings.APP_PATH)
            
        driver = webdriver.Remote(
            command_executor=settings.APPIUM_SERVER_URL,
            options=options
        )
        return driver
