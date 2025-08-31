from playwright.sync_api import Playwright, Browser, BrowserContext, Page, expect
import time

def test_item_one_purchase(login: Page):
# Add 1 item to cart, checkout, fill out data, finish, back to home
    login.locator("#add-to-cart-sauce-labs-backpack").click()
    expect(login.locator("[data-test='shopping-cart-badge']")).to_have_text("1")
    login.locator(".shopping_cart_link").click()
    login.locator("#checkout").click()
    login.get_by_placeholder("First Name").fill("Tester")
    login.get_by_placeholder("Last Name").fill("McTester")
    login.get_by_placeholder("Zip/Postal Code").fill("98106")
    login.locator("#continue").click()
    login.locator("#finish").click()
    login.locator("#back-to-products").click()
    expect(login.locator("[data-test='shopping-cart-badge']")).to_be_hidden()


def test_item_add_one_item_to_cart(login: Page):
    login.locator("#add-to-cart-sauce-labs-backpack").click()
    expect(login.locator("[data-test='shopping-cart-badge']")).to_have_text("1")
    login.locator("#remove-sauce-labs-backpack").click()
    expect(login.locator("[data-test='shopping-cart-badge']")).to_be_hidden()


def test_item_remove_from_cart(login: Page):
    login.locator("#add-to-cart-sauce-labs-backpack").click()
    login.locator("#remove-sauce-labs-backpack").click()
    expect(login.locator(".shopping_cart_badge")).to_be_hidden()
    expect(login.locator("[data-test='shopping-cart-badge']")).to_be_hidden()


def test_item_remove_from_cart_on_cart_page(login: Page):
    login.locator("#add-to-cart-sauce-labs-backpack").click()
    login.locator(".shopping_cart_link").click()
    (login.locator("#remove-sauce-labs-backpack").click())
    expect(login.locator("[data-test='shopping-cart-badge']")).to_be_hidden()
    expect(login.locator("#checkout")).to_be_hidden()    # The user should be able to check out with no items.  Webpage design issue, it will fail.
    login.locator("#continue-shopping").click()


