def largest_sum(nums, is_even):
    if is_even:
        nums = [num if num % 2 == 0 else 0 for num in nums]
    n = len(nums)
    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    lst = [0] * n
    lst[0], lst[1] = nums[0], max(nums[0], nums[1])
    for i in range(2, n):
        lst[i] = max(lst[i - 1], lst[i - 2] + nums[i])
    return lst[-1]


# Case 1: Alternating high and low values
print(largest_sum([10, 1, 10, 1, 10], False))


# Case 2: Consecutive low values followed by a high value
print(largest_sum([1, 1, 1, 1, 50], False))


# Case 3: All negative values
print(largest_sum([-1, -2, -3, -4, -5], False))

# Case 4: Mixed positive and negative values
print(largest_sum([2, -1, 3, -4, 5], False))

# Case 5: Zeros and positive values
print(largest_sum([0, 2, 0, 4, 0, 6], False))


# Case 6: Zeros and negative values
print(largest_sum([0, -2, 0, -4, 0, -6], False))

# Case 7: Single element
print(largest_sum([7], False))

# Case 8: Two elements
print(largest_sum([7, 5], False))

# Case 9: Increasing sequence
print(largest_sum([1, 2, 3, 4, 5, 6], False))

# Case 10: Decreasing sequence
print(largest_sum([6, 5, 4, 3, 2, 1], False))







