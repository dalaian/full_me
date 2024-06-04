import pytest
from playwright.sync_api import Page


@pytest.mark.sanity
def test_sorting_low_high(login):
    """
    Testing low high sort
    """
    page = login
    page.get_by_test_id("product-sort-container").select_option("lohi")
    previous_price = 0
    for price in page.get_by_test_id("inventory-item-price").all_inner_texts():
        current_price = float(price.replace("$", ""))
        assert (current_price >= previous_price) is True
        previous_price = current_price
