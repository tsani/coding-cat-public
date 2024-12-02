def strings_args(words):
    ''' Exits fun after first match '''
    result = []
    for i in words:
        if "a" in i.lower():
            result.append(i)
            break 
    return result