import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
import os


@pytest.fixture
def driver():
    load_dotenv()
    website = os.getenv('website')
    chromedriver_path = os.getenv('chromedriver_path')
    if not website or not chromedriver_path:
        raise ValueError("Environment variables 'website' or 'path' not loaded correctly.")

    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service)
    driver.get(website)
    yield driver
    driver.quit()

