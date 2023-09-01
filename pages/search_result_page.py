from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultPage(Page):
    SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
    SEARCH_RESULT_1 = (By.CSS_SELECTOR, 'div[cel_widget_id="MAIN-SEARCH_RESULTS-3"] img.s-image')
    #def verify_search_result(self, expected_text):
    #    actual_text = self.find_element(*self.SEARCH_RESULT).text
    #    assert actual_text == expected_text,  \
    #        f'Error, expected {expected_text} did not match actual {actual_text}'

    def verify_search_result(self, result):  # "tea"
        self.verify_text(result, *self.SEARCH_RESULT)

    def click_product_result(self):
        self.click(*self.SEARCH_RESULT_1)
