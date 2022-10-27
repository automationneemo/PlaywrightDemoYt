from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(http_credentials={'username':'admin', 'password':'admin'})
    # context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/digest_auth")

    result = page.locator("#content p")

    expect(result).to_have_text('Congratulations! You must have the proper credentials.')

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
