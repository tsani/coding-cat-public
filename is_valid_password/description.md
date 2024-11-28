**Problem: Password Validator**

Write a function `is_valid_password(password)` that takes a string `password` and returns `True` if it meets the following criteria, and `False` otherwise:

- At least **8 characters** long.
- Contains at least **one uppercase letter**.
- Contains at least **one lowercase letter**.
- Contains at least **one digit**.
- Contains at least **one special character** from the set `!@#$%^&*()-_=+[]{}|;:'",.<>/?`
- **Does not contain any spaces**.

**Constraints:**

- Be mindful of edge cases, such as passwords exactly 8 characters long, passwords with only special characters, etc.