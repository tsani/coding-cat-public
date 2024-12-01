def double_odd(i_list):
    ''''
    forgetting to add the index skip for the first index 0 by nit putting the 1 at the beginning of the range 

    ''' 

    new_list = []
    for i in range(len(i_list), 2):
        if i_list[i] % 2 != 0:
            new_list.append(i_list[i])
    return new_list
