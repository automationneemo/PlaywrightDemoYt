import os
from playwright.sync_api import Page, expect


def test_file_download(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/download")
    with page.expect_download() as download_i:
        page.locator("//a[text()='selenium.txt']").click()
    dl = download_i.value

    print(dl.path())

    page.wait_for_timeout(5000)

    working_dir_path = os.getcwd()

    final_path = os.path.join(working_dir_path, "testdata/myFile.txt")

    dl.save_as(final_path)

