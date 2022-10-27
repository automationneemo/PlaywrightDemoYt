from playwright.sync_api import Page, expect


def test_wait_for_load_icon_to_finish(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/dynamic_controls")
    # Remove the checkbox
    loading_icon = page.locator("//form[@id='checkbox-example']/div[1]")
    add_remove_btn = page.locator("//form[@id='checkbox-example']/button")
    add_remove_btn.click()
    expect(loading_icon).not_to_be_visible(timeout=15000)
    checkbox = page.locator("//form[@id='checkbox-example']//input[@id='checkbox']")
    message_txt = page.locator("p#message")
    expect(message_txt).to_have_text("It's gone!", timeout=1000)
