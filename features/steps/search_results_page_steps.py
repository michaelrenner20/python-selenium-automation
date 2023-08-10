from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')


@then('Verify search result is {expected_result}')
def verify_search_result(context, expected_result):
    actual_result = context.driver.find_element(*SEARCH_RESULT).text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'


# @then('Verify Your Amazon Cart is empty')
# def verify_search_result(context):
#     expected_result = 'Your Amazon Cart is empty'
#     actual_result = context.driver.find_element(By.CSS_SELECTOR, '.a-row.sc-your-amazon-cart-is-empty').text
#     assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
#




