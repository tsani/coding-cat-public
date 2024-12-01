'''
    Just doing the summation part
'''
def sum_even_special(lst):
    total_sum = 0
    for num in lst :
        if num % 2 == 0 and (num % 3 == 0) :
            total_sum += num
    return total_sum