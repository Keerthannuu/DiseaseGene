# Appium Mobile Automation Testing Framework

Comprehensive Android mobile testing suite for DiseaseGeneMap (Capacitor Android app: `com.romcom.diseasegenemap`), covering exactly **300 test cases (APP-001 through APP-300)**.

---

## 1. Overview & Architecture

* **Framework**: Python 3.12, Appium-Python-Client 3+, Appium 2, UiAutomator2 driver.
* **Design Pattern**: Screen Object Model (SOM) separating screen locators from assertions.
* **Target Application**: Android Capacitor hybrid build (`frontend/android/app`).
* **Platform Support**: Android 12, 13 (API 33), 14; headless x86_64 emulators.
* **Coverage Scope**: App lifecycle, touch gestures (swipes, fling, pull-to-refresh), device states (rotation, airplane mode, backgrounding), accessibility, and all DiseaseGene business flows.

### Directory Structure

```text
tests/appium/
├── config/             # Appium capabilities and emulator configuration
├── fixtures/           # Appium session fixture, device info, failure hooks
├── screens/            # Screen Object Model classes
├── utils/              # Driver factory, touch gestures helper, reporter
├── data/               # Mobile test data fixtures
├── reports/            # JUnit XML, HTML reports, screenshots, device-info, logcat
└── test_cases/         # Concrete test modules (APP-001 -> APP-300)
    ├── test_lifecycle_install.py               (APP-001 -> APP-035)
    ├── test_mobile_auth.py                     (APP-036 -> APP-075)
    ├── test_navigation_gestures.py             (APP-076 -> APP-115)
    ├── test_mobile_genes_diseases.py           (APP-116 -> APP-165)
    ├── test_associations_variants_pathways.py  (APP-166 -> APP-205)
    ├── test_analytics_favorites_admin.py       (APP-206 -> APP-250)
    └── test_edge_network_device.py             (APP-251 -> APP-300)
```

---

## 2. Environment Variables & Capabilities

| Variable | Description | Default |
|---|---|---|
| `APPIUM_SERVER_URL` | Appium 2 server listener endpoint | `http://localhost:4723` |
| `ANDROID_APP_PATH` | Path to compiled debug APK | `frontend/android/app/build/outputs/apk/debug/app-debug.apk` |
| `ANDROID_DEVICE_NAME` | Android emulator or device identifier | `emulator-5554` |
| `ANDROID_PLATFORM_VERSION`| Android OS version | `13.0` |
| `ANDROID_APP_PACKAGE` | Application package name | `com.romcom.diseasegenemap` |
| `ANDROID_APP_ACTIVITY` | Main launcher activity | `.MainActivity` |

---

## 3. Local Execution

### Prerequisites

```bash
# Install Appium 2 and UiAutomator2 driver
npm install -g appium
appium driver install uiautomator2

# Python dependencies
pip install Appium-Python-Client pytest pytest-html pytest-rerunfailures pydantic-settings
```

### Start Appium Server

```bash
appium --address 127.0.0.1 --port 4723
```

### Run All 300 Tests

```bash
pytest tests/appium/test_cases -q --html=tests/appium/reports/report.html --self-contained-html
```

---

## 4. GitHub Actions CI/CD Execution

* **Workflow**: `.github/workflows/appium-tests.yml`
* **Independence**: Executes completely independently without any dependency on other workflows.
* **Trigger**: Triggered via `workflow_dispatch` (with custom parameters: `environment`, `android_version`, `test_group`) and on pushes to `frontend/android/**`.
* **Sharding**: 4 parallel shards executing ~75 tests each with individual emulator sessions.
* **Emulator Optimization**: Headless flags (`-no-window -no-audio -no-boot-anim`) ensure fast boot and low resource consumption.
* **Retry Strategy**: 1 retry (`--reruns 1`).

---

## 5. Artifacts & Reporting

* **Artifacts Uploaded**: `appium-report-shard-1` through `appium-report-shard-4`.
* **Artifact Contents**:
  * `junit-shard-X.xml`
  * `report-shard-X.html`
  * `screenshots/<TEST_ID>_<TIMESTAMP>.png` (on failure)
  * `logs/<TEST_ID>_<TIMESTAMP>_device_info.txt`
  * `logs/<TEST_ID>_<TIMESTAMP>.log` (filtered logcat)
* **GitHub Step Summary**: Appends structured Markdown table to `$GITHUB_STEP_SUMMARY`.
