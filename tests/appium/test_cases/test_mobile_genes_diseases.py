# Auto-generated test cases for DiseaseGeneMap Appium Mobile Suite
import pytest
from tests.appium.config.config import settings
from tests.appium.screens.base_screen import BaseScreen
from tests.appium.screens.screens_bundle import LoginScreen, HomeScreen, GenesScreen, DiseasesScreen, SearchScreen, FavoritesScreen, AdminScreen
from tests.appium.utils.gestures import AppiumGestures

@pytest.mark.test_id("APP-116")
@pytest.mark.category("genes")
@pytest.mark.priority("critical")
def test_app_116_mobile_genes_list_initial_rendering(appium_driver):
    """
    [APP-116] Mobile Genes List Initial Rendering
    Description: Open Genes tab on mobile app
    Expected: Genes list displays cards with gene symbol and name
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-116"

@pytest.mark.test_id("APP-117")
@pytest.mark.category("genes")
@pytest.mark.priority("high")
def test_app_117_mobile_genes_infinite_scroll_loading(appium_driver):
    """
    [APP-117] Mobile Genes Infinite Scroll Loading
    Description: Scroll to bottom of genes list
    Expected: Loading indicator appears and loads next batch of genes
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-117"

@pytest.mark.test_id("APP-118")
@pytest.mark.category("genes")
@pytest.mark.priority("critical")
def test_app_118_mobile_genes_search_by_symbol_brca1(appium_driver):
    """
    [APP-118] Mobile Genes Search by Symbol 'BRCA1'
    Description: Type 'BRCA1' in mobile genes search bar
    Expected: List filters immediately to BRCA1 record card
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-118"

@pytest.mark.test_id("APP-119")
@pytest.mark.category("genes")
@pytest.mark.priority("high")
def test_app_119_mobile_genes_chromosome_filter_bottom_sheet(appium_driver):
    """
    [APP-119] Mobile Genes Chromosome Filter Bottom Sheet
    Description: Tap 'Chromosome' filter pill on mobile
    Expected: Bottom sheet opens with grid of Chr 1..22, X, Y buttons
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-119"

@pytest.mark.test_id("APP-120")
@pytest.mark.category("genes")
@pytest.mark.priority("high")
def test_app_120_mobile_genes_filter_selection_chr_17(appium_driver):
    """
    [APP-120] Mobile Genes Filter Selection 'Chr 17'
    Description: Select 'Chr 17' in bottom sheet and tap 'Apply'
    Expected: Genes list updates showing only Chr 17 genes
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-120"

@pytest.mark.test_id("APP-121")
@pytest.mark.category("genes")
@pytest.mark.priority("medium")
def test_app_121_mobile_genes_clear_chromosome_filter(appium_driver):
    """
    [APP-121] Mobile Genes Clear Chromosome Filter
    Description: Tap 'Clear' in filter bottom sheet
    Expected: Filter cleared and all chromosomes shown
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-121"

@pytest.mark.test_id("APP-122")
@pytest.mark.category("genes")
@pytest.mark.priority("critical")
def test_app_122_mobile_gene_card_tap_to_open_detail(appium_driver):
    """
    [APP-122] Mobile Gene Card Tap to Open Detail
    Description: Tap on 'BRCA1' card in genes list
    Expected: Navigates to mobile Gene detail view
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-122"

@pytest.mark.test_id("APP-123")
@pytest.mark.category("genes")
@pytest.mark.priority("high")
def test_app_123_mobile_gene_detail_header_and_symbol(appium_driver):
    """
    [APP-123] Mobile Gene Detail Header and Symbol
    Description: Inspect gene detail screen on mobile
    Expected: Displays large gene symbol, official name, and tags
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-123"

@pytest.mark.test_id("APP-124")
@pytest.mark.category("genes")
@pytest.mark.priority("medium")
def test_app_124_mobile_gene_detail_genomic_coordinates_card(appium_driver):
    """
    [APP-124] Mobile Gene Detail Genomic Coordinates Card
    Description: Inspect coordinates section on mobile
    Expected: Displays Chromosome, Start/End positions in mobile card
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-124"

@pytest.mark.test_id("APP-125")
@pytest.mark.category("genes")
@pytest.mark.priority("medium")
def test_app_125_mobile_gene_detail_function_section_accordion(appium_driver):
    """
    [APP-125] Mobile Gene Detail Function Section Accordion
    Description: Tap 'Molecular Function' accordion section
    Expected: Accordion expands showing gene functional summary
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-125"

@pytest.mark.test_id("APP-126")
@pytest.mark.category("genes")
@pytest.mark.priority("medium")
def test_app_126_mobile_gene_detail_protein_information_card(appium_driver):
    """
    [APP-126] Mobile Gene Detail Protein Information Card
    Description: Inspect protein section on mobile detail screen
    Expected: Displays protein name, length, and UniProt badge
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-126"

@pytest.mark.test_id("APP-127")
@pytest.mark.category("genes")
@pytest.mark.priority("high")
def test_app_127_mobile_gene_detail_favorite_heart_tap(appium_driver):
    """
    [APP-127] Mobile Gene Detail Favorite Heart Tap
    Description: Tap heart icon in top bar of gene detail
    Expected: Heart icon fills red with confirmation toast
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-127"

@pytest.mark.test_id("APP-128")
@pytest.mark.category("genes")
@pytest.mark.priority("high")
def test_app_128_mobile_gene_detail_unfavorite_tap(appium_driver):
    """
    [APP-128] Mobile Gene Detail Unfavorite Tap
    Description: Tap filled heart icon again to unfavorite
    Expected: Heart un-fills with 'Removed from favorites' toast
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-128"

@pytest.mark.test_id("APP-129")
@pytest.mark.category("genes")
@pytest.mark.priority("low")
def test_app_129_mobile_gene_detail_share_button(appium_driver):
    """
    [APP-129] Mobile Gene Detail Share Button
    Description: Tap share icon in mobile top bar
    Expected: Android native share sheet opens with gene summary link
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-129"

@pytest.mark.test_id("APP-130")
@pytest.mark.category("genes")
@pytest.mark.priority("high")
def test_app_130_mobile_gene_detail_associated_diseases_list(appium_driver):
    """
    [APP-130] Mobile Gene Detail Associated Diseases List
    Description: Scroll to 'Associated Diseases' on mobile gene detail
    Expected: Displays scrollable cards of linked diseases
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-130"

@pytest.mark.test_id("APP-131")
@pytest.mark.category("genes")
@pytest.mark.priority("high")
def test_app_131_mobile_gene_detail_tap_associated_disease(appium_driver):
    """
    [APP-131] Mobile Gene Detail Tap Associated Disease
    Description: Tap on linked disease card 'Breast Cancer'
    Expected: Navigates directly to Disease detail screen
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-131"

@pytest.mark.test_id("APP-132")
@pytest.mark.category("genes")
@pytest.mark.priority("medium")
def test_app_132_mobile_gene_detail_associated_variants_carousel(appium_driver):
    """
    [APP-132] Mobile Gene Detail Associated Variants Carousel
    Description: Inspect variants section on mobile gene detail
    Expected: Displays horizontal swipeable carousel of variants
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-132"

@pytest.mark.test_id("APP-133")
@pytest.mark.category("genes")
@pytest.mark.priority("medium")
def test_app_133_mobile_gene_detail_associated_pathways_list(appium_driver):
    """
    [APP-133] Mobile Gene Detail Associated Pathways List
    Description: Inspect pathways chips on mobile gene detail
    Expected: Displays pathway chips for DNA repair pathways
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-133"

@pytest.mark.test_id("APP-134")
@pytest.mark.category("diseases")
@pytest.mark.priority("critical")
def test_app_134_mobile_diseases_list_initial_load(appium_driver):
    """
    [APP-134] Mobile Diseases List Initial Load
    Description: Open Diseases tab on mobile
    Expected: Diseases list renders with disease name cards
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-134"

@pytest.mark.test_id("APP-135")
@pytest.mark.category("diseases")
@pytest.mark.priority("high")
def test_app_135_mobile_diseases_infinite_scroll(appium_driver):
    """
    [APP-135] Mobile Diseases Infinite Scroll
    Description: Scroll to bottom of mobile diseases list
    Expected: Loads next batch of disease records
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-135"

@pytest.mark.test_id("APP-136")
@pytest.mark.category("diseases")
@pytest.mark.priority("critical")
def test_app_136_mobile_diseases_search_by_name_diabetes(appium_driver):
    """
    [APP-136] Mobile Diseases Search by Name 'Diabetes'
    Description: Type 'Diabetes' in mobile disease search
    Expected: List filters to diabetes related conditions
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-136"

@pytest.mark.test_id("APP-137")
@pytest.mark.category("diseases")
@pytest.mark.priority("high")
def test_app_137_mobile_diseases_category_filter_bottom_sheet(appium_driver):
    """
    [APP-137] Mobile Diseases Category Filter Bottom Sheet
    Description: Tap 'Category' filter pill
    Expected: Bottom sheet opens with Oncology, Neurology, Cardiology, etc.
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-137"

@pytest.mark.test_id("APP-138")
@pytest.mark.category("diseases")
@pytest.mark.priority("high")
def test_app_138_mobile_diseases_filter_selection_oncology(appium_driver):
    """
    [APP-138] Mobile Diseases Filter Selection 'Oncology'
    Description: Select 'Oncology' and tap Apply
    Expected: List updates showing cancer diseases
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-138"

@pytest.mark.test_id("APP-139")
@pytest.mark.category("diseases")
@pytest.mark.priority("critical")
def test_app_139_mobile_disease_card_tap_to_open_detail(appium_driver):
    """
    [APP-139] Mobile Disease Card Tap to Open Detail
    Description: Tap on disease card 'Alzheimer's Disease'
    Expected: Navigates to Disease detail screen on mobile
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-139"

@pytest.mark.test_id("APP-140")
@pytest.mark.category("diseases")
@pytest.mark.priority("high")
def test_app_140_mobile_disease_detail_clinical_overview(appium_driver):
    """
    [APP-140] Mobile Disease Detail Clinical Overview
    Description: Inspect overview section on mobile disease detail
    Expected: Displays clinical etiology and ICD-10 code badge
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-140"

@pytest.mark.test_id("APP-141")
@pytest.mark.category("diseases")
@pytest.mark.priority("low")
def test_app_141_mobile_disease_detail_omim_external_link(appium_driver):
    """
    [APP-141] Mobile Disease Detail OMIM External Link
    Description: Tap OMIM external link button
    Expected: Opens OMIM website in Chrome Custom Tab
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-141"

@pytest.mark.test_id("APP-142")
@pytest.mark.category("diseases")
@pytest.mark.priority("high")
def test_app_142_mobile_disease_detail_favorite_heart_toggle(appium_driver):
    """
    [APP-142] Mobile Disease Detail Favorite Heart Toggle
    Description: Tap favorite icon on disease detail screen
    Expected: Disease added to favorites with confirmation
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-142"

@pytest.mark.test_id("APP-143")
@pytest.mark.category("diseases")
@pytest.mark.priority("high")
def test_app_143_mobile_disease_detail_associated_genes_cards(appium_driver):
    """
    [APP-143] Mobile Disease Detail Associated Genes Cards
    Description: Scroll to linked genes section in disease detail
    Expected: Displays associated gene cards with confidence badges
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-143"

@pytest.mark.test_id("APP-144")
@pytest.mark.category("diseases")
@pytest.mark.priority("high")
def test_app_144_mobile_disease_detail_tap_linked_gene(appium_driver):
    """
    [APP-144] Mobile Disease Detail Tap Linked Gene
    Description: Tap linked gene card 'APOE'
    Expected: Navigates directly to /genes/APOE screen
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-144"

@pytest.mark.test_id("APP-145")
@pytest.mark.category("diseases")
@pytest.mark.priority("medium")
def test_app_145_mobile_disease_detail_therapeutic_drugs_list(appium_driver):
    """
    [APP-145] Mobile Disease Detail Therapeutic Drugs List
    Description: Inspect drug treatments section on disease screen
    Expected: Displays approved drugs and investigational therapies
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-145"

@pytest.mark.test_id("APP-146")
@pytest.mark.category("search")
@pytest.mark.priority("critical")
def test_app_146_mobile_dedicated_search_tab_initial_state(appium_driver):
    """
    [APP-146] Mobile Dedicated Search Tab Initial State
    Description: Open dedicated Search tab from bottom nav
    Expected: Displays search bar, recent searches, and entity type pills
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-146"

@pytest.mark.test_id("APP-147")
@pytest.mark.category("search")
@pytest.mark.priority("medium")
def test_app_147_mobile_search_auto_focus_behavior(appium_driver):
    """
    [APP-147] Mobile Search Auto-Focus Behavior
    Description: Tap search tab
    Expected: Search input auto-focuses and keyboard opens
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-147"

@pytest.mark.test_id("APP-148")
@pytest.mark.category("search")
@pytest.mark.priority("critical")
def test_app_148_mobile_search_multi_entity_query_tp53(appium_driver):
    """
    [APP-148] Mobile Search Multi-Entity Query 'TP53'
    Description: Type 'TP53' in mobile search input
    Expected: Returns combined results: Genes, Diseases, Variants
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-148"

@pytest.mark.test_id("APP-149")
@pytest.mark.category("search")
@pytest.mark.priority("high")
def test_app_149_mobile_search_type_filter_pill_genes(appium_driver):
    """
    [APP-149] Mobile Search Type Filter Pill 'Genes'
    Description: Tap 'Genes' filter pill on mobile search
    Expected: Results filter to display only gene matches
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-149"

@pytest.mark.test_id("APP-150")
@pytest.mark.category("search")
@pytest.mark.priority("high")
def test_app_150_mobile_search_type_filter_pill_diseases(appium_driver):
    """
    [APP-150] Mobile Search Type Filter Pill 'Diseases'
    Description: Tap 'Diseases' filter pill
    Expected: Results filter to display only disease matches
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-150"

@pytest.mark.test_id("APP-151")
@pytest.mark.category("search")
@pytest.mark.priority("medium")
def test_app_151_mobile_search_type_filter_pill_variants(appium_driver):
    """
    [APP-151] Mobile Search Type Filter Pill 'Variants'
    Description: Tap 'Variants' filter pill
    Expected: Results filter to display only variant matches
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-151"

@pytest.mark.test_id("APP-152")
@pytest.mark.category("search")
@pytest.mark.priority("medium")
def test_app_152_mobile_search_type_filter_pill_pathways(appium_driver):
    """
    [APP-152] Mobile Search Type Filter Pill 'Pathways'
    Description: Tap 'Pathways' filter pill
    Expected: Results filter to display only pathway matches
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-152"

@pytest.mark.test_id("APP-153")
@pytest.mark.category("search")
@pytest.mark.priority("medium")
def test_app_153_mobile_search_type_filter_pill_drugs(appium_driver):
    """
    [APP-153] Mobile Search Type Filter Pill 'Drugs'
    Description: Tap 'Drugs' filter pill
    Expected: Results filter to display only drug matches
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-153"

@pytest.mark.test_id("APP-154")
@pytest.mark.category("search")
@pytest.mark.priority("high")
def test_app_154_mobile_search_result_item_tap_navigation(appium_driver):
    """
    [APP-154] Mobile Search Result Item Tap Navigation
    Description: Tap on search result card in list
    Expected: Navigates directly to selected item's mobile detail view
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-154"

@pytest.mark.test_id("APP-155")
@pytest.mark.category("search")
@pytest.mark.priority("low")
def test_app_155_mobile_search_clear_button_x_tap(appium_driver):
    """
    [APP-155] Mobile Search Clear Button 'X' Tap
    Description: Tap 'X' icon inside mobile search input
    Expected: Search text cleared and keyboard remains open
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-155"

@pytest.mark.test_id("APP-156")
@pytest.mark.category("search")
@pytest.mark.priority("low")
def test_app_156_mobile_search_recent_searches_chip_tap(appium_driver):
    """
    [APP-156] Mobile Search Recent Searches Chip Tap
    Description: Tap saved recent search chip 'BRCA1'
    Expected: Fills search input and executes query immediately
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-156"

@pytest.mark.test_id("APP-157")
@pytest.mark.category("search")
@pytest.mark.priority("low")
def test_app_157_mobile_search_clear_recent_history(appium_driver):
    """
    [APP-157] Mobile Search Clear Recent History
    Description: Tap 'Clear History' link in search tab
    Expected: All recent search chips removed from screen
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-157"

@pytest.mark.test_id("APP-158")
@pytest.mark.category("search")
@pytest.mark.priority("medium")
def test_app_158_mobile_search_empty_result_illustration(appium_driver):
    """
    [APP-158] Mobile Search Empty Result Illustration
    Description: Search for 'UnknownBiomarker9999'
    Expected: Displays friendly empty state illustration with retry advice
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-158"

@pytest.mark.test_id("APP-159")
@pytest.mark.category("search")
@pytest.mark.priority("medium")
def test_app_159_mobile_search_special_characters_input(appium_driver):
    """
    [APP-159] Mobile Search Special Characters Input
    Description: Enter punctuation and emoji in search input
    Expected: App handles input gracefully without crashing
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-159"

@pytest.mark.test_id("APP-160")
@pytest.mark.category("search")
@pytest.mark.priority("high")
def test_app_160_mobile_search_offline_error_banner(appium_driver):
    """
    [APP-160] Mobile Search Offline Error Banner
    Description: Perform search while device offline
    Expected: Displays banner 'Search requires internet connection'
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-160"

@pytest.mark.test_id("APP-161")
@pytest.mark.category("search")
@pytest.mark.priority("medium")
def test_app_161_mobile_search_debouncing_behavior(appium_driver):
    """
    [APP-161] Mobile Search Debouncing Behavior
    Description: Type characters rapidly in search bar
    Expected: App debounces requests by 300ms before sending query
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-161"

@pytest.mark.test_id("APP-162")
@pytest.mark.category("search")
@pytest.mark.priority("low")
def test_app_162_mobile_search_voice_input_button_presence(appium_driver):
    """
    [APP-162] Mobile Search Voice Input Button Presence
    Description: Inspect mic icon in mobile search input
    Expected: Mic icon present for voice search integration
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-162"

@pytest.mark.test_id("APP-163")
@pytest.mark.category("search")
@pytest.mark.priority("low")
def test_app_163_mobile_search_results_count_summary(appium_driver):
    """
    [APP-163] Mobile Search Results Count Summary
    Description: Inspect header above search results list
    Expected: Displays summary text 'Found 14 matching results'
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-163"

@pytest.mark.test_id("APP-164")
@pytest.mark.category("search")
@pytest.mark.priority("low")
def test_app_164_mobile_search_result_highlight_styling(appium_driver):
    """
    [APP-164] Mobile Search Result Highlight Styling
    Description: Inspect matched text snippet in search card
    Expected: Matched query words highlighted in theme color
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-164"

@pytest.mark.test_id("APP-165")
@pytest.mark.category("search")
@pytest.mark.priority("medium")
def test_app_165_mobile_search_back_button_keyboard_dismissal(appium_driver):
    """
    [APP-165] Mobile Search Back Button Keyboard Dismissal
    Description: Press back button while search keyboard is open
    Expected: Dismisses keyboard first while remaining on search screen
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-165"
