from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///C:/Users/Talha%20Qureshi/Desktop/SE%20assignment%206/user.html")
time.sleep(2)

# Fill registration form using CSS selectors
name = driver.find_element(By.CSS_SELECTOR, "#reg-name")
email = driver.find_element(By.CSS_SELECTOR, "#reg-email")
password = driver.find_element(By.CSS_SELECTOR, "#reg-password")
confirm = driver.find_element(By.CSS_SELECTOR, "#reg-confirm")
register_btn = driver.find_element(By.CSS_SELECTOR, "#register-btn")

name.send_keys("Talha Qureshi")
email.send_keys("talha@example.com")
password.send_keys("talha123456")
confirm.send_keys("talha123456")
register_btn.click()

# Save screenshot
driver.save_screenshot("register_css_success.png")

input("Register (CSS) test complete. Press Enter to exit...")
driver.quit()
