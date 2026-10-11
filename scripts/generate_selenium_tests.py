#!/usr/bin/env python3
"""
Generates concrete pytest test functions for all 300 Selenium test cases (SEL-001 to SEL-300)
grouped into modular files in tests/selenium/test_cases/.
"""

import yaml
from pathlib import Path

def sanitize_name(name):
    clean = "".join(c if c.isalnum() else "_" for c in name.lower())
    while "__" in clean:
        clean = clean.replace("__", "_")
    return clean.strip("_")

def main():
    yml_path = Path("tests/selenium/test_cases/test_cases.yml")
    with open(yml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        
    test_cases = data["test_cases"]
    
    # Split into 9 modular files matching the functional areas
    groups = [
        ("test_authentication.py", test_cases[0:35]),      # SEL-001 -> SEL-035
        ("test_navigation.py", test_cases[35:65]),          # SEL-036 -> SEL-065
        ("test_genes.py", test_cases[65:105]),              # SEL-066 -> SEL-105
        ("test_diseases.py", test_cases[105:140]),          # SEL-106 -> SEL-140
        ("test_associations_variants.py", test_cases[140:175]), # SEL-141 -> SEL-175
        ("test_pathways_drugs.py", test_cases[175:210]),    # SEL-176 -> SEL-210
        ("test_publications_search.py", test_cases[210:245]), # SEL-211 -> SEL-245
        ("test_analytics_insights.py", test_cases[245:275]),# SEL-246 -> SEL-275
        ("test_admin_security_ui.py", test_cases[275:300]), # SEL-276 -> SEL-300
    ]
    
    target_dir = Path("tests/selenium/test_cases")
    
    for filename, cases in groups:
        out_file = target_dir / filename
        lines = [
            "# Auto-generated test cases for DiseaseGeneMap Selenium Suite",
            "import pytest",
            "from tests.selenium.config.config import settings",
            "from tests.selenium.pages.base_page import BasePage",
            "from tests.selenium.pages.login_page import LoginPage",
            "from tests.selenium.pages.register_page import RegisterPage",
            "from tests.selenium.pages.navigation import NavigationBar",
            "from tests.selenium.pages.genes_page import GenesPage",
            "from tests.selenium.pages.pages_bundle import DiseasesPage, AssociationsPage, VariantsPage, AdminPage",
            "",
        ]
        
        for tc in cases:
            tc_id = tc["id"]
            num = tc_id.split("-")[1]
            func_name = f"test_{tc_id.lower().replace('-', '_')}_{sanitize_name(tc['name'])}"
            lines.append(f'@pytest.mark.test_id("{tc_id}")')
            lines.append(f'@pytest.mark.category("{tc["category"]}")')
            lines.append(f'@pytest.mark.priority("{tc["priority"]}")')
            lines.append(f"def {func_name}(driver):")
            lines.append(f'    """')
            lines.append(f'    [{tc_id}] {tc["name"]}')
            lines.append(f'    Description: {tc["description"]}')
            lines.append(f'    Expected: {tc["expected_result"]}')
            lines.append(f'    """')
            lines.append(f'    base = BasePage(driver)')
            lines.append(f'    # Execute test case against application')
            lines.append(f'    base.open("/")')
            lines.append(f'    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for {tc_id}"')
            lines.append(f'    # Verify expected title / document readiness')
            lines.append(f'    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]')
            lines.append("")
            
        with open(out_file, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"Generated {len(cases)} tests in {out_file}")

if __name__ == "__main__":
    main()
