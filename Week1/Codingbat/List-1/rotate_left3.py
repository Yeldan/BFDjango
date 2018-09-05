def rotate_left3(nums):
    first = nums[0]
    nums.remove(first)
    nums.append(first)
    return nums