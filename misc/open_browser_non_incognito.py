import os
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    app_data_path = os.getenv("LOCALAPPDATA")
    user_data_path = os.path.join(app_data_path, 'Chromium\\User Data\\Default')
    context = playwright.chromium.launch_persistent_context(user_data_path, channel='chrome', headless=False, args=['--start-maximized'], no_viewport=True)
    page = context.new_page()
    page.goto("https://www.google.com/")
    page.wait_for_timeout(5000)

with sync_playwright() as playwright:
    run(playwright)
