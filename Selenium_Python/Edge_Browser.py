from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# Install EdgeDriver and initialize the WebDriver with the service
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# Open the Google homepage
driver.get("https://google.com")

# Wait for 2 seconds to view the opened browser
time.sleep(2)

# Close the browser
driver.close()
driver.quit()

print("Edge web browser opened with google.com")