
from playwright.sync_api import Page, expect


def test_button_disabled(page: Page) -> None:
    page.goto("https://us.megabus.com/account-management/login")

    signup_tab = page.locator("//a[@data-gtm-id='account-management-sign-up']")

    signup_tab.click()
    signup_btn = page.locator("//button[@data-gtm-id='account-management-sign-up-submit']")
    expect(signup_btn).to_be_disabled()
    expect(signup_btn).not_to_be_enabled()
    email = page.locator("#email")
    email.fill("anyemail@g.com")
    confirm_email = page.locator("#confirmEmail")
    confirm_email.fill("anyemail@g.com")

    password = page.locator("#choosePassword")
    password.fill("qwert12345")
    confirm_password = page.locator("#confirmPassword")
    confirm_password.fill("qwert12345")

    checkbox_terms_privacy = page.locator("#termsAndPrivacy")
    checkbox_terms_privacy.check(force=True)

    expect(signup_btn).to_be_enabled()
    expect(signup_btn).not_to_be_disabled()




