from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

import time

# Install the GeckoDriver and create a service object
service = Service(GeckoDriverManager().install())

# Create Firefox options
options = webdriver.FirefoxOptions()
# Optional: Add options to run headless if needed
# options.add_argument('--headless')

try:
    # Initialize the Firefox WebDriver with the service object and options
    driver = webdriver.Firefox(service=service, options=options)

    # Open the Google homepage
    driver.get("https://google.com")

    # Wait for 2 seconds to view the opened browser
    time.sleep(2)

    # Close the browser
    driver.close()
    driver.quit()

    print("Firefox web browser opened with google.com")
except Exception as e:
    print(f"An error occurred: {e}")