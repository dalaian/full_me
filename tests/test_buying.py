import re
from playwright.sync_api import expect


def test_buying(login):
    """
    This test uses the fixture login to login, and then, buy one item 
    and verifies the Complete Order title is displayed.
    """
    page = login
    page.get_by_test_id("add-to-cart-sauce-labs-backpack").click()
    page.get_by_test_id("shopping-cart-link").click()
    page.get_by_test_id("checkout").click()
    page.get_by_test_id("firstName").click()
    page.get_by_test_id("firstName").fill("Testname")
    page.get_by_test_id("lastName").fill("Testlastname")
    page.get_by_test_id("postalCode").fill("30105")
    page.get_by_test_id("continue").click()
    page.get_by_test_id("finish").click()
    expect(page.get_by_test_id("complete-header")).to_be_visible()
