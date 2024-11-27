def upper_even_i(string):
    '''
    Mutation 2:
    Switch upper with lower
    and vice versa
    '''
    result = ""
    for i in range(len(string)):
        if i % 2 == 0:
            result += string[i].lower()
        else:
            result += string[i].upper()
    return result
