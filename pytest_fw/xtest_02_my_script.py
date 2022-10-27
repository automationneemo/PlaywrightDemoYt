import pytest
from playwright.sync_api import Page, expect

@pytest.mark.sanity
def test_example(page: Page) -> None:

    # Go to https://www.saucedemo.com/
    page.goto("https://www.saucedemo.com/")

    # Click [data-test="username"]
    page.locator("[data-test=\"username\"]").click()

    # Fill [data-test="username"]
    page.locator("[data-test=\"username\"]").fill("standard_user")

    # Press Tab
    page.locator("[data-test=\"username\"]").press("Tab")

    # Fill [data-test="password"]
    page.locator("[data-test=\"password\"]").fill("secret_sauce")

    # Click [data-test="login-button"]
    page.locator("[data-test=\"login-button\"]").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    # Click text=Open Menu
    page.locator("text=Open Menu").click()

    # Click text=Logout
    page.locator("text=Logout").click()
    expect(page).to_have_url("https://www.saucedemo.com/")

    print("Test completed")
