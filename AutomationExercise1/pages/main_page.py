from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base_Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_button(self, by, value):
        button = self.wait.until(EC.element_to_be_clickable((by, value)))
        button.click()




