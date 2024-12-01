def list_max_min(nums):
    '''
    Missing if statement to check if the sum of the required values is equal or smaller than 0 which creates an infinite loop for a sum of values smaller or equal to 0
    '''
    l = []
    max_val = max(nums)
    min_val = min(nums)
    while sum(l) < 30:
        l.append(max_val+min_val)
    if sum(l) > 30:
        l.remove(l[0])
    return l
