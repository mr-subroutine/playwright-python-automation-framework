from playwright.sync_api import Playwright, Browser, BrowserContext, Page, expect
import time

def test_logging_in(page: Page):
    page.goto("https://www.saucedemo.com/")  # Test webpage not created by this project owner
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")

    #WIP ADD EXPECT FOR PROPER LOGIN
    with page.expect_navigation():
        page.get_by_role("button").click()
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")




