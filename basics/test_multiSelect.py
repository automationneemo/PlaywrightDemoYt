from builtins import int
import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    # Go to https://selenium08.blogspot.com/2019/11/dropdown.html
    page.goto("https://selenium08.blogspot.com/2019/11/dropdown.html")
    # page.locator("select[name='Month']").select_option(['Sept', 'May', 'July'])
    # page.locator("select[name='Month']").select_option(value='Feb', index=6, label='January')
    page.locator("select[name='Month']").select_option(index=[2, 4, 6])
    page.wait_for_timeout(2000)
    page.locator("select[name='Month']").select_option()

    page.wait_for_timeout(4000)


def test_example2(page: Page) -> None:
    page.goto("https://selenium08.blogspot.com/2019/11/dropdown.html")
    multi_sel_dropdown = page.locator("select[name='Month']")
    multi_sel_dropdown.select_option(['Sept', 'May', 'July'])
    page.wait_for_timeout(2000)
    # Assertion
    # expect(multi_sel_dropdown).to_have_values(['May', 'July', 'Sept'])
    expect(multi_sel_dropdown).to_have_values([re.compile(r"M"), re.compile(r"J"), re.compile(r"S")])





