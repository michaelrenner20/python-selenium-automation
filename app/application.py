from pages.main_page import MainPage
from pages.privacy_notice_page import PrivacyNotice
from pages.not_found_page import NotFoundPage
from pages.header import Header
from pages.search_result_page import SearchResultPage
from pages.signin_page import SignInPage
from pages.cart_page import Cart

class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.privacy_notice_page = PrivacyNotice(driver)
        self.not_found_page = NotFoundPage(driver)
        self.header = Header(driver)
        self.search_result_page = SearchResultPage(driver)
        self.signin_page = SignInPage(driver)
        self.cart_page = Cart(driver)

# app = Application()
# app.main_page.open_main()
# app.header.search_product()