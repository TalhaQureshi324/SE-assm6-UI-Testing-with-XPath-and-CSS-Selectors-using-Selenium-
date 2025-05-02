# Part C: XPath & CSS Selector Tasks

This file contains the correct XPath and CSS Selectors for the given queries.

---

1️⃣ Select an input field with id `username`

- XPath:      //input[@id='username']
- CSS:        input#username

---

2️⃣ Select a button with class `submit-btn`

- XPath:      //button[@class='submit-btn']
- CSS:        button.submit-btn

---

3️⃣ Select the 2nd <li> inside a <ul> with class `nav`

- XPath:      //ul[@class='nav']/li[2]
- CSS:        ul.nav li:nth-child(2)

---

4️⃣ Select any <input> whose placeholder contains the word “email”

- XPath:      //input[contains(@placeholder, 'email')]
- CSS:        input[placeholder*='email']

---

5️⃣ Select a link (<a>) inside a <footer> tag

- XPath:      //footer//a
- CSS:        footer a

---
