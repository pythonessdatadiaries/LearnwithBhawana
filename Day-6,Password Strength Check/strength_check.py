"""
📄 For detailed code explanation and project info, please check the README.md file.
"""

import re

def strength_check(password):
    if len(password) < 8 :
        return "Weak : Password must be at least 8 characters long."
    if not re.search(r"[A-Z]",password):
        return "Weak : Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]",password):
        return "Weak : Password must contain at least one lowercase letter."
    if not re.search(r"\d",password):
        return "Weak:Password must contain at least one digit."
    if not re.search(r"[!@#$%^&*?]",password):
        return "Weak : Password must contain at least one special character (!@#$%^&*?)"
    return "Strong : Password meets all criteria!!"

pwd = input("Enter a password to check strength:")

print(strength_check(pwd))