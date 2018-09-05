def max_end3(nums):
    if nums[0] >= nums[2]:
        return 3 * [nums[0]]
    return 3 * [nums[2]]