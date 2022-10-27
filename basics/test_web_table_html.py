from playwright.sync_api import Page


def get_data_by_company(page, company_name, colum_name):
    rows = page.locator("table#customers tr")
    column_headers = page.locator("table#customers th")
    column_index = None
    index = 1

    while index <= column_headers.count():
        if column_headers.nth(index - 1).inner_text() == colum_name:
            column_index = index

        index += 1

    contact = rows.locator(":scope", has_text=company_name).locator(f"//td[{column_index}]")
    return contact.inner_text()


def get_all_data_for_a_column(page, column_name):
    column_index = None
    column_headers = page.locator("table#customers th")
    index = 1

    while index <= column_headers.count():
        if column_headers.nth(index - 1).inner_text() == column_name:
            column_index = index

        index += 1
    column_data = page.locator(f"//table[@id='customers']//tr/td[{column_index}]")

    return column_data.all_inner_texts()


def test_web_table_html(page: Page) -> None:
    page.goto("https://www.w3schools.com/html/html_tables.asp")

    rows = page.locator("table#customers tr")

    index = 1

    while index < rows.count():
        print(rows.nth(index).inner_text())
        index += 1
    company_name = 'Laughing Bacchus Winecellars'
    column_name = 'Contact'
    contact_value = get_data_by_company(page, company_name, column_name)

    # print(contact_value)
    print("------------------------")

    column_data = get_all_data_for_a_column(page, column_name)
    print(column_data)


