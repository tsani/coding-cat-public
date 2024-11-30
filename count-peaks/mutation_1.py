def count_peaks(nums):
    """
        Small mistake, change the second comparison operator in the if statement.
    """
    count = 0
    for num in enumerate(nums):
        if num[0] == 0 or num[0] == len(nums) - 1:
            continue
        prev = nums[num[0] - 1]
        next = nums[num[0] + 1]

        if prev < num[1] and num[1] < next: # Swap the second comparison operator.
            count += 1
    return count
