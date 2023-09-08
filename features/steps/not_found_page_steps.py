from behave import given, when, then
from selenium.webdriver.common.by import By

PRIVACY_LINK = (By.CSS_SELECTOR, "a.help-display-cond[href='https://www.amazon.com/privacy']")

original_window = None

@given('Open Amazon T&C page')
def amazon_terms_page(context):
    context.driver.get(
        'https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8'
        '&nodeId=508088')


@when('Store original window')
def store_original_window(context):
    global original_window
    original_window = context.app.not_found_page.store_original_window()


@then('Return to original window')
def return_to_original_window(context):
    context.app.privacy_notice_page.switch_to_window(original_window)


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice_link(context):
    privacy_page_link = context.driver.find_element(*PRIVACY_LINK)
    privacy_page_link.click()

# @when('Switch to the newly opened window')
