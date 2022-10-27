import time

from playwright.sync_api import Page


def test_click_for_js_alert(page: Page) -> None:
    '''
        Handle javascript alert pop up
    '''
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    click_js_alrt_btn = page.locator("text=Click for JS Alert")
    click_js_alrt_btn.click()
    result_msg_loc = page.locator("#result")
    assert result_msg_loc.inner_text() == 'You successfully clicked an alert'

def test_click_for_js_confirm(page: Page) -> None:
    '''
        Handle javascript alert pop up with ok and cancel button
    '''
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    click_js_alrt_btn = page.locator("text=Click for JS Confirm")
    page.on("dialog", lambda dialog: dialog.accept())
    click_js_alrt_btn.click()
    result_msg_loc = page.locator("#result")
    assert result_msg_loc.inner_text() == 'You clicked: Ok'

def test_click_for_js_prompt(page: Page) -> None:
    '''
        Handle javascript alert prompt with ok and cancel button
    '''
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    click_js_alrt_btn = page.locator("text=Click for JS Prompt")
    # page.on("dialog", lambda dialog: dialog.accept())
    # page.on("dialog", lambda dialog: print(dialog.message))
    # page.on("dialog", lambda dialog: dialog.accept(promptText='AutomationNeemo'))
    page.on("dialog", lambda dialog: dialog.accept(prompt_text='AutomationNeemo'))
    click_js_alrt_btn.click()
    result_msg_loc = page.locator("#result")
    assert result_msg_loc.inner_text() == 'You entered: AutomationNeemo'
