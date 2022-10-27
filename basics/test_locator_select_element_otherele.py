from playwright.sync_api import Page, expect


def test_locator_example(page: Page) -> None:
    page.goto("https://git-scm.com/docs/git-push")
    # download_link = page.locator("a", has_text="Download")
    # download_link.click()
    # page.wait_for_timeout(3000)

    four_elements = page.locator("ul.expanded", has=page.locator("a", has_text="Reference"))
    texts = four_elements.all_inner_texts()
    print(texts)
    page.wait_for_timeout(3000)

    page.goto("https://selenium08.blogspot.com/2019/11/dropdown.html")
    page.wait_for_timeout(3000)
    print(page.locator("select:has(option[value='AF'])").text_content())
    page.wait_for_timeout(3000)




