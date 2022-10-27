import time

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


@pytest.fixture(scope='session')
def create_browser_context(playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator('#password').fill("SuperSecretPassword!")
    page.locator("//button[@type='submit']").click()
    yield context
    time.sleep(5)


@pytest.fixture()
def set_up_tear_down(create_browser_context) -> None:
    # Go to https://the-internet.herokuapp.com/login
    context = create_browser_context
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/secure")
    yield page
    time.sleep(5)
