from playwright.sync_api import Page, expect


def test_double_click(page: Page) -> None:
    page.goto("https://api.jquery.com/dblclick/")
    color_box = page.frame_locator("//iframe").locator("//span[text()='Double click the block']/parent::body/div")
    color_box.dblclick()
    expect(color_box).to_have_class('dbl')
