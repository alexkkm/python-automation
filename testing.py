from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Step 1: Launch browser (Chrome in this case)
driver = webdriver.Chrome()

# Step 2: Open a website
driver.get("https://example.com")

# Step 3: Print page content (Hello World style)
print("Page title is:", driver.title)
print("Page content snippet:", driver.page_source[:200])  # first 200 chars

# Step 4: Find and click a button (replace with actual button selector)
try:
    button = driver.find_element(By.ID, "myButton")  # Example: button with id="myButton"
    button.click()
    print("Button clicked successfully!")
except Exception as e:
    print("Could not find or click the button:", e)

# Step 5: Wait a bit to see the result
time.sleep(5)

# Step 6: Close browser
driver.quit()
