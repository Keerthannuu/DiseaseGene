from selenium.webdriver.common.by import By
from tests.selenium.pages.base_page import BasePage

class NavigationBar(BasePage):
    BRAND_LOGO = (By.CSS_SELECTOR, "a[href='/'], .logo")
    GENES_LINK = (By.CSS_SELECTOR, "a[href='/genes']")
    DISEASES_LINK = (By.CSS_SELECTOR, "a[href='/diseases']")
    ASSOCIATIONS_LINK = (By.CSS_SELECTOR, "a[href='/associations']")
    VARIANTS_LINK = (By.CSS_SELECTOR, "a[href='/variants']")
    PATHWAYS_LINK = (By.CSS_SELECTOR, "a[href='/pathways']")
    DRUGS_LINK = (By.CSS_SELECTOR, "a[href='/drugs']")
    PUBLICATIONS_LINK = (By.CSS_SELECTOR, "a[href='/publications']")
    ANALYTICS_LINK = (By.CSS_SELECTOR, "a[href='/analytics']")
    AI_INSIGHTS_LINK = (By.CSS_SELECTOR, "a[href='/ai-insights']")
    DATABASE_LINK = (By.CSS_SELECTOR, "a[href='/database']")
    ADMIN_LINK = (By.CSS_SELECTOR, "a[href='/admin']")
    THEME_TOGGLE = (By.CSS_SELECTOR, "button[aria-label*='theme' i], button.theme-toggle")
    GLOBAL_SEARCH_INPUT = (By.CSS_SELECTOR, "header input[placeholder*='search' i], input[type='search']")
    USER_PROFILE_BUTTON = (By.CSS_SELECTOR, "header button[aria-label*='user' i], .user-avatar")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "button[data-testid='logout'], button:has-text('Logout')")

    def navigate_to_genes(self):
        self.click(self.GENES_LINK)

    def navigate_to_diseases(self):
        self.click(self.DISEASES_LINK)

    def navigate_to_associations(self):
        self.click(self.ASSOCIATIONS_LINK)

    def navigate_to_variants(self):
        self.click(self.VARIANTS_LINK)

    def navigate_to_pathways(self):
        self.click(self.PATHWAYS_LINK)

    def navigate_to_admin(self):
        self.click(self.ADMIN_LINK)
