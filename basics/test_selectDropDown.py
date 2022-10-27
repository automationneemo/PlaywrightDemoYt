from builtins import int

from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    # Go to https://selenium08.blogspot.com/2019/11/dropdown.html
    page.goto("https://selenium08.blogspot.com/2019/11/dropdown.html")
    page.locator("//select[@name='country']").select_option(label="India")
    # expect(page.locator("//select[@name='country']")).to_have_value('IN')
    page.wait_for_timeout(2000)
    # page.locator("//select[@name='country']").select_option(value="KH")
    # page.locator("//select[@name='country']").select_option(index=5)
    page.locator("//select[@name='country']").select_option()
    page.wait_for_timeout(4000)


def test_example2(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/dropdown")
    page.wait_for_timeout(2000)
    dropdown = page.locator("select[id='dropdown']")
    dropdown.select_option(label='Option 2')
    page.wait_for_timeout(2000)
    selected_value = page.locator("select[id='dropdown'] > option[selected='selected']")

    assert selected_value.inner_text() == 'Option 2'
