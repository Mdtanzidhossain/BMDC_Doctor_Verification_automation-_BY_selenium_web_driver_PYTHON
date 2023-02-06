from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

# Open the browser
driver = webdriver.Chrome (executable_path="C:\Webdrivers\chromedriver.exe")

# Navigate to the BMDC website
driver.get("https://verify.bmdc.org.bd/")

# Find the search bar
search_bar = driver.find_element(By.ID,"reg_ful_no")

# Enter the doctor's registration number
search_bar.send_keys("40562")
time.sleep(10)
# Click the search button
search_bar.send_keys(Keys.RETURN)

# Wait for the results to load
# Add wait logic here using WebDriverWait or Implicit Wait

# Verify if the doctor's registration information is displayed
# Add verification logic here

# Close the browser
time.sleep(20)
driver.quit()
