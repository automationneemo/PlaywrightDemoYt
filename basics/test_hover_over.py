from playwright.sync_api import Page, expect


def test_hover_example(page: Page) -> None:
    page.goto("https://www.globalsqa.com/demo-site/")

    header_menu = page.locator("#menu-item-7128", has_text="Free Ebooks")

    print(header_menu.inner_text())
    print(header_menu.count())

    header_menu.hover()

    page.wait_for_timeout(3000)


def get_header_submenu_loc(menu, submenu):
    return f"//div[@class='dark_menu']//a[text()='{menu}']/parent::li//ul[@class='sub-menu']//a[contains(., '{submenu}')]"


# setTimeout(function(){debugger;}, 5000)
def test_select_element_after_hover(page: Page) -> None:
    page.goto("https://www.globalsqa.com/demo-site/")
    free_book = page.locator("#menu-item-7128", has_text="Free Ebooks")
    free_book.hover()

    page.wait_for_timeout(3000)
    all_free_ebooks = page.locator("//li[@id='menu-item-7128']//ul[@class='sub-menu']//a")
    print(all_free_ebooks.all_inner_texts())

    free_deep_learning_book = page.locator(get_header_submenu_loc("Free Ebooks", "Tensorflow"))
    free_deep_learning_book.click()
    page.wait_for_timeout(10000)
    print(page.title())
    # //li[@id='menu-item-7128']//ul[@class='sub-menu']//a[contains(., 'Deep Learning')]
    # //div[@class='dark_menu']//a[text()='Free Ebooks']/parent::li//ul[@class='sub-menu']//a[contains(., 'Deep Learning')]
