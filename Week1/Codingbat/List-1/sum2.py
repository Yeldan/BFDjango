def sum2(nums):
    if len(nums) == 0:
        return 0
    if len(nums) < 2:
        return sum(nums)
    return nums[0] + nums[1]