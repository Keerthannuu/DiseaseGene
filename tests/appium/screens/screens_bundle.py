from appium.webdriver.common.appiumby import AppiumBy
from tests.appium.screens.base_screen import BaseScreen

class LoginScreen(BaseScreen):
    USERNAME_INPUT = (AppiumBy.XPATH, "//android.widget.EditText[contains(@resource-id, 'username') or contains(@text, 'Username')]")
    PASSWORD_INPUT = (AppiumBy.XPATH, "//android.widget.EditText[contains(@resource-id, 'password') or contains(@password, 'true')]")
    SIGNIN_BUTTON = (AppiumBy.XPATH, "//android.widget.Button[contains(@text, 'Sign In') or contains(@text, 'Login')]")
    FORGOT_PASSWORD_LINK = (AppiumBy.XPATH, "//*[contains(@text, 'Forgot Password')]")


class HomeScreen(BaseScreen):
    BOTTOM_NAV_HOME = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc, 'Home')] | //*[contains(@text, 'Home')]")
    BOTTOM_NAV_GENES = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc, 'Genes')] | //*[contains(@text, 'Genes')]")
    BOTTOM_NAV_DISEASES = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc, 'Diseases')] | //*[contains(@text, 'Diseases')]")
    BOTTOM_NAV_SEARCH = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc, 'Search')] | //*[contains(@text, 'Search')]")
    BOTTOM_NAV_MORE = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc, 'More')] | //*[contains(@text, 'More')]")


class GenesScreen(BaseScreen):
    SEARCH_INPUT = (AppiumBy.XPATH, "//android.widget.EditText[contains(@text, 'Search') or contains(@content-desc, 'Search')]")
    CHROMOSOME_FILTER_BTN = (AppiumBy.XPATH, "//*[contains(@text, 'Chromosome') or contains(@content-desc, 'Chromosome')]")
    GENE_CARD = (AppiumBy.XPATH, "//*[contains(@resource-id, 'gene-card') or contains(@content-desc, 'Gene')]")


class DiseasesScreen(BaseScreen):
    SEARCH_INPUT = (AppiumBy.XPATH, "//android.widget.EditText[contains(@text, 'Search')]")
    CATEGORY_FILTER_BTN = (AppiumBy.XPATH, "//*[contains(@text, 'Category')]")


class SearchScreen(BaseScreen):
    SEARCH_INPUT = (AppiumBy.XPATH, "//android.widget.EditText")
    GENES_FILTER_CHIP = (AppiumBy.XPATH, "//*[contains(@text, 'Genes')]")
    DISEASES_FILTER_CHIP = (AppiumBy.XPATH, "//*[contains(@text, 'Diseases')]")


class FavoritesScreen(BaseScreen):
    GENES_TAB = (AppiumBy.XPATH, "//*[contains(@text, 'Saved Genes')]")
    DISEASES_TAB = (AppiumBy.XPATH, "//*[contains(@text, 'Saved Diseases')]")


class AdminScreen(BaseScreen):
    OVERVIEW_TITLE = (AppiumBy.XPATH, "//*[contains(@text, 'Admin') or contains(@text, 'Overview')]")
