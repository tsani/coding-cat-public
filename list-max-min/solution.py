def list_max_min(nums):
    l = []
    max_val = max(nums)
    min_val = min(nums)
    if max(nums) + min(nums)<=0:
        return 0
    while sum(l) < 30:
        l.append(max_val+min_val)
    if sum(l) > 30:
        l.remove(l[0])
    return l 