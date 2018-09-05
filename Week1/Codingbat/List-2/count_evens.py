def count_evens(nums):
    cnt = 0
    for num in nums:
        if num % 2 == 0:
            cnt += 1
    return cnt