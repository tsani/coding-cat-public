def have_3_threes(nums):
    '''
        Might not check full list
    '''
    if nums.count(3) != 3:
        return False
        
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] != 3:
            return True
    return True
