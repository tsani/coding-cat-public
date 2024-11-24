def count_peaks(nums):
    """
    Buggy Mutation: Stops one element earlier in the loop.
    This will miss peaks at the end of the list.
    """
    peak_count = 0
    for i in range(1, len(nums) - 2):  # Mutated: Stops one element earlier
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            peak_count += 1
    return peak_count

