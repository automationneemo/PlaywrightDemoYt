
from playwright.sync_api import Page


def test_pgae_source(page: Page) -> None:
    page.goto("https://www.google.com/")
    print(page.content())


