from playwright.sync_api import Page, expect


def test_tool_tip(page: Page) -> None:
    page.goto("https://jqueryui.com/tooltip/")

    age_input = page.frame_locator("iframe.demo-frame").locator("#age")
    age_input.hover()
    tool_tip_msg = page.frame_locator("iframe.demo-frame").locator("div.ui-tooltip-content")
    expected_txt = "We ask for your age only for statistical purposes."
    expect(tool_tip_msg).to_have_text(expected_txt)