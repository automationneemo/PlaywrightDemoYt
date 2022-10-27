from playwright.sync_api import Page, expect


def test_horizontal_slider(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/horizontal_slider")

    slider = page.locator("div.sliderContainer input")
    slider_point = page.locator("#range")

    range_max = '2.5'

    slider.click()
    while True:
        if slider_point.inner_text() == range_max:
            break
        slider.press('ArrowRight')
        page.wait_for_timeout(1000)
        if slider_point.inner_text() == '5':
            break

    expect(slider_point).to_have_text(range_max)
    page.wait_for_timeout(5000)



