from selenium.webdriver.common.by import By
from tests.selenium.pages.base_page import BasePage

class DiseasesPage(BasePage):
    PATH = "/diseases"
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[placeholder*='search' i], input[data-testid='disease-search']")
    CATEGORY_SELECT = (By.CSS_SELECTOR, "select[name='category'], button[data-testid='category-filter']")
    DISEASE_ROWS = (By.CSS_SELECTOR, "table tbody tr, .disease-card")

    def open_diseases(self):
        return self.open(self.PATH)

    def search_disease(self, query):
        self.type_text(self.SEARCH_INPUT, query)


class AssociationsPage(BasePage):
    PATH = "/associations"
    EVIDENCE_FILTER = (By.CSS_SELECTOR, "select[name='evidence_level'], [data-testid='evidence-filter']")
    SCORE_SLIDER = (By.CSS_SELECTOR, "input[type='range'], [data-testid='score-slider']")
    ASSOCIATION_ROWS = (By.CSS_SELECTOR, "table tbody tr, .association-card")

    def open_associations(self):
        return self.open(self.PATH)


class VariantsPage(BasePage):
    PATH = "/variants"
    CLIN_SIG_SELECT = (By.CSS_SELECTOR, "select[name='clinical_significance'], [data-testid='clinsig-filter']")
    MUTATION_SELECT = (By.CSS_SELECTOR, "select[name='mutation_type'], [data-testid='mutation-filter']")
    VARIANT_ROWS = (By.CSS_SELECTOR, "table tbody tr, .variant-card")

    def open_variants(self):
        return self.open(self.PATH)


class AdminPage(BasePage):
    PATH = "/admin"
    METRIC_CARDS = (By.CSS_SELECTOR, ".metric-card, [data-testid='metric-card']")
    PROFILE_USERNAME_INPUT = (By.CSS_SELECTOR, "input[name='admin_username'], input[placeholder*='username' i]")
    PROFILE_EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='admin_email'], input[placeholder*='email' i]")
    SAVE_PROFILE_BUTTON = (By.CSS_SELECTOR, "button:has-text('Save'), button[type='submit']")

    def open_admin(self):
        return self.open(self.PATH)
