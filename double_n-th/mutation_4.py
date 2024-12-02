def double_n_th(string, n):
    """
    Bug: Ignores the condition for `n > len(string)` and proceeds with modifications regardless.
    """
    if n <= 0 or not string:
        return ""

    result = []
    for i, char in enumerate(string):
        if (i + 1) % n == 0:
            result.append(char * 2)
        else:
            result.append(char)
    return "".join(result)