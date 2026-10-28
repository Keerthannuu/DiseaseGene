#!/usr/bin/env python3
"""
Test Case Validation Script for DiseaseGene Automated Testing Framework.
Validates that exactly 300 unique, sequential test cases exist in each YAML suite:
  - Selenium:   SEL-001 -> SEL-300
  - Appium:     APP-001 -> APP-300
  - k6 Load:    LOAD-001 -> LOAD-300
  - Security:   SEC-001 -> SEC-300
Total: 1,200 test cases.
Checks:
  - Exactly 300 test cases per file
  - No duplicate IDs
  - Continuous sequential numbering without gaps
  - Presence of all required fields: id, category, name, description, priority, expected_result
"""

import sys
import re
from pathlib import Path
import yaml

SUITES = [
    {
        "name": "Selenium",
        "file": Path("tests/selenium/test_cases/test_cases.yml"),
        "prefix": "SEL",
        "expected_count": 300,
    },
    {
        "name": "Appium",
        "file": Path("tests/appium/test_cases/test_cases.yml"),
        "prefix": "APP",
        "expected_count": 300,
    },
    {
        "name": "k6 Load",
        "file": Path("tests/load/test_cases/test_cases.yml"),
        "prefix": "LOAD",
        "expected_count": 300,
    },
    {
        "name": "Security",
        "file": Path("tests/security/test_cases/test_cases.yml"),
        "prefix": "SEC",
        "expected_count": 300,
    },
]

REQUIRED_FIELDS = ["id", "category", "name", "description", "priority", "expected_result"]


def validate_suite(suite_info):
    name = suite_info["name"]
    file_path = suite_info["file"]
    prefix = suite_info["prefix"]
    expected_count = suite_info["expected_count"]

    errors = []

    if not file_path.exists():
        return False, [f"File not found: {file_path}"]

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except Exception as e:
        return False, [f"YAML parsing error in {file_path}: {e}"]

    if not isinstance(data, dict) or "test_cases" not in data:
        return False, [f"Missing top-level 'test_cases' list in {file_path}"]

    test_cases = data["test_cases"]
    actual_count = len(test_cases)

    if actual_count != expected_count:
        errors.append(f"Count mismatch: Expected {expected_count}, got {actual_count}")

    seen_ids = set()
    id_pattern = re.compile(rf"^{prefix}-(\d{{3}})$")
    found_indices = set()

    for idx, tc in enumerate(test_cases, start=1):
        if not isinstance(tc, dict):
            errors.append(f"Item #{idx} is not a dictionary mapping")
            continue

        # Check required fields
        for field in REQUIRED_FIELDS:
            if field not in tc or tc[field] is None or str(tc[field]).strip() == "":
                errors.append(f"Test item #{idx} ({tc.get('id', 'UNKNOWN')}) missing or empty required field: '{field}'")

        tc_id = tc.get("id", "")
        if not tc_id:
            continue

        # Check duplicate
        if tc_id in seen_ids:
            errors.append(f"Duplicate test ID detected: {tc_id}")
        seen_ids.add(tc_id)

        # Check ID format
        match = id_pattern.match(tc_id)
        if not match:
            errors.append(f"Invalid ID format '{tc_id}': must match pattern '{prefix}-XXX'")
        else:
            num = int(match.group(1))
            found_indices.add(num)

    # Check for missing sequential IDs (1 to expected_count)
    expected_indices = set(range(1, expected_count + 1))
    missing = expected_indices - found_indices
    if missing:
        missing_sorted = sorted(list(missing))
        sample_missing = missing_sorted[:10]
        extra_info = f" (+ {len(missing) - 10} more)" if len(missing) > 10 else ""
        errors.append(f"Missing {len(missing)} IDs: {[f'{prefix}-{i:03d}' for i in sample_missing]}{extra_info}")

    is_valid = len(errors) == 0
    return is_valid, errors


def main():
    print("=" * 60)
    print("TEST CASE VALIDATION SUITE")
    print("=" * 60)

    total_valid = 0
    total_expected = sum(s["expected_count"] for s in SUITES)
    overall_passed = True

    for suite in SUITES:
        is_valid, errors = validate_suite(suite)
        status_str = "PASS" if is_valid else "FAIL"
        print(f"\n[{status_str}] {suite['name']} Suite ({suite['prefix']}-001 -> {suite['prefix']}-{suite['expected_count']:03d})")
        print(f"      Target: {suite['file']}")

        if is_valid:
            print(f"      Verified: Exactly {suite['expected_count']} unique, sequentially numbered test cases.")
            total_valid += suite["expected_count"]
        else:
            overall_passed = False
            print(f"      Errors ({len(errors)}):")
            for err in errors[:10]:
                print(f"        - {err}")
            if len(errors) > 10:
                print(f"        ... and {len(errors) - 10} additional errors.")

    print("\n" + "=" * 60)
    print(f"SUMMARY: {total_valid} / {total_expected} test cases verified.")
    if overall_passed:
        print("ALL 1,200 TEST CASES VALIDATED SUCCESSFULLY!")
        print("=" * 60)
        return 0
    else:
        print("VALIDATION FAILED - Please fix the errors listed above.")
        print("=" * 60)
        return 1


if __name__ == "__main__":
    sys.exit(main())
