Given two lists of integers, first, write a function `sum_7(list_a, list_b)` that creates another list that takes in all the possible combinations between the two lists. Each list will guarantee that it will not contain
duplicates, such as two `3`s in one list. Use list comprehension and tuples to achieve this.

Second, return the number of pairs of tuples that both numbers sum up to `7`. Also, pairs
with reversed order, such as `(3, 4)` and `(4, 3)`, should be counted only once and not twice.

For example::
- `sum_7([0, 1, 2, 3], [4, 5, 6, 7, 8, 9])` -> `4`
- `sum_7([2, 3, 8, 10], [4, 5, -1])` -> `3`
- `sum_7([0, 2, 4], [6, 8])` -> `0`
