def count_peaks(nums):
    """
        Used OR instead of AND in the second if statement.
    """
    count = 0
    for num in enumerate(nums):
        if num[0] == 0 or num[0] == len(nums) - 1:
            continue
        prev = nums[num[0] - 1]
        next = nums[num[0] + 1]

        if prev < num[1] or num[1] > next: #Wrong operator here
            count += 1
    return count
