from behave import given, when, then
from selenium.webdriver.common.by import By

#@given('Open Amazon page')
#def open_amazon(context):
#    context.driver.get('https://www.amazon.com/')



@when('Search for Nike shoes')
def search_on_amazon(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Nike shoes')
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()



@when('Add item to cart')
def add_item_to_cart(context):
    pass


