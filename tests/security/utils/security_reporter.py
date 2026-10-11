import json
from datetime import datetime
from pathlib import Path
from tests.security.config.config import settings

def ensure_report_dirs():
    settings.HEADERS_DIR.mkdir(parents=True, exist_ok=True)
    settings.DEP_DIR.mkdir(parents=True, exist_ok=True)
    settings.TRIVY_DIR.mkdir(parents=True, exist_ok=True)
    settings.API_DIR.mkdir(parents=True, exist_ok=True)
    settings.ZAP_DIR.mkdir(parents=True, exist_ok=True)
    settings.SUMMARY_DIR.mkdir(parents=True, exist_ok=True)

def record_finding(category, test_id, name, severity, status, evidence="", remediation=""):
    ensure_report_dirs()
    finding = {
        "test_id": test_id,
        "name": name,
        "category": category,
        "severity": severity,
        "status": status,
        "evidence": evidence,
        "remediation": remediation,
        "timestamp": datetime.now().isoformat()
    }
    
    cat_file = settings.REPORT_DIR / f"{category}" / f"{test_id}.json"
    cat_file.parent.mkdir(parents=True, exist_ok=True)
    with open(cat_file, "w", encoding="utf-8") as f:
        json.dump(finding, f, indent=2)
    return finding
