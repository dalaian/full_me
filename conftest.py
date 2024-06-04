import os
import pytest
from utils import email
from pathlib import Path
from playwright.sync_api import expect, Playwright
import utils.config as config

AUTH_FILE = 'playwright/.auth/user.json'

@pytest.fixture(scope='session')
def create_browser_context(browser, playwright):
    playwright.selectors.set_test_id_attribute("data-test")
    context = browser.new_context()
    page = context.new_page()
    page.goto(config.url)
    page.get_by_test_id("username").fill(config.user_name)
    page.get_by_placeholder("Password").fill(config.user_pass)
    page.get_by_role("button").click()
    page.wait_for_url(config.url_logged)
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
    page.goto(config.url_logged)
    yield page
    context.close()

def pytest_sessionfinish(session, exitstatus):
    """ 
    Executes this method when execution finishes
    """
    if config.CI:
        email.send_email()

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "sanity: test that is part of the sanity testing"
    )
    config.addinivalue_line(
        "markers", "regression: test that is part of the regression testing"
    )


#################### Not used ####################

@pytest.fixture()
def navigate(page):
    page.goto(config.url)
    yield # Test

@pytest.fixture(autouse=True)
def configure_playwright_test_id_attribute(playwright):
    playwright.selectors.set_test_id_attribute("data-test")
