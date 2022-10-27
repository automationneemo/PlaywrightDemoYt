from playwright.sync_api import Page, expect


def test_check_checkbox(page: Page) -> None:
    page.goto("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
    page.wait_for_timeout(3000)
    page.locator(get_days_checkbox("Monday")).check(force=True)
    # page.locator('label', has_text='Monday').check()
    page.wait_for_timeout(3000)
    # assert page.locator(get_days_checkbox("Monday")).is_checked()
    expect(page.locator(get_days_checkbox("Monday"))).to_be_checked()
    page.locator(get_days_checkbox("Monday")).uncheck(force=True)
    page.wait_for_timeout(3000)
    # assert not page.locator(get_days_checkbox("Monday")).is_checked()
    expect(page.locator(get_days_checkbox("Monday"))).not_to_be_checked(timeout=15000)


def test_internet_check_uncheck(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/checkboxes")

    checkboxes = page.locator("#checkboxes input")

    expect(checkboxes.nth(0)).not_to_be_checked()
    checkboxes.nth(0).check()

    expect(checkboxes.nth(0)).to_be_checked()


def get_days_checkbox(day):
    return f"//label[text()='{day}']/preceding-sibling::input"
