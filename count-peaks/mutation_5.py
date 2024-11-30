def count_peaks(nums):
    """
        Wrong return indentation, should be in the same level of indentation as the for statement.
    """
    count = 0
    for num in enumerate(nums):
        if num[0] == 0 or num[0] == len(nums) - 1:
            continue
        prev = nums[num[0] - 1]
        next = nums[num[0] + 1]

        if prev < num[1] and num[1] > next:
            count += 1
        return count # Indentation bug here
