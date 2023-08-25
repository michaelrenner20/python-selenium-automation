from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignIn(Page):

    SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")


    def verify_sigin(self, expected_text):
        actual_result = self.find_element(*self.SIGNIN_HEADER).text
        assert expected_text == actual_result, f'Error, expected {expected_text} did not match actual {actual_result}'