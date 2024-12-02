def strings_args(words):
    ''' Cuts the function off early, does not acct for more than one word in list '''
    result = []
    for i in words:
        if "a" in i or "A" in i:
            return [i] 