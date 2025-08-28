import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser_setup(playwright):
    browser = playwright.chromium.launch(headless=False)
    yield
    browser.close()

