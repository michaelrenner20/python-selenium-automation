
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
service = Service(executable_path='/chromedriver.exe')
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
