from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///C:/Users/Talha%20Qureshi/Desktop/SE%20assignment%206/user.html")
time.sleep(2)

# Fill registration form using relative XPath
name = driver.find_element(By.XPATH, "//input[@id='reg-name']")
email = driver.find_element(By.XPATH, "//input[@id='reg-email']")
password = driver.find_element(By.XPATH, "//input[@id='reg-password']")
confirm = driver.find_element(By.XPATH, "//input[@id='reg-confirm']")
register_btn = driver.find_element(By.XPATH, "//button[@id='register-btn']")

name.send_keys("Talha Qureshi")
email.send_keys("talha@example.com")
password.send_keys("talha123456")
confirm.send_keys("talha123456")
register_btn.click()

# Save screenshot
driver.save_screenshot("register_xpath_success.png")

input("Register (XPath) test complete. Press Enter to exit...")
driver.quit()
