from selenium.webdriver.common.by import By
from .main_page import Base_Page
import time
from selenium.webdriver.support import expected_conditions as EC

class TzokerPage(Base_Page):

    CREATE_SLIP = (By.XPATH, "/html/body/div[1]/div[2]/section/div[1]/section[1]/div/div/div/div[2]/div[2]/div/div/section/div/div[2]/div/div/div/div/div[2]/div[2]/a[1]/button")
    SELECT_BUTTON_MOBILE = (By.XPATH, "/html/body/div[1]/div[2]/section/div[1]/section[3]/div/div/div[2]/div/div/div/section/div/div[2]/div/div/div/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/button[1]")
    SELECT_BUTTON_DESKTOP = (By.XPATH, "/html/body/div[1]/div[2]/section/div[1]/section[3]/div/div/div[2]/div/div/div/section/div/div[2]/div/div/div/div/div/div[1]/div[2]/div/fieldset/section/div/div/div[1]/div/div/button[1]")
    COST_VALUE = (By.CSS_SELECTOR, ".ptz-select-numbers-modal__number--green[id='ptz-select-numbers-modal__number']")
    ADD_BUTTON = (By.ID, "ptz-select-numbers-modal-confirm-button")

    def create_slip(self):

        try:
            self.click_button(*self.CREATE_SLIP)
            print("Create slip button has been pressed")
            time.sleep(0.5)
            return True
        except Exception as e:
            print(f"Error creating slip: {str(e)}")
            return False

    def click_select(self):

        try:

            self.click_button(*self.SELECT_BUTTON_MOBILE)
        except:

            self.click_button(*self.SELECT_BUTTON_DESKTOP)
        print("Select Numbers has been pressed")
        time.sleep(0.5)

    def select_numbers(self, numbers, joker):

        try:

            for number in numbers:
                selector = f".ptz-select-numbers-modal-main__numbers button[id='ptz-select-numbers-modal-main-number-{number}']"
                self.click_button(By.CSS_SELECTOR, selector)
                print(f"Number {number} has been pressed")
                time.sleep(1)


            joker_selector = f".ptz-select-numbers-modal-tzoker__numbers button[id='ptz-select-numbers-modal-tzoker-number-{joker}']"
            self.click_button(By.CSS_SELECTOR, joker_selector)
            print(f"Joker number {joker} has been pressed")
            time.sleep(2)
            return True
        except Exception as e:
            print(f"Error selecting numbers: {str(e)}")
            return False

    def verify_cost_and_add(self):

        try:
            cost_element = self.driver.find_element(*self.COST_VALUE)
            if cost_element.text == "€1,00":
                print("Cost value is equal to €1,00, please continue")
                time.sleep(0.5)
                self.click_button(*self.ADD_BUTTON)
                return True
            return False
        except Exception as e:
            print(f"Error verifying cost: {str(e)}")
            return False

    def validate_coupon(self):

        try:
            coupon = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".opap-selected-numbers__wrapper-content.otw-cursor-pointer")))
            if coupon:
                print("The coupon was found")
                time.sleep(3)
                return True
            print("The coupon was not found")
            return False
        except Exception as e:
            print(f"Error validating coupon: {str(e)}")
            return False





