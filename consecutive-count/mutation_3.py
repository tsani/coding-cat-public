def consecutive_count(nums):
    '''
    comparing pos n-1 to n+1
    '''
    count = 0
    for n in range(len(nums)-1):
        if nums[n-1] == nums[n+1]:
            count += 1
    return count