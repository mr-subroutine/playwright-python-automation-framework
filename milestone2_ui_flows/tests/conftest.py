import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="session")
def browser_setup(playwright):
    browser = playwright.chromium.launch(headless=False)
    yield
    browser.close()


@pytest.fixture
def login(page: Page):

    page.goto("https://www.saucedemo.com/") # Test webpage not created by this project owner
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    return page

