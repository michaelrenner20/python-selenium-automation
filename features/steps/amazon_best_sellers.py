from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


BEST_SELLERS = (By.CSS_SELECTOR, "div[class*='nav-tab-all_style_zg-tabs'] li")

@given('Open Amazon Best Sellers page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify Best Sellers has {expected_amount} links')
def verify_link_amount(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*BEST_SELLERS)
    # print(f'Total links: {len(links)}')
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'