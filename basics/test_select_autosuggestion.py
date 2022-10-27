import time

from playwright.sync_api import Page


def select_subject(page, subject):
    auto_suggestions = page.locator("div.subjects-auto-complete__menu-list div")
    index = 0
    while index < auto_suggestions.count():
        if auto_suggestions.nth(index).inner_text() == subject:
            auto_suggestions.nth(index).click()
        index += 1


def get_subject_autosuggestion(subject):
    return f"//div[contains(@class, 'subjects-auto-complete__menu-list')]//div[text()='{subject}']"


def select_subject2(page, subject):
    subject_autosuggestion = page.locator(get_subject_autosuggestion(subject))
    subject_autosuggestion.click()


def test_autosuggestion(page: Page) -> None:
    page.goto("https://demoqa.com/automation-practice-form")
    subject_input = page.locator("#subjectsInput")
    subject_input.fill("E")
    select_subject2(page, "English")
    subject_input.fill("P")
    select_subject2(page, "Physics")
    subject_input.fill("E")
    select_subject2(page, "Commerce")
