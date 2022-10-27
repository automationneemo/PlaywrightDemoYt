from playwright.sync_api import Page, expect


def select_dropdown(page, value):
    dropdown_option = page.frame("previewFrame").locator(f"//ul[@class='select-menu box']/li[contains(., '{value}')]")
    dropdown_option.click()


def select_dropdown_while_loop(page, value):
    dropdown_option = page.frame("previewFrame").locator("//ul[@class='select-menu box']/li")
    index = 0
    while index < dropdown_option.count():
        if dropdown_option.nth(index).inner_text() == value:
            dropdown_option.nth(index).click()
            break
        index += 1


def test_non_select_dropdown(page: Page) -> None:
    page.goto("https://stackblitz.com/edit/angular-dfy6hf?file=src%2Fapp%2Fapp.component.ts", timeout=60000)
    page.wait_for_timeout(15000)
    dropdown = page.frame("previewFrame").locator("#undefined")
    # dropdown.wait_for(timeout=30000)
    dropdown.click()
    select_dropdown_while_loop(page, "Label 2")
    expect(dropdown).to_have_value('Label 2')


