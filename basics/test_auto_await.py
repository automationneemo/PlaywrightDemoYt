from playwright.sync_api import Page


def test_ajax_call_autowait(page: Page) -> None:
    page.goto("http://uitestingplayground.com/ajax")

    button = page.locator('text=Button Triggering AJAX Request')
    button.click()

    final_msg = page.locator("p.bg-success").inner_text()
    print(final_msg)


def test_wait_for_hidden_element_visible(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    page.locator("button", has_text='Start').click()

    print(page.locator("#finish h4").inner_text())


def test_wait_for_visible(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")
    page.locator("button", has_text='Start').click()
    result = page.locator("#finish h4")
    result.wait_for(timeout=60000)
    print(page.locator("#finish h4").inner_text())
