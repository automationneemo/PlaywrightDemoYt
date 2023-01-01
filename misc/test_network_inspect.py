from playwright.sync_api import Page, expect


def test_track_network_event(page: Page) -> None:

    # with page.expect_request("**/secure") as req:
    #     page.goto("https://the-internet.herokuapp.com/login")
    #     page.locator("#username").fill("tomsmith")
    #     page.locator("#password").fill(("SuperSecretPassword!"))
    #     page.get_by_role("button", name="Login").click()

    # print(req.value.url)
    # print(req.value.method)
    # print(req.value.redirected_from)
    # print(req.value.redirected_to)
    # print(req.value.all_headers())


    with page.expect_response("**/secure") as res:
        page.goto("https://the-internet.herokuapp.com/login")
        page.locator("#username").fill("tomsmith")
        page.locator("#password").fill(("SuperSecretPassword!"))
        page.get_by_role("button", name="Login").click()
    print(res.value.all_headers())
    print(res.value.status_text)
    print(res.value.status)
    print(res.value.body())

