import time

from playwright.sync_api import Page


def test_sweet_alert(page: Page) -> None:
    page.goto("https://sweetalert2.github.io/")
    show_success_msg = page.locator("//button[normalize-space(text())='Show success message']")
    show_success_msg.click()

    alert_msg = page.locator("#swal2-title")
    alert_msg_txt = alert_msg.inner_text()
    print(alert_msg_txt)
    assert alert_msg_txt == 'Good job!'
    page.locator("button", has_text='OK').click()

    assert not alert_msg.is_visible(), "The sweet alert pop up does not get closed"


