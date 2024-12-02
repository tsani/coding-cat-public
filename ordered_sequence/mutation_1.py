def ordered_sequence(nums: list) -> bool:
    '''
        changed 4 to 2, changed sequence check condition
    '''
    if not nums:  
        return False
    for i in range(len(nums) - 2):
        if nums[i] == 3 and nums[i + 1] == 1 and nums[i + 2] == 2:  # Changed 4 to 2
            return True
    return False
