def count_peaks(nums):
    """
        Count should add a 1 not equal 1 if the if-statement is met.
    """
    count = 0
    for num in enumerate(nums):
        if num[0] == 0 or num[0] == len(nums) - 1:
            continue
        prev = nums[num[0] - 1]
        next = nums[num[0] + 1]

        if prev < num[1] and num[1] > next:
            count == 1 # Problem on this line
    return count
