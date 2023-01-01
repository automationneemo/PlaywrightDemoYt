import time

from playwright.sync_api import Page, expect


def test_drag_n_drop(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/drag_and_drop")
    src = page.locator("#column-a")
    dest = page.locator("id=column-b")
    src.drag_to(dest)
    expect(dest).to_have_text("A")
    expect(src).to_have_text("B")


def test_drag_n_drop_2nd_approach(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/drag_and_drop")
    src = page.locator("#column-a")
    dest = page.locator("id=column-b")
    page.drag_and_drop('#column-a', 'id=column-b')
    expect(dest).to_have_text("A")
    expect(src).to_have_text("B")


def test_drag_n_drop_3rd_approach(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/drag_and_drop")
    src = page.locator("#column-a")
    dest = page.locator("id=column-b")
    src.hover()
    page.mouse.down()
    dest.hover()
    page.mouse.up()
    expect(dest).to_have_text("A")
    expect(src).to_have_text("B")
