from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///C:/Users/Talha%20Qureshi/Desktop/SE%20assignment%206/user.html")
time.sleep(2)

# Corrected Absolute XPath to match container structure
username = driver.find_element(By.XPATH, "/html/body/div[1]/form/input[@id='login-username']")
password = driver.find_element(By.XPATH, "/html/body/div[1]/form/input[@id='login-password']")
login_btn = driver.find_element(By.XPATH, "/html/body/div[1]/form/button[@id='login-btn']")

username.send_keys("TalhaQureshi127")
password.send_keys("talha123456")
login_btn.click()

# Save screenshot
driver.save_screenshot("login_xpath_success.png")

input("Login (XPath) test complete. Press Enter to exit...")
driver.quit()
# This code uses XPath to locate elements in the login form and simulate a user login. It also saves a screenshot of the successful login.
# The XPath expressions are corrected to match the structure of the HTML document.