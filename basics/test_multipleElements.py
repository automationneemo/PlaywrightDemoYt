from playwright.sync_api import Page, expect


def test_multi_elements(page: Page) -> None:
    # Go to https://selenium08.blogspot.com/2019/11/dropdown.html
    page.goto("https://selenium08.blogspot.com/2019/11/dropdown.html")
    country_options = page.locator("select[name='country'] option")
    # print(type(country_options))
    # print(country_options.all_inner_texts())
    # print(country_options.count())
    #
    # print(country_options.first.inner_text())
    # print(country_options.last.inner_text())

    index = 0;
    while index > country_options.count():
        print(country_options.nth(index).inner_text())
        index = index + 1








