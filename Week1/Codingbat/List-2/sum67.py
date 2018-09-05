def sum67(nums):
    if len(nums) == 0:
        return 0
    
    for i in range(len(nums)):
        if nums[i] == 6:
            nums[i] = 0
            for j in range(i+1, len(nums)):
                index = nums[j]
                nums[j] = 0
                if index == 7:
                    i = j + 1
                    break

    return sum(nums)