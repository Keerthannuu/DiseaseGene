from selenium.webdriver.common.by import By
from tests.selenium.pages.base_page import BasePage

class GenesPage(BasePage):
    PATH = "/genes"

    SEARCH_INPUT = (By.CSS_SELECTOR, "input[placeholder*='search' i], input[data-testid='gene-search']")
    CHROMOSOME_SELECT = (By.CSS_SELECTOR, "select[name='chromosome'], button[data-testid='chr-filter']")
    GENE_ROWS = (By.CSS_SELECTOR, "table tbody tr, .gene-card")
    PAGINATION_NEXT = (By.CSS_SELECTOR, "button:has-text('Next'), [aria-label='Next page']")
    PAGINATION_PREV = (By.CSS_SELECTOR, "button:has-text('Previous'), [aria-label='Previous page']")
    FAVORITE_BUTTON = (By.CSS_SELECTOR, "button[aria-label*='favorite' i], button svg.heart")

    def open_genes(self):
        return self.open(self.PATH)

    def search_gene(self, query):
        self.type_text(self.SEARCH_INPUT, query)

    def filter_by_chromosome(self, chromosome):
        if self.is_visible(self.CHROMOSOME_SELECT):
            self.click(self.CHROMOSOME_SELECT)
            opt_locator = (By.XPATH, f"//option[text()='Chr {chromosome}' or text()='{chromosome}'] | //button[text()='Chr {chromosome}']")
            self.click(opt_locator)

    def get_gene_count(self):
        return len(self.find_all(self.GENE_ROWS))
