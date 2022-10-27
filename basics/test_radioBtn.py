from playwright.sync_api import Page


def test_radio_button(page: Page) -> None:
    page.goto("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
    page.wait_for_timeout(3000)
    page.locator("//label[text()='Male']/preceding-sibling::input").check(force=True)
    page.wait_for_timeout(3000)
    assert page.locator("//label[text()='Male']/preceding-sibling::input").is_checked()
    page.locator("//label[text()='Female']/preceding-sibling::input").check(force=True)
    page.wait_for_timeout(3000)
    assert not page.locator("//label[text()='Male']/preceding-sibling::input").is_checked()
    page.wait_for_timeout(3000)








