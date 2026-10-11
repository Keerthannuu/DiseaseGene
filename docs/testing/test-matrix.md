# Comprehensive Automated Testing Matrix (1,200 Tests)

Full traceability matrix for DiseaseGeneMap automated test suites.

---

## 1. Executive Summary

| Test Suite | ID Range | Total Tests | Shards | Execution Engine | Primary Artifact |
|---|---|---:|---|---|---|
| **Selenium UI** | SEL-001 → SEL-300 | 300 | 4 parallel shards (75/shard) | Python 3.12 + pytest + pytest-xdist | `selenium-report-shard-X` |
| **Appium Mobile** | APP-001 → APP-300 | 300 | 4 parallel shards (75/shard) | Python 3.12 + Appium 2 + UiAutomator2 | `appium-report-shard-X` |
| **k6 Performance** | LOAD-001 → LOAD-300 | 300 | Profile-based (smoke/load/stress/spike/soak/api) | k6 Go Engine | `k6-load-test-report` |
| **Security / SAST / DAST** | SEC-001 → SEC-300 | 300 | Parallel scanners | Bandit, Semgrep, Trivy, pip/npm-audit, ZAP | `security-test-report` |
| **TOTAL** | | **1,200** | | | |

---

## 2. Selenium UI Test Matrix (SEL-001 → SEL-300)

| Module / Category | ID Range | Count | Primary Focus | Shard |
|---|---|---:|---|---|
| Authentication & Session | SEL-001 → SEL-035 | 35 | Login, Register, Forgot Password, OTP, Token, Roles, Session Expiry | Shard 1 |
| Navigation, Layout & UI | SEL-036 → SEL-065 | 30 | Top navigation, Dark/Light theme, Hamburger, 404, Responsive breakpoints | Shard 1 |
| Genes Exploration | SEL-066 → SEL-105 | 40 | Genes table, Chromosome filters (1..22, X, Y), Detail view, Favorites | Shard 2 |
| Diseases Catalog | SEL-106 → SEL-140 | 35 | Disease catalog, Category filters, ICD-10, OMIM links, Detail views | Shard 2 |
| Associations & Variants | SEL-141 → SEL-175 | 35 | Confidence sliders, Evidence A-D, Pathogenicity badges, rsID search | Shard 3 |
| Pathways & Drugs | SEL-176 → SEL-210 | 35 | KEGG/Reactome pathways, FDA approved drugs, targets, clinical phases | Shard 3 |
| Publications & Global Search | SEL-211 → SEL-245 | 35 | PubMed citations, year filters, Cmd+K search modal, type filters | Shard 4 |
| Analytics & AI Insights | SEL-246 → SEL-275 | 30 | Metric counts, Chromosome/Evidence charts, D3 network graph, Database explorer | Shard 4 |
| Admin Panel & Security UI | SEL-276 → SEL-300 | 25 | Admin overview (403 guard), Profile update, CSV upload, XSS/SQLi UI defense | Shard 4 |
| **Total** | | **300** | | |

---

## 3. Appium Mobile Test Matrix (APP-001 → APP-300)

| Category | ID Range | Count | Primary Focus | Shard |
|---|---|---:|---|---|
| Installation, Launch & Lifecycle | APP-001 → APP-035 | 35 | APK install, cold launch, splash screen, backgrounding (10s/60s), rotation | Shard 1 |
| Mobile Authentication & Account | APP-036 → APP-075 | 40 | Mobile inputs, soft keyboard done/next, login, signup, OTP, profile | Shard 1 |
| Mobile Navigation & Gestures | APP-076 → APP-115 | 40 | Bottom navigation bar, drawer swipe, pull-to-refresh, fling scroll, touch targets | Shard 2 |
| Mobile Genes & Diseases Screens | APP-116 → APP-165 | 50 | Mobile gene cards, infinite scroll, category bottom sheets, OMIM custom tabs | Shard 3 |
| Associations, Variants & Pathways | APP-166 → APP-205 | 40 | Mobile cards, score badges, clinical significance tags, pathway chips | Shard 3 |
| Analytics, Favorites & Admin | APP-206 → APP-250 | 45 | Mobile charts, touch tooltips, favorites tabs, admin mobile views | Shard 4 |
| Edge Cases, Network & Device | APP-251 → APP-300 | 50 | Offline banner, slow 3G, Android 13/14 compatibility, deep links, permissions | Shard 4 |
| **Total** | | **300** | | |

---

## 4. k6 Load Testing Matrix (LOAD-001 → LOAD-300)

| Profile | ID Range | Count | Target VUs & Duration | Target Endpoints | Trigger |
|---|---|---:|---|---|---|
| **Smoke** | LOAD-001 → LOAD-040 | 40 | 1–2 VUs, 20s | `/health`, `/api/v1/stats`, `/genes`, `/diseases`, `/search` | PR, Manual |
| **Normal Load** | LOAD-041 → LOAD-100 | 60 | 20–30 VUs, 2m | Browsing genes, pagination, chromosome filters, search queries | Manual |
| **Stress** | LOAD-101 → LOAD-160 | 60 | 50–200 VUs, 2.5m | Heavy multi-type search, complex joins, pool saturation | Manual |
| **Spike** | LOAD-161 → LOAD-200 | 40 | 10 → 250 VUs, 1m | Instantaneous query bursts, 429 rate limit checks | Manual |
| **Soak** | LOAD-201 → LOAD-240 | 40 | 20 VUs, 6.5m | Sustained background traffic, memory leak & connection leak checks | Manual |
| **API Performance** | LOAD-241 → LOAD-275 | 35 | 15–25 VUs, 1m | Aggregations, deep offsets, JSON serialization, ACID transactions | Manual |
| **Authentication** | LOAD-276 → LOAD-300 | 25 | 10–20 VUs, 40s | Concurrent registration, bcrypt hashing load, JWT verification rate | Manual |
| **Total** | | **300** | | | |

---

## 5. Security & Vulnerability Test Matrix (SEC-001 → SEC-300)

| Category | ID Range | Count | Tooling | Primary Focus |
|---|---|---:|---|---|
| Security Headers & Transport | SEC-001 → SEC-045 | 45 | Requests, Mozilla Observatory | HSTS, nosniff, CSP, X-Frame-Options, CORS, Cookie flags |
| Dependencies & Supply Chain | SEC-046 → SEC-085 | 40 | pip-audit, npm audit, Trivy | FastAPI, Next.js, React, Capacitor, CVE databases |
| SAST & Code Security | SEC-086 → SEC-125 | 40 | Bandit, Semgrep | Unsafe deserialization, shell=True, SQL injection patterns |
| Authentication & RBAC | SEC-126 → SEC-175 | 50 | Pytest Security Suite | JWT algorithm confusion, OTP replay defense, Researcher vs Admin RBAC |
| Injection & Input Validation | SEC-176 → SEC-240 | 65 | Pytest Security Suite | SQLi in search/filters, XSS sanitization, Path traversal, CSV injection |
| OWASP ZAP Baseline & Passive | SEC-241 → SEC-300 | 60 | OWASP ZAP Baseline Scanner | Passive rules, anti-clickjacking, server leakage, sensitive disclosure |
| **Total** | | **300** | | |

---

## 6. Workflow Independence Matrix

| Workflow File | Triggers | Shards | Dependencies | Artifact Output |
|---|---|---|---|---|
| `selenium-tests.yml` | push, pull_request, workflow_dispatch | 4 | **NONE** (completely independent) | `selenium-report-shard-1..4` |
| `appium-tests.yml` | workflow_dispatch, push (`frontend/android/**`) | 4 | **NONE** (completely independent) | `appium-report-shard-1..4` |
| `load-tests.yml` | workflow_dispatch, pull_request (backend paths) | 1 (Profile) | **NONE** (completely independent) | `k6-load-test-report` |
| `vulnerability-tests.yml` | push, pull_request, schedule, workflow_dispatch | 1 (Multi-tool) | **NONE** (completely independent) | `security-test-report` |

> [!NOTE]
> There are zero `workflow_run` triggers or `needs: <other_workflow>` directives between any of the 4 workflows. Each executes in complete isolation.
