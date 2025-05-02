# UI Testing with XPath and CSS Selectors using Selenium

This project demonstrates automated UI testing for a simple login and registration page using **Selenium WebDriver** in Python. It includes test scripts using both **XPath** (absolute and relative) and **CSS selectors**, and captures screenshots as visual proof of test execution.

---

## 📁 Files Included

| File Name               | Description                                                       |
|-------------------------|-------------------------------------------------------------------|
| `user.html`             | HTML page with login and registration forms                       |
| `test_login_css.py`     | Automates login using **CSS selectors**                           |
| `test_login_xpath.py`   | Automates login using **absolute XPath**                          |
| `test_register_css.py`  | Automates registration using **CSS selectors**                    |
| `test_register_xpath.py`| Automates registration using **relative XPath**                   |
| `*.png`                 | Screenshots saved during test execution                           |
| `README.md`             | Documentation with setup, usage, and explanation                  |

---

## 📋 Requirements

- **Python 3.x**
- **Google Chrome** installed
- **ChromeDriver** (must match your Chrome version)
- **Selenium** package:

Install it via terminal or command prompt:
```bash
pip install selenium

🔧 Setup Instructions
Clone or download this folder to your local machine.

Place all files in the same directory.

Ensure user.html path is correctly referenced in each script. Example:
driver.get("file:///C:/Users/Talha%20Qureshi/Desktop/SE%20assignment%206/user.html")
Make sure spaces in the path are replaced with %20.

4. Launch the script you want using:
         python test_login_css.py
or use Run in VS Code.

▶️ How to Run the Scripts
This project is divided into two main test areas:

🟢 Login Form (Scripts for Testing Login Only)
Use these if you want to test the login form functionality:

test_login_css.py → uses CSS selectors

test_login_xpath.py → uses absolute XPath

These scripts will:

Locate the login input fields

Fill in the login credentials (TalhaQureshi127, talha123456)

Click the login button

Show “Login successful!” message

Save a screenshot (e.g., login_css_success.png)

🟢 Registration Form (Scripts for Testing Registration Only)
Use these if you want to test the registration form functionality:

test_register_css.py → uses CSS selectors

test_register_xpath.py → uses relative XPath

These scripts will:

Fill in name, email, password, and confirm password

Click the register button

Show “Registration successful!” message

Save a screenshot (e.g., register_xpath_success.png)

💡 Features Demonstrated
XPath & CSS selector usage in Selenium

Difference between absolute and relative XPath

Clean form UI using HTML & CSS

Success message display simulation

Screenshot capture via Selenium

✅ Output Summary
✅ Browser opens

✅ Form fields are auto-filled

✅ Success message appears

✅ Screenshot is saved in the project folder

✅ User presses Enter to close browser window

🧪 Screenshot Files
These are auto-generated after each test:

Script File	Screenshot Name
test_login_css.py	        login_css_success.png
test_login_xpath.py	      login_xpath_success.png
test_register_css.py	    register_css_success.png
test_register_xpath.py	  register_xpath_success.png


