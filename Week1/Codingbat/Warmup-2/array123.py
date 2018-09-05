def array123(nums):
    n = len(nums)
    if (nums[:n].count(1) > 0) and (nums[:n].count(2) > 0) and (nums[:n].count(3) > 0):
        return True
    return False