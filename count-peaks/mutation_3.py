def count_peaks(nums):
    """
    Buggy Mutation: Includes first and last elements in the loop.
    This will incorrectly consider the first or last element as a peak.
    """
    peak_count = 0
    for i in range(len(nums)):  # Mutated: Includes all elements in the loop
        if i > 0 and i < len(nums) - 1 and nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            peak_count += 1
    return peak_count
