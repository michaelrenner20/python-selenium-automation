from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from selenium.webdriver.chrome.options import Options
from support.logger import logger

# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/bestsellers.feature


def browser_init(context):
# def browser_init(context, scenario_name):  # add scenario_name if you want to use it in Browserstack
    """
    :param context: Behave context
    """
    #driver_path = ChromeDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Chrome(service=service)

    service = Service(executable_path=r'C:/Users/micha/python-selenium-automation/chromedriver.exe')
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()

    ### OTHER BROWSERS ###
    # service = Service(executable_path=r'C:/Users/micha/python-selenium-automation/geckodriver')
    # context.driver = webdriver.Firefox(service=service)
    # context.driver = webdriver.Safari()

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # service = Service(executable_path=r'C:/Users/micha/python-selenium-automation/chromedriver.exe')
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = ''
    # bs_key = ''
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     'os': 'Windows',
    #     'osVersion': '10',
    #     'browserName': 'Firefox',
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)


    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context)
 # Pass scenario.name to init() for browserstack config:
 #    browser_init(context, scenario.name)

def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.error(f'Step failed: {step}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
