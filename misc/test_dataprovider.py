import pytest
from playwright.sync_api import Page, expect


@pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce"),
                                                pytest.param("locked_out_user", "secret_sauce", marks=pytest.mark.xfail),
                                                ("problem_user", "secret_sauce"),
                                                ("performance_glitch_user", "secret_sauce")])
def test_data_provider(page, username, password) -> None:
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill(username)
    page.locator("#password").fill(password)

    page.locator("#login-button").click()

    products_loc = page.locator("//span[text()='Products']")

    expect(products_loc).to_be_visible()
