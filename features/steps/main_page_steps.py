from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
ORDERS_BTN = (By.ID, 'nav-orders')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem')
SIGNIN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-signin-button')


@given('Open Amazon page')
def open_amazon(context):
    #context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()

@when('Search for {search_word}')
def search_on_amazon(context, search_word):
    #context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    #context.driver.find_element(*SEARCH_BTN).click()
    context.app.header.search_product(search_word)


@when('Click Orders')
def click_orders(context):
    #context.driver.find_element(*ORDERS_BTN).click()
    context.app.header.click_orders()
    # context.app.header.click_orders_btn()
    #context.driver.find_element(*ORDERS_BTN).click()
    #context.driver.wait.until(
    #    EC.element_to_be_clickable(ORDERS_BTN),
     #   message='Orders Button not Clickable'
    #).click()



@when('Click on button from SignIn popup')
def click_signin_from_popup(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(SIGNIN_BTN),
        message='SignIn btn from popup not clickable'
    ).click()
    # context.driver.wait.until(
    #     EC.element_to_be_clickable(SIGNIN_BTN),
    #     message='SignIn btn from popup not clickable'
    # ).click()
    context.app.header.click_signin_from_popup()


@when('Wait for 3 sec')
def wait_sec(context):
    sleep(3)


@when('Click on cart icon')
def click_cart(context):
    context.app.header.click_cart_icon()

@then('Verify Sign In is clickable')
def verify_signin_btn_clickable(context):
    # context.driver.wait.until(
    #     EC.element_to_be_clickable(SIGNIN_BTN),
    #     message='SignIn btn from popup not clickable'
    # )
    context.app.header.verify_signin_btn_clickable()


@then('Verify {actual_text} text present')
def verify_cart_text(context, actual_text):
    context.app.cart_page.verify_cart_text(actual_text)

@then('Verify Sign in dissappears')
def verify_signin_btn_disappears(context):
    context.app.header.verify_signin_btn_disappears()
    # context.driver.wait.until(
    #     EC.element_to_be_clickable(SIGNIN_BTN),
    #     message='SignIn btn did not disappear'
    # ).click()



@then('Verify footer has {expected_amount} links')
def verify_link_amount(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*FOOTER_LINKS)
    # print(f'Total links: {len(links)}')
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'


@then('Verify many links are shown in the footer')
def verify_many_links(context):
    # context.driver.find_element(*FOOTER_LINKS)
    links = context.driver.find_elements(*FOOTER_LINKS)
    assert len(links) > 1