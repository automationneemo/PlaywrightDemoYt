import pytest_check as check
from playwright.sync_api import Page, expect


def test_tool_tip(page: Page) -> None:
    page.goto("https://jqueryui.com/tooltip/")

    age_input = page.frame_locator("iframe.demo-frame").locator("#age")
    age_input.hover()
    tool_tip_msg = page.frame_locator("iframe.demo-frame").locator("div.ui-tooltip-content")
    expected_txt = "We ask for your age onlyy for statistical purposes."
    check.equal(tool_tip_msg.inner_text(), expected_txt)
    # expect(tool_tip_msg).to_have_text(expected_txt)
    value = age_input.input_value()
    check.equal(value, "")
    # expect(age_input).to_be_empty()

    age_input.fill("25")
    value = age_input.input_value()
    # expect(age_input).not_to_be_empty()
    check.equal(value, "250")
    # expect(age_input).to_have_value("25")