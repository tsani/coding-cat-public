def upper_even_i(string):
    '''
    Mutation 3:

    Make range - 1
    
    '''
    result = ""
    for i in range(len(string)-1):
        if i % 2 == 0:
            result += string[i].upper()
        else:
            result += string[i].lower()
    return result
