from selenium.webdriver.common.by import By
from pages.base_page import Page


class Cart(Page):

    CART_TEXT = (By.CSS_SELECTOR, 'div#sc-saved-cart-list-caption-container h2')
    ADDED_TO_CART_TEXT =(By.CSS_SELECTOR,'span.a-size-medium-plus.a-color-base.sw-atc-text.a-text-bold')
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')

    def verify_cart_text(self, expected_cart_text):
        self.verify_text(expected_cart_text, *self.CART_TEXT)

    def verify_cart_not_empty(self, expected_cart_text):
        self.verify_text(expected_cart_text, *self.ADDED_TO_CART_TEXT)
        # expected_result = 'Added to Cart'
        # actual_result = context.driver.find_element(By.CSS_SELECTOR, 'span.a-size-medium-plus.a-color-base.sw-atc-text.a-text-bold').text
        # assert actual_result == expected_result, f'Expected {expected_result} but got {actual_result}'
        # self.verify_cart_text(expected_cart_text, *self.ADDED_TO_CART_TEXT)


    def add_item_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)
        # context.driver.find_element(By.ID, 'add-to-cart-button').click()



