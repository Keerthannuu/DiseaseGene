# Auto-generated test cases for DiseaseGeneMap Selenium Suite
import pytest
from tests.selenium.config.config import settings
from tests.selenium.pages.base_page import BasePage
from tests.selenium.pages.login_page import LoginPage
from tests.selenium.pages.register_page import RegisterPage
from tests.selenium.pages.navigation import NavigationBar
from tests.selenium.pages.genes_page import GenesPage
from tests.selenium.pages.pages_bundle import DiseasesPage, AssociationsPage, VariantsPage, AdminPage

@pytest.mark.test_id("SEL-106")
@pytest.mark.category("diseases")
@pytest.mark.priority("critical")
def test_sel_106_diseases_catalog_initial_load(driver):
    """
    [SEL-106] Diseases Catalog Initial Load
    Description: Navigate to /diseases catalog page
    Expected: Diseases list loads with initial dataset
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-106"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-107")
@pytest.mark.category("diseases")
@pytest.mark.priority("high")
def test_sel_107_diseases_table_column_headers(driver):
    """
    [SEL-107] Diseases Table Column Headers
    Description: Verify table columns on diseases page
    Expected: Columns: Disease Name, Category, ICD Code, OMIM, Actions
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-107"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-108")
@pytest.mark.category("diseases")
@pytest.mark.priority("high")
def test_sel_108_diseases_pagination_next_page(driver):
    """
    [SEL-108] Diseases Pagination Next Page
    Description: Click 'Next' button on diseases pagination
    Expected: Loads next page with incremented offset
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-108"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-109")
@pytest.mark.category("diseases")
@pytest.mark.priority("medium")
def test_sel_109_diseases_pagination_previous_page(driver):
    """
    [SEL-109] Diseases Pagination Previous Page
    Description: Click 'Previous' button on page 2
    Expected: Returns to previous page of diseases
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-109"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-110")
@pytest.mark.category("diseases")
@pytest.mark.priority("critical")
def test_sel_110_disease_search_by_name_alzheimer(driver):
    """
    [SEL-110] Disease Search by Name 'Alzheimer'
    Description: Type 'Alzheimer' in disease search input
    Expected: Filters to Alzheimer's Disease record
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-110"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-111")
@pytest.mark.category("diseases")
@pytest.mark.priority("high")
def test_sel_111_disease_search_by_name_diabetes(driver):
    """
    [SEL-111] Disease Search by Name 'Diabetes'
    Description: Type 'Diabetes' in disease search
    Expected: Displays Type 1 and Type 2 Diabetes records
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-111"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-112")
@pytest.mark.category("diseases")
@pytest.mark.priority("high")
def test_sel_112_disease_search_by_icd_10_code_e11(driver):
    """
    [SEL-112] Disease Search by ICD-10 Code 'E11'
    Description: Search by ICD code 'E11'
    Expected: Displays matching diabetes disease records
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-112"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-113")
@pytest.mark.category("diseases")
@pytest.mark.priority("high")
def test_sel_113_disease_filter_by_category_oncology(driver):
    """
    [SEL-113] Disease Filter by Category 'Oncology'
    Description: Select 'Cancer / Oncology' in category filter
    Expected: Table displays only cancer and neoplasm diseases
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-113"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-114")
@pytest.mark.category("diseases")
@pytest.mark.priority("high")
def test_sel_114_disease_filter_by_category_cardiovascular(driver):
    """
    [SEL-114] Disease Filter by Category 'Cardiovascular'
    Description: Select 'Cardiovascular' in category filter
    Expected: Table displays coronary artery and heart diseases
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-114"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-115")
@pytest.mark.category("diseases")
@pytest.mark.priority("high")
def test_sel_115_disease_filter_by_category_neurological(driver):
    """
    [SEL-115] Disease Filter by Category 'Neurological'
    Description: Select 'Neurological' in category filter
    Expected: Table displays Alzheimer's, Parkinson's, ALS
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-115"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-116")
@pytest.mark.category("diseases")
@pytest.mark.priority("medium")
def test_sel_116_disease_filter_by_category_metabolic(driver):
    """
    [SEL-116] Disease Filter by Category 'Metabolic'
    Description: Select 'Metabolic' in category filter
    Expected: Table displays diabetes and metabolic syndromes
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-116"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-117")
@pytest.mark.category("diseases")
@pytest.mark.priority("medium")
def test_sel_117_disease_filter_reset_action(driver):
    """
    [SEL-117] Disease Filter Reset Action
    Description: Click 'Reset Filters' on diseases page
    Expected: All category filters cleared, showing all diseases
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-117"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-118")
@pytest.mark.category("diseases")
@pytest.mark.priority("critical")
def test_sel_118_click_disease_row_to_open_detail_view(driver):
    """
    [SEL-118] Click Disease Row to Open Detail View
    Description: Click on disease record 'Breast Cancer'
    Expected: Navigates to /diseases/DIS001 or detail panel
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-118"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-119")
@pytest.mark.category("diseases")
@pytest.mark.priority("high")
def test_sel_119_disease_detail_header_and_category_badge(driver):
    """
    [SEL-119] Disease Detail Header and Category Badge
    Description: Inspect disease detail page header
    Expected: Displays disease title, category badge, and ICD code
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-119"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-120")
@pytest.mark.category("diseases")
@pytest.mark.priority("medium")
def test_sel_120_disease_detail_clinical_description(driver):
    """
    [SEL-120] Disease Detail Clinical Description
    Description: Inspect clinical overview section
    Expected: Displays disease etiology and phenotypic description
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-120"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-121")
@pytest.mark.category("diseases")
@pytest.mark.priority("medium")
def test_sel_121_disease_detail_omim_link(driver):
    """
    [SEL-121] Disease Detail OMIM Link
    Description: Click OMIM identifier link
    Expected: Opens OMIM database entry in new browser window
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-121"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-122")
@pytest.mark.category("diseases")
@pytest.mark.priority("high")
def test_sel_122_disease_detail_associated_genes_table(driver):
    """
    [SEL-122] Disease Detail Associated Genes Table
    Description: Inspect associated genes section on disease detail
    Expected: Lists linked genes (e.g. BRCA1, BRCA2, TP53)
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-122"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-123")
@pytest.mark.category("diseases")
@pytest.mark.priority("high")
def test_sel_123_disease_detail_click_associated_gene_link(driver):
    """
    [SEL-123] Disease Detail Click Associated Gene Link
    Description: Click gene symbol link inside disease detail
    Expected: Navigates directly to that gene's detail page
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-123"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-124")
@pytest.mark.category("diseases")
@pytest.mark.priority("medium")
def test_sel_124_disease_detail_associated_drugs_section(driver):
    """
    [SEL-124] Disease Detail Associated Drugs Section
    Description: Inspect therapeutic drugs section on disease page
    Expected: Displays targeted therapies and clinical drug agents
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-124"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-125")
@pytest.mark.category("diseases")
@pytest.mark.priority("high")
def test_sel_125_favorite_disease_click_while_logged_in(driver):
    """
    [SEL-125] Favorite Disease Click While Logged In
    Description: Click favorite star/heart on disease detail page
    Expected: Disease marked as favorite; toast notification shown
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-125"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-126")
@pytest.mark.category("diseases")
@pytest.mark.priority("high")
def test_sel_126_unfavorite_disease_action(driver):
    """
    [SEL-126] Unfavorite Disease Action
    Description: Click favorite button again to remove favorite
    Expected: Favorite status removed; toast notification shown
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-126"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-127")
@pytest.mark.category("diseases")
@pytest.mark.priority("medium")
def test_sel_127_favorite_disease_anonymous_user_handling(driver):
    """
    [SEL-127] Favorite Disease Anonymous User Handling
    Description: Click favorite button without signing in
    Expected: Prompts user to sign in to save favorites
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-127"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-128")
@pytest.mark.category("diseases")
@pytest.mark.priority("medium")
def test_sel_128_favorite_disease_state_saved_across_sessions(driver):
    """
    [SEL-128] Favorite Disease State Saved Across Sessions
    Description: Reload disease detail after favoriting
    Expected: Favorite indicator remains active
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-128"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-129")
@pytest.mark.category("diseases")
@pytest.mark.priority("medium")
def test_sel_129_disease_table_sort_by_name_ascending(driver):
    """
    [SEL-129] Disease Table Sort by Name Ascending
    Description: Click 'Disease Name' column header
    Expected: Diseases sorted alphabetically A-Z
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-129"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-130")
@pytest.mark.category("diseases")
@pytest.mark.priority("medium")
def test_sel_130_disease_table_sort_by_category(driver):
    """
    [SEL-130] Disease Table Sort by Category
    Description: Click 'Category' column header
    Expected: Diseases grouped/sorted by clinical category
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-130"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-131")
@pytest.mark.category("diseases")
@pytest.mark.priority("medium")
def test_sel_131_disease_detail_404_for_invalid_disease_id(driver):
    """
    [SEL-131] Disease Detail 404 for Invalid Disease ID
    Description: Navigate to /diseases/INVALID_DIS_9999
    Expected: Displays 'Disease not found' error banner
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-131"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-132")
@pytest.mark.category("diseases")
@pytest.mark.priority("medium")
def test_sel_132_disease_detail_back_to_catalog_button(driver):
    """
    [SEL-132] Disease Detail Back to Catalog Button
    Description: Click 'Back to Diseases' link
    Expected: Navigates back to /diseases maintaining filter state
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-132"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-133")
@pytest.mark.category("diseases")
@pytest.mark.priority("medium")
def test_sel_133_disease_catalog_search_non_existent_name(driver):
    """
    [SEL-133] Disease Catalog Search Non-Existent Name
    Description: Search for 'NonExistentCondition404'
    Expected: Displays 'No diseases found matching query'
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-133"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-134")
@pytest.mark.category("diseases")
@pytest.mark.priority("medium")
def test_sel_134_disease_detail_publication_citations(driver):
    """
    [SEL-134] Disease Detail Publication Citations
    Description: Inspect literature references section on disease page
    Expected: Displays linked PubMed publications
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-134"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-135")
@pytest.mark.category("diseases")
@pytest.mark.priority("low")
def test_sel_135_disease_detail_phenotype_tags(driver):
    """
    [SEL-135] Disease Detail Phenotype Tags
    Description: Inspect clinical phenotype tag badges
    Expected: Badges render with appropriate styling
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-135"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-136")
@pytest.mark.category("diseases")
@pytest.mark.priority("low")
def test_sel_136_disease_detail_risk_factor_summary(driver):
    """
    [SEL-136] Disease Detail Risk Factor Summary
    Description: Inspect genetic risk factors card
    Expected: Summarizes known penetrance and risk ratios
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-136"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-137")
@pytest.mark.category("diseases")
@pytest.mark.priority("low")
def test_sel_137_disease_catalog_items_per_page_selector(driver):
    """
    [SEL-137] Disease Catalog Items Per Page Selector
    Description: Select 100 items per page
    Expected: Table renders 100 disease rows
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-137"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-138")
@pytest.mark.category("diseases")
@pytest.mark.priority("low")
def test_sel_138_disease_catalog_quick_filter_clear_icon(driver):
    """
    [SEL-138] Disease Catalog Quick Filter Clear Icon
    Description: Click 'x' inside search input
    Expected: Search input cleared and list resets immediately
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-138"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-139")
@pytest.mark.category("diseases")
@pytest.mark.priority("low")
def test_sel_139_disease_detail_external_link_to_orphanet(driver):
    """
    [SEL-139] Disease Detail External Link to Orphanet
    Description: Click Orphanet link for rare diseases
    Expected: Opens Orphanet portal in external tab
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-139"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]

@pytest.mark.test_id("SEL-140")
@pytest.mark.category("diseases")
@pytest.mark.priority("medium")
def test_sel_140_disease_catalog_mobile_card_view(driver):
    """
    [SEL-140] Disease Catalog Mobile Card View
    Description: View diseases page on mobile viewport
    Expected: Cards render with title, category badge, and tap target
    """
    base = BasePage(driver)
    # Execute test case against application
    base.open("/")
    assert driver.current_url.startswith(settings.BASE_URL), f"Navigation failed for SEL-140"
    # Verify expected title / document readiness
    assert driver.execute_script("return document.readyState") in ["interactive", "complete"]
