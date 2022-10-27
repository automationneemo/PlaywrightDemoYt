from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()
    context2 = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://the-internet.herokuapp.com/windows
    page.goto("https://the-internet.herokuapp.com/windows", timeout=60000)

    page2 = context2.new_page()
    page2.goto("https://playwright.dev/python/docs/intro", timeout=60000)
    page3 = context2.new_page()
    page3.goto("https://google.com", timeout=60000)
    page.wait_for_timeout(3000)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
