from playwright.sync_api import Playwright, sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.guru99.com/')
    page.keyboard.press("T")
    page.get_by_role("textbox", name="search").click()
    page.wait_for_timeout(5000)
    browser.close()