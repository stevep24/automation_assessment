from selenium.webdriver.common.by import By
from .main_page import Base_Page


class Popup_Page(Base_Page):   # Κληρονομεί από BasePage

    pop_up_message_closed = (By.CLASS_NAME, "webpush-swal2-close")
    cookies_message_reject = (By.ID, "onetrust-reject-all-handler")

    def handle_popups(self):
        try:
            self.click_button(*self.pop_up_message_closed)
            self.click_button(*self.cookies_message_reject)
            return True
        except Exception as e:
            print(f"Error: {str(e)}")
            return False