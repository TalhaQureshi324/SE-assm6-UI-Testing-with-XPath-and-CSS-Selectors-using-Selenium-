# UI Testing with XPath and CSS Selectors using Selenium

This project demonstrates automated UI testing for a simple login and registration page using **Selenium WebDriver** in Python. It includes test scripts using both **XPath** (absolute and relative) and **CSS selectors**, and captures screenshots as visual proof of test execution.

---

## 📁 Files Included

| File Name                | Description                                                       |
|--------------------------|-------------------------------------------------------------------|
| `user.html`              | HTML page with login and registration forms                       |
| `test_login_css.py`      | Automates login using **CSS selectors**                           |
| `test_login_xpath.py`    | Automates login using **absolute XPath**                          |
| `test_register_css.py`   | Automates registration using **CSS selectors**                    |
| `test_register_xpath.py` | Automates registration using **relative XPath**                   |
| `*.png`                  | Screenshots saved during test execution                           |
| `README.md`              | Documentation with setup, usage, and explanation                  |

---

## 📋 Requirements

- **Python 3.x**
- **Google Chrome** installed
- **ChromeDriver** (must match your Chrome version)
- **Selenium** package

Install Selenium via terminal or command prompt:

```bash
pip install selenium
```

---

## 🔧 Setup Instructions

1. Clone or download this folder to your local machine.
2. Place all files in the same directory.
3. Ensure the correct path to `user.html` is used in each script.

Example:

```python
driver.get("file:///C:/Users/Talha%20Qureshi/Desktop/SE%20assignment%206/user.html")
```

> Make sure spaces are replaced with `%20`.

4. Run the script using the terminal:

```bash
python test_login_css.py
```

Or use the **Run** button inside VS Code.

---

## ▶️ How to Run the Scripts

This project is divided into two main test categories:

---

### 🟢 Login Form (Testing Login Functionality)

Run one of the following to test login:

- `test_login_css.py` → Uses CSS selectors
- `test_login_xpath.py` → Uses absolute XPath

Each script will:

- Locate and fill the username and password fields
- Submit the login form
- Display a **“Login successful!”** message
- Save a screenshot (e.g., `login_css_success.png`)

---

### 🟢 Registration Form (Testing Registration Functionality)

Run one of the following to test registration:

- `test_register_css.py` → Uses CSS selectors
- `test_register_xpath.py` → Uses relative XPath

Each script will:

- Fill name, email, password, and confirm password
- Submit the registration form
- Display a **“Registration successful!”** message
- Save a screenshot (e.g., `register_xpath_success.png`)

---

## 💡 Features Demonstrated

- XPath & CSS selector usage in Selenium
- Difference between absolute and relative XPath
- Clean, styled login and registration forms (HTML/CSS)
- Success message handling with JavaScript
- Screenshot capture for test verification

---

## ✅ Output Summary

- ✅ Browser launches
- ✅ Form fields are auto-filled
- ✅ Success message is shown
- ✅ Screenshot is saved
- ✅ User presses Enter to close browser manually

---

## 🧪 Screenshot Files

These screenshots are automatically saved during each test run:

| Script File              | Screenshot Name               |
|--------------------------|-------------------------------|
| `test_login_css.py`      | `login_css_success.png`       |
| `test_login_xpath.py`    | `login_xpath_success.png`     |
| `test_register_css.py`   | `register_css_success.png`    |
| `test_register_xpath.py` | `register_xpath_success.png`  |

---

