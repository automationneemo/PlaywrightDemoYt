from playwright.sync_api import Page, expect


def test_horizontal_slider(page: Page) -> None:
    page.goto("https://codepen.io/BoringCode/pen/nYbrep", timeout=30000)

    send_btn = page.frame_locator("#result").locator("//button[text()='Send >>']")
    print(send_btn.inner_text())
    slide_to_send = page.frame_locator("#result").locator("div.slide-submit>label")

    send_btn.click()
    send_btn.drag_to(slide_to_send)
    submit_btn = page.frame_locator("#result").locator("div.slide-submit>button")
    expect(submit_btn).to_have_text("Submitting...")

    page.wait_for_timeout(5000)


