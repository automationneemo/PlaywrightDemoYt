import os
from playwright.sync_api import Page, expect


def test_file_upload(page: Page) -> None:
    page.goto("https://davidwalsh.name/demo/multiple-file-upload.php")

    # page.locator('id=filesToUpload').set_input_files()
    current_working_dir = os.getcwd()
    file_path = os.path.join(current_working_dir, 'testdata\\MyTestUpload1.txt')
    file_path2 = os.path.join(current_working_dir, 'testdata\\MyTestUpload2.txt')
    # page.set_input_files('id=filesToUpload', file_path)
    page.locator('id=filesToUpload').set_input_files([file_path, file_path2])
    page.wait_for_timeout(4000)