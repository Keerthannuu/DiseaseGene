# k6 Performance & Load Testing Framework

Scalable performance and reliability testing framework for DiseaseGeneMap API using k6, comprising exactly **300 load testing scenarios (LOAD-001 through LOAD-300)**.

---

## 1. Overview & Profiles

To safeguard test environments and avoid unnecessary traffic noise, the 300 load scenarios are partitioned into **execution profiles**. **All 300 scenarios are never run simultaneously.**

| Profile | Scenario Range | Target VUs | Duration | Purpose |
|---|---|---|---|---|
| `smoke` | LOAD-001 – LOAD-040 | 1–2 VUs | 20s | Fast baseline sanity checks across all API endpoints |
| `load` | LOAD-041 – LOAD-100 | 20–30 VUs | 2m | Normal day-to-day user concurrency and browsing |
| `stress` | LOAD-101 – LOAD-160 | 50–200 VUs | 2.5m | Finding breaking points and database saturation |
| `spike` | LOAD-161 – LOAD-200 | 10 -> 250 VUs | 1m | Sudden surge traffic handling and recovery verification |
| `soak` | LOAD-201 – LOAD-240 | 20 VUs | 6.5m | Memory leak and connection leak endurance testing |
| `api` | LOAD-241 – LOAD-275 | 15–25 VUs | 1m | Database-heavy aggregations, deep offsets, serialization |
| `authentication` | LOAD-276 – LOAD-300 | 10–20 VUs | 40s | Concurrent registration, bcrypt hashing, JWT throughput |

---

## 2. Thresholds & SLA Governance

Thresholds are strictly enforced in `tests/load/utils/thresholds.js`:

```javascript
export const THRESHOLDS = {
  smoke: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<300']
  },
  load: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500']
  },
  stress: {
    http_req_failed: ['rate<0.05'],
    http_req_duration: ['p(95)<1000']
  }
};
```

---

## 3. Local Execution

### Install k6

* **Windows**: `winget install k6` or `choco install k6`
* **macOS**: `brew install k6`
* **Linux**: `sudo apt install k6`

### Execute Smoke Profile

```bash
LOAD_TEST_BASE_URL="http://localhost:8000" LOAD_TEST_PROFILE="smoke" k6 run tests/load/runner.js
```

### Execute Normal Load Profile

```bash
LOAD_TEST_BASE_URL="http://localhost:8000" LOAD_TEST_PROFILE="load" k6 run tests/load/runner.js
```

### Custom VUs and Duration Override

```bash
LOAD_TEST_BASE_URL="http://localhost:8000" LOAD_TEST_PROFILE="api" k6 run --vus 25 --duration 1m tests/load/runner.js
```

---

## 4. GitHub Actions CI/CD Execution

* **Workflow**: `.github/workflows/load-tests.yml`
* **Independence**: Executes completely independently with zero dependencies on Selenium, Appium, or Security workflows.
* **Default CI Trigger**: Only lightweight `smoke` profile executes on PRs touching backend code.
* **Manual Trigger**: Supports `workflow_dispatch` with parameter selection:
  * `profile`: `smoke`, `load`, `stress`, `spike`, `soak`, `api`, `authentication`
  * `duration`: Custom duration (e.g. `30s`, `2m`)
  * `vus`: Virtual users count
* **Safety Guard**: High-volume profiles (stress, spike, soak) cannot be triggered automatically against production environments.

---

## 5. Artifacts & Reporting

* **Artifacts Uploaded**: `k6-load-test-report`.
* **Artifact Contents**:
  * `tests/load/reports/summary.json` (Structured JSON metrics: p50, p90, p95, p99, total requests, error rates)
  * `tests/load/reports/results.json` (Full raw k6 summary export)
* **GitHub Step Summary**: Formatted performance metrics table written directly to `$GITHUB_STEP_SUMMARY`.
