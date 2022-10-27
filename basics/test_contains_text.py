from playwright.sync_api import Page, expect


def test_contains_text(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    user_name = page.locator("id=user-name")
    user_name.fill("standard_user")
    pass_word = page.locator("id=password")
    pass_word.fill("saashfg")
    login_btn = page.locator("id=login-button")
    login_btn.click()

    error_msg = page.locator("data-test=error")

    expect(error_msg).to_contain_text("Username and password do not match")
    expect(error_msg).not_to_have_text("Test")

    expect(user_name).to_have_attribute('placeholder', 'Username')
    expect(pass_word).to_have_attribute('placeholder', 'Password')

