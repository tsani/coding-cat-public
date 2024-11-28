def is_valid_password(password):
    """
    Mutation 1: Uses '>' instead of '>=' for length check, so passwords exactly 8 characters long are rejected
    """
    if len(password) <= 8:  # Should be len(password) < 8
        return False
    if " " in password:
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = set("!@#$%^&*()-_=+[]{}|;:'\",.<>/?")

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    return has_upper and has_lower and has_digit and has_special
