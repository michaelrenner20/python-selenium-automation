#Practice with locators.
#Create locators + search strategy for these page elements of Amazon Sign in page:


# Amazon Logo - (By.XPATH, "//i[@class='a-icon a-icon-logo']")
# Email Field - (By.id, 'ap_email')
# Continue Button - (By.id, 'continue')
# Conditions of use link - (By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_desktop_footer_cou?ie=UTF8&nodeId=508088']")
# Privacy Notice link - (By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")
# Need help link - By.XPATH, "//span[@class="a-expander-prompt']")
# Forgot your password link - (By.id, 'auth-fpp-link-bottom')
# Other issues with Sign-in link - (By.id, 'ap-other-signin-issues-link')
# Create your Amazon account button - (By.id, 'createAccountSubmit')


#Create a test case for the Sign In page using python & selenium script.
#(Make sure to use Incognito browser mode when searching for locators)

#Test Case: Logged out user sees Sign in page when clicking Orders
#1. Open https://www.amazon.com
#2. Click Orders
#3. Verify Sign in page opened: Sign In header is visible, email input field is present.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
# driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(executable_path='C:/Users/micha/python-selenium-automation/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

#click on orders button
# driver.find_element(By.XPATH, "//span[text() ='Orders']").click()
driver.find_element(By.ID, 'nav-orders').click()

sleep(4)

expected_result = 'Sign in'
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

#
assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'
print('Test case passed')

driver.quit()
