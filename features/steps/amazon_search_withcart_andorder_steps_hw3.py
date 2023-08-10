from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
#@given('Open Amazon page')
#def open_amazon(context):
#    context.driver.get('https://www.amazon.com/')



@when('Search for playstation')
def search_on_amazon(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('playstation')
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@when('Click icon')
def click_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div[cel_widget_id="MAIN-SEARCH_RESULTS-5"] img.s-image').click()


@when('Click the Add to cart button')
def add_item_to_cart(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()


@then('Verify item was added to cart')
def verify_cart_not_empty(context):
    expected_result = 'Added to Cart'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'span.a-size-medium-plus.a-color-base.sw-atc-text.a-text-bold').text
    assert actual_result == expected_result, f'Expected {expected_result} but got {actual_result}'
