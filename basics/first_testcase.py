from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000, args=['--start-maximized'])
    context = browser.new_context()

    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    # Open new page
    page = context.new_page()

    # Go to https://www.google.com/
    page.goto("https://www.google.com/")

    # Click [aria-label="Search"]
    page.locator("[aria-label=\"Search\"]").click()

    # Fill [aria-label="Search"]
    page.locator("[aria-label=\"Search\"]").fill("Playwright")

    # Press Enter
    # with page.expect_navigation(url="https://www.google.com/search?q=Playwright&source=hp&ei=xedmYsyXEc_M-Qa8s7e4Aw&iflsig=AHkkrS4AAAAAYmb11aUt3uUSXogIKV8VoRpZyjteDUR7&ved=0ahUKEwiMjqiw66_3AhVPZt4KHbzZDTcQ4dUDCAc&uact=5&oq=Playwright&gs_lcp=Cgdnd3Mtd2l6EAMyCAgAEIAEELEDMggIABCABBCxAzIFCAAQgAQyCwgAEIAEELEDEIMBMgUIABCABDIFCAAQgAQyBQgAEIAEMgsIABCABBCxAxCDATIFCAAQgAQyBQgAEIAEOg4IABCPARDqAhCMAxDlAjoOCC4QjwEQ6gIQjAMQ5QI6EQguEI8BENQCEOoCEIwDEOUCOgUILhCABDoICAAQsQMQgwE6CwguEIAEELEDEIMBOgQIABADOggIABCABBDJAzoFCAAQkgM6CggAELEDEIMBEApQnghY5hxg90ZoAXAAeACAAcYBiAGIDZIBBDAuMTCYAQCgAQGwAQo&sclient=gws-wiz"):
    with page.expect_navigation():
        page.locator("[aria-label=\"Search\"]").press("Enter")
    # expect(page).to_have_url("https://www.google.com/search?q=Playwright&source=hp&ei=xedmYsyXEc_M-Qa8s7e4Aw&iflsig=AHkkrS4AAAAAYmb11aUt3uUSXogIKV8VoRpZyjteDUR7&ved=0ahUKEwiMjqiw66_3AhVPZt4KHbzZDTcQ4dUDCAc&uact=5&oq=Playwright&gs_lcp=Cgdnd3Mtd2l6EAMyCAgAEIAEELEDMggIABCABBCxAzIFCAAQgAQyCwgAEIAEELEDEIMBMgUIABCABDIFCAAQgAQyBQgAEIAEMgsIABCABBCxAxCDATIFCAAQgAQyBQgAEIAEOg4IABCPARDqAhCMAxDlAjoOCC4QjwEQ6gIQjAMQ5QI6EQguEI8BENQCEOoCEIwDEOUCOgUILhCABDoICAAQsQMQgwE6CwguEIAEELEDEIMBOgQIABADOggIABCABBDJAzoFCAAQkgM6CggAELEDEIMBEApQnghY5hxg90ZoAXAAeACAAcYBiAGIDZIBBDAuMTCYAQCgAQGwAQo&sclient=gws-wiz")

    # Click text=Playwright: Fast and reliable end-to-end testing for modern ...
    page.locator("text=Playwright: Fast and reliable end-to-end testing for modern ...").click()
    # expect(page).to_have_url("https://playwright.dev/")

    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path="trace.zip")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
