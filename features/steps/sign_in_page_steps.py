from behave import given, when, then
from selenium.webdriver.common.by import By


@then('Verify sign in page opened')
def verify_signin_opened(context):
    expected_result = 'Sign in'
    #actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    #assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
    context.app.signin_page.verify_sigin(expected_result)
