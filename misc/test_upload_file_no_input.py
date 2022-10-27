import os
from playwright.sync_api import Page, expect


def test_file_upload(page: Page) -> None:
    page.goto("https://online2pdf.com/")
    current_working_dir = os.getcwd()
    file_path = os.path.join(current_working_dir, 'testdata\\MyTestUpload1.txt')

    with page.expect_file_chooser() as fc_info:
        page.locator("text=Select files").click()
    file_chooser = fc_info.value
    file_chooser.set_files(file_path)
    # page.locator("text=Select files").set_input_files(file_path)

    page.wait_for_timeout(3000)
