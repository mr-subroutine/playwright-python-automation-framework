from playwright.sync_api import Page, expect


def test_login_password_fail(page: Page):
    page.goto("https://www.saucedemo.com/")  # Test webpage not created by this project owner
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce111111") #wrong pw
    page.get_by_role("button", name="Login").click()

    expect(page).not_to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator("[data-test='error']")).to_contain_text("Epic sadface: Username and password do not match any user in this service")


def test_login_username_fail(page: Page):
    page.goto("https://www.saucedemo.com/")  # Test webpage not created by this project owner
    page.get_by_placeholder("Username").fill("standard_user11111") # wrong username
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(page).not_to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator("[data-test='error']")).to_contain_text("Epic sadface: Username and password do not match any user in this service")