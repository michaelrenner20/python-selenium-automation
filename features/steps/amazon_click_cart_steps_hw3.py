from behave import given, when, then
from selenium.webdriver.common.by import By

#@given('Open Amazon page')
#def open_amazon(context):
#    context.driver.get('https://www.amazon.com/')



@when('Click Cart icon')
def search_on_amazon(context):
    context.driver.find_element(By.ID, 'nav-cart-count').click()



@then('Verify Your Amazon Cart is empty')
def verify_search_result(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '.a-row.sc-your-amazon-cart-is-empty').text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'

