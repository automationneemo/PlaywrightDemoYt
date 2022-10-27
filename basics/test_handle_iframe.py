import time

from playwright.sync_api import Page


def test_iframe(page: Page) -> None:
    page.goto("https://jqueryui.com/autocomplete/")
    frame_element = page.frame_locator("iframe.demo-frame")
    input_field = frame_element.locator("input.ui-autocomplete-input")
    input_field.fill("e")
    page.wait_for_timeout(3000)


def test_iframe_2(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/iframe")
    input_area = page.frame("mce_0_ifr").locator("body#tinymce")
    input_area.type("AutomationNeemo")
    page.wait_for_timeout(3000)

