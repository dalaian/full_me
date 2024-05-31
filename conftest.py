import os
import pytest
from utils import email
from pathlib import Path
from playwright.sync_api import expect, Playwright

AUTH_FILE = 'playwright/.auth/user.json'

@pytest.fixture(scope='session')
def create_browser_context(browser, playwright):
    playwright.selectors.set_test_id_attribute("data-test")
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com")
    page.get_by_test_id("username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button").click()
    page.wait_for_url("https://www.saucedemo.com/inventory.html")
    expect(page.get_by_test_id("title")).to_be_visible()

    # Creates the auth file if needed
    Path(AUTH_FILE).parent.mkdir(parents=True, exist_ok=True)
    Path(AUTH_FILE).touch()

    context.storage_state(path=AUTH_FILE)
    yield context

@pytest.fixture()
def login(create_browser_context, browser):
    context = browser.new_context(storage_state=AUTH_FILE)
    page = context.new_page()
    page.goto("https://www.saucedemo.com/inventory.html")
    yield page
    context.close()

def pytest_sessionfinish(session, exitstatus):
    """ 
    Executes this method when execution finishes
    """
    if os.environ.get('CI', False):
        email.send_email()


#################### Not used ####################

@pytest.fixture()
def navigate(page):
    page.goto("https://www.saucedemo.com/")
    yield

@pytest.fixture(autouse=True)
def configure_playwright_test_id_attribute(playwright):
    playwright.selectors.set_test_id_attribute("data-test")