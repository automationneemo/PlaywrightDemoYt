from playwright.sync_api import Page, expect


def test_handle_graph(page: Page) -> None:
    page.goto("https://frappe.io/charts")

    events_list = page.locator("//*[@id='line-composite-1']//*[name()='svg']//*[local-name()='circle']//following-sibling::*[local-name()='text']")
    print(events_list.count())
    index = 0
    while index < events_list.count():
        print(events_list.nth(index).text_content())
        index += 1