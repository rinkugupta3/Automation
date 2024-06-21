from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# Install EdgeDriver and initialize the WebDriver with the service
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# Open the Google homepage
driver.get("https://google.com")

# Wait for the page to load
time.sleep(2)

# Find the search input element by its name attribute
search_box = driver.find_element(By.NAME, "q")

# Enter the search term
search_box.send_keys("Cnn News")

# Submit the search form
search_box.submit()

# Wait for the search results to load
time.sleep(5)

# Find the link to cnn.com
cnn_link = driver.find_elements(By.CLASS_NAME, 'LC20lb')

# Ensure that the list is not empty
if cnn_link:
    # Click the first link in the search results
    cnn_link[0].click()
else:
    print("No links found")

# Wait for a few seconds to ensure the page loads
time.sleep(10)

# Close the browser
driver.close()
driver.quit()

#print message after test completed
print("Performed Google search with Selenium WebDriver")