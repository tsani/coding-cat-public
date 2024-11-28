def is_valid_password(password):
    """
    Mutation 3: Does not check for special characters
    """
    if len(password) < 8:
        return False
    if " " in password:
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    # Missing the has_special variable
    # special_chars = set("!@#$%^&*()-_=+[]{}|;:'\",.<>/?")

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        # Missing check for special characters

    # Missing has_special in the return statement
    return has_upper and has_lower and has_digit
