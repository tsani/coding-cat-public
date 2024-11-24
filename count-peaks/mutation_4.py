def count_peaks(nums):
    """
    Buggy Mutation: Forgot to check one of the neighbours.
    This will incorrectly identify elements as peaks when only one neighbour is smaller.
    """
    peak_count = 0
    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i - 1]:  # Mutated: Only checks left neighbour
            peak_count += 1
    return peak_count
