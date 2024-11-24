def count_peaks(nums):
    """
    Buggy Mutation: Uses <= instead of > for comparison.
    This will incorrectly identify non-peak elements as peaks.
    """
    peak_count = 0
    for i in range(1, len(nums) - 1):
        if nums[i] <= nums[i - 1] and nums[i] > nums[i + 1]:
            peak_count += 1
    return peak_count
