from playwright.sync_api import Page, expect
import time


def clear_input_text(page, loc):
    page.locator(loc).press("Control+KeyA")
    page.locator(loc).press("Backspace")


def test_example2(page: Page) -> None:

    # Go to https://the-internet.herokuapp.com/login
    page.goto("https://the-internet.herokuapp.com/login")
    user_name = page.locator("#username")
    user_name.fill("username1")
    # Clear input field
    # page.locator("#username").fill("")
    clear_input_text(page, '#username')
    user_name.fill("tomsmith")
    expect(user_name).to_have_value("tomsmith", timeout=2000)
    page.wait_for_timeout(3000)

