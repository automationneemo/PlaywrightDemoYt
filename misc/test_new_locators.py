from playwright.sync_api import Page, expect


def test_new_locator_api(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    username = page.get_by_placeholder("Username")
    password = page.get_by_placeholder("Password")
    password.get_by_role()
    login_btn = page.get_by_text("Login")

    username.fill("standard_user")
    password.fill("secret_sauce")
    login_btn.click()

def test_new_locator_api2(page: Page) -> None:
    page.goto("https://www.google.com/")
    search_box = page.get_by_role("combobox", name="Search")
    search_box.fill("Playwright")
    page.get_by_role("button", name="Google Search").nth(0).click()


def test_new_locator_api3(page: Page) -> None:
    page.goto("https://demo.opencart.com/index.php?route=product/product&language=en-gb&product_id=40")

    quantity = page.get_by_label("Qty")

    expect(quantity).to_be_visible()