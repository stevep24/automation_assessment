from pages.tzoker_page import TzokerPage
from pages.popups_page import Popup_Page  # Αν θα χρησιμοποιήσεις και το popup handling
from configure_test import driver



def test_tzoker(driver):
    popup_page = Popup_Page(driver)
    popup_page.handle_popups()
    tzoker_page = TzokerPage(driver)
    tzoker_page.create_slip()
    tzoker_page.click_select()
    tzoker_page.select_numbers([3, 14, 25, 35, 45], 18)
    tzoker_page.verify_cost_and_add()
    assert tzoker_page.validate_coupon()