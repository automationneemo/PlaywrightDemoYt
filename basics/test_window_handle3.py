from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()
    # Open new page
    page = context.new_page()

    # Go to https://the-internet.herokuapp.com/windows
    page.goto("https://the-internet.herokuapp.com/windows", timeout=60000)

    page.locator("text=Click Here").click()
    all_pages = context.pages
    page2 = all_pages[1]
    new_window_txt = page2.locator(".example h3")
    # print(new_window_txt.inner_text())
    # print(page2.title())
    page.wait_for_timeout(2000)
    page.locator("text=Click Here").click()
    all_pages = context.pages
    third_tab = all_pages[2].locator(".example h3")
    # print(third_tab.inner_text())
    all_pages[1].bring_to_front()
    page.wait_for_timeout(3000)

    for page in all_pages:
        print(page.title())
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
