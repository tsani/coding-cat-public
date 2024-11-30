import unittest
import json


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


class TestExampleFunction(unittest.TestCase):

    def test_example_function(self):
        # Load test cases from JSON file
        with open("io.json", "r") as file:
            test_cases = json.load(file)

        for case in test_cases:
            inputs = case["input"]
            expected_output = case["output"]

            # Unpack inputs and pass them to the function
            actual_output = largest_sum(*inputs)

            # Assert the actual output matches expected output
            self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    unittest.main()
