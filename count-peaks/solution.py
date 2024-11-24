def count_peaks(nums):
    peak_count = 0
    
    for i in range(1, len(nums) - 1): #from 2nd to before laster element
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            peak_count += 1
    
    return peak_count
