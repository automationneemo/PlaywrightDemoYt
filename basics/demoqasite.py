from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False, channel='msedge-beta',slow_mo=3000, executable_path='C:\\Users\\Soumya\\Downloads\\MicrosoftEdgeSetupBeta.exe')
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://demoqa.com/sortable
    page.goto("https://demoqa.com/sortable")

    page.wait_for_timeout(10000)

    # # Click #demo-tabpane-list >> text=One
    # page.locator("//div[@id='demo-tabpane-list']//div[text()='One']").click(button="right")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
