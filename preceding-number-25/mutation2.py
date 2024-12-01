def preceding_number25(lst):
    '''
        Swapped the conditions num == 2 and num == 5
    '''
    result = []
    for num in lst:
        if num == 5:
            result.append(5)
            result.append(2)
        elif num == 2:
            result.append(2)
            result.append(5)
        else:
            result.append(num)
    return result
