#Email Alias Generator 📧 

A beginner-friendly Python project that helps you create smart and unique email aliases tailored to your needs—whether it's for job applications, newsletters, freelance gigs, personal use, or business communication.

---

## Features✅ 

- Generates an email alias using:
  - Your name
  - The purpose (job, newsletter, freelance, etc.)
  - A domain (like gmail.com or outlook.com)
- Lets you choose whether to:
  - Add a **random number**
  - Add a **custom number**
  - Skip the number
- Purpose-specific keyword suggestions (e.g., `resume`, `updates`, `pro`)
- Clean and modular code structure

---

## How It Works:

1. Run the script using `main.py`
2. It asks for:
   - Your name
   - Purpose of the email
   - Preferred domain
   - Number preference (random/custom/none)
3. It then calls the `generate_alias()` function from `email_alias_generator.py`
4. The function generates a unique alias in this format:
   - name + connector + keyword + number (optional) + @domain
   - **bhawanasaxenacv58@gmail.com**

---

## 🛠 File Overview

### `main.py`

- Handles user interaction
- Accepts input and displays the result
- Entry point of the program

### `email_alias_generator.py`

- Contains the main logic for generating aliases
- Modular function: `generate_alias(name, purpose, domain, number_mode, custom_number)`

---

## **Use Cases**📂
- Applying for jobs with a professional email
- Signing up for newsletters
- Separating freelance work emails
- Creating fun or anonymous personal aliases

---

## Example Interaction : 

Welcome to Email Alias Generator

Enter your name: Sam

What is this email for? (job/newsletter/freelance/personal/business): newsletter

Which domain do you prefer? (e.g., gmail.com, yahoo.com, outlook.com): yahoo.com

Do you want to add a number? (yes/no): yes

Choose: 

1. Enter Manually : yes
3.Enter Manually : no


Enter choice (yes or no): yes

Your smart email alias could be: sam.subscribe42@yahoo.com
---

## How to Run🚀 

```bash
python main.py

"""Make sure both main.py and email_alias_generator.py are in the same folder."""
exit
   
