import os
from pathlib import Path
from pydantic_settings import BaseSettings

class SecurityConfig(BaseSettings):
    TARGET_URL: str = os.getenv("SECURITY_TEST_TARGET", "http://localhost:8000")
    SCAN_TYPE: str = os.getenv("SCAN_TYPE", "fast")
    ZAP_PORT: int = int(os.getenv("ZAP_PORT", "8080"))
    
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent.parent
    REPORT_DIR: Path = Path(__file__).resolve().parent.parent / "reports"
    HEADERS_DIR: Path = REPORT_DIR / "headers"
    DEP_DIR: Path = REPORT_DIR / "dependencies"
    TRIVY_DIR: Path = REPORT_DIR / "trivy"
    API_DIR: Path = REPORT_DIR / "api"
    ZAP_DIR: Path = REPORT_DIR / "zap"
    SUMMARY_DIR: Path = REPORT_DIR / "summary"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = SecurityConfig()
