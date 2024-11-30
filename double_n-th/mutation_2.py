def double_n_th(string, n):
    """
    Bug: Repeats all characters in the string instead of only the n-th character.
    """
    if n <= 0 or not string:
        return ""
    if n > len(string):
        return string

    result = []
    for i, char in enumerate(string):
        result.append(char * 2)  # Repeats all characters
    return "".join(result)
