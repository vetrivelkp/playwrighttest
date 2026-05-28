from playwright.sync_api import Page, expect

BASE_URL = "http://127.0.0.1:8000/"

def test_square_function(page: Page):
    page.goto(BASE_URL)

    input_value = page.locator("input#numberInput")

    input_value.fill("5")

    button = page.get_by_role("button", name="Square", exact=True)

    button.click()

    expect(page.locator("h3#result")).to_have_text("5 to the power of 2 is 25")

def test_square_function_Empty_input(page: Page):
    page.goto(BASE_URL)

    input_value = page.locator("input#numberInput")

    input_value.fill("")

    button = page.get_by_role("button", name="Square", exact=True)

    button.click()

    expect(page.locator("h3#result")).to_have_text("Please enter a number")

