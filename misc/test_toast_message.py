from playwright.sync_api import Page, expect


def test_toast_message(page: Page) -> None:
    page.goto("https://codeseven.github.io/toastr/demo.html")

    show_toast_btn = page.locator("button#showtoast")
    show_toast_btn.click()
    toaster_msg = page.locator("div.toast-message")
    print(toaster_msg.inner_text())

    expect(toaster_msg).to_contain_text("My name is Inigo Montoya")



