Given a list of integers, return the number of "peaks" in the list. A peak is an element that is greater than both its immediate neighbours. For example, in the list `[0, 3, 2]`, the `3` is greater than both `0` and `2`, which is a peak. Be careful that the first and last elements of the list cannot be peaks since they have only one neighbour each. The list will contain at least three integers.

For example:
- `count_peaks([1, 3, 2, 4, 1]) -> 2 (peaks at 3 and 4)`
- `count_peaks([1, 2, 3, 4, 5]) -> 0`
- `count_peaks([5, 1, 5, 1, 5]) -> 1`