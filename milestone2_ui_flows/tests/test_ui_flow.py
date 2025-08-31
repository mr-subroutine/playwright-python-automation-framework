from playwright.sync_api import Playwright, Browser, BrowserContext, Page, expect
import time

def test_logging_and_one_purchase(page: Page):
    page.goto("https://www.saucedemo.com/")  # Test webpage not created by this project owner
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")

    with page.expect_navigation():
        page.get_by_role("button").click()
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


# Add 1 item to cart, checkout, fill out data, finish, back to home
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    page.locator(".shopping_cart_link").click()
    page.locator("#checkout").click()
    page.get_by_placeholder("First Name").fill("Tester")
    page.get_by_placeholder("Last Name").fill("McTester")
    page.get_by_placeholder("Zip/Postal Code").fill("98106")
    page.locator("#continue").click()
    page.locator("#finish").click()
    page.locator("#back-to-products").click()

def test_add_one_item_from_cart(page: Page):
    page.goto("https://www.saucedemo.com/")  # Test webpage not created by this project owner
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")

    with page.expect_navigation():
        page.get_by_role("button").click()
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    page.locator("#add-to-cart-sauce-labs-backpack").click()
    expect(page.locator("[data-test='shopping-cart-badge']")).to_have_text("1")
    page.locator("#remove-sauce-labs-backpack").click()

def test_remove_one_item_from_cart(page: Page):
    page.goto("https://www.saucedemo.com/")  # Test webpage not created by this project owner
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")

    with page.expect_navigation():
        page.get_by_role("button").click()
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    page.locator("#add-to-cart-sauce-labs-backpack").click()
    page.locator("#remove-sauce-labs-backpack").click()
    expect(page.locator(".shopping_cart_badge")).to_be_hidden()


