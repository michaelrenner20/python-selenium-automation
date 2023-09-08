from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class NotFoundPage(Page):
    PRIVACY_NOTICE_LINK = (By.CSS_SELECTOR, "a.help-display-cond[href='https://www.amazon.com/privacy']")

    def store_original_window(self):
        return self.get_current_window()

    def click_privacy_notice_link(self):
        self.click(*self.PRIVACY_NOTICE_LINK)