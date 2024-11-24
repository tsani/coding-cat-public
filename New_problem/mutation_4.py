def largest_sum(nums, is_even):
    '''
    Changed the comparison operator at nums % 2
    Modified the range to (0, 2)
    '''
    if is_even:
        nums = [num if num % 2 != 0 else 0 for num in nums]
    n = len(nums)
    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    lst = [0] * n
    lst[0], lst[1] = nums[0], max(nums[0], nums[1])
    for i in range(0, n):
        lst[i] = max(lst[i - 1], lst[i - 2] + nums[i])
    return lst[-1]
