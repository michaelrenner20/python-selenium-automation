from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):

    SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
    EMAIL_INPUT =(By.ID, 'ap_email')

    def verify_signin(self, expected_text):
        actual_result = self.find_element(*self.SIGNIN_HEADER).text
        assert expected_text == actual_result, f'Error, expected {expected_text} did not match actual {actual_result}'

    def verify_signin_opened(self):
        self.verify_text('Sign in', *self.SIGNIN_HEADER)
        # Verify email field present
        self.driver.find_element(*self.EMAIL_INPUT)
        self.verify_partial_url('ap/signin')