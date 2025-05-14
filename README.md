# 🧪 Automation Assessments

This repository contains automated tests for OPAP's Tzoker platform and API, using **Selenium**, **Pytest**, and **Python**.

## 📁 Project Structure
.
├── pages/
│ ├── main_page.py # Base Page Object Model (POM) class
│ ├── popups_page.py # Handles UI popups and cookies
│ └── tzoker_page.py # Automation flows for creating and validating Tzoker slips
├── test_opap.py # Main UI test script using Selenium
├── configure_test.py # Pytest fixture with Chrome WebDriver setup
├── exercise_2.py # Script calling the OPAP API for draw data
├── test_square.py # Tests based on API data validation
└── .env # Environment variables (not included in repo)


## 🚀 Features

- Automates Tzoker slip creation and number selection
- Verifies cost and coupon appearance
- Handles pop-ups and cookie consents
- Validates OPAP API responses for draw data

## 🛠 Technologies Used

- Python 3.x
- Selenium WebDriver
- Pytest
- Requests
- Python-dotenv

## 🧪 Running the Tests

1. Install dependencies:
  pip install -r requirements.txt

2.Create a .env file in the root directory:
  website=https://www.opap.gr/tzoker
  path=/path/to/chromedriver

3.Run UI test:
  pytest test_opap.py
  
4.Run API test:
  pytest test_square.py

📌 Notes
Make sure you have ChromeDriver installed and its path correctly set in .env.
Adjust delays or selectors if the OPAP website structure changes.
