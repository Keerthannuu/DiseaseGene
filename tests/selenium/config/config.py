import os
from pathlib import Path
from pydantic_settings import BaseSettings

class SeleniumConfig(BaseSettings):
    BASE_URL: str = os.getenv("BASE_URL", "http://localhost:3000")
    TEST_USERNAME: str = os.getenv("TEST_USERNAME", "test_researcher")
    TEST_PASSWORD: str = os.getenv("TEST_PASSWORD", "TestPassword123!")
    ADMIN_USERNAME: str = os.getenv("ADMIN_USERNAME", "test_admin")
    ADMIN_PASSWORD: str = os.getenv("ADMIN_PASSWORD", "AdminPassword123!")
    
    BROWSER: str = os.getenv("SELENIUM_BROWSER", "chrome")
    HEADLESS: bool = os.getenv("HEADLESS", "true").lower() in ("true", "1", "yes")
    EXPLICIT_WAIT: int = int(os.getenv("SELENIUM_EXPLICIT_WAIT", "10"))
    IMPLICIT_WAIT: int = int(os.getenv("SELENIUM_IMPLICIT_WAIT", "0"))
    
    REPORT_DIR: Path = Path(__file__).resolve().parent.parent / "reports"
    SCREENSHOT_DIR: Path = REPORT_DIR / "screenshots"
    LOGS_DIR: Path = REPORT_DIR / "logs"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = SeleniumConfig()
