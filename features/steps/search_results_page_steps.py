from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
PRODUCT_TITLE = (By.CSS_SELECTOR, 'h2 span.a-text-normal')
PRODUCT_IMG = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()
    sleep(2)

@when('Click the Add to cart button')
def add_item_to_cart(context):
    # context.driver.find_element(By.ID, 'add-to-cart-button').click()
    context.app.cart_page.add_item_to_cart()

@when('Click icon')
def click_icon(context):
    #context.driver.find_element(By.CSS_SELECTOR, 'div[cel_widget_id="MAIN-SEARCH_RESULTS-3"] img.s-image').click()
    context.app.search_result_page.click_product_result()

@then('Verify search result is {expected_result}')
def verify_search_result(context, expected_result):
    context.app.search_result_page.verify_search_result(expected_result)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)

    for product in all_products:
        product_title = product.find_element(*PRODUCT_TITLE).text
        print(product_title)
        assert product_title, 'Product title not shown'
        product.find_element(*PRODUCT_IMG)

@then('Verify item was added to cart')
def verify_cart_not_empty(context):
    context.app.cart_page.verify_cart_not_empty('Added to Cart')
    # expected_result = 'Added to Cart'
    # actual_result = context.driver.find_element(By.CSS_SELECTOR, 'span.a-size-medium-plus.a-color-base.sw-atc-text.a-text-bold').text
    # assert actual_result == expected_result, f'Expected {expected_result} but got {actual_result}'



# @then('Verify Your Amazon Cart is empty')
# def verify_search_result(context):
#     expected_result = 'Your Amazon Cart is empty'
#     actual_result = context.driver.find_element(By.CSS_SELECTOR, '.a-row.sc-your-amazon-cart-is-empty').text
#     assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
#




