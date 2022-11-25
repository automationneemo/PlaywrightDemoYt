import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope='module', autouse=True)
def before_each_after_each(browser):
    print("beforeEach")
    page = browser.new_page()
    # Go to the starting url before each test.
    page.goto("https://playwright.dev/")
    yield
    print("afterEach")

def test_main_navigation(page):
    # Assertions use the expect API.
    expect(page).to_have_url("https://playwright.dev/")

def test_main_navigation2(page):
    # Assertions use the expect API.
    expect(page).to_have_url("https://api.jquery.com/dblclick/")






# def test_sessonstart():
#     print('TEST')

