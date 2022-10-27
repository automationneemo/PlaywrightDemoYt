from playwright.sync_api import Page


def test_nested_frame(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/nested_frames")

    mf = page.main_frame
    for child_frame in mf.child_frames:
        print(child_frame.name)

    top_frame = page.main_frame.child_frames[0]
    bottom_frame = page.main_frame.child_frames[1]

    left_top_frame = top_frame.child_frames[0]
    middle_top_frame = top_frame.child_frames[1]
    right_top_frame = top_frame.child_frames[2]

    print(left_top_frame.locator("body").inner_text())
    print(middle_top_frame.locator("body").inner_text())
    print(right_top_frame.locator("body").inner_text())
