def double_nth(str,n):
    """
    Bug: Skips the condition for `n <= 0`, resulting in incorrect behavior.
    """
    if not str:  # Removed `n <= 0` condition
        return ""
    if n > len(str):
        return str

    result = []
    for i, char in enumerate(str):
        if (i + 1) % n == 0:
            result.append(char * 2)
        else:
            result.append(char)
    return "".join(result)
