from playwright.sync_api import Page, expect


def test_clear_input(page: Page) -> None:
    page.goto("https://www.google.com/")

    search_input = page.get_by_title("Search")
    # search_input.fill("Playwright")
    search_input.fill("Playwright")

    search_input.clear()

    page.wait_for_timeout(2000)

    expect(search_input).to_be_empty()