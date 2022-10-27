from playwright.sync_api import Page


def get_loc_city(city):
    '''
    :param city: pass city name or city code
    :return: it returns xpath of the city
    '''
    return f"//div[text()='{city}']"


def test_dynamic_dropdown(page: Page) -> None:
    page.goto("https://www.spicejet.com/")
    from_input= page.locator("//div[@data-testid='to-testID-origin']//input")
    from_input.click()
    from_input.fill("ko")
    page.locator(get_loc_city("Kolkata")).click()

