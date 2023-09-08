from behave import then

@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_page_opened(context):
    context.app.privacy_notice_page.verify_opened()

@then('User can close new window')
def close_window(context):
    context.app.privacy_notice_page.close_page()

@then('Return to original window')
def return_to_original_window(context):
    context.app.privacy_notice_page.switch_to_window(context.orignal_window)


