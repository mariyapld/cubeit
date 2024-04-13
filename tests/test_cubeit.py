from playwright.sync_api import Page, expect

SITE_URL = "http://127.0.0.1:8000/2-index.html"
def test_cubeit(page: Page):
    page.goto(SITE_URL)

    inp_filed = page.get_by_placeholder("enter number...")
    inp_filed.fill("4")

    page.get_by_role("button", name="Cube").click()

    result = page.locator("css=p#result")

    expect(result).to_contain_text("64")

def test_no_input(page: Page):
    page.goto(SITE_URL)

    input_filed = page.get_by_placeholder("enter number...")
    input_filed.fill("")

    page.get_by_role("button", name="Cube").click()

    result = page.locator("css=p#result")
    expect(result).to_have_text("Enter something!")











