import pytest
from playwright.sync_api import Page, expect

test_data = {
    "locked_user": "locked_out_user",
    "locked_user_pass": "secret_sauce",
    "invalid_user": "Invalid user",
    "invalid_user_pass": "invalid password",
    "valid_user": "standard_user",
    "valid_user_pass": "secret_sauce",
}


@pytest.mark.sanity
def test_locked_user(page: Page, navigate):
    """
    Testing error when user is locked
    """
    page.get_by_test_id("username").fill(test_data["locked_user"])
    page.get_by_placeholder("Password").fill(test_data["locked_user_pass"])
    page.get_by_role("button").click()
    expect(page.get_by_test_id("error")).to_contain_text(
        "Epic sadface: Sorry, this user has been locked out."
    )


@pytest.mark.sanity
def test_invalid_user(page: Page, navigate):
    """
    Testing invalid user
    """
    page.get_by_test_id("username").fill(test_data["invalid_user"])
    page.get_by_placeholder("Password").fill(test_data["invalid_user_pass"])
    page.get_by_role("button").click()
    expect(page.get_by_test_id("error")).to_contain_text(
        "Epic sadface: Username and password do not match any user in this service"
    )


@pytest.mark.sanity
def test_valid_user(page: Page, navigate):
    """
    Testing valid login
    """
    page.get_by_test_id("username").fill(test_data["valid_user"])
    page.get_by_placeholder("Password").fill(test_data["valid_user_pass"])
    page.get_by_role("button").click()
    expect(page.locator(".app_logo")).to_have_text("Swag Labs")
