import time

from playwright.sync_api import Page, expect


def test_field_editable(page: Page) -> None:
    page.goto("https://jsfiddle.net/L96svw3c")
    editable_field = page.frame("result").locator("#readonly")
    expect(editable_field).to_be_editable()


def test_read_only_field(page: Page) -> None:
    page.goto("https://jsfiddle.net/L96svw3c")
    read_only_field = page.frame("result").locator("#readOnly")
    expect(read_only_field).not_to_be_editable()



