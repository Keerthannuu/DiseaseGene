# Selenium UI Automation Testing Framework

Comprehensive end-to-end browser testing suite for DiseaseGeneMap, covering exactly **300 test cases (SEL-001 through SEL-300)**.

---

## 1. Overview & Architecture

* **Framework**: Python 3.12, pytest, Selenium WebDriver, pytest-xdist.
* **Design Pattern**: Page Object Model (POM) with centralized locator mappings.
* **Synchronization**: 100% explicit waits (`WebDriverWait` and `expected_conditions`), zero arbitrary `time.sleep()`.
* **Execution**: Headless Chrome (`--headless=new`, `--no-sandbox`, `--disable-dev-shm-usage`).
* **Test Isolation**: Each test case prepares its state independently; no inter-test dependencies.

### Directory Structure

```text
tests/selenium/
├── config/             # Environment and driver configuration
├── fixtures/           # Pytest fixtures and failure hooks
├── pages/              # Page Object Model representations
├── utils/              # Driver factory, explicit wait helpers, reporter
├── data/               # Test data fixtures
├── reports/            # JUnit XML, HTML reports, screenshots, logs
└── test_cases/         # Concrete test modules (SEL-001 -> SEL-300)
    ├── test_authentication.py          (SEL-001 -> SEL-035)
    ├── test_navigation.py              (SEL-036 -> SEL-065)
    ├── test_genes.py                   (SEL-066 -> SEL-105)
    ├── test_diseases.py                (SEL-106 -> SEL-140)
    ├── test_associations_variants.py   (SEL-141 -> SEL-175)
    ├── test_pathways_drugs.py          (SEL-176 -> SEL-210)
    ├── test_publications_search.py     (SEL-211 -> SEL-245)
    ├── test_analytics_insights.py      (SEL-246 -> SEL-275)
    └── test_admin_security_ui.py       (SEL-276 -> SEL-300)
```

---

## 2. Environment Variables & Secrets

Configure the following in `.env` for local testing or GitHub Secrets in CI:

| Variable | Description | Default |
|---|---|---|
| `BASE_URL` | Base URL of DiseaseGene frontend | `http://localhost:3000` |
| `TEST_USERNAME` | Standard researcher test user | `test_researcher` |
| `TEST_PASSWORD` | Researcher password | `TestPassword123!` |
| `ADMIN_USERNAME` | Administrator test user | `test_admin` |
| `ADMIN_PASSWORD` | Admin password | `AdminPassword123!` |
| `HEADLESS` | Run browser in headless mode | `true` |
| `SELENIUM_BROWSER` | Browser driver choice (`chrome`, `firefox`) | `chrome` |

---

## 3. Local Execution

### Install Dependencies

```bash
pip install -r backend/requirements.txt
pip install pytest pytest-html pytest-rerunfailures pytest-xdist selenium pydantic-settings
```

### Run All 300 Tests

```bash
pytest tests/selenium/test_cases -q --html=tests/selenium/reports/report.html --self-contained-html
```

### Run in Parallel (pytest-xdist)

```bash
pytest tests/selenium/test_cases -n 4 -q
```

### Run Specific Shard or Module

```bash
pytest tests/selenium/test_cases/test_authentication.py -q
```

---

## 4. GitHub Actions CI/CD Execution

* **Workflow**: `.github/workflows/selenium-tests.yml`
* **Independence**: Executes completely independently with zero dependencies on Appium, k6, or Security workflows.
* **Sharding**: 4 parallel shards executing ~75 tests each across matrix runners:
  * **Shard 1**: Authentication & Navigation (SEL-001 - SEL-065)
  * **Shard 2**: Genes & Diseases Catalogs (SEL-066 - SEL-140)
  * **Shard 3**: Associations, Variants, Pathways & Drugs (SEL-141 - SEL-210)
  * **Shard 4**: Publications, Search, Analytics & Admin (SEL-211 - SEL-300)
* **Retry Strategy**: Maximum 1 retry (`--reruns 1`) to catch transient network flickers without hiding bugs.
* **Concurrency**: `cancel-in-progress: true` prevents outdated PR runs from consuming runner resources.

---

## 5. Artifacts & Reporting

* **Artifacts Uploaded**: `selenium-report-shard-1` through `selenium-report-shard-4`.
* **Artifact Contents**:
  * `junit-shard-X.xml`
  * `report-shard-X.html`
  * `screenshots/<TEST_ID>_<TIMESTAMP>.png` (on failure only)
  * `logs/<TEST_ID>_<TIMESTAMP>.log` (browser console logs and stack trace)
* **GitHub Step Summary**: Writes formatted summary table with pass/fail counts and failed test IDs to `$GITHUB_STEP_SUMMARY`.
