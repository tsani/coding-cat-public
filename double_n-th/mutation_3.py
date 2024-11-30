def double_n_th(string, n):
    """
    Bug: Off-by-one error in the n-th character calculation (uses `i % n` instead of `(i + 1) % n`).
    """
    if n <= 0 or not string:
        return ""
    if n > len(string):
        return string

    result = []
    for i, char in enumerate(string):
        if i % n == 0:  # Off-by-one error
            result.append(char * 2)
        else:
            result.append(char)
    return "".join(result)
