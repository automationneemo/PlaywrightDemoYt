from playwright.sync_api import Page, expect


def test_css_property(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")

    login_btn = page.get_by_text("Login")

    expect(login_btn).to_have_css("color", "rgb(255, 255, 255)")
    expect(login_btn).to_have_css("text-align", "center")
    expect(login_btn).to_have_css("font-style", "normal")
    expect(login_btn).to_have_css("font-size", "18px")