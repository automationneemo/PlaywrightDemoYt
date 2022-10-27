from playwright.sync_api import Page, expect


def test_right_click(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/context_menu")

    context_area = page.locator("#hot-spot")

    context_area.click(button="right")