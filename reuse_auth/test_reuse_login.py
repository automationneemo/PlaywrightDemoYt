from playwright.sync_api import Playwright, sync_playwright, expect


def test_01_Login_success(set_up_tear_down) -> None:
    page = set_up_tear_down
    logout = page.locator("//i[text()=' Logout']/parent::a")
    assert logout.is_visible()


def test_02_Login_logout(set_up_tear_down) -> None:
    page = set_up_tear_down
    page.locator("//i[text()=' Logout']/parent::a").click()

    success_message = page.locator('#flash').inner_text()
    print(success_message)

    assert 'You logged out of the secure area!' in success_message


