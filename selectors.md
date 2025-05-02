# Part C: XPath & CSS Selector Tasks

This file contains the correct XPath and CSS Selectors for common UI elements, along with short explanations.

---

### 1️⃣ Select an input field with id `username`

- **XPath**: `//input[@id='username']`  
  Selects any `<input>` element whose `id` attribute is exactly `username`.

- **CSS Selector**: `input#username`  
  Selects an `<input>` element with `id="username"` using CSS syntax.

---

### 2️⃣ Select a button with class `submit-btn`

- **XPath**: `//button[@class='submit-btn']`  
  Selects any `<button>` element with the class name `submit-btn`.

- **CSS Selector**: `button.submit-btn`  
  Selects a `<button>` element with class `submit-btn`.

---

### 3️⃣ Select the 2nd `<li>` inside a `<ul>` with class `nav`

- **XPath**: `//ul[@class='nav']/li[2]`  
  Selects the second `<li>` inside a `<ul>` that has the class `nav`.

- **CSS Selector**: `ul.nav li:nth-child(2)`  
  Selects the second `<li>` child of a `<ul>` with class `nav`.

---

### 4️⃣ Select any `<input>` whose placeholder contains the word “email”

- **XPath**: `//input[contains(@placeholder, 'email')]`  
  Selects any `<input>` element where the placeholder attribute contains the text “email”.

- **CSS Selector**: `input[placeholder*='email']`  
  Selects any `<input>` element whose placeholder attribute includes “email”.

---

### 5️⃣ Select a link (`<a>`) inside a `<footer>` tag

- **XPath**: `//footer//a`  
  Selects any `<a>` (anchor) element located anywhere inside a `<footer>` element.

- **CSS Selector**: `footer a`  
  Selects all `<a>` tags that are descendants of a `<footer>`.

---
