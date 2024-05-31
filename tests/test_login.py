from playwright.sync_api import Page, expect

def test_locked_user(page: Page, navigate):
    """
    Testing error when user is locked
    """
    page.get_by_test_id("username").fill("locked_out_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button").click()
    expect(page.get_by_test_id("error")).to_contain_text("Epic sadface: Sorry, this user has been locked out.")

def test_invalid_user(page: Page, navigate):
    """
    Testing invalid user
    """
    page.get_by_test_id("username").fill("Invalid user")
    page.get_by_placeholder("Password").fill("invalid passwrod")
    page.get_by_role("button").click()
    expect(page.get_by_test_id("error")).to_contain_text("Epic sadface: Username and password do not match any user in this service")

def test_valid_user(page: Page, navigate):
    """
    Testing valid login
    """
    page.get_by_test_id("username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button").click()
    expect(page.locator(".app_logo")).to_have_text("Swag Labs")