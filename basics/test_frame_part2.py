import time

from playwright.sync_api import Page


def test_handle_iframe_by_name(page: Page) -> None:
    page.goto("https://www.rediff.com/")
    # iframe_locator = page.frame("moneyiframe")
    # iframe_locator = page.main_frame.child_frames[0]
    mf = page.main_frame
    iframe_locator = get_frame_by_index(mf, 0)
    print(type(iframe_locator))
    nse_index = iframe_locator.locator("span#nseindex")
    print(nse_index.inner_text())
    page.wait_for_timeout(10000)
    for iframe in page.main_frame.child_frames:
        print(iframe.name)
    print(len(page.main_frame.child_frames))


def get_frame_by_index(parent_frame, index):
    return parent_frame.child_frames[index]
