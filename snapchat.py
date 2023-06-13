import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://web.snapchat.com/")

input("Please login and press Enter to continue...")

# Remove notification pop-up
try:
    driver.find_element(By.XPATH, "//button[contains(text(), 'C’est compris !')]")
    driver.execute_script("document.elementFromPoint(0, 0).click();")
except:
    print("Notification button not found")

# Get all elements with property "role" set to "listitem"
elements = driver.find_elements(By.XPATH, "//div[@role='listitem']")
print("Found", len(elements), " conversations")

# For each conversation 
for element in elements:
    #  Get conversation name
    span = element.find_element(By.XPATH, ".//span[@dir='auto']")
    text = span.text
    
    if text == "My AI":
        element.click()
        print("My AI conversation found")
        break

