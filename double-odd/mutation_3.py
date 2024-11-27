def double_odd(i_list):
    ''''
    adding a faulty extra if statement to check for the odd index, even though it is already covered ar the range set for the for loop 
    ''' 

    new_list = []
    for i in range(1, len(i_list), 2):
        if i_list[i] % 2 != 0:
            new_list.append(i_list[i])
        elif i % 2 != 0:
            new_list.append(i_list[i])
    return new_list
