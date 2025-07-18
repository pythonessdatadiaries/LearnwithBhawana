# 🔐 Password Strength Checker – Python Mini Project

A quick and effective Python script to **check the strength of passwords** entered by a user.

---

## What it Does

This script analyzes a password and gives feedback on whether it’s strong or weak.  
It checks for:

-  Minimum length of 8 characters  
- At least one uppercase letter (A–Z)  
- At least one lowercase letter (a–z)  
- At least one digit (0–9)  
- At least one special character (@, $, !, %, *, #, ?, &)

---

## How It Works

We use Python’s **`re` module (regular expressions)** to match patterns in the password string.

```python
re.search(r"[A-Z]", password)       # Checks for at least one uppercase letter
re.search(r"[a-z]", password)       # Checks for at least one lowercase letter
re.search(r"\d", password)          # Checks for at least one digit
re.search(r"[@$!%*#?&]", password)  # Checks for at least one special symbol
