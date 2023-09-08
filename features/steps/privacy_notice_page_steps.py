from behave import then


@then('Switch to the newly opened window')
def switch_to_new_window_step(context):
    context.app.privacy_notice_page.switch_to_new_window()


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_page_opened(context):
    context.app.privacy_notice_page.verify_opened()


@then('User can close new window')
def close_window(context):
    context.app.privacy_notice_page.close_page()
