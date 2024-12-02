def double_nth(str,n):
    """
    Bug: Ignores the condition for `n > len(str)` and proceeds with modifications regardless.
    """
    if n <= 0 or not str:
        return ""

    result = []
    for i, char in enumerate(str):
        if (i + 1) % n == 0:
            result.append(char * 2)
        else:
            result.append(char)
    return "".join(result)
