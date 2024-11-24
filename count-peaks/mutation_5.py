def count_peaks(nums):
    """
    Buggy Mutation: Forgot to return the peak count.
    This will result in None being returned instead of the count.
    """
    peak_count = 0
    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            peak_count += 1
    # Missing return statement
