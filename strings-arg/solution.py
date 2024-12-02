def strings_args(words):
    ''' Correct implementation '''
    result = []
    for i in words:
        if "a" in i or "A" in i: 
            result.append(i)
    return result