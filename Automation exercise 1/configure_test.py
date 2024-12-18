import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
import os



@pytest.fixture
def driver():
    #load_dotenv()
    website = "https://opaponline.opap.gr/en/"
    path = "C:\\Users\\STEVE\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
    #website=os.getenv("website")
    #path=os.getenv("path")
    print(website,path)
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service)
    driver.get(website)
    yield driver
    driver.quit()

