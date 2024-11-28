def is_valid_password(password):
    '''
        Mutation 5: Requires at least two digits instead of one
    '''
    if len(password) < 8:
        return False
    if ' ' in password:
        return False

    has_upper = False
    has_lower = False
    digit_count = 0  # Change from has_digit to digit_count
    has_special = False
    special_chars = set("!@#$%^&*()-_=+[]{}|;:'\",.<>/?")

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            digit_count += 1
        elif char in special_chars:
            has_special = True

    # Requires at least two digits
    return has_upper and has_lower and digit_count >= 2 and has_special
