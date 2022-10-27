import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


# @pytest.mark.xfail(reason="BUG 1767")
@pytest.mark.regression
def test_01_login_with_valid_credentials(set_up_tear_down) -> None:
    page = set_up_tear_down

    products_header = page.locator("//span[text()='Products']")
    assert products_header.is_visible(), "User is unable to login"
    # ---------------------


# @pytest.mark.skip(reason="Not implemented")
@pytest.mark.sanity
@pytest.mark.regression
def test_02_logout(set_up_tear_down) -> None:
    page = set_up_tear_down
    burger_menu = page.locator("#react-burger-menu-btn")
    burger_menu.click()
    # page.screenshot(path="Screenshots/screenshot.png")
    logout_btn = page.locator("//div[@class='bm-menu']//a[text()='Logout']")

    logout_btn.click()

    login_btn = page.locator("#login-button")

    assert login_btn.is_visible(), "Logout is not successful"


@pytest.mark.regression
def test_03_login_with_invalid_credentials(set_up_tear_down_no_login) -> None:
    page = set_up_tear_down_no_login
    page.locator("#user-name").fill("standard_user", timeout=5000)
    page.locator("#password").fill("wrong_sauce")
    page.locator("#login-button").click()
    error_text = page.locator("//div[@class='error-message-container error']/h3")
    error_text.wait_for()
    expected_err_text = "xUsername and password do not match any user in this service"
    assert expected_err_text in error_text.inner_text(), "Correct error message is not displayed"
    # ---------------------


@pytest.mark.regression
@pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce"),
                                                pytest.param("locked_out_user", "secret_sauce", marks=pytest.mark.xfail),
                                                pytest.param("DummyUser", "DummyPassword", marks=pytest.mark.xfail)])
def test_04_login_with_different_credentials(set_up_tear_down_no_login, username, password) -> None:
    page = set_up_tear_down_no_login
    page.locator("#user-name").fill(username, timeout=5000)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()
    products_header = page.locator("//span[text()='Products']")
    assert products_header.is_visible(), "User is unable to login"
