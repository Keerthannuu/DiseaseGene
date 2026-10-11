from appium import webdriver
from appium.options.android import UiAutomator2Options
from tests.appium.config.config import settings
import os

class AppiumDriverFactory:
    @staticmethod
    def get_driver():
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
