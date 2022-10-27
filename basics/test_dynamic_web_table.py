
from playwright.sync_api import Page, expect


def test_angular_web_table(page: Page) -> None:
    page.goto("https://primefaces.org/primeng/table")
    # Click on a checkbox by customer name
    rows = page.locator("table.p-datatable-table tr")

    checkbox = rows.locator(":scope", has_text="Donette Foller").locator("div.p-checkbox-box")

    checkbox.check()

    expect(checkbox).to_be_checked()

    # Print all data from the table

    index = 0

    while index < rows.count():
        print(rows.nth(index).inner_text())
        index += 1

    # Get the balance of a customer
    balance = rows.locator(":scope", has_text="Mitsue Tollner").locator("//span[text()='Balance']//parent::td")

    print(balance.inner_text())
    print(balance.text_content())

    expect(balance).to_contain_text('$58,706.00')








