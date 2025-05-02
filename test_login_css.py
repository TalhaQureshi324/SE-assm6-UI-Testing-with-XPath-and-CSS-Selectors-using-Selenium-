from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///C:/Users/Talha%20Qureshi/Desktop/SE%20assignment%206/user.html")
time.sleep(2)

# Fill login form using CSS selectors
username = driver.find_element(By.CSS_SELECTOR, "#login-username")
password = driver.find_element(By.CSS_SELECTOR, "#login-password")
login_btn = driver.find_element(By.CSS_SELECTOR, "#login-btn")

username.send_keys("TalhaQureshi127")
password.send_keys("talha123456")
login_btn.click()

# Save screenshot
driver.save_screenshot("login_css_success.png")

input("Login (CSS) test complete. Press Enter to exit...")
driver.quit()

# This code uses CSS selectors to locate elements in the login form and simulate a user login.  
