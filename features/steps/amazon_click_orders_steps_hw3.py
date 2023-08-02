from behave import given, when, then
from selenium.webdriver.common.by import By

#@given('Open Amazon page')
#def open_amazon(context):
#    context.driver.get('https://www.amazon.com/')



@when('Click Orders')
def search_on_amazon(context):
    context.driver.find_element(By.ID, 'nav-orders').click()



@then('Verify sign in page opened')
def verify_search_result(context):
    expected_result = 'Sign in'
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'

