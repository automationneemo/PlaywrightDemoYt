import time

from playwright.sync_api import Page, expect


def test_refresh_amazon(page: Page) -> None:
    page.goto("https://www.amazon.in/")
    time.sleep(5)
    page.reload(timeout=0)
    time.sleep(5)
    # expect(page).to_have_url('https://www.amazon.in/', timeout=10000)
    expect(page).not_to_have_url('https://www.amazon.com/', timeout=10000)


