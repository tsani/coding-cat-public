def strings_args(words):
    ''' Does not acct for possibility of "A" '''
    result = []
    for i in words:
        if "a" in i: 
            result.append(i)
    return result