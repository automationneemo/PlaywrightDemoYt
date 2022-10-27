from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.google.com/?gws_rd=ssl
    page.goto("https://www.google.com/")
    print(page.url)

    # click on Gmail link
    page.locator("text=Gmail").click()
    # Get the url
    print(page.url)
    # Navigate back
    page.go_back()
    print(page.url)
    # Navigate forward
    page.go_forward(wait_until="networkidle")
    print(page.url)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
