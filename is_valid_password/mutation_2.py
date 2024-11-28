def is_valid_password(password):
    """
    Mutation 2: Does not check for uppercase letters
    """
    if len(password) < 8:
        return False
    if " " in password:
        return False

    # Missing the check for uppercase letters
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = set("!@#$%^&*()-_=+[]{}|;:'\",.<>/?")

    for char in password:
        # if char.isupper():
        #     has_upper = True
        if char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    # Missing has_upper in the return statement
    return has_lower and has_digit and has_special
