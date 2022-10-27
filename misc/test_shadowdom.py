import os
from playwright.sync_api import Page, expect


def test_shadow_dom(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/shadowdom")

    text_ele = page.locator("//span[@slot='my-text']")

    print(text_ele.inner_text())
    expect(text_ele).to_contain_text('different text!')
    page.wait_for_timeout(2000)




