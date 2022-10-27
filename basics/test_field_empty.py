from playwright.sync_api import Page, expect


def test_field_visible(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/inputs")


def test_field_empty(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/inputs")



