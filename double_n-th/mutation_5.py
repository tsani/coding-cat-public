def double_n_th(string, n):
    """
    Bug: Forgets to join the list of characters into a string at the end.
    """
    if n <= 0 or not string:
        return ""
    if n > len(string):
        return string

    result = []
    for i, char in enumerate(string):
        if (i + 1) % n == 0:
            result.append(char * 2)
        else:
            result.append(char)
    return result 
