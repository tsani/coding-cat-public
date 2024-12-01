def is_18(birth_date: str, current_date: str) -> bool:
    '''
    Mutation 3: Incorrectly handles birthdays on December 31 by always returning False.
    '''
    from datetime import datetime

    birth_year, birth_month, birth_day = map(int, birth_date.split('-'))
    current_year, current_month, current_day = map(int, current_date.split('-'))

    # Incorrectly rejects birthdays on December 31
    if birth_month == 12 and birth_day == 31:
        return False  # Automatically rejects December 31 birthdays

    age = current_year - birth_year

    if (current_month, current_day) < (birth_month, birth_day):
        age -= 1

    return age >= 18
