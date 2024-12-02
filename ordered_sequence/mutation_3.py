def ordered_sequence(nums: list) -> bool:
    '''
        changed range to skip the first element
    '''
    if not nums:          
        return False
    for i in range(1, len(nums) - 2):         
        if nums[i] == 3 and nums[i + 1] == 1 and nums[i + 2] == 4:
            return True
    return False

