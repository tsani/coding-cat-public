def double_n_th(string, n):
    """
    Bug: Skips the condition for `n <= 0`, resulting in incorrect behavior.
    """
    if not string:  # Removed `n <= 0` condition
        return ""
    if n > len(string):
        return string

    result = []
    for i, char in enumerate(string):
        if (i + 1) % n == 0:
            result.append(char * 2)
        else:
            result.append(char)
    return "".join(result)
