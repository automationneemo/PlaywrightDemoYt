import time

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


@pytest.fixture(scope='session')
def create_browser_context(browser) -> None:
    # browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator('#password').fill("SuperSecretPassword!")
    page.locator("//button[@type='submit']").click()
    time.sleep(2)
    context.storage_state(path="state.json")
    yield context
    time.sleep(2)


@pytest.fixture()
def set_up_tear_down(create_browser_context, browser) -> None:
    # Go to https://the-internet.herokuapp.com/login
    context = browser.new_context(storage_state="state.json")
    # context = browser.new_context()
    # context = create_browser_context
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/secure")
    yield page
    time.sleep(2)
    context.close()
